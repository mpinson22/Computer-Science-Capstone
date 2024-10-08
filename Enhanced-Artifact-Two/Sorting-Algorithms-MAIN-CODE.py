import PySimpleGUI as sg
import matplotlib.pyplot as plt
import numpy as np

# ------------------------------------------------GUI Interface------------------------------------------------
layout = [[sg.Push(), sg.Text(text='Welcome to the Sorting Algorithms Applet!',
                              size=(41, 1),
                              font=('Georgia', 25),
                              justification='center',
                              pad=((0, 0), (20, 0)),
                              auto_size_text=True,
                              key='title'), sg.Push()],
          [sg.HorizontalSeparator(pad=(20, 20))],
          [sg.Push(),
           sg.Checkbox('Bubble Sort', font='Georgia', auto_size_text=True, key='-BUBBLE-', enable_events=True),
           sg.Checkbox('Selection Sort', font='Georgia', auto_size_text=True, key='-SELECTION-', enable_events=True),
           sg.Checkbox('Quick Sort', font='Georgia', auto_size_text=True, key='-QUICK-', enable_events=True),
           sg.Checkbox('Merge Sort', font='Georgia', auto_size_text=True, key='-MERGE-', enable_events=True),
           sg.Push()],
          [sg.HorizontalSeparator(pad=(20, 20))],
          [sg.Text(text='Enter a number of values to be sorted (1-500)*:',
                   size=(50, 1),
                   font='Georgia',
                   justification='left',
                   pad=((0, 0), (0, 8)),
                   key='enter-vals')],
          [sg.Push(), sg.Input(default_text='',
                               font=('Georgia', 15),
                               enable_events=True,
                               key='-NUM-INPUT-'), sg.Push()],
          [sg.HorizontalSeparator(pad=(20, 20))],
          [sg.Text(text='Enter an upper bound for values in the data set (1-500)*:',
                   size=(50, 1),
                   font=('Georgia', 15),
                   justification='left',
                   pad=((0, 0), (0, 8)),
                   key='enter-max')],
          [sg.Push(), sg.Input(default_text='',
                               font=('Georgia', 15),
                               enable_events=True,
                               key='-MAX-INPUT-'), sg.Push()],
          [sg.HorizontalSeparator(pad=(20, 20))],
          [sg.Push(), sg.Button('Plot', expand_x=True, pad=((0, 0), (0, 10))), sg.Push()],
          [sg.Push(), sg.Button('Stop', expand_x=True, pad=((0, 0), (10, 0)), disabled=True), sg.Push()],
          [sg.HorizontalSeparator(pad=(20, 10))],
          [sg.Push(), sg.Text(text='',
                              font='Georgia',
                              justification='center',
                              key='-DIALOG-BOX-',
                              expand_y=True), sg.Push()],
          [sg.Text(text='*Optimal animation performance with sample sizes less than or equal to 100',
                   font=('Georgia', 10))]]

main_window = sg.Window('Sorting Algorithms', layout, size=(750, 750))


# ----------------------------------------------------------------------------------------------------------------------

# Resets the interface after a successful sort or user interrupt
def resetInterface(window):
    window['-BUBBLE-'].update(value=False, disabled=False)
    window['-SELECTION-'].update(value=False, disabled=False)
    window['-QUICK-'].update(value=False, disabled=False)
    window['-MERGE-'].update(value=False, disabled=False)
    window['Stop'].update(disabled=True)
    window['-NUM-INPUT-'].update(value='')
    window['-MAX-INPUT-'].update(value='')


# Exception for handling a user interrupt via the 'Stop' button
class UserInterrupt(Exception):
    # Raised when user presses the stop button in the GUI window
    pass


# ------------------------------------------------Sorting Algorithms------------------------------------------------

# BUBBLE SORT ALGORITHM
# takes as parameters maximum value, number of values, and the GUI window to listen for events
def bubble_sort(maxVal, n, window):
    # creates a random list of n numbers ranging from 0 to max
    numList = list(np.random.randint(low=1, high=maxVal + 1, size=n))
    # defines a set x of all the whole numbers between 0 and n inclusive
    x = np.arange(0, n, 1)
    # initializes empty vector for bar colors
    colors = []
    # iterates through entire list
    for i in range(n):
        # iterates through unsorted part of list
        for j in range(0, n - i - 1):
            for k in range(n):
                # assigns a color that will be more red or blue based
                # on the proportion between a given value and the maximum value
                color = ((numList[k] / maxVal), 0.0, 1 - (numList[k] / maxVal))
                colors.append(color)
            # plots a bar graph of all the values in the list with their corresponding colors
            plt.title('Bubble Sort')
            plt.bar(x, numList, color=colors)
            # pauses to create a frame
            plt.pause(0.001)
            # listens for an interrupt from user to exit function
            plot_events, plot_values = window.read(timeout=1)
            if plot_events == 'Stop':
                plt.close('all')
                raise UserInterrupt
            # clears the graph to prepare for the next iteration of the list to be plotted
            plt.clf()
            # clears the color vector to keep it a reasonable size
            colors.clear()
            # swaps two values if a given value is larger than the value to its "right"
            if numList[j] > numList[j + 1]:
                numList[j], numList[j + 1] = numList[j + 1], numList[j]
    return numList


# SELECTION SORT ALGORITHM
# takes as parameters: maximum value, number of values, and the GUI window to listen for events
def selection_sort(maxVal, n, window):
    numList = list(np.random.randint(low=1, high=maxVal + 1, size=n))
    x = np.arange(0, n, 1)
    colors = []
    for i in range(n):
        minVal = i
        for j in range(i + 1, n):
            # finds the index of the smallest value in the list
            if numList[j] < numList[minVal]:
                minVal = j
        if minVal != i:
            for k in range(n):
                color = ((numList[k] / maxVal), 0.0, 1 - (numList[k] / maxVal))
                colors.append(color)
            plt.title('Selection Sort')
            plt.bar(x, numList, color=colors)
            plt.pause(0.001)
            plot_events, plot_values = window.read(timeout=1)
            if plot_events == 'Stop':
                plt.close('all')
                raise UserInterrupt
            plt.clf()
            # swaps the minimum value with the value at index i
            numList[minVal], numList[i] = numList[i], numList[minVal]
            colors.clear()

    return numList


# PARTITION ALGORITHM FOR QUICK SORT
# takes as parameters: a list of numbers, starting index, ending index, number of values, maximum value, and the GUI
# window to listen for events
def partition(numList, begin, end, n, maxVal, window):
    plot_events, plot_values = window.read(timeout=1)
    if plot_events == 'Stop':
        plt.close('all')
        raise UserInterrupt
    # initializes low and high indices
    low = begin + 1
    high = end

    pivot = numList[begin]

    x = np.arange(0, n, 1)
    colors = []
    while True:
        # increments the low index while values at the low index are less than the pivot value
        while low <= high and numList[low] <= pivot:
            low += 1
        # decrements the high index while values at the high index are greater than the pivot value
        while high >= low and numList[high] >= pivot:
            high -= 1
        if low >= high:
            break
        else:
            for k in range(n):
                color = ((numList[k] / maxVal), 0.0, 1 - (numList[k] / maxVal))
                colors.append(color)
            plt.title('Quick Sort')
            plt.bar(x, numList, color=colors)
            plt.pause(0.001)
            plt.clf()
            colors.clear()
            # swaps two values when they are on the "wrong" side of the pivot
            numList[low], numList[high] = numList[high], numList[low]

            low += 1
            high -= 1
    for k in range(n):
        color = ((numList[k] / maxVal), 0.0, 1 - (numList[k] / maxVal))
        colors.append(color)
    plt.title('Quick Sort')
    plt.bar(x, numList, color=colors)
    plt.pause(0.001)
    plt.clf()
    colors.clear()
    numList[begin], numList[high] = numList[high], numList[begin]

    return high


# QUICK SORT ALGORITHM (recursive)
# takes as parameters: a list of numbers, a beginning index, an ending index, a number of values, and a maximum value
def quick_sort(numList, begin, end, n, maxVal, window):
    plot_events, plot_values = window.read(timeout=1)
    if plot_events == 'Stop':
        plt.close('all')
        raise UserInterrupt
    # exits the function call if the beginning index is greater than the ending index
    # which indicates that a particular portion of the list is sorted properly.
    if begin >= end:
        return
    # finds the midpoint by using the partition function
    mid = partition(numList, begin, end, n, maxVal, window)

    # recursively calls quick sort on either side of the partition
    quick_sort(numList, begin, mid - 1, n, maxVal, window)
    quick_sort(numList, mid + 1, end, n, maxVal, window)

    return numList


# MERGE FUNCTION FOR MERGE SORT
# takes as parameters: a list of numbers, a left index, a right index, and a middle index
def merge_func(numList, left, right, middle):
    # defines left and right partitions by copying halves of the original list
    leftPartition = numList[left:middle + 1]
    rightPartition = numList[middle + 1:right + 1]

    low = 0
    high = 0

    for i in range(left, right + 1):
        # if branch is executed when the left and right partitions each have unsorted parts
        if low < len(leftPartition) and high < len(rightPartition):
            # the partitions are already sorted, so this function will thread the two lists together by
            # selecting the smallest unmerged value and putting it into its respective index in the
            # original list of numbers.
            if leftPartition[low] <= rightPartition[high]:
                numList[i] = leftPartition[low]
                low += 1
            else:
                numList[i] = rightPartition[high]
                high += 1
        # accounts for the case that all values of the right partition have
        # been placed and copies the remainder of the left partition to the list
        elif low < len(leftPartition):
            numList[i] = leftPartition[low]
            low += 1
        # accounts for the case that all values of the left partition have
        # been placed and copies the remainder of the right partition to the list
        elif high < len(rightPartition):
            numList[i] = rightPartition[high]
            high += 1


# MERGE SORT ALGORITHM (recursive)
# takes as parameters: a list of numbers, a left index, a right index,a maximum value, a number of values,
# and the GUI window to listen for events
def merge_sort(numList, left, right, maxVal, n, window):
    plot_events, plot_values = window.read(timeout=1)
    if plot_events == 'Stop':
        plt.close('all')
        raise UserInterrupt
    x = np.arange(0, n, 1)
    colors = []
    # exits function call if left index is larger than right index
    # which indicates that portion of the list has been sorted
    if left >= right:
        return

    # finds the midpoint index of the list
    mid = (left + right) // 2

    for k in range(len(numList)):
        color = ((numList[k] / maxVal), 0.0, 1 - (numList[k] / maxVal))
        colors.append(color)
    plt.title('Merge Sort')
    plt.bar(x, numList, color=colors)
    plt.pause(.001)
    plt.clf()
    colors.clear()

    # recursively calls merge sort on either side of the midpoint index
    merge_sort(numList, left, mid, maxVal, n, window)
    for k in range(len(numList)):
        color = ((numList[k] / maxVal), 0.0, 1 - (numList[k] / maxVal))
        colors.append(color)
    plt.title('Merge Sort')
    plt.bar(x, numList, color=colors)
    plt.pause(.001)
    plt.clf()
    colors.clear()
    merge_sort(numList, mid + 1, right, maxVal, n, window)

    # merges the lists on either side of the midpoint
    merge_func(numList, left, right, mid)

    for k in range(len(numList)):
        color = ((numList[k] / maxVal), 0.0, 1 - (numList[k] / maxVal))
        colors.append(color)
    plt.title('Merge Sort')
    plt.bar(x, numList, color=colors)
    plt.pause(.001)
    plt.clf()
    colors.clear()

    return numList


# ------------------------------------------------Main Code------------------------------------------------
def main():
    # GUI event loop
    while True:
        event, values = main_window.read()
        # if user closes the window
        if event in (sg.WIN_CLOSED, 'Cancel'):
            break
        # event listener for text input boxes
        elif event == '-NUM-INPUT-' or event == '-MAX-INPUT-':
            plt.close()
            num = values[event]
            # input verification
            try:
                # will throw ValueError exception if user attempts to enter non-numerical input
                numInt = int(num)

                if numInt > 500:
                    main_window[event].update(value='500', text_color='black', font=('Georgia', 15))
                if num[0] == '0':  # checks for 0 value
                    main_window[event].update(value='Cannot be zero', text_color='gray', font=('Georgia', 15, 'italic'))
                elif len(num) > 3:  # limits user input to 3 characters
                    main_window[event].update(value=num[0:3], text_color='black', font=('Georgia', 15))

            except ValueError:
                # exception displays user feedback to guide correct input
                if num != '' and num[0].isalpha() and num[-1] == '0':
                    main_window[event].update(value='Cannot be zero', text_color='gray', font=('Georgia', 15, 'italic'))
                    continue
                acceptableChars = ''
                for i in range(0, len(num)):
                    if num[i].isdigit():
                        acceptableChars += num[i]
                main_window[event].update(value=acceptableChars[0:3], text_color='black', font=('Georgia', 15))
                if acceptableChars == '':
                    main_window[event].update(value='Only numerical input is allowed',
                                              text_color='gray',
                                              font=('Georgia', 15, 'italic'))
                    continue

        # event listener for checkboxes
        elif event in ['-BUBBLE-', '-SELECTION-', '-QUICK-', '-MERGE-']:
            if values[event]:  # ensures that only one checkbox can be selected at a time
                for checkbox in ['-BUBBLE-', '-SELECTION-', '-QUICK-', '-MERGE-']:
                    main_window[checkbox].update(disabled=True)
                main_window[event].update(disabled=False)
            else:  # enables all checkboxes when a checkbox is unselected
                for checkbox in ['-BUBBLE-', '-SELECTION-', '-QUICK-', '-MERGE-']:
                    main_window[checkbox].update(disabled=False)

        # event listener for plot button
        elif event == 'Plot':
            # provides user feedback if either field is empty
            if values['-MAX-INPUT-'] != '' and values['-NUM-INPUT-'] != '':
                userMax = int(values['-MAX-INPUT-'])
                userCount = int(values['-NUM-INPUT-'])
            else:
                main_window['-DIALOG-BOX-'].update(value='All fields required. Please try again.')
                continue
            colors = []

            # calls sorting algorithm based on user checkbox selection at the time of 'Plot' button event
            if values['-BUBBLE-']:
                # try/except structure enables user to interrupt the plotting of the sort
                try:
                    main_window['Stop'].update(disabled=False)  # enables 'Stop' button while sort is happening
                    sortedList = bubble_sort(userMax, userCount, main_window)
                except UserInterrupt:
                    sortedList = []
            elif values['-SELECTION-']:
                try:
                    main_window['Stop'].update(disabled=False)
                    sortedList = selection_sort(userMax, userCount, main_window)
                except UserInterrupt:
                    sortedList = []
            elif values['-QUICK-']:
                try:
                    main_window['Stop'].update(disabled=False)
                    sortedList = quick_sort(list(np.random.randint(low=1, high=userMax + 1, size=userCount)), 0,
                                            userCount - 1, userCount, userMax, main_window)
                except UserInterrupt:
                    sortedList = []
            elif values['-MERGE-']:
                try:
                    main_window['Stop'].update(disabled=False)
                    sortedList = merge_sort(list(np.random.randint(low=1, high=userMax + 1, size=userCount)), 0,
                                            userCount, userMax, userCount, main_window)
                except UserInterrupt:
                    sortedList = []
            else:  # executes if user has not selected any of the checkboxes
                main_window['-DIALOG-BOX-'].update(value='Please select a sorting algorithm.')
                continue
            # accounts for user interrupt
            if len(sortedList) == 0:
                main_window['-DIALOG-BOX-'].update(value='User has cancelled plotting process')
                resetInterface(main_window)
                continue

            # plots the sorted data
            x = np.arange(0, userCount, 1)
            for k in range(0, userCount):
                color = ((sortedList[k] / userMax), 0.0, 1 - (sortedList[k] / userMax))
                colors.append(color)
            plt.title('All Done')
            plt.bar(x, sortedList, color=colors)
            plt.show()

            # resets the interface to prepare for another sorting call
            main_window['-DIALOG-BOX-']. \
                update(value='Sort successfully completed\nPlease run another sort, or close the window to exit.')
            resetInterface(main_window)

    # closes the window upon user exit
    main_window.close()


if __name__ == "__main__":
    main()
