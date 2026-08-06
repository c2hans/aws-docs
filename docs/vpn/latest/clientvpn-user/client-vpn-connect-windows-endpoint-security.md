---
source_url: https://docs.aws.amazon.com/vpn/latest/clientvpn-user/client-vpn-connect-windows-endpoint-security.html
---

# Endpoint security software compatibility
<a name="client-vpn-connect-windows-endpoint-security"></a>

Enterprise endpoint security products such as host-based firewalls, endpoint detection and response (EDR) agents, and antivirus software can sometimes interfere with AWS Client VPN connections. If you experience connectivity issues when using the AWS provided client for Windows, you might need to configure exclusions in your endpoint security software.

## AWS Client VPN executable paths
<a name="client-vpn-windows-executable-path"></a>

The AWS provided client for Windows installs the following key executables. You might need these paths when configuring firewall rules, application allowlists, or endpoint security policies.

**Version 6.0 and later**

Graphical user interface

```
C:\Program Files\Amazon\AWS VPN Client\AWS VPN Client.exe
```

Command line interface

```
C:\Program Files\Amazon\AWS VPN Client\aws-vpn-client.exe
```

Windows service

```
C:\Program Files\Amazon\AWS VPN Client\aws-client-vpn-daemon.exe
```
This is the core process that establishes and maintains the VPN tunnel connection.

**Before version 6.0**

VPN client application

```
C:\Program Files\Amazon\AWS VPN Client\AWSVPNClient.exe
```

OpenVPN process

```
C:\Program Files\Amazon\AWS VPN Client\Resources\openvpn\acvc-openvpn.exe
```
This is the core process that establishes and maintains the VPN tunnel connection.

Windows service

```
C:\Program Files\Amazon\AWS VPN Client\AWSVPNClient.Service.exe
```

## Network requirements
<a name="client-vpn-windows-network-requirements"></a>

The AWS provided client requires outbound network access to the Client VPN endpoint to establish a VPN connection. Ensure that your firewall or endpoint security software allows outbound traffic from the VPN tunnel process to the port and protocol configured on your Client VPN endpoint.
+ **Version 6.0 and later:** `aws-client-vpn-daemon.exe`
+ **Before version 6.0:** `acvc-openvpn.exe`

## Configuring endpoint security exclusions
<a name="client-vpn-windows-security-exclusions"></a>

If your endpoint security product interferes with AWS provided client connectivity, review the following exclusion categories with your security administrator:

Process-based exclusions
Add the executables listed in [AWS Client VPN executable paths](#client-vpn-windows-executable-path) to your endpoint security product's process allowlist or exclusion list.

Network-based exclusions
Allow outbound traffic from the VPN tunnel process (`aws-client-vpn-daemon.exe` for version 6.0 and later, or `acvc-openvpn.exe` for earlier versions) to your Client VPN endpoint's port and protocol.

Path-based exclusions
Exclude the AWS provided client installation directory from real-time scanning or behavioral analysis:

```
C:\Program Files\Amazon\AWS VPN Client\
```

**Important**
Prescriptive configuration instructions for specific third-party endpoint security products are outside the scope of AWS documentation due to variability across product versions and configurations. Consult your endpoint security vendor's documentation for detailed instructions on configuring exclusions for your specific product.
