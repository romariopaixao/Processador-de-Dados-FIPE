from data_processor import process_data

def main():
    input_file = "FIPE_API.xlsx"
    output_file = process_data(input_file)
    print(f"Processamento concluído. Arquivo de saída: {output_file}")

if __name__ == "__main__":
    main()