import robotControllerMethods

def getDriveCommand(move):
    if move == 'Forward':
        robotControllerMethods.Forward()

    elif move == 'Backward':
        robotControllerMethods.Backward()

    elif move == 'Left':
        robotControllerMethods.Left()

    elif move == 'Right':
        robotControllerMethods.Right()

    elif move == 'Stop':
        robotControllerMethods.Stop()
