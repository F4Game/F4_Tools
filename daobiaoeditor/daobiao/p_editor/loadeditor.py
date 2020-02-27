import p_editor.p_person as person

editorList = [
    person.PersonEditor(),
]

for ed in editorList:
    ed.WriteAllObj()
    ed.WriteAllDfeine()
    ed.WriteAllLoad()
