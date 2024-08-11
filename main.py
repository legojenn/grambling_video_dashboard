####################################################################################################
# Modules                                                                                       #
####################################################################################################

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import numpy as np
import pandas as pd
import pyqtgraph as pg

####################################################################################################
# Constants                                                                                        #
####################################################################################################

# Colour Names
COLOUR_GREEN = '#00FF00'
COLOUR_RED = '#FF0000'
COLOUR_BLACK = '#000000'
COLOUR_WHITE = '#FFFFFF'
COLOUR_YELLOW = 'yellow'
COLOUR_GREY = 'grey'

# Canvas
WINDOW_WIDTH = 1920
WINDOW_HEIGHT = 1080
CANVAS_TITLE = 'Video Background'
COLOUR_CANVAS = COLOUR_BLACK
COLOUR_VIDEO_PLACEHOLDER = COLOUR_YELLOW
COLOUR_WIDGET_BORDER = COLOUR_YELLOW

#Data
INPUT_FILE = 'single_chart_input.ods'
OUTPUT_FILE = 'single_chart_output.csv'

# Chart
CHART_HEIGHT = 200
UPPER_LEFT_WIDTH = int(WINDOW_WIDTH * 0.65)
UPPER_LEFT_HEIGHT = int(WINDOW_HEIGHT * 0.65)
CURRENCY = '§'
COLOUR_POSITIVE = COLOUR_GREEN
COLOUR_NEGATIVE = COLOUR_RED
COLOUR_CHART = COLOUR_GREY
COLOUR_CHART_BACKGROUND = COLOUR_CANVAS
LINE_WIDTH = 6
AXIS_FONT_SIZE = 12
CHART_HIGH = 50
CHART_LOW = -350
TICKS = 50
NUMBERS_DRAWN = 100
BUFFER_VALUE =4

# Spun Number
SPUN_NUMBER_SIZE = 36
BOX_SIZE = 100
COLOUR_SPUN_BORDER = COLOUR_WHITE
SPUN_NUMBER_X = 1800
SPUN_NUMBER_Y =   20

# Cumulative values
CUMULATIVE_SIZE = 36
COLOUR_CUMULATIVE = COLOUR_WHITE
COLOUR_CUMULATIVE_BORDER = COLOUR_WHITE

# To find a place
COLOUR_WIDGET_MARGIN = COLOUR_YELLOW
WIDGET_MARGIN_SIZE=1

####################################################################################################
# Get number colour                                                                                #
####################################################################################################
# Function to determine the colour based on the roulette number
def get_roulette_colour(number):
    if number in ['0', '00']:
        return COLOUR_GREEN
    # Red numbers on a roulette wheel
    red_numbers = ['1', '3', '5', '7', '9', '12', '14', '16', '18', '19', '21', '23', '25', '27', '30', '32', '34', '36']
    return COLOUR_RED if number in red_numbers else COLOUR_BLACK

####################################################################################################
# Main                                                                                             #
####################################################################################################

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, results, cumulative_values):
        super().__init__()
        ############################################################################################
        # Draw canvas                                                                              #
        ############################################################################################        
        self.setWindowTitle(CANVAS_TITLE)
        self.setGeometry(100, 100, WINDOW_WIDTH, WINDOW_HEIGHT)
        self.setStyleSheet(f"background-color: {COLOUR_CANVAS};")

        # Blanked out upper left corner (video goes here)
        self.blank_area = QtWidgets.QWidget(self)
        self.blank_area.setGeometry(0, 0, UPPER_LEFT_WIDTH, UPPER_LEFT_HEIGHT)
        self.blank_area.setStyleSheet(f"background-color: {COLOUR_VIDEO_PLACEHOLDER};")

        ############################################################################################
        # Chart                                                                                    #
        ############################################################################################  
        self.plotWidget = pg.PlotWidget(self)
        self.plotWidget.setGeometry(0, WINDOW_HEIGHT - CHART_HEIGHT, WINDOW_WIDTH, CHART_HEIGHT)
        self.plotWidget.setFixedHeight(CHART_HEIGHT)
        self.plotWidget.setBackground(COLOUR_CHART_BACKGROUND)
        self.plotWidget.setXRange(0, NUMBERS_DRAWN + BUFFER_VALUE) 
        self.plotWidget.setYRange(CHART_LOW - (TICKS/5), CHART_HIGH + (TICKS/5))
        self.plotWidget.showGrid(x=False, y=True)
        self.plotWidget.setStyleSheet(f"border: {WIDGET_MARGIN_SIZE}px solid {COLOUR_WIDGET_MARGIN};")  # Yellow border for development

        self.plot = None
        self.results = results  # Store the roulette results
        self.cumulative_values = cumulative_values  # Store the cumulative values
        self.index = 0

        self.plotWidget.keyPressEvent = self.keyPressEvent

        # Plot the initial empty point at (0,0)
        self.plot = self.plotWidget.plot(pen=pg.mkPen(color=COLOUR_POSITIVE, width=LINE_WIDTH))
        self.plot.setData([0], [0])

        # Format y-axis labels as currency
        currency_labels = self.set_currency_labels(CHART_LOW, CHART_HIGH, TICKS)
        y_axis = self.plotWidget.getAxis('left')
        y_axis.setTicks([currency_labels.items()])
        font_y = QtGui.QFont()
        font_y.setPointSize(AXIS_FONT_SIZE)
        font_y.setBold(True)
        y_axis.setTickFont(font_y)

        x_axis = self.plotWidget.getAxis('bottom')
        font_x = QtGui.QFont()
        font_x.setPointSize(AXIS_FONT_SIZE)
        font_x.setBold(True)
        x_axis.setTickFont(font_x)

        ############################################################################################
        # Last spin                                                                                #
        ############################################################################################ 
        self.result_label = QtWidgets.QLabel(self)
        self.result_label.setGeometry(SPUN_NUMBER_X, SPUN_NUMBER_Y, BOX_SIZE, BOX_SIZE)  # Adjusted to be square
        self.result_label.setStyleSheet(f"font-size: {SPUN_NUMBER_SIZE}px; color: {COLOUR_CANVAS}; font-weight: bold; border: 1px solid {COLOUR_SPUN_BORDER};")
        self.result_label.setAlignment(QtCore.Qt.AlignCenter)

        ############################################################################################
        # Cumulative value                                                                         #
        ############################################################################################ 
        self.cumulative_value_label = QtWidgets.QLabel(self)
        self.cumulative_value_label.setGeometry(UPPER_LEFT_WIDTH + 240, 20, 200, 100)
        self.cumulative_value_label.setStyleSheet(f"font-size: {CUMULATIVE_SIZE}px; color: {COLOUR_CUMULATIVE}; font-weight: bold; border: 1px solid {COLOUR_CUMULATIVE_BORDER};")  # Yellow border for development
        self.cumulative_value_label.setAlignment(QtCore.Qt.AlignCenter)
        self.cumulative_value_label.setText(f"{CURRENCY}0.00")  # Initial cumulative value display

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Space:
            if self.index < len(self.results):  # Ensure index is within bounds
                # Update the result and colour based on roulette rules
                result = str(self.results[self.index])
                spin_colour = get_roulette_colour(result)
                self.result_label.setText(result)
                self.result_label.setStyleSheet(f"font-size: {SPUN_NUMBER_SIZE}px; color: {COLOUR_WHITE}; font-weight: bold; background-color: {spin_colour}; border: 1px solid {COLOUR_SPUN_BORDER};")

                # Update the cumulative value with currency sign
                cumulative_value = self.cumulative_values[self.index + 1]  # Adjust index for cumulative
                self.cumulative_value_label.setText(f"{CURRENCY}{cumulative_value:.2f}")

                # Plot the cumulative values up to the current index
                y = self.cumulative_values[:self.index + 2]  # Adjust index for cumulative
                pen = pg.mkPen(color=COLOUR_POSITIVE if y[-1] >= 0 else COLOUR_NEGATIVE, width=LINE_WIDTH)
                self.plot.setData(x=np.arange(len(y)), y=y, pen=pen)
                self.plotWidget.addLine(y=0, pen=pg.mkPen(color=COLOUR_CHART, width=2, style=QtCore.Qt.DotLine))

                self.index += 1
    
    def set_currency_labels(self, low, high, step):
        currency_labels = {}
        for i in range(low, high + 1, step):
            currency_labels[i] = f'{CURRENCY}{i:,.2f}' if i >= 0 else f'-{CURRENCY}{abs(i):,.2f}'
        return currency_labels

if __name__ == '__main__':
    ############################################################################################
    # Load widgets                                                                             #
    ############################################################################################  
    app = QtWidgets.QApplication(sys.argv)
    ############################################################################################
    # Load data                                                                                #
    ############################################################################################ 
    df = pd.read_excel(INPUT_FILE, "results")
    scoring = pd.read_excel(INPUT_FILE, "scoring")
    df = pd.merge(df, scoring, on='Result', how='left')
    df['Cumulative'] = df['Change'].cumsum()
    ############################################################################################
    # Export Data                                                                              #
    ############################################################################################
    df.to_csv(OUTPUT_FILE, index=False)



    ############################################################################################
    # TBD                                                                                      #
    ############################################################################################
    cumulative = df['Cumulative'].to_numpy()
    # Add a zero at the beginning of the cumulative array
    cumulative = np.insert(cumulative, 0, 0)
    cumulative = cumulative[-105:]
    results = df['Result'].tolist()

    window = MainWindow(results, cumulative)
    window.show()
    sys.exit(app.exec_())
