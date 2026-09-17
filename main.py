from src.db.db_config import SessionLocal
from src.service.movie_service import MovieService
from src.service.review_service import ReviewService
from src.service.user_Service import UserService
def main():
    session = SessionLocal()
    user_service = UserService(session)
    movie_service = MovieService(session)
    review_service = ReviewService(session)

    current_user = None

    while True:
        print("\n=== Movie Management System ===")

        if not current_user:
            print("1. Register User")
            print("2. Login User")
        else:
            if current_user.role == "admin":
                print(f"\nWelcome Admin {current_user.full_name}")
                print("3. Add Movie")
                print("4. Update Movie")
                print("5. Delete Movie")
                print("6. List Movies")
                print("7. Logout")
            else:
                print(f"\nWelcome {current_user.full_name}")
                print("8. Add Review")
                print("9. List Reviews")
                print("10. List Movies")
                print("11. Logout")

        print("0. Exit")

        try:
            choice = int(input("Enter choice: "))
        except ValueError:
            print(" Invalid input! Please enter a number.")
            continue

        if not current_user:
            if choice == 1:
                username = input("Username: ")
                password = input("Password: ")
                email = input("Email: ")
                full_name = input("Full Name: ")
                role = input("Role (admin/user): ").strip().lower()
                user = user_service.register(username, password, email, full_name, role)
                print(f" User registered: {user.username}")

            elif choice == 2:
                username = input("Username: ")
                password = input("Password: ")
                user = user_service.login(username, password)
                if user:
                    current_user = user
                    print(f" Login successful! Welcome {user.full_name}")
                else:
                    print("Invalid credentials")

            elif choice == 0:
                print(" Exiting...")
                break

        else:
            if current_user.role == "admin":
                if choice == 3:
                    title = input("Title: ")
                    genre = input("Genre: ")
                    year = int(input("Year: "))
                    movie_service.add_movie(title, genre, year)
                    print(" Movie added")

                elif choice == 4:
                    movie_id = int(input("Movie ID: "))
                    title = input("New Title: ")
                    genre = input("New Genre: ")
                    year = int(input("New Year: "))
                    movie_service.update_movie(movie_id, title, genre, year)
                    print(" Movie updated")

                elif choice == 5:
                    movie_id = int(input("Movie ID: "))
                    try:
                        movie_service.delete_movie(movie_id)
                        print(" Movie deleted")
                    except Exception as err:
                        print(f" Error deleting movie: {err}")

                elif choice == 6:
                    movies = movie_service.list_movies()
                    for m in movies:
                        print(f"{m.id}. {m.title} ({m.year}) - {m.genre}")

                elif choice == 7:
                    print(f" Logged out {current_user.full_name}")
                    current_user = None

                elif choice == 0:
                    print(" Exiting...")
                    break

                else:
                    print("Invalid choice")

            else:  # User role
                if choice == 8:
                    movie_id = int(input("Movie ID: "))
                    rating = float(input("Rating (0-5): "))
                    comment = input("Comment: ")
                    review_service.add_review(current_user.id, movie_id, rating, comment)
                    print(" Review added")

                elif choice == 9:
                    reviews = review_service.list_reviews()
                    for r in reviews:
                        print(f"Review {r.id}: User {r.user.username} → Movie {r.movie.title} | {r.rating}/5 | {r.comment}")

                elif choice == 10:
                    movies = movie_service.list_movies()
                    for m in movies:
                        print(f"{m.id}. {m.title} ({m.year}) - {m.genre}")

                elif choice == 11:
                    print(f" Logged out {current_user.full_name}")
                    current_user = None

                elif choice == 0:
                    print(" Exiting...")
                    break

                else:
                    print(" Invalid choice")


if __name__ == "__main__":
    main()
