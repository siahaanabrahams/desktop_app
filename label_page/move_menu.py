def move_menu(self, page_select, index) :
    selected_text = page_select.currentText()  
    if selected_text == 'Anomaly' :
        from label_page.anomaly.anomaly import anomaly
        anomaly(self)
    elif selected_text == "Defect" :
        from label_page.defect.defect import defect
        defect(self)