from pprint import pprint
import threading
import pyaudio
import random
import wave
import time
import timeit
import sys

soundFile = {'0': './zero.wav', '1': './one.wav', '2': './two.wav', '3': './three.wav', '4': './four.wav', '5': './five.wav', '6': './six.wav', '7': './seven.wav', '8': './eight.wav', '9': './nine.wav', '10': './ten.wav'}

while True:
    n = int(input('How many back will this experiment be?  '))
    waitTime = float(input('How many seconds in between numbers?  '))
    quantityNumbers = int(input('How many numbers would you like to present?  '))

    numbers = []
    responses = []
    key = []
    correct = 0
    incorrect = 0
    for i in range(quantityNumbers):
      num = str(random.randint(1, 10))
      numbers.append(num)




    def callback(in_data, frame_count, time_info, status):
      global wf
      data = wf.readframes(frame_count)
      return (data, pyaudio.paContinue)

    def runAudio():
      global numbers, waitTime, soundFile, wf

      # Start the clock
      #time.clock()
      startTime = time.time() + waitTime

      for num in numbers:
        wf = wave.open(soundFile[num], 'rb')

        p = pyaudio.PyAudio()
        stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                      channels=wf.getnchannels(),
                      rate=wf.getframerate(),
                      output=True,
                      stream_callback=callback)

        while (time.time() < startTime):
          time.sleep(0.1)

        stream.start_stream()
        while stream.is_active():
            time.sleep(0.1)

        stream.stop_stream()
        stream.close()
        wf.close()
        p.terminate()

        startTime = time.time() + waitTime

    repeat = True

    while repeat:
      input('\n\nPress [Enter] to begin the trial...')
      
      thread = threading.Thread(target=runAudio)
      thread.daemon = True
      thread.start()
      

      for i in range(quantityNumbers):
        r = input('What was the participant\'s response ([Enter] for no response)?   ')
        if not r:
          r = 'NaN'
          responses.append('-')
        else:
          responses.append(r)


        if (i >= n):
          if (r == numbers[i-n]):
            print('Correct!\n', end='')
            correct += 1
          else:
            print('Incorrect.\tCorrect Answer: ', numbers[i-n], '\n')
            incorrect += 1
          key.append(numbers[i-n])

        else:
          if (r == 'NaN'):
            print('Correct!\n')
            correct += 1
          else:
            print('Incorrect.\tCorrect Answer: NaN\n')
            incorrect += 1
          key.append('-')

        print('Percent Correct: {:.2%}\n\n'.format(correct / (i+1)))


      print('******************************************************')
      print('Numbers Presented:\t', end='')
      pprint(numbers)
      print('\nCorrect Response:\t', end='')
      pprint(key)
      print('Participant Response:\t', end='')
      pprint(responses)

      print('\nPercent Correct: {:.2%}'.format(correct/quantityNumbers))
      print()
      
      temp = input('Would you like to start again? (y/n)  ')
      if (temp[0] == 'y'):
        repeat = True
        
        numbers = []
        responses = []
        key = []
        correct = 0
        incorrect = 0
        for i in range(quantityNumbers):
          num = str(random.randint(1, 10))
          numbers.append(num)
          
      else:
        repeat = False


'''

import pyaudio
import wave
import time
import sys

if len(sys.argv) < 2:
    print("Plays a wave file.\n\nUsage: %s filename.wav" % sys.argv[0])
    sys.exit(-1)

wf = wave.open(sys.argv[1], 'rb')

p = pyaudio.PyAudio()

def callback(in_data, frame_count, time_info, status):
    data = wf.readframes(frame_count)
    return (data, pyaudio.paContinue)

stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                output=True,
                stream_callback=callback)

stream.start_stream()

while stream.is_active():
    time.sleep(0.1)

stream.stop_stream()
stream.close()
wf.close()

p.terminate()

'''
