import openpyxl
import docx
import docxtpl
from openpyxl import load_workbook
from docxtpl import DocxTemplate

wb = load_workbook("people.xlsx")
ws = wb.active

doc = docx.Document()

for i in range(3):
    paragraph =\
        f'{{{{ context{i} }}}}'
    doc.add_page_break()

doc.save('templ.docx')

doc = DocxTemplate("templ.docx")
dict_of_contexts = {}
i = 0
for x in ws.values:
    context = {
        "surname": x[0],
        "name": x[1],
        "pat": x[2],
        "school": x[3],
    }
    dict_of_contexts[f'context{i}'] = context

doc.render(dict_of_contexts)
doc.save("generated_doc.docx")

# for x in list_of_contexts:
#     doc.render(context)
#     doc.add_page_break()
#
# doc.save("generated_doc.docx")
# ##############################3
#
#
#
# for x in ws.values:
#     print(x)
#     doc = docxtpl.DocxTemplate('Дипломанты.docx')
#     context = {
#     'surname': x[0],
#     'name': x[1],
#     'patronymic': x[2],
#     'school': x[3],
# }
#     doc.render(context)
#     doc.save("Дипломанты.docx")
