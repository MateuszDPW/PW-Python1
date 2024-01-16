class Rolnik:
    filename = "class_fields.txt"
    farmer_name = "Jan Adamski"
    fields = [(25.5,20.3),(17.26)]



    def __init__(self):
        self.file_path = filename

    def save(self):
        f_fields = self.format_fields_data(self.fields)
        write_fields_data_to_file(self.farmer,f_fields)

    def write_fields_data_to_file(self, farmer, fields_data):
        with open(filename, 'a') as file:
            file.write(f"{farmer}; {fields_data}\n")

    def format_fields_data(fields):
        return ",".join([(f"{l}x{w}") for l,w in fields])

    def main():
        famrer_name = "Jan Adamski"
        filename = "class_fields.txt"
        fields = [(25.5,20.3),(17.26)]

        f_fields = format_fields_data(fields)
        write_fields_data_to_file(filename,farmer_name,f_fields)
        read_and_display_fields_data(filename)

if __name__ == '__main__':
    main()

rolnik = Rolnik()