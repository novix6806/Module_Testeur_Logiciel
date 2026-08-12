FORM_PAGE_URL = "https://fluentforms.com/forms/contact-form-demo/"
FIRST_NAME_LOCATOR = "id=ff_3_names_first_name_"
LAST_NAME_LOCATOR = "id=ff_3_names_last_name_"
EMAIL_LOCATOR = "id=ff_3_email"
SUBJECT_LOCATOR = "id=ff_3_subject"
MESSAGE_LOCATOR = "id=ff_3_message"
SEND_BUTTON_LOCATOR = "//button[text()='Send Message']"

#Jeu de données pour le formulaire
USERS = [
    # Indice 0 (utilisé dans le test "Soumission Formulaire Avec Données Valides")
    {
        "first_name": "test",
        "last_name": "user",
        "email": "user@example.com",
        "subject": "Form test",
        "message": "This is a test message."
    },
    # Indice 1 (utilisé dans le test "Soumission Formulaire Pour Chaque Utilisateur")
    {
        "first_name": "John",
        "last_name": "Doe",
        "email": "john.doe@example.com",
        "subject": "Form test",
        "message": "This is a test message."
    },
    # Indice 2 (utilisé dans le test "Soumission Formulaire Pour Chaque Utilisateur")
    {
        "first_name": "Jane",
        "last_name": "Smith",
        "email": "jane.smith@example.com",
        "subject": "Form test",
        "message": "This is another test message."
    },
    # Indice 3 (utilisé dans le test "Soumission Formulaire Pour Chaque Utilisateur")
    {
        "first_name": "Bob",
        "last_name": "Johnson",
        "email": "bob.johnson@example.com",
        "subject": "Form test",
        "message": "This is a third test message."
    }
]