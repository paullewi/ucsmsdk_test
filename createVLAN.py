#skeleton script

#import ucshandle class from ucshandle
from ucsmsdk.ucshandle import UcsHandle

#init handle
handle = UcsHandle("192.168.157.153", "admin", "password", secure=False)

# Login
handle.login()

#####IPNUT GENERATED CODE



from ucsmsdk.mometa.fabric.FabricVlan import FabricVlan

mo = FabricVlan(parent_mo_or_dn="fabric/lan", sharing="none", name="vlan123", id="123", mcast_policy_name="", policy_owner="local", default_net="no", pub_nw_name="", compression_type="included")
handle.add_mo(mo)

handle.commit()



# Logout after execution
handle.logout()
