    def displayPanels(self):
        ###Toolbar panel####
        Toolbar = QLabel(self)
        Toolbar.resize(1440, 79)
        Toolbar.move(0,0)
        Toolbar.setStyleSheet("background-color:rgb(54,54,54);")

        current_directory = str(pathlib.Path(__file__).parent.absolute())
        path = current_directory + '/icons/State_text'
        #print(path)
        State_text_pic = QPixmap(path)
        State_text = QLabel(self)
        State_text.resize(137, 27)
        State_text.move(1150,25)
        State_text.setPixmap(State_text_pic)
        ############

        ###Tape panel####
        Tape = QLabel(self)
        Tape.resize(1440, 152)
        Tape.move(0,60)
        Tape.setStyleSheet("background-color:rgb(49,54,59);") # 39, 41, 45);")

        Right_button = QLabel(self)
        Right_button.resize(45, 80)
        Right_button.move(1395, 95)
        Right_button.setStyleSheet("background-color:rgb(54,54,54);")
        Left_button = QLabel(self)
        Left_button.resize(45, 80)
        Left_button.move(0, 95)
        Left_button.setStyleSheet("background-color:rgb(54,54,54);")
        ############

        ###Undertape panel####
        Undertape = QLabel(self)
        Undertape.resize(1440, 40)
        Undertape.move(0,210)
        Undertape.setStyleSheet("background-color:rgb(37,37,38);")
        ############

        ###Table####
        Back_table = QLabel(self)
        Back_table.resize(1360, 700)
        Back_table.move(40,290)
        Back_table.setStyleSheet("background-color:rgb(37,37,38);")

        Front_table = QLabel(self)
        Front_table.resize(1300, 655)
        Front_table.move(100,335)
        Front_table.setStyleSheet("background-color:rgb(255,255,255);")

        lines1 = list()
        for i in range(0,23):
            lines1.append(QLabel(self))
            lines1[i].resize(1, 700)
            lines1[i].move(100+i*60,290)
            lines1[i].setStyleSheet("background-color:rgb(0,0,0);")

        lines2 = list()
        for i in range(0,15):
            lines2.append(QLabel(self))
            lines2[i].resize(1360, 1)
            lines2[i].move(40,335+i*45)
            lines2[i].setStyleSheet("background-color:rgb(0,0,0);")
        ############
