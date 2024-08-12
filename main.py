from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import numpy as np
import pandas as pd
import pyqtgraph as pg
from roulette_table_widget import RouletteTableWidget

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

# Data
INPUT_FILE = 'single_chart_input.ods'
OUTPUT_FILE = 'single_chart_output.csv'

# Chart
CHART_HEIGHT = 250
CURRENCY = '§'
COLOUR_POSITIVE = COLOUR_GREEN
COLOUR_NEGATIVE = COLOUR_RED
COLOUR_CHART = COLOUR_GREY
COLOUR_CHART_BACKGROUND = COLOUR_CANVAS
LINE_WIDTH = 6
AXIS_FONT_SIZE = 12
CHART_HIGH = 20
CHART_LOW = -50
TICKS = 10
NUMBERS_DRAWN = 100
BUFFER_VALUE = 4

# Spin Number
SPIN_NUMBER_BOX_FONT_SIZE = 48
SPIN_NUMBER_BOX_SIZE_X = 100
SPIN_NUMBER_BOX_SIZE_Y = SPIN_NUMBER_BOX_SIZE_X
COLOUR_SPIN_NUMBER = COLOUR_WHITE
COLOUR_SPIN_NUMBER_BOX_BORDER = COLOUR_SPIN_NUMBER
SPIN_NUMBER_BOX_X_POS = 18
SPIN_NUMBER_BOX_Y_POS = 20
#
SPIN_NUMBER_TITLE_FONT_SIZE = 16
COLOUR_SPIN_NUMBER_TITLE = COLOUR_WHITE
COLOUR_SPIN_NUMBER_TITLE_BORDER = COLOUR_BLACK
SPIN_NUMBER_TITLE_SIZE_X = 136
SPIN_NUMBER_TITLE_SIZE_Y = int(SPIN_NUMBER_TITLE_FONT_SIZE * 1.55) 
SPIN_NUMBER_TITLE_X_POS = 0
SPIN_NUMBER_TITLE_Y_POS = SPIN_NUMBER_BOX_Y_POS + SPIN_NUMBER_BOX_SIZE_Y
SPIN_NUMBER_TITLE_TEXT = 'Last Spin'

# Cumulative values
CUMULATIVE_VALUE_FONT_SIZE = 24
COLOUR_CUMULATIVE_VALUE = COLOUR_WHITE
COLOUR_CUMULATIVE_VALUE_BORDER = COLOUR_BLACK
CUMULATIVE_VALUE_SIZE_X = SPIN_NUMBER_TITLE_SIZE_X
CUMULATIVE_VALUE_SIZE_Y = CUMULATIVE_VALUE_FONT_SIZE
CUMULATIVE_VALUE_X_POS = 0
CUMULATIVE_VALUE_Y_POS = 200
PEA_GAP = 75
#
CUMULATIVE_VALUE_TITLE_FONT_SIZE = SPIN_NUMBER_TITLE_FONT_SIZE
COLOUR_CUMULATIVE_VALUE_TITLE = COLOUR_SPIN_NUMBER_TITLE
COLOUR_CUMULATIVE_VALUE_TITLE_BORDER = COLOUR_SPIN_NUMBER_TITLE_BORDER
CUMULATIVE_VALUE_TITLE_SIZE_X = CUMULATIVE_VALUE_SIZE_X 
CUMULATIVE_VALUE_TITLE_SIZE_Y = CUMULATIVE_VALUE_TITLE_FONT_SIZE 
CUMULATIVE_VALUE_TITLE_X_POS = CUMULATIVE_VALUE_X_POS
CUMULATIVE_VALUE_TITLE_Y_POS = CUMULATIVE_VALUE_Y_POS + CUMULATIVE_VALUE_SIZE_Y
CUMULATIVE_VALUE_TITLE_TEXT = 'Profit/Loss'

# Expected Percentage Values
EXPECTED_PERCENTAGE_FONT_SIZE = CUMULATIVE_VALUE_FONT_SIZE
EXPECTED_PERCENTAGE_SIZE_X = CUMULATIVE_VALUE_SIZE_X 
EXPECTED_PERCENTAGE_SIZE_Y = EXPECTED_PERCENTAGE_FONT_SIZE
COLOUR_EXPECTED_PERCENTAGE = COLOUR_CUMULATIVE_VALUE
COLOUR_EXPECTED_PERCENTAGE_BORDER = COLOUR_CUMULATIVE_VALUE_BORDER
EXPECTED_PERCENTAGE_X_POS = 0
EXPECTED_PERCENTAGE_Y_POS = CUMULATIVE_VALUE_Y_POS + PEA_GAP
#
EXPECTED_PERCENTAGE_TITLE_FONT_SIZE = SPIN_NUMBER_TITLE_FONT_SIZE
COLOUR_EXPECTED_PERCENTAGE_TITLE = COLOUR_SPIN_NUMBER_TITLE
COLOUR_EXPECTED_PERCENTAGE_TITLE_BORDER = COLOUR_SPIN_NUMBER_TITLE_BORDER
EXPECTED_PERCENTAGE_TITLE_SIZE_X = CUMULATIVE_VALUE_SIZE_X 
EXPECTED_PERCENTAGE_TITLE_SIZE_Y = int(EXPECTED_PERCENTAGE_TITLE_FONT_SIZE * 2.5)
EXPECTED_PERCENTAGE_TITLE_X_POS = CUMULATIVE_VALUE_X_POS
EXPECTED_PERCENTAGE_TITLE_Y_POS = EXPECTED_PERCENTAGE_Y_POS + EXPECTED_PERCENTAGE_SIZE_Y
EXPECTED_PERCENTAGE_TITLE_TEXT = 'Expected\nPercentage'

# Expected Percentage Values
ACTUAL_PERCENTAGE_FONT_SIZE = CUMULATIVE_VALUE_FONT_SIZE
ACTUAL_PERCENTAGE_SIZE_X = CUMULATIVE_VALUE_SIZE_X 
ACTUAL_PERCENTAGE_SIZE_Y = ACTUAL_PERCENTAGE_FONT_SIZE
COLOUR_ACTUAL_PERCENTAGE = COLOUR_CUMULATIVE_VALUE
COLOUR_ACTUAL_PERCENTAGE_BORDER = COLOUR_CUMULATIVE_VALUE_BORDER
ACTUAL_PERCENTAGE_X_POS = 0
ACTUAL_PERCENTAGE_Y_POS = EXPECTED_PERCENTAGE_Y_POS + PEA_GAP
#
ACTUAL_PERCENTAGE_TITLE_FONT_SIZE = SPIN_NUMBER_TITLE_FONT_SIZE
COLOUR_ACTUAL_PERCENTAGE_TITLE = COLOUR_SPIN_NUMBER_TITLE
COLOUR_ACTUAL_PERCENTAGE_TITLE_BORDER = COLOUR_SPIN_NUMBER_TITLE_BORDER
ACTUAL_PERCENTAGE_TITLE_SIZE_X = CUMULATIVE_VALUE_SIZE_X 
ACTUAL_PERCENTAGE_TITLE_SIZE_Y = int(ACTUAL_PERCENTAGE_TITLE_FONT_SIZE * 2.5)
ACTUAL_PERCENTAGE_TITLE_X_POS = CUMULATIVE_VALUE_X_POS
ACTUAL_PERCENTAGE_TITLE_Y_POS = ACTUAL_PERCENTAGE_Y_POS + ACTUAL_PERCENTAGE_SIZE_Y
ACTUAL_PERCENTAGE_TITLE_TEXT = 'Actual\nPercentage'

# Win Values
WINS_FONT_SIZE = 20
WINS_SIZE_X = CUMULATIVE_VALUE_SIZE_X 
WINS_SIZE_Y = WINS_FONT_SIZE
COLOUR_WINS = COLOUR_CUMULATIVE_VALUE
COLOUR_WINS_BORDER = COLOUR_CUMULATIVE_VALUE_BORDER
WINS_X_POS = 0
WINS_Y_POS = 450
WPL_GAP    = 65
#
WINS_TITLE_FONT_SIZE = 18
COLOUR_WINS_TITLE = COLOUR_SPIN_NUMBER_TITLE
COLOUR_WINS_TITLE_BORDER = COLOUR_SPIN_NUMBER_TITLE_BORDER
WINS_TITLE_SIZE_X = CUMULATIVE_VALUE_SIZE_X 
WINS_TITLE_SIZE_Y = WINS_TITLE_FONT_SIZE
WINS_TITLE_X_POS = CUMULATIVE_VALUE_X_POS
WINS_TITLE_Y_POS = WINS_Y_POS + WINS_SIZE_Y
WINS_TITLE_TEXT = 'Wins'

# Pushes Values
PUSHES_FONT_SIZE = WINS_FONT_SIZE
PUSHES_SIZE_X = CUMULATIVE_VALUE_SIZE_X 
PUSHES_SIZE_Y = PUSHES_FONT_SIZE
COLOUR_PUSHES = COLOUR_CUMULATIVE_VALUE
COLOUR_PUSHES_BORDER = COLOUR_CUMULATIVE_VALUE_BORDER
PUSHES_X_POS = 0
PUSHES_Y_POS = WINS_Y_POS + WPL_GAP 
#
PUSHES_TITLE_FONT_SIZE = WINS_TITLE_FONT_SIZE
COLOUR_PUSHES_TITLE = COLOUR_SPIN_NUMBER_TITLE
COLOUR_PUSHES_TITLE_BORDER = COLOUR_SPIN_NUMBER_TITLE_BORDER
PUSHES_TITLE_SIZE_X = CUMULATIVE_VALUE_SIZE_X 
PUSHES_TITLE_SIZE_Y = PUSHES_TITLE_FONT_SIZE
PUSHES_TITLE_X_POS = CUMULATIVE_VALUE_X_POS
PUSHES_TITLE_Y_POS = PUSHES_Y_POS + PUSHES_SIZE_Y
PUSHES_TITLE_TEXT = 'Pushes'

# Losses Values
LOSSES_FONT_SIZE = WINS_FONT_SIZE
LOSSES_SIZE_X = CUMULATIVE_VALUE_SIZE_X 
LOSSES_SIZE_Y = LOSSES_FONT_SIZE
COLOUR_LOSSES = COLOUR_CUMULATIVE_VALUE
COLOUR_LOSSES_BORDER = COLOUR_CUMULATIVE_VALUE_BORDER
LOSSES_X_POS = 0
LOSSES_Y_POS = PUSHES_Y_POS + WPL_GAP 
#
LOSSES_TITLE_FONT_SIZE = WINS_TITLE_FONT_SIZE
COLOUR_LOSSES_TITLE = COLOUR_SPIN_NUMBER_TITLE
COLOUR_LOSSES_TITLE_BORDER = COLOUR_SPIN_NUMBER_TITLE_BORDER
LOSSES_TITLE_SIZE_X = CUMULATIVE_VALUE_SIZE_X 
LOSSES_TITLE_SIZE_Y = LOSSES_TITLE_FONT_SIZE
LOSSES_TITLE_X_POS = CUMULATIVE_VALUE_X_POS
LOSSES_TITLE_Y_POS = LOSSES_Y_POS + LOSSES_SIZE_Y
LOSSES_TITLE_TEXT = 'Pushes'

#Payout Widget
PAYOUT_WIDGET_POS_X = 186
PAYOUT_WIDGET_POS_Y = 660
PAYOUT_WIDGET_WIDTH = 1050
PAYOUT_WIDGET_HEIGHT = 150


# Video (Blanked out area)
COLOUR_VIDEO_PLACEHOLDER = COLOUR_YELLOW
COLOUR_WIDGET_BORDER = COLOUR_YELLOW
UPPER_LEFT_WIDTH = 1150
UPPER_LEFT_HEIGHT = 650
VIDEO_X_POS = 136 # for centre
VIDEO_Y_POS = 0

# Wheel
WHEEL_FORMAT = 'EU-0' #Options EU-0; US-00; or US-000

# To find a place
COLOUR_WIDGET_MARGIN = COLOUR_YELLOW
WIDGET_MARGIN_SIZE=1

####################################################################################################
# Wheel calculations                                                                               #
####################################################################################################

if (WHEEL_FORMAT == 'US-000'):
    NUMBERS_ON_WHEEL = 39
elif (WHEEL_FORMAT == 'US-00'):
    NUMBERS_ON_WHEEL = 38
else: #default and errors are considered European
    NUMBERS_ON_WHEEL = 37

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
# Function to ensure 'Result' remains a distinct string                                            #
####################################################################################################
def ensure_string_result(df):
    df['Result'] = df['Result'].apply(lambda x: str(x))
    return df

####################################################################################################
# Main                                                                                             #
####################################################################################################

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, results, cumulative_values, expected_percentage,scoring, WHEEL_FORMAT):
        super().__init__()

        self.temp_wins = 0  # Initialize the win counter
        self.temp_losses = 0  # Initialize the loss counter
        self.temp_pushes = 0  # Initialize the push counter
        self.actual_percentage = 0

        ############################################################################################
        # Draw canvas                                                                              #
        ############################################################################################        
        self.setWindowTitle(CANVAS_TITLE)
        self.setGeometry(100, 100, WINDOW_WIDTH, WINDOW_HEIGHT)
        self.setStyleSheet(f"background-color: {COLOUR_CANVAS};")

        ############################################################################################
        # Payouts                                                                                  #
        ############################################################################################ 
        self.roulette_table = RouletteTableWidget(scoring, WHEEL_FORMAT, self)
        self.roulette_table.setGeometry(PAYOUT_WIDGET_POS_X, PAYOUT_WIDGET_POS_Y, PAYOUT_WIDGET_WIDTH, PAYOUT_WIDGET_HEIGHT)  # Set the position and size (x, y, width, height)
        self.roulette_table.show()

        ############################################################################################
        # Video Placeholder                                                                        #
        ############################################################################################   
        self.blank_area = QtWidgets.QWidget(self)
        self.blank_area.setGeometry(VIDEO_X_POS, VIDEO_Y_POS, UPPER_LEFT_WIDTH, UPPER_LEFT_HEIGHT)
        self.blank_area.setStyleSheet(f"background-color: {COLOUR_VIDEO_PLACEHOLDER};")

        ############################################################################################
        # Chart                                                                                    #
        ############################################################################################  
        self.plotWidget = pg.PlotWidget(self)
        self.plotWidget.setGeometry(0, WINDOW_HEIGHT - CHART_HEIGHT, WINDOW_WIDTH, CHART_HEIGHT)
        self.plotWidget.setFixedHeight(CHART_HEIGHT)
        self.plotWidget.setBackground(COLOUR_CHART_BACKGROUND)
        self.plotWidget.setXRange(0, NUMBERS_DRAWN) 
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
        # Widget
        self.result_label = QtWidgets.QLabel(self)
        self.result_label.setGeometry(SPIN_NUMBER_BOX_X_POS, SPIN_NUMBER_BOX_Y_POS, SPIN_NUMBER_BOX_SIZE_X, SPIN_NUMBER_BOX_SIZE_Y)  # Adjusted to be square
        self.result_label.setStyleSheet(f"font-size: {SPIN_NUMBER_BOX_FONT_SIZE}px; color: {COLOUR_CANVAS}; font-weight: bold; border: 1px solid {COLOUR_SPIN_NUMBER_BOX_BORDER};")
        self.result_label.setAlignment(QtCore.Qt.AlignCenter)
        # Label
        self.result_title_label = QtWidgets.QLabel(self)
        self.result_title_label.setGeometry(SPIN_NUMBER_TITLE_X_POS, SPIN_NUMBER_TITLE_Y_POS, SPIN_NUMBER_TITLE_SIZE_X, SPIN_NUMBER_TITLE_SIZE_Y)
        self.result_title_label.setStyleSheet(f"font-size: {SPIN_NUMBER_TITLE_FONT_SIZE}px; color: {COLOUR_WHITE}; font-weight: normal; border: 1px solid {COLOUR_SPIN_NUMBER_TITLE_BORDER};")
        self.result_title_label.setAlignment(QtCore.Qt.AlignCenter)
        self.result_title_label.setText(SPIN_NUMBER_TITLE_TEXT)

        ############################################################################################
        # Cumulative value                                                                         #
        ############################################################################################ 
        #Widget
        self.cumulative_value_label = QtWidgets.QLabel(self)
        self.cumulative_value_label.setGeometry(CUMULATIVE_VALUE_X_POS, CUMULATIVE_VALUE_Y_POS, CUMULATIVE_VALUE_SIZE_X, CUMULATIVE_VALUE_SIZE_Y)
        self.cumulative_value_label.setStyleSheet(f"font-size: {CUMULATIVE_VALUE_FONT_SIZE}px; color: {COLOUR_CUMULATIVE_VALUE}; font-weight: bold; border: 1px solid {COLOUR_CUMULATIVE_VALUE_BORDER};")  # Yellow border for development
        self.cumulative_value_label.setAlignment(QtCore.Qt.AlignCenter)
        self.cumulative_value_label.setText(f"{CURRENCY}0.00")  # Initial cumulative value display

        # Label
        self.cumulative_value_title_label = QtWidgets.QLabel(self)
        self.cumulative_value_title_label.setGeometry(CUMULATIVE_VALUE_TITLE_X_POS, CUMULATIVE_VALUE_TITLE_Y_POS, CUMULATIVE_VALUE_TITLE_SIZE_X, CUMULATIVE_VALUE_TITLE_SIZE_Y)
        self.cumulative_value_title_label.setStyleSheet(f"font-size: {CUMULATIVE_VALUE_TITLE_FONT_SIZE}px; color: {COLOUR_WHITE}; font-weight: normal; border: 1px solid {COLOUR_CUMULATIVE_VALUE_BORDER};")
        self.cumulative_value_title_label.setAlignment(QtCore.Qt.AlignCenter)
        self.cumulative_value_title_label.setText(CUMULATIVE_VALUE_TITLE_TEXT)

        ############################################################################################
        # Expected Percentage                                                                      #
        ############################################################################################
        #Widget
        self.expected_percentage_label = QtWidgets.QLabel(self)
        self.expected_percentage_label.setGeometry(EXPECTED_PERCENTAGE_X_POS, EXPECTED_PERCENTAGE_Y_POS, EXPECTED_PERCENTAGE_SIZE_X, EXPECTED_PERCENTAGE_SIZE_Y)
        self.expected_percentage_label.setStyleSheet(f"font-size: {EXPECTED_PERCENTAGE_FONT_SIZE}px; color: {COLOUR_WHITE}; font-weight: bold; border: 1px solid {COLOUR_EXPECTED_PERCENTAGE_BORDER};") 
        self.expected_percentage_label.setAlignment(QtCore.Qt.AlignCenter)
        self.expected_percentage_label.setText(f"{expected_percentage:.1f}%")
        # Label
        self.expected_percentage_title_label = QtWidgets.QLabel(self)
        self.expected_percentage_title_label.setGeometry(EXPECTED_PERCENTAGE_TITLE_X_POS, EXPECTED_PERCENTAGE_TITLE_Y_POS, EXPECTED_PERCENTAGE_TITLE_SIZE_X, EXPECTED_PERCENTAGE_TITLE_SIZE_Y)
        self.expected_percentage_title_label.setStyleSheet(f"font-size: {EXPECTED_PERCENTAGE_TITLE_FONT_SIZE}px; color: {COLOUR_WHITE}; font-weight: normal; border: 1px solid {COLOUR_EXPECTED_PERCENTAGE_BORDER};")
        self.expected_percentage_title_label.setAlignment(QtCore.Qt.AlignCenter)
        self.expected_percentage_title_label.setText(EXPECTED_PERCENTAGE_TITLE_TEXT)

        ############################################################################################
        # Actual Percentage                                                                        #
        ############################################################################################
        #Widget
        self.actual_percentage_label = QtWidgets.QLabel(self)
        self.actual_percentage_label.setGeometry(ACTUAL_PERCENTAGE_X_POS, ACTUAL_PERCENTAGE_Y_POS, ACTUAL_PERCENTAGE_SIZE_X, ACTUAL_PERCENTAGE_SIZE_Y)
        self.actual_percentage_label.setStyleSheet(f"font-size: {ACTUAL_PERCENTAGE_FONT_SIZE}px; color: {COLOUR_WHITE}; font-weight: bold; border: 1px solid {COLOUR_ACTUAL_PERCENTAGE_BORDER};") 
        self.actual_percentage_label.setAlignment(QtCore.Qt.AlignCenter)
        self.actual_percentage_label.setText(f"{self.actual_percentage:.1f}%")
        # Label
        self.actual_percentage_title_label = QtWidgets.QLabel(self)
        self.actual_percentage_title_label.setGeometry(ACTUAL_PERCENTAGE_TITLE_X_POS, ACTUAL_PERCENTAGE_TITLE_Y_POS, ACTUAL_PERCENTAGE_TITLE_SIZE_X, ACTUAL_PERCENTAGE_TITLE_SIZE_Y)
        self.actual_percentage_title_label.setStyleSheet(f"font-size: {ACTUAL_PERCENTAGE_TITLE_FONT_SIZE}px; color: {COLOUR_WHITE}; font-weight: normal; border: 1px solid {COLOUR_ACTUAL_PERCENTAGE_BORDER};")
        self.actual_percentage_title_label.setAlignment(QtCore.Qt.AlignCenter)
        self.actual_percentage_title_label.setText(ACTUAL_PERCENTAGE_TITLE_TEXT)
        
        ############################################################################################
        # Wins                                                                       #
        ############################################################################################
        #Widget
        self.wins_label = QtWidgets.QLabel(self)
        self.wins_label.setGeometry(WINS_X_POS, WINS_Y_POS, WINS_SIZE_X, WINS_SIZE_Y)
        self.wins_label.setStyleSheet(f"font-size: {WINS_FONT_SIZE}px; color: {COLOUR_WHITE}; font-weight: bold; border: 1px solid {COLOUR_WINS_BORDER};") 
        self.wins_label.setAlignment(QtCore.Qt.AlignCenter)
        self.wins_label.setText(f"{self.temp_wins}")
        # Label
        self.wins_title_label = QtWidgets.QLabel(self)
        self.wins_title_label.setGeometry(WINS_TITLE_X_POS, WINS_TITLE_Y_POS, WINS_TITLE_SIZE_X, WINS_TITLE_SIZE_Y)
        self.wins_title_label.setStyleSheet(f"font-size: {WINS_TITLE_FONT_SIZE}px; color: {COLOUR_WHITE}; font-weight: normal; border: 1px solid {COLOUR_WINS_BORDER};")
        self.wins_title_label.setAlignment(QtCore.Qt.AlignCenter)
        self.wins_title_label.setText(WINS_TITLE_TEXT)

        ############################################################################################
        # Pushes                                                                                   #
        ############################################################################################
        #Widget
        self.pushes_label = QtWidgets.QLabel(self)
        self.pushes_label.setGeometry(PUSHES_X_POS, PUSHES_Y_POS, PUSHES_SIZE_X, PUSHES_SIZE_Y)
        self.pushes_label.setStyleSheet(f"font-size: {PUSHES_FONT_SIZE}px; color: {COLOUR_WHITE}; font-weight: bold; border: 1px solid {COLOUR_PUSHES_BORDER};") 
        self.pushes_label.setAlignment(QtCore.Qt.AlignCenter)
        self.pushes_label.setText(f"{self.temp_pushes}")
        # Label
        self.pushes_title_label = QtWidgets.QLabel(self)
        self.pushes_title_label.setGeometry(PUSHES_TITLE_X_POS, PUSHES_TITLE_Y_POS, PUSHES_TITLE_SIZE_X, PUSHES_TITLE_SIZE_Y)
        self.pushes_title_label.setStyleSheet(f"font-size: {PUSHES_TITLE_FONT_SIZE}px; color: {COLOUR_WHITE}; font-weight: normal; border: 1px solid {COLOUR_PUSHES_BORDER};")
        self.pushes_title_label.setAlignment(QtCore.Qt.AlignCenter)
        self.pushes_title_label.setText(PUSHES_TITLE_TEXT)

        ############################################################################################
        # Losses                                                                                   #
        ############################################################################################
        #Widget
        self.losses_label = QtWidgets.QLabel(self)
        self.losses_label.setGeometry(LOSSES_X_POS, LOSSES_Y_POS, LOSSES_SIZE_X, LOSSES_SIZE_Y)
        self.losses_label.setStyleSheet(f"font-size: {LOSSES_FONT_SIZE}px; color: {COLOUR_WHITE}; font-weight: bold; border: 1px solid {COLOUR_LOSSES_BORDER};") 
        self.losses_label.setAlignment(QtCore.Qt.AlignCenter)
        self.losses_label.setText(f"{self.temp_losses}")
        # Label
        self.losses_title_label = QtWidgets.QLabel(self)
        self.losses_title_label.setGeometry(LOSSES_TITLE_X_POS, LOSSES_TITLE_Y_POS, LOSSES_TITLE_SIZE_X, LOSSES_TITLE_SIZE_Y)
        self.losses_title_label.setStyleSheet(f"font-size: {LOSSES_TITLE_FONT_SIZE}px; color: {COLOUR_WHITE}; font-weight: normal; border: 1px solid {COLOUR_LOSSES_BORDER};")
        self.losses_title_label.setAlignment(QtCore.Qt.AlignCenter)
        self.losses_title_label.setText(LOSSES_TITLE_TEXT)

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Space:
            
            if self.index < len(self.results):  # Ensure index is within bounds
                # Update the result and colour based on roulette rules
                result = str(self.results[self.index])
                spin_colour = get_roulette_colour(result)
                self.result_label.setText(result)
                self.result_label.setStyleSheet(f"font-size: {SPIN_NUMBER_BOX_FONT_SIZE }px; color: {COLOUR_SPIN_NUMBER}; font-weight: bold; background-color: {spin_colour}; border: 1px solid {COLOUR_SPIN_NUMBER_BOX_BORDER};")

                # Check the current index and cumulative value for debugging
                #print(f"Current index: {self.index}")
                #print(f"Cumulative Values: {self.cumulative_values}")
                
                # Update the cumulative value with currency sign
                if self.index + 1 < len(self.cumulative_values):
                    cumulative_value = self.cumulative_values[self.index + 1]  # Adjust index for cumulative
                    #print(f"Cumulative value: {cumulative_value}")  # Debugging
                    self.cumulative_value_label.setText(f"{CURRENCY}{cumulative_value:.1f}")
                else:
                    pass
                    #print("Index out of range for cumulative values")

                # Plot the cumulative values up to the current index
                y = self.cumulative_values[:self.index + 2]  # Adjust index for cumulative
                pen = pg.mkPen(color=COLOUR_POSITIVE if y[-1] >= 0 else COLOUR_NEGATIVE, width=LINE_WIDTH)
                self.plot.setData(x=np.arange(len(y)), y=y, pen=pen)
                self.plotWidget.addLine(y=0, pen=pg.mkPen(color=COLOUR_CHART, width=2, style=QtCore.Qt.DotLine))
                # Increment counters based on the value of Change
                if df['Change'][self.index] > 0:
                    self.temp_wins += 1
                elif df['Change'][self.index] < 0:
                    self.temp_losses += 1
                else:
                    self.temp_pushes += 1

                # Update the labels
                self.wins_label.setText(str(self.temp_wins))
                self.losses_label.setText(str(self.temp_losses))
                self.pushes_label.setText(str(self.temp_pushes))

                self.index += 1
                actual_percentage = self.temp_wins / self.index *100
                self.actual_percentage_label.setText(f"{actual_percentage:.1f}%")
    
    def set_currency_labels(self, low, high, step):
        currency_labels = {}
        for i in range(low, high + 1, step):
            currency_labels[i] = f'{CURRENCY}{i:,.2f}' if i >= 0 else f'-{CURRENCY}{abs(i):,.2f}'
        return currency_labels

####################################################################################################
# Main                                                                                             #
####################################################################################################
if __name__ == '__main__':
    # Load the application
    app = QtWidgets.QApplication(sys.argv)
    
    # Load and process data
    df = pd.read_excel(INPUT_FILE, sheet_name='results', dtype={'Result': str})
    scoring = pd.read_excel(INPUT_FILE, sheet_name='scoring', dtype={'Result': str})

    # Ensure 'Change' is treated as an integer for calculations
    scoring['Change'] = pd.to_numeric(scoring['Change'], errors='coerce')
    
    # Merge data on 'Result'
    df = pd.merge(df, scoring, on='Result', how='left')

    # Calculate cumulative values
    df['Cumulative'] = df['Change'].cumsum()

    # Calculate expected and actual percentages
    winning_spins = scoring[scoring['Change'] > 0].shape[0]
    expected_percentage = (winning_spins / NUMBERS_ON_WHEEL) * 100

    # Save the output to CSV
    df.to_csv(OUTPUT_FILE, index=False)
    
    # Prepare the cumulative array
    cumulative = df['Cumulative'].to_numpy()
    cumulative = np.insert(cumulative, 0, 0)
        
    results = df['Result'].tolist()

    # Initialize the main window with processed data
    window = MainWindow(results, cumulative, expected_percentage, scoring, WHEEL_FORMAT)
    window.show()

    # Start the application loop
    sys.exit(app.exec_())
