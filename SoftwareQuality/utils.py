import platform


def convert_docx_to_pdf(input_file, output_file):
    system = platform.system()
    if system == "Windows":
        # Используем docx2pdf на Windows
        from docx2pdf import convert

        convert(input_file, output_file)
    elif system == "Linux":
        # Используем unoconv на Linux
        import subprocess

        subprocess.run(["unoconv", "-f", "pdf", "-o", output_file, input_file])
    else:
        raise NotImplementedError(f"Unsupported OS: {system}")
