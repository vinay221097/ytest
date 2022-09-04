from PyQt5.QtWidgets import QApplication
from PyQt5 import QtWidgets,QtWebEngineWidgets,QtCore
from PyQt5.QtCore import QUrl,Qt,QEvent
from PyQt5.QtWebEngineWidgets import QWebEngineView
import os,sys
from pywinauto.application import Application
from PyQt5 import QtGui
url = 'https://www.youtube.com/watch?v=ku3HSNT0I-g'

# app = QApplication(sys.argv)


# browser = QWebEngineView()
# browser.load(QUrl(url))
# browser.triggerAction(QWebEnginePage.Back)
key_event = QtGui.QKeyEvent(QEvent.KeyPress,Qt.Key_Space, Qt.NoModifier, " ")
# QtCore.QCoreApplication.sendEvent(self.titleEdit, key_event)
# app.postEvent(browser, key_event)
# sys.exit(app.exec_()) 

def html_to_pdf(html, pdf):
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowTitle("myapp")
    app2 = Application(backend="uia").connect(title_re=".*myapp*") 

    page = QtWebEngineWidgets.QWebEngineView()

    def handle_print_finished(filename, status):
        print("finished", filename, status)
        QtWidgets.QApplication.quit()

    def handle_load_finished(status):
        if status:
            page.show()
            app.postEvent(page, key_event)
            # page.printToPdf(pdf)
        else:
            print("Failed")
            QtWidgets.QApplication.quit()



    # page.pdfPrintingFinished.connect(handle_print_finished)
    page.loadFinished.connect(handle_load_finished)
    page.load(QtCore.QUrl('https://www.youtube.com/watch?v=ku3HSNT0I-g'))
    
    


    app.exec_()


if __name__ == "__main__":

    CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
    filename = os.path.join(CURRENT_DIR, "index.html")
    print(filename)

    html_to_pdf(filename, "test.pdf")