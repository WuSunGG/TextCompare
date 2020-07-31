from component.trans.html2txt import html2txt


def test_a():
    t=html2txt()
    assert(t.htmlcontent("<a>我们</a>")=="我们")
    assert(t.htmlcontent("我们")=="我们")
    assert(t.htmlcontent("")=="")
