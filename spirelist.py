from xml.dom.minidom import Document

from spire.doc import *
from spire.doc.common import *

doc = Document()
section = doc.AddSection()

list_style = ListStyle(doc, ListType.Numbered)
list_style.Name = "MyNumberedList"
list_style.Levels[0].PatternType = ListPatternType.Arabic
doc.ListStyles.Add(list_style)

items = ["First item", "Second item", "Third item"]
for text in items:
    paragraph = section.AddParagraph()
    paragraph.AppendText(text)
    paragraph.ListFormat.ApplyStyle("MyNumberedList")
    paragraph.ListFormat.ListLevelNumber = 0

doc.SaveToFile("NumberedList.docx", FileFormat.Docx2019)
doc.Dispose()