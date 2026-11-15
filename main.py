from config.config import API_KEY

def main():
    print("="*50)
    print("RETAIL SALES ETL PIPELINE")
    print("="*50)
    print(f"API Base URL: {API_KEY}")

    print("\nProject initialized successfully!")

    print("\nUpcoming pipeline stages:")
    print("1. Extract")
    print("2. Transform")
    print("3. Validate")
    print("4. Load")
    print("5. Schedule")


if __name__ == "__main__":
    main()