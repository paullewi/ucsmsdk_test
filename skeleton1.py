#skeleton script

#import ucshandle class from ucshandle
from ucsmsdk.ucshandle import UcsHandle

#init handle
handle = UcsHandle("192.168.157.153", "admin", "password", secure=False)

# Login
handle.login()

#####IPNUT GENERATED CODE


# Logout after execution
handle.logout()
