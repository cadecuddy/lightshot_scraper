# lightshot_scraper

## Introduction
A popular image sharing/screenshot creating software, [Lightshot](https://app.prntscr.com/en/index.html), hosts images in urls in a sequence of 6 characters made up of ascii lettersa and integers. 
Now, this means that it's incredibly incrediblely easy to bruteforce these url endings and find publically hosted images that were uploaded by random users across the internet. This script enables its user to do so. This tool's intent is image set generation.

## Parameters & Requirements
The requirements of the script can be found in the **requirements.txt**. Once prereqs are installed, the script runs entirely in the command line. 
Run the script in the script's main directory with ``` python lightshot_explorer.py ```.

From there it'll ask how many attempts at link generation/downloading you want, and it'll perform them in real time until completition

**DISCLAIMER: There's no way of knowing what pictures will be downloaded as the links are randomly generated. Run this tool at your own risk. This tool's intent is image set generation.**
