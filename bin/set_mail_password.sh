#!/usr/bin/python

user = $1
if [-z "$user" ]
then
    user = "hotyrobot@gmail.com"
fi

python -c "import keyring; import getpass; keyring.set_password('aci_mail_bot', '$1', getpass.getpass('Password:'))"