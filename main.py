import os
from os import listdir, system, name
from os.path import isfile, join
import zipfile
from videoprops import get_video_properties, get_audio_properties
import configparser

config = configparser.ConfigParser()
config.sections()
config.read('config.ini')
myPath = config['Section1']['folderPath'] + '/'

def txt():
    fileList = [f for f in listdir(myPath) if isfile(join(myPath, f))]

    for file in [x for x in fileList if 'mp4' in x or 'mkv' in x or 'avi' in x]:
        if '.mp4' in file:
            orgName = file.replace('.mp4', '')
            fileType = 'mp4'
        elif '.mkv' in file:
            orgName = file.replace('.mkv', '')
            fileType = 'mkv'
        elif '.avi' in file:
            orgName = file.replace('.avi', '')
            fileType = 'avi'
        else:
            break

        videoPATH = myPath + file
        print('Collecting data - ' + file)
        videoProps = get_video_properties(videoPATH)
        audioProps = get_audio_properties(videoPATH)

        fileSize = str(int(round((os.path.getsize(videoPATH) / 1048576), 2))) + 'mb'

        try:
            videoCodec = videoProps['codec_name']
        except KeyError:
            videoCodec = 'no data'
        try:
            videoDuration = str(round((float(videoProps['duration']) / 60), 2)) + 'min'
        except KeyError:
            videoDuration = 'no data'
        try:
            videoResolution = str(videoProps['width']) + 'x' + str(videoProps['height'])
        except KeyError:
            videoResolution = 'no data'
        try:
            videoFPS = videoProps['avg_frame_rate']
            videoFPS = videoFPS.split('/')
            videoFPS = str(round(float(videoFPS[0]) / float(videoFPS[1]), 2)) + 'fps'
        except KeyError:
            videoFPS = 'no data'
        try:
            videoAspectRatio = videoProps['display_aspect_ratio']
        except KeyError:
            videoAspectRatio = 'no data'
        try:           
            videoBitrate = str(round(float(videoProps['bit_rate']) / 1000, 2)) + 'kb/s'
        except KeyError:
            videoBitrate = 'no data'
        try:
            audioCodec = audioProps['codec_name']
        except KeyError:
            audioCodec = 'no data'
        try:
            audioChannels = str(audioProps['channels'])
        except KeyError:
            audioChannels = 'no data'
        try:
            audioSampleRate = str(audioProps['sample_rate'])
        except KeyError:
            audioSampleRate = 'no data'
        try:
            audioBitrate = str(round(float(audioProps['bit_rate']) / 1000, 2)) + 'kb/s'
        except KeyError:
            audioBitrate = 'no data'

        print('Creating text file - ' + orgName + '.txt')
        f = open(myPath + orgName + '.txt', 'w')
        f.write(orgName + '\n\n')
        f.write('Information\n')
        f.write('Size.............: ' + fileSize + '\n')
        f.write('File type........: ' + fileType + '\n\n')

        f.write('Video\n')
        f.write('Codec............: ' + videoCodec + '\n')
        f.write('Duration.........: ' + videoDuration + '\n')
        f.write('Resolution.......: ' + videoResolution + '\n')
        f.write('Frame rate.......: ' + videoFPS + '\n')
        f.write('Aspect ratio.....: ' + videoAspectRatio + '\n')
        f.write('Bitrate..........: ' + videoBitrate + '\n')

        f.write('\nAudio\n')
        f.write('Codec............: ' + audioCodec + '\n')
        f.write('Channels.........: ' + audioChannels + '\n')
        f.write('Sample rate......: ' + audioSampleRate + '\n')
        f.write('Bitrate..........: ' + audioBitrate + '\n')

        f.close()

def zipping():
    fileList = [f for f in listdir(myPath) if isfile(join(myPath, f))]

    for file in [x for x in fileList if 'mp4' in x or 'mkv' in x or 'avi' in x]:
        if '.mp4' in file:
            zipName = file.replace('.mp4', '.zip')
        elif '.mkv' in file:
            zipName = file.replace('.mkv', '.zip')
        elif '.avi' in file:
            zipName = file.replace('.avi', '.zip')
        else:
            pass

        newZip = myPath + zipName
        print('Zipping - ' + file)
        archive = zipfile.ZipFile(newZip, mode='w')
        archive.write(myPath + file, file)
        print('Files added.')

        print('Reading files now.')
        archive.close()

        zip_archive = zipfile.ZipFile(newZip, 'r')
        for file_info in zip_archive.infolist():
            zipSize = round(((file_info.file_size) / 1048576), 2)
            print(file_info.filename, zipSize, 'MB')

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

loop1 = False
while loop1 != True:
    print('1. Metadata --> .txt')
    print('2. Create new ZIP archives')
    print('3+ Exit')
    print('(default is 1)')

    try:
        userInput = int(input('\nInput >>> ') or 1)
        if userInput == 1:
            clear()
            txt()

        elif userInput == 2:
            clear()
            zipping()

        elif userInput >= 3:
            loop1 = True

        else:
            pass

    except ValueError:
        print ('Invalid input\n')
