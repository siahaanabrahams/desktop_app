def move_menu(self, page_select, index) :
    selected_text = page_select.currentText()  
    if selected_text == 'Upload' :
        from detect_page.upload_menu.upload_menu import upload_menu
        upload_menu(self)
    elif selected_text == "Real Time" :
        from detect_page.real_time.real_time import real_time
        real_time(self)