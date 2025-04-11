def move_menu(self, page_select, index) :
    selected_text = page_select.currentText()  
    if selected_text == 'Create User' :
        from admin_page.create_user.create_user import create_user
        create_user(self)
    elif selected_text == "Delete User" :
        from admin_page.delete_user.delete_user import delete_user
        delete_user(self)
    elif selected_text == 'Change Password' :
        from admin_page.change_password.change_password import change_password
        change_password(self)