#!/usr/bin/env python3

import webbrowser

doi = input("Paste manuscript DOI here: ")
url = "https://doi-org.biblio.iit.it/"+doi
webbrowser.open_new_tab(url)
