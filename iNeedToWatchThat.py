#imports
import time

def testcreatefiles():
    '''
    () -> ()
    Checks to see if .txt files needed for program is present
    If not found, creates new formatted files
    '''
    try:
        towatch = open('towatch.txt','r')
        
    except:
        print('towatch.txt does not exist...')
        print('Creating new file...')
        createtowatch()
        towatch = open('towatch.txt','r')
    
    try:
        watched = open('watched.txt','r')
    except:
        print('towatch.txt does not exist...')
        print('Creating new file...')
        createwatched()
        watched = open('watched.txt','r')

    towatch.close()
    watched.close()

def havewatched():
    '''
    () -> (boolean)

    Ask user if they have watched the film or not
    '''
    status = {'1': False, '2': True}

    validchoice = False

    while not validchoice:
        print('Did you watch this title yet?')
        print('[1] No (Add this title to your "to-watch" list)')
        print('[2] Yes (Add to your "watched" list)')
        userstatus = input('Enter the number of your answer: ')
        if userstatus in status:
            validchoice = True
        else:
            print('ERROR: Invalid input, please try again...')
    
    return status[userstatus]

def createtowatch():
    '''
    () -> ()
    Creates new towatch.txt file with formatted header
    '''
    header = ['[Title]', '[Type]', '[Date Entered]']
    outfile = open('towatch.txt','w')
    for item in header:
        part = item + '\t'
        outfile.write(part)
    outfile.write('\n')
    outfile.close()

def createwatched():
    '''
    () -> ()
    Creates new watched.txt file with formatted header
    '''
    header = ['[Title]', '[Type]', '[Watch Count]', '[Last Watched]']
    outfile = open('watched.txt', 'w')
    for item in header:
        part = item + '\t'
        outfile.write(part)
    outfile.write('\n')
    outfile.close()

def newtitle():
    '''
    () -> (str)
    Asks user for title and type of media
    returns a dictionary of relevant information
    '''
    typeindex = {'1':'Film or Movie', '2':'Series or TV Show','3':'Other'}
    title = input('Enter the name of Film or Media: ')

    validchoice = False

    while not validchoice:
        time.sleep(1)
        print('Is this piece a:')
        print('[1] Film or Movie')
        print('[2] Series or TV Show')
        print('[3] Other')
        typechoice = input('Enter the number of the media type: ')
        time.sleep(0.5)

        if typechoice in typeindex:
            validchoice = True
        else:
            print('ERROR: Invalid input, please try again...')
    
    return [title, typeindex[typechoice]]

def finishedfilm(newentry):
    #check if movie is in towatch list
    #if not in towatch list, check to see if movie is in watched list
    #if movie is in watched list (if true + 1 to watch count)
    #if movie is not in watched list add new entry to watched
    if checktowatch(newentry[0]):
        #remove movie from towatch list
        pass
    else:
        #check watched list
        checkwatched(newentry[0])
        
    pass

def checktowatch(film):
    #check towatch list
    # if the title appears in the list return True
    # if not then return False
    pass

def checkwatched(film):
    #check watched list
    #if the title appears in the watched list return True
    #if  not then return False
    pass

def writetowatch(linelist):
    '''
    (list)->(str)
    
    Open towatch.txt
    Take list with strings for to-watch list and combines them into a single formatted string
    Write line to towatch.txt
    '''
    outfile = open('towatch.txt','a')
    line = ''
    for part in linelist:
        line += part + '\t'
    line += '\n'
    outfile.write(line)
    outfile.close()

def main():
    testcreatefiles()
    newentry = newtitle()
    watchedstatus = havewatched()

    if watchedstatus:
        finishedfilm(newentry)
    
    else:
        writetowatch(newentry)

    print('Finished main()')

main()