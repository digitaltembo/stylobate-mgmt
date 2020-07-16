# README
<code>
 ,---.   ,--.           ,--.       ,--.             ,--.          
'   .-',-'  '-.,--. ,--.|  | ,---. |  |-.  ,--,--.,-'  '-. ,---.  
`.  `-.'-.  .-' \  '  / |  || .-. || .-. '' ,-.  |'-.  .-'| .-. : 
.-'    | |  |    \   '  |  |' '-' '| `-' |\ '-'  |  |  |  \   --. 
`-----'  `--'  .-'  /   `--' `---'  `---'  `--`--'  `--'   `----' 
               `---'                                              
                         Mgmt
</code>

Management script for managing applications based off of [stylobate](https://github.com/digitaltembo/stylobate).

Inspired basically by Flask's `manage.py`, it is mostly thin wrappers around bash scripts that would be tedious to type in full each time.
Adapted from a previous collection of a bunch of aliases and bash scripts

## Features

* Build/compile front-end sources and docker images with `stylo build`
* Manage the database with auto-generated migrations and shell access in `stylo db`
* Auto-fork and set up a new stylobate project with `stylo init`
* Follow logs with `stylo logs`
* Run frontend, backend, and dockerized servers with `stylo run`
* Is your web server running? Use `stylo stop`
* Access the docker shells with `stylo shell`

## Installation

If you want to use `stylo init`, you must first install the [GitHub CLI](https://github.com/cli/cli#installation))

After doing or skipping that, simply run ```pip install stylobate-mgmt```

## Usage

Use `stylo --help` to access the help page, or `stylo <command> --help` to access the help page for a specific command

Note that for clarity's sake in most descriptions I use the long version of arguments, e.g. `stylo db --gen-migrations`. All arguments have a shorter form as well that should be intuitive; in this case `stylo db -g`.