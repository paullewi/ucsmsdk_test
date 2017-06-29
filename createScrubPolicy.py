# !/usr/local/bin/python
# -*- coding: utf-8 -*-


#import ucshandle class from ucshandle
from ucsmsdk.ucshandle import UcsHandle

#init handle
handle = UcsHandle("192.168.157.153", "admin", "password", secure=False)

# Login
handle.login()

#####IPNUT GENERATED CODE


from ucsmsdk_samples.ucsmsdk_samples.server.scrub_policy import scrub_policy_remove


scrub_policy_remove(handle, name="sample_scrub", parent_dn="org-root")



# Logout after execution
handle.logout()




