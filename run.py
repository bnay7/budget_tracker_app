from src.app import database, main

if __name__ == "__main__":
    database.init_db()

    main.run_app()
