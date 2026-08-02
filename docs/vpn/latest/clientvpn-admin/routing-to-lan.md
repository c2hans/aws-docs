---
source_url: https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/routing-to-lan.html
---

# Troubleshooting AWS Client VPN: Routing traffic to LAN not working as expected
<a name="routing-to-lan"></a>

**Problem**
Trying to route traffic to local area network (LAN) not working as expected when the LAN IP address ranges are not within the following standard private IP address ranges: `10.0.0.0/8`, `172.16.0.0/12`, `192.168.0.0/16`, or `169.254.0.0/16`.

**Cause**
If the client LAN address range is detected to fall outside of the above standard ranges, the Client VPN endpoint will automatically push the OpenVPN directive "redirect-gateway block-local" to the client, forcing all LAN traffic into the VPN. For more information, see [Rules and best practices for using AWS Client VPN](what-is-best-practices.md).

**Solution**
If you require LAN access during VPN connections, it is advised that you use the conventional address ranges listed above for your LAN.
