# from https://stackoverflow.com/questions/2693820/extract-images-from-pdf-without-resampling-in-python
import PyPDF4

from PIL import Image

def pdf_to_image(pdf_path, image_path):
    input1 = PyPDF4.PdfFileReader(open(pdf_path, "rb"))
    page0 = input1.getPage(0)
    xObject = page0['/Resources']['/XObject'].getObject()

    for obj in xObject:
        if xObject[obj]['/Subtype'] == '/Image':
            size = (xObject[obj]['/Width'], xObject[obj]['/Height'])
            data = xObject[obj].getData()
            if xObject[obj]['/ColorSpace'] == '/DeviceRGB':
                mode = "RGB"
            else:
                mode = "P"

            if xObject[obj]['/Filter'] == '/FlateDecode':
                img = Image.frombytes(mode, size, data)
                img.save(image_path + ".png")
                return "png"
            elif xObject[obj]['/Filter'] == '/DCTDecode':
                img = open(image_path + ".jpg", "wb")
                img.write(data)
                img.close()
                return "jpg"
            elif xObject[obj]['/Filter'] == '/JPXDecode':
                img = open(image_path + ".jp2", "wb")
                img.write(data)
                img.close()
                return "jp2"