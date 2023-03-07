# Purpose
A Python script and systemd service file (for running on boot) meant to
solve the issue of randomly generated SSH URLs on ngrok's free plan. The
script emails a mobile carrier's Email-To-SMS address the command given by
ngrok to access the SSH tunnel, which will then appear as a text to the
provided phone number.

# Requirements
ngrok and Python3 must be installed and network access must be available.
The 'mutt' email client, set up with an email account.
A phone number.

# Note
If using a Gmail account, you will want to use an 'App Password' for
setting up the IMAP password in .muttrc.

# Steps
1. Change the 'User' and 'WorkingDirectory' fields in .service file to the
current user and directory location of the .py file, respectively.

2. Move or copy .service file to '/etc/systemd/system', or wherever systemd
looks for services.

3. Enable the .service file (typically using 'systemctl enable').

3. Change the 'TARGET\_EMAIL' variable in .py to your Email-to-SMS address,
which can be found online.

Important! Change the .service file if moving the location of .py file.
