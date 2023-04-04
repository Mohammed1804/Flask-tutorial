Debugging errors
1) error ocurs when you try and change username into one that is already registered by another user
2) get stack trace sent to email (config)
3) Created an SMTPhandler instance reports errors and not warnings, informational or debugging messages.
4) tested using smtp debugging server
5) Set a real email server *export MAIL_SERVER=smtp.googlemail.com
export MAIL_PORT=587
export MAIL_USE_TLS=1
export MAIL_USERNAME=<your-gmail-username>
export MAIL_PASSWORD=<your-gmail-password>
6) create a log file for the application for failures that dont cause app to crash but are useful for debugging purposes
7) Fixing username error by checking the changed username is not in the database but if user does not change their username the database should allow it (forms)