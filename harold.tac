from twisted.application import service

from conf import HaroldConfiguration
import irc
import http

# read configuration
config = HaroldConfiguration("harold.ini")

# build the application
application = service.Application("Harold")

# make the http root resource
http_root, harold_root = http.make_root(config)

# set up the irc service
irc_service = irc.make_service(config, harold_root)
irc_service.setServiceParent(application)

# set up the http service
http_service = http.make_service(config, http_root)
http_service.setServiceParent(application)
