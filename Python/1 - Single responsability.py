# Single Responsability: Each class must have a single responsability
# Responsabilidad Unica :Cada clase debería tener una sola resonsabilidad


# Bad
class UserRegistry:
    def create_user(email, password):
        salt = crypt.gen_salt()
        encripted_password = crypt(password)
        new_user = User(email, encripted_password)
        UserRepository.save_to_database(new_user)


# Correct
class UserRegistry:
    def create_user(email, password):
        encripted_password = PasswordEncrypted.encrypt(password)
        new_user = User(email, encripted_password)
        UserRepository.saveToDatabase(new_user)


class PasswordEncrypted:
    def encrypt(password):
        salt = encrypt.gen_salt()
        encripted_password = crypt.hash(password, salt)
        return encripted_password