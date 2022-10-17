def test_login(home):

    login_page = home.nav_to_login_page()
    
    logged_in_page = login_page.be_logged_in('arsen@finca.am', 'Pass123()')

    customer_email = 'Hello arsen@finca.am!' 
    
    

    
    assert logged_in_page.read_email() == customer_email

def test_login_without_email_and_password(home):
    login_page = home.nav_to_login_page()

    logged_in_page = login_page.be_logged_in('', '')
    email_error = 'The Email field is required.'
    password_error = 'The Password field is required.'
    

    assert login_page.read_email_error() == email_error
    assert login_page.read_password_error() == password_error
    

