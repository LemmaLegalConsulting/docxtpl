# -*- coding: utf-8 -*-
'''
Created : 2022-07-09

@author: Bryce Willey
'''

from docxtpl import DocxTemplate


tpl = DocxTemplate('templates/merge_docx_master_tpl_with_2.docx')
sd = tpl.new_subdoc('templates/merge_docx_subdoc1.docx')
sd2 = tpl.new_subdoc('templates/merge_docx_subdoc2.docx')

context = {
    'mysubdocs': [sd, sd2],
}

tpl.render(context)
tpl.save('output/merge_docx.docx')