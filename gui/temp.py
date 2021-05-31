###Pause Button####
        current_directory = str(pathlib.Path(__file__).parent.absolute())
        path = current_directory + '/icons/pause_button'
        pause_button_icon = QIcon()
        pause_button_icon.addPixmap(QPixmap(path), QIcon.Normal, QIcon.Off)

        pause_button = QPushButton(self)
        #run_button.clicked.connect(self.run_buttonClicked)
        pause_button.resize(14, 25)
        pause_button.move(96, 36)
        pause_button.setIcon(pause_button_icon)
        pause_button.setIconSize(QSize(14, 25))
        pause_button.setStyleSheet("border: none;")
        #########

        ####Stop Button####
        current_directory = str(pathlib.Path(__file__).parent.absolute())
        path = current_directory + '/icons/stop_button'
        stop_button_icon = QIcon()
        stop_button_icon.addPixmap(QPixmap(path), QIcon.Normal, QIcon.Off)

        stop_button = QPushButton(self)
        #stop_button.clicked.connect(self.run_buttonClicked)
        stop_button.resize(25, 25)
        stop_button.move(170, 36)
        stop_button.setIcon(stop_button_icon)
        stop_button.setIconSize(QSize(25, 25))
        stop_button.setStyleSheet("border: none;")
        #########

        ####Save Button####
        current_directory = str(pathlib.Path(__file__).parent.absolute())
        path = current_directory + '/icons/save_button'
        save_button_icon = QIcon()
        save_button_icon.addPixmap(QPixmap(path), QIcon.Normal, QIcon.Off)

        save_button = QPushButton(self)
        #run_button.clicked.connect(self.run_buttonClicked)
        save_button.resize(36, 36)
        save_button.move(244, 36)
        save_button.setIcon(save_button_icon)
        save_button.setIconSize(QSize(36,36))
        save_button.setStyleSheet("border: none;")
        #########
        
        ####Reset Button####
        current_directory = str(pathlib.Path(__file__).parent.absolute())
        path = current_directory + '/icons/reset_button'
        reset_button_icon = QIcon()
        reset_button_icon.addPixmap(QPixmap(path), QIcon.Normal, QIcon.Off)

        reset_button = QPushButton(self)
        #run_button.clicked.connect(self.run_buttonClicked)
        reset_button.resize(318, 36)
        reset_button.move(22, 36)
        reset_button.setIcon(reset_button_icon)
        reset_button.setIconSize(QSize(36,36))
        reset_button.setStyleSheet("border: none;")
        #########