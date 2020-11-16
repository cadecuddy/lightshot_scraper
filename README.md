# lightshot_scraper

## Introduction
A popular image sharing/screenshot creating software, [Lightshot](https://app.prntscr.com/en/index.html), hosts images in urls in a sequence of 6 characters made up of ascii lettersa and integers. 
Now, this means that it's incredebily incrediblely easy to bruteforce these url endings and find publically hosted images that were uploaded by random users across the internet. This script enables its user to do so.

## Parameters & Requirements
The requirements of the script can be found in the **requirements.txt**. Once prereqs are installed, the script runs entirely in the command line. 
Run the script in the script's main directory with ``` python lightshot_explorer.py ```.

From there it'll ask how many attempts at link generation/downloading you want, and it'll perform them in real time until completition

**NOTE: There's no way of knowing what pictures you'll find, but this has a lot of practical usage, such as image set generation**
