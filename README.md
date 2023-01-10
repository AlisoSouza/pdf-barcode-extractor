# pdf-barcode-extractor

Fiz esse script porque tem uma empresa que me envia um boleto sem código de barras e com uma imagem do c ao invés do texto.

## Instalação

### Linux (debian)

```sh
sudo apt install tesseract-ocr
sudo apt install libtesseract-dev

poetry install
```

```
python barcode-extractor.py nome-arquivo.pdf
```
