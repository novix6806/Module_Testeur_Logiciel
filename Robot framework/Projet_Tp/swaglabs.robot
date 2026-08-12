*** Settings ***
Resource                        swaglabs.resource
Suite Setup                     Open Login Page
Suite Teardown                  Close Browser
Test Setup                      User Logged In
Test Teardown                   Reset App

*** Test Cases ***
Test Connexion
    [Setup]                     No Operation
    User Logged In

Test de présence des produits
    FOR   ${product_dict}    IN    @{products}
          Run Keyword And Continue On Failure       Product Should Exist     ${product_dict['name']}
    END


Test de prix des produits
    [Documentation]             Vérifie que la page de produits contient bien les produits souhaités
    [Template]                  Product Should Have Price

    # product_name              product_price
    Sauce Labs Backpack         29.99
    Sauce Labs Bike Light       9.99
    Sauce Labs Bolt T-Shirt     15.99

Test d’images des produits
    [Documentation]             Vérifie que chaque produit est bien illustré par la bonne image
    [Template]                  Product Image Should Be
    # product_name              image_name
    Sauce Labs Fleece Jacket    sauce-pullover
    Sauce Labs Bolt T-Shirt     bolt-shirt

Test d’ajout de produit au panier
    Cart Badge Should Be Empty
    Check Add to cart feature           Sauce Labs Onesie        1

Test d’ajout de tous les produits au panier
    [Template]                                Check Add to cart feature
    Sauce Labs Backpack                       1
    Sauce Labs Fleece Jacket                  2
    Sauce Labs Bolt T-Shirt                   3
    Sauce Labs Onesie                         4
    Test.allTheThings() T-Shirt (Red)         5
    Sauce Labs Bike Light                     6

Test de parcours complet
    Rajout de Sauce Labs Backpack au panier
#    Navigation sur le panier
#    Cliquer sur le bouton Checkout
#    Remplir le formulaire avec pour nom Test, prénom Alice, et code postal 12345
#    Cliquer sur le bouton Continue
    La page de confirmation doit contenir Sauce Labs Backpack, et un total de 32.39 dollars
#    Cliquer sur le bouton Finish
#    La commande doit être validée