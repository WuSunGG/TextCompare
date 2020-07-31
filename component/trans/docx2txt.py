from docx import Document
import os

from component.logger import debug


class docx2txt:

    def docx2txt(self, docfile):
        if os.path.isfile(docfile):
            document = Document(docfile)
            tpaperTxt = ""
            debug("traning doc {} to txt is success".format(docfile))
            for paragraph in document.paragraphs:
                tpaperTxt += paragraph.text + "/r/n"
            debug("contents is {}".format(tpaperTxt))
            return tpaperTxt
        else:
            debug("file {} is not existed".format(docfile))
            return False
