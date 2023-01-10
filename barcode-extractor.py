import io
import sys
import fitz
import PIL.Image
import pytesseract


def get_pdf_image(pdf_file):
    """Extrai a imagem do pdf"""
    pdf = fitz.open(pdf_file)
    counter = 1
    for i in range(len(pdf)):
        page = pdf[i]
        images = page.get_images()
        for image in images:
            base_img = pdf.extract_image(image[0])
            image_data = base_img["image"]
            img = PIL.Image.open(io.BytesIO(image_data))
            extension = base_img["ext"]
            img_name = f"image{counter}.{extension}"
            img.save(open(img_name, "wb"))
            counter += 1
            return img_name


def get_image_text(image_file):
    """Transforma a imagem em texto e printa o texto no terminal"""
    image = PIL.Image.open(image_file)
    text = pytesseract.image_to_string(image)
    print(text)


if __name__ == "__main__":
    pdf_file = sys.argv[1]
    imagem = get_pdf_image(pdf_file)
    get_image_text(imagem)
