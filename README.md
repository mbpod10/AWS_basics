# Configure AWS Account

Create AWS Account (free is fine)
Get Credentials

Of `AWS Access Key ID` and `KEY AWS Secret Access Key`

```
# Default User With No Specific User Name

(MyDjangoEnv) brock@Brocks-MBP AWS Automation % aws configure
AWS Access Key ID [None]: asdfasdfasdfasdfaw2ewq
AWS Secret Access Key [None]: 123ksoiudnxasdlp=-alsmal1-3e802
Default region name [None]: us-east-1
Default output format [None]: json
```
Once This is Done, Open New Terminal, and execute `ls -a`, a `.aws` directory with `credentials` and `config` will be there (the `.aws` directory will be in the very root of the computer as in `Users/brock/.aws`)

Credentials File Will Be:
```
[default]
aws_access_key_id = asdfasdfasdfasdfaw2ewq
aws_secret_access_key = 123ksoiudnxasdlp=-alsmal1-3e802
```

Config File Will Be
```
[default]
region = us-east-1
output = json
```