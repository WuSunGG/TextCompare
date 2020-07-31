from component.trans.docx2txt import docx2txt


def test_a():
    t = docx2txt()
    assert (t.docx2txt("a") == False)
    assert (t.docx2txt("a.txt")==False)
    assert (t.docx2txt("")==False)
    assert (t.docx2txt("11.docx").find("11")==0)
