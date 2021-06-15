import zipfile
import tabula

# Read pdf into list of DataFrame
file = tabula.read_pdf("TISS.pdf", pages="79-85")

# convert PDF into CSV file
tabula.convert_into("TISS.pdf", "tabela_1.csv", output_format="csv", pages="79", stream=True)

tabula.convert_into("TISS.pdf", "tabela_2.csv", output_format="csv", pages="79-84", stream=True)

tabula.convert_into("TISS.pdf", "tabela_3.csv", output_format="csv", pages="85", stream=True)

zip_file=zipfile.ZipFile('Teste_Intuitive_Care_Vinicius.zip', 'w')
zip_file.write("tabela_1.csv") 
zip_file.write("tabela_2.csv")
zip_file.write("tabela_3.csv")
zip_file.close