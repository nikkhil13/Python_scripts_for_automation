# Python_scripts_for_automation
A list of scripts to automate your daily tasks

# How to use the files

## Torrent Downloader
1. Download the *torrent_downloader.py* file and save it any directory that you wish.
2. Run the file using
> python torrent_downloader.py
3. In the same directory, you will find a *test.txt* file which contains the magnet link of your selected torrent. Open your torrent client. Click on the icon resembling [--] i.e Add torrent from URL.
   Copy the entire magnet link and paste it in the box provided and your torrent will start streaming. I've done it for one the proxies of the pirate bay and they have stopped providing *.torrent* files.
   If you manage to get the *.torrent* file, you can automate the last step as well. I'll stick with the magnet link.

## Downloads folder cleaner
1. Download the *clean_folder.py* file and save it in your *Downloads* directory.
2. Run the file using
> python clean_folder.py
3. Your files will be arranged. You can add more extensions in the code if you like.

## MovieDB and subtile renamer
1. Download the *movie_db_and_subs_renamer.py* and paste it in your *Movies* directory if you have one.
2. Run the file using 
> python movie_db_and_subs_renamer.py
  * I haven't considered all the cases of movie names here. This'll work best if you have a folder of movies with folder names containing only the respective movie name and year of release or just the movie name.
    This script can be improved further by forming a regex to match any folder name and extracting only the movie name from it.
