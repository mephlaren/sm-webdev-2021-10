#pip install <package-name>
from prettytable import PrettyTable
table = PrettyTable()

#oszlopnevek
table.field_names = ['Fajta', 'Háziasított', 'Fogyasztjuk']
#egy sor hozzáadása
table.add_row(['Kutya', 'Igen', 'Nem'])
#több sor hozzáadása
table.add_rows(
    [
        ['Tehén', 'Igen','Igen'],
        ['Macska', 'Igen', 'Nem'],
        ['Emu', 'Nem','Nem']
    ]
)
print(table)