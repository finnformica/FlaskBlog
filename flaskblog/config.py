
class Config:
    SECRET_KEY              = '7862745889beb30355a0a7c1dfe36b63' # good practice to set this to environment variables
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db' # and this
    MAIL_SERVER             = 'smtp.googlemail.com'
    MAIL_PORT               = 587
    MAIL_USE_TLS            = True
    MAIL_USERNAME           = 'finnformica@gmail.com' # and this
    MAIL_PASSWORD           = 'nqlahasxbjlnkkfd' # google app password / and this
