### quackmyip

This script allows you to keep your public IP address updated, when using the
[Duck DNS](https://www.duckdns.org/) service.  

##### Requirements
In order to work, the latest version of this little script, needs the following Python 3 libraries:
* [requests](http://docs.python-requests.org/en/master/) (tested with v2.12.4)
* [urllib3](https://urllib3.readthedocs.io/en/latest/)  (tested with v1.19.1)

##### Syntax
```
usage: quackmyip [-h] -f FILE

Update your IP address for your duckdns registered domain

optional arguments:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  The configuration file to use
```
For its usage, it's recommended to create a daily cron job!.

##### Configuration file
Prior to its usage, a configuration file must be created, as shown in the following example:
```
[duckdns]
token = [YOUR_TOKEN]
domain = [YOUR_DOMAIN]

```
