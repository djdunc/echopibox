from subprocess import call
import datetime
import os
from PIL import Image


#Global Variables
sample_rate='192000' #192000 using Ultramic 
channels='1' #set 1 with Ultramic , stereo Mic can have 2 or more
audio_length='0.25' #in seconds - this is the amount of time each chunck of audio is recorded - 0.25s is about 200 pixel width of data when converted to spectrogram


def main():
    if __name__ == "__main__":
        
        i = 1
        while (i < 2):
            try:
                # for each instance of recording we create a timestamped record number
                start_now = datetime.datetime.now().strftime('%Y%m%d-%H%M%S')
                
                # first we create the audio recording - am using flac since smaller than wav but same detail
                output_recording= 'rec_%s.flac' %start_now 
                
                # command line args being passed into sox function:
                # -- -c defines how many channels we are recording on - ultramic is mono
                # -- -r defines sample rate - ultramic is at 192k
                # -- -t defines which audio input to use - developed on mac so used coreaudio
                # --    run: "sox -V6 -n -t coreaudio junkname" in terminal to see which mics are connected 
                # --    if using default mic of system then you can delete: '-t', 'coreaudio',  'UltraMic 192K 1', 
                # -- output_recording - is the file name of the audio
                # -- trim 0 audio_length - specifies to trim the audio to 0 to 0.25 seconds - ie stops recording after audio_length secs
                args=['sox', '-c', channels ,'-r', sample_rate, '-t', 'coreaudio',  'UltraMic 192K 1', output_recording, 'trim','0',audio_length]
                call(args)
                

                # next we use sox again to create a spectrogram of the audio and save it as a png file 
                output_spectrogram = 'spectro_%s.png' %start_now
                args2=['sox', output_recording,'-n', 'spectrogram','-o',output_spectrogram]
                call(args2)

                # finally we are saving only the region of interest in the spectrogram (for input to classifier)
                # starts at point 60, 30, crops to 764x392
                # and clearing up unused files
                output_spectrogram_square= '%s.png' %start_now
                im = Image.open(output_spectrogram)
                width, height = im.size
                # Crop to the optimised region of the image 
                im = im.crop((60, 30, 844, 422))
                # Resize to 196x196 which is used as input to classifier, when creating the spectrogram 
                # it is stretched in the horizontal so changing aspect ratio back should be fine 
                im = im.resize((196,196)).save(output_spectrogram_square)
                os.remove(output_recording)
                #os.remove(im)


            except KeyboardInterrupt:
                break
            
            i += 1

main()