# Host Open v0.1

## Synopsis

When connected to a vagrant machine over ssh, this allows the user to open a file on the host machine without tunnelling.

## Requirements
- python3
- vagrant

## Usage
_Note: an alias could be setup to make these commands easier._

### Client
`python3 client.py file1.py folder/`  
Will open `file.py` and `folder/` separately on the server.

### Server
`python3 server.py subl`  
Filepaths received will be opened with sublime.  


## Setup

### Vagrantfile
Add the following line to the Vagrantfile:  
`config.vm.synced_folder ".vagrant/machines/default/virtualbox", "/.vagrant_info"`  
_This assumes the machine is named 'default'. Change where appropriate._



### SSH
`vagrant ssh -- -R 12355:localhost:12355`  
The arbitrarily chosen default port of 12355 can be changed.

## TO-DO
- Allow client to override the app specified on the server
- Allow client to optionally add extra flags to run
- Compile python to binary and setup aliases automatically

## License
Copyright (c) Jake Treacher. All rights reserved.  
Licensed under the [MIT](LICENSE.txt) License.