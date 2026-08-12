*** Settings ***
Library                         OperatingSystem
Library                         SeleniumLibrary
Variables                       swaglabs_vars.py

*** Variables ***
${base_url}                     https://saucedemo.com
${username}                     standard_user
${password}                     secret_sauce
#@{products}                     Sauce Labs Backpack         Sauce Labs Bike Light        Sauce Labs Bolt T-Shirt
#...                             Sauce Labs Fleece Jacket    Sauce Labs Onesie            Test.allTheThings() T-Shirt (Red)

*** Keywords ***
Open Login Page
    # Suppression des anciens fichiers de log et screenshots
    Remove Files                    geckodriver-*.log          selenium-screenshot-*.png
    Open Browser                    ${base_url}                browser=firefox                alias=default

Reset App
    [Documentation]                 Resets web app state, and logs out
    Click Button                    react-burger-menu-btn
    Wait Until Element Is Visible   logout_sidebar_link
    Click Link                      Reset App State
    Click Link                      Logout
    Element Should Be Visible       login-button

User Logged In
    [Documentation]                 Authenticates an user on the website
    Input Text                      user-name                    ${username}
    Input Password                  password                     ${password}
    Submit Form
    Page Should Contain             Products

Product Should Have Price
    [Documentation]                Checks if the given product name is on the webpage, and that it has the given price
    [Arguments]                    ${product_name}             ${product_price}
    ${price_element}               Get Product Element         ${product_name}        class:inventory_item_price
    Element Text Should Be         ${price_element}            $${product_price}

Product Image Should Be
    [Documentation]                Checks if the given product have the correct image filename
    [Arguments]                    ${product_name}             ${image_name}
    ${image}                       Get Product Element         ${product_name}        tag:img
    ${image_src}                   Get Element Attribute       ${image}               src
    Should Contain                 ${image_src}                ${image_name}

Get Product Element
    [Documentation]                Renvoie un élément présent dans un produit de la page,
    ...                            d’après son titre passé en argument, et un sélecteur Selenium
    ...                            à rechercher au sein de ce produit (qui peut être du CSS, une class, du XPath, etc.)
    ...                            Renvoie l’objet WebElement trouvé
    [Arguments]                    ${product_name}             ${locator}
    # attention à ne pas oublier l’espace à la fin de la classe CSS
    ${product_locator1}            Set Variable                xpath://div[@class="inventory_item_name "][text()="${product_name}"]/ancestor::div[@class="inventory_item"]
    ${product_locator_list}        Create List                 ${product_locator1}        ${locator}
    ${product_info}                Get WebElement              ${product_locator_list}
    RETURN                         ${product_info}

Cart Badge Should Be Empty
    [Documentation]                    Checks that the badge pill over the cart icon is invisible or inexistent, meaning that
    ...                                the cart is currently empty
    Page Should Not Contain Element    class:shopping_cart_badge           message=Cart isn’t empty

Cart Badge Should Be
    [Documentation]                    Checks that the badge pill over the cart icon contains the correct amount of products
    [Arguments]                        ${expected_amount}
    Element Text Should Be             class:shopping_cart_badge           ${expected_amount}
    ...                                message=Cart doesn’t contain the correct amount of products

Click Cart
    Click Link                         class:shopping_cart_link
    Location Should Contain            cart.html                           message=Cart button didn’t lead to the cart page

Add Product To Cart
    [Documentation]                    Clicks the "Add to cart" button on a product item on the inventory page
    [Arguments]                        ${product_name}
    ${btn}                             Get Product Element                 ${product_name}           class:btn_inventory
    Element Text Should Be             ${btn}                              Add to cart               message=Product is already in cart
    Click Button                       ${btn}

Cart Page Should Contain Amount
    [Arguments]                        ${expected_amount}
    ${item_count}                      Get Element Count                   class:cart_item
    Should Be Equal As Integers        ${item_count}                       ${expected_amount}        msg=Cart contains ${item_count} items, not ${expected_amount}

Cart Page Should Contain Product
    [Documentation]                    Checks if the given product is present in the cart, from the cart page
    [Arguments]                        ${product_name}
    Page Should Contain Element        xpath://div[@class="inventory_item_name"][text()="${product_name}"]          message=Cart doesn’t contain the product "${product_name}"

Check Add to cart feature
    [Documentation]                    Automates all actions to add a product to cart from the inventory page, and checks if it works correctly
    [Arguments]                        ${product_name}                      ${cart_amount}
    [Teardown]                         Click Button                         Continue Shopping
    Add Product To Cart                ${product_name}
    Cart Badge Should Be               ${cart_amount}
    Click Cart
    Cart Page Should Contain Amount    ${cart_amount}
    Cart Page Should Contain Product   ${product_name}

Product Should Exist
    [Arguments]                        ${product_name}
    Get Product Element                ${product_name}        class:inventory_item_name


Rajout de ${product_name} au panier
    Add Product To Cart                ${product_name}

La page de confirmation doit contenir ${product_name}, et un total de ${total_price} dollars
    No Operation