# pdf-barcode-extractor

Fiz esse script porque tem uma empresa que me envia um boleto sem código de barras e imagem ao invés do texto.

## Instalação

### Linux (debian)

```sh
sudo apt install libtesseract-dev

poetry install
```

```
python barcode-extractor.py nome-arquivo.pdf
```