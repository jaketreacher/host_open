# Host Open

## Synopsis

When connected to a vagrant VM over ssh, this allows the user to open a file on the host machine without tunnelling.


## Example

### Configuration
Vagrantfile:
`config.vm.synced_folder "/Users/Jake/code", "/vagrant"`

### Code
`python3 host_open /vagrant/project/file.py`

Converts `/vagrant/project/file.py` to `/Users/Jake/code/project/file.py`.
Sends the filepath to the host, and opens with the desired editor.  

## License

[MIT](https://github.com/jaketreacher/profile_manager/blob/master/LICENSE.md)