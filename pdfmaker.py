import tkinter as tk
from tkinter import filedialog, messagebox
from pypdf import PdfMerger


class PdfMergerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PDF Merger")
        self.root.geometry("700x450")

        self.pdf_files = []

        title = tk.Label(root, text="PDF Merger", font=("Segoe UI", 18, "bold"))
        title.pack(pady=10)

        controls = tk.Frame(root)
        controls.pack(pady=5)

        tk.Button(controls, text="Add PDFs", width=14, command=self.add_pdfs).grid(row=0, column=0, padx=4)
        tk.Button(controls, text="Remove Selected", width=14, command=self.remove_selected).grid(row=0, column=1, padx=4)
        tk.Button(controls, text="Move Up", width=10, command=self.move_up).grid(row=0, column=2, padx=4)
        tk.Button(controls, text="Move Down", width=10, command=self.move_down).grid(row=0, column=3, padx=4)

        list_frame = tk.Frame(root)
        list_frame.pack(fill="both", expand=True, padx=20, pady=10)

        self.listbox = tk.Listbox(list_frame, selectmode=tk.SINGLE)
        self.listbox.pack(side="left", fill="both", expand=True)

        scrollbar = tk.Scrollbar(list_frame, orient="vertical", command=self.listbox.yview)
        scrollbar.pack(side="right", fill="y")
        self.listbox.config(yscrollcommand=scrollbar.set)

        output_frame = tk.Frame(root)
        output_frame.pack(fill="x", padx=20)

        tk.Label(output_frame, text="Output File:").pack(side="left")

        self.output_var = tk.StringVar(value="merged-pdf.pdf")
        self.output_entry = tk.Entry(output_frame, textvariable=self.output_var)
        self.output_entry.pack(side="left", fill="x", expand=True, padx=8)

        tk.Button(output_frame, text="Browse", command=self.choose_output).pack(side="left")

        tk.Button(root, text="Merge PDFs", width=18, command=self.merge_pdfs).pack(pady=14)

    def refresh_listbox(self):
        self.listbox.delete(0, tk.END)
        for pdf in self.pdf_files:
            self.listbox.insert(tk.END, pdf)

    def add_pdfs(self):
        files = filedialog.askopenfilenames(
            title="Select PDF Files",
            filetypes=[("PDF Files", "*.pdf")]
        )
        if files:
            self.pdf_files.extend(files)
            self.refresh_listbox()

    def remove_selected(self):
        selected = self.listbox.curselection()
        if not selected:
            return
        index = selected[0]
        self.pdf_files.pop(index)
        self.refresh_listbox()

    def move_up(self):
        selected = self.listbox.curselection()
        if not selected:
            return
        index = selected[0]
        if index == 0:
            return
        self.pdf_files[index - 1], self.pdf_files[index] = self.pdf_files[index], self.pdf_files[index - 1]
        self.refresh_listbox()
        self.listbox.selection_set(index - 1)

    def move_down(self):
        selected = self.listbox.curselection()
        if not selected:
            return
        index = selected[0]
        if index == len(self.pdf_files) - 1:
            return
        self.pdf_files[index + 1], self.pdf_files[index] = self.pdf_files[index], self.pdf_files[index + 1]
        self.refresh_listbox()
        self.listbox.selection_set(index + 1)

    def choose_output(self):
        output_path = filedialog.asksaveasfilename(
            title="Save Merged PDF As",
            defaultextension=".pdf",
            filetypes=[("PDF Files", "*.pdf")]
        )
        if output_path:
            self.output_var.set(output_path)

    def merge_pdfs(self):
        if not self.pdf_files:
            messagebox.showwarning("No Files", "Please add at least one PDF file.")
            return

        output_file = self.output_var.get().strip()
        if not output_file:
            messagebox.showwarning("Output Missing", "Please provide an output file name.")
            return

        merger = PdfMerger()
        try:
            for pdf in self.pdf_files:
                merger.append(pdf)
            merger.write(output_file)
            messagebox.showinfo("Success", f"Merged PDF created:\n{output_file}")
        except Exception as exc:
            messagebox.showerror("Error", f"Could not merge PDFs:\n{exc}")
        finally:
            merger.close()


if __name__ == "__main__":
    root = tk.Tk()
    app = PdfMergerApp(root)
    root.mainloop()
