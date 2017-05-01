import os
import re
import urllib
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

k = os.getcwd()
original_names = os.listdir(k) 
movies = os.listdir(k)

error = []
m = re.compile(r'(\(\d{4}\))') #regex to match the date and remove it because omdb api responds only to the movie name

'''I have considered that your movie folder name contains only the movie name with the year or no year. Eg - Whiplash (2014)
   However, a seperate script can be written to rename the folder containing any other special names. Such as Brrip, 720p, YIFY, Shaanig and a million other schemes'''

url = 'http://www.omdbapi.com/?t='

def clean_names():
    for i in range(len(movies)):
        x = movies[i]
        k = m.search(x)
        if k is not None:
            movies[i] = x.replace(k.group()," ")
        movies[i] = movies[i].strip()
        
 

def rename_subtitles():       
    for i in range(len(original_names)):
        original_movie_name = original_names[i]
        changed_movie_name = movies[i]
        folder = k + '\\' + original_movie_name
        dir_path = folder + '\\'
        if os.path.isdir(folder):
            inside_folder = os.listdir(folder)
            flag = 0
            for names in inside_folder:
                if names.endswith('.mkv') or names.endswith('.mp4'):
                    mov_name = os.path.splitext(os.path.basename(names))[0]
                elif names.endswith('.srt'):
                    srt_name = os.path.splitext(os.path.basename(names))[0]
                    flag = 1
                else:
                    continue
            if flag == 1:
                
                if mov_name != srt_name:
                    try:
                        os.rename(dir_path + srt_name + '.srt' ,dir_path + mov_name + '.srt')
                    except:
                        print 'Srt already renamed for %s' % mov_name
                else:
                    print 'Srt already renamed for %s' % mov_name

            print '%s' % changed_movie_name            
            url_visit = url + changed_movie_name
            response = urllib.urlopen(url_visit).read()
            values = json.loads(response)
            ans = '\n\n'.join('{} - {}'.format(key, val) for key, val in sorted(values.items()))
            
            with open(dir_path + 'Details.txt','w') as outputfile:
                outputfile.write(ans)

            print 'Done'
                   

if __name__ == '__main__':
    clean_names()
    rename_subtitles()



        
