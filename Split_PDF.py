#Separación de Archivos PDF
#Para separar archivos PDF, puedes usar la biblioteca PyPDF2.
import PyPDF2

def separar_pdf(input_pdf, output_pdf, start_page, end_page):
    pdf_reader = PyPDF2.PdfFileReader(input_pdf)
    pdf_writer = PyPDF2.PdfFileWriter()

    for page_num in range(start_page, end_page):
        pdf_writer.addPage(pdf_reader.getPage(page_num))

    with open(output_pdf, 'wb') as output_file:
        pdf_writer.write(output_file)

# Uso de la función
separar_pdf('documento.pdf', 'documento_separado.pdf', 0, 5)
