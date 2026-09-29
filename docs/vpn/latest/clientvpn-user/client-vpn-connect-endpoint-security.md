---
source_url: https://docs.aws.amazon.com/vpn/latest/clientvpn-user/client-vpn-connect-endpoint-security.html
---

# Endpoint security software compatibility
<a name="client-vpn-connect-endpoint-security"></a>

Enterprise endpoint security products such as host-based firewalls, endpoint detection and response (EDR) agents, and antivirus software can sometimes interfere with AWS Client VPN connections. If you experience connectivity issues when using the AWS provided client, you might need to configure exclusions in your endpoint security software.

## AWS Client VPN executable paths
<a name="client-vpn-executable-paths"></a>

The AWS provided client installs the following key executables. You might need these paths when configuring firewall rules, application allowlists, or endpoint security policies.

### Windows
<a name="client-vpn-executable-paths-windows"></a>

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

Device posture agent

```
C:\Program Files\Amazon\AWS VPN Client\aws-vpn-client-agent.exe
```
When you connect to an endpoint that has device posture enabled, this process reads the device posture data from your device trust provider.

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

### macOS
<a name="client-vpn-executable-paths-macos"></a>

**Version 6.0 and later**

Graphical user interface

```
/Applications/AWS VPN Client/AWS VPN Client.app/Contents/MacOS/AWS VPN Client
```

Command line interface

```
/Applications/AWS VPN Client/AWS VPN Client.app/Contents/MacOS/aws-vpn-client
```
A convenience symlink is also installed at `/usr/local/bin/aws-vpn-client`.

Daemon

```
/Applications/AWS VPN Client/AWS VPN Client.app/Contents/Helpers/aws-client-vpn-daemon
```
This is the core process that establishes and maintains the VPN tunnel connection.

Device posture agent

```
/Applications/AWS VPN Client/AWS VPN Client.app/Contents/Helpers/aws-vpn-client-agent
```
When you connect to an endpoint that has device posture enabled, this process reads the device posture data from your device trust provider.

**Before version 6.0**

VPN client application

```
/Applications/AWS VPN Client/AWS VPN Client.app/Contents/MacOS/AWS VPN Client
```

OpenVPN process

```
/Applications/AWS VPN Client/AWS VPN Client.app/Contents/Resources/openvpn/acvc-openvpn
```
This is the core process that establishes and maintains the VPN tunnel connection.

Privileged helper

```
/Library/PrivilegedHelperTools/com.amazonaws.acvc.helper
```
Manages routes and DNS configuration on behalf of the application.

### Linux
<a name="client-vpn-executable-paths-linux"></a>

**Version 6.0 and later**

Graphical user interface

```
/opt/awsvpnclient/AWS VPN Client
```

Command line interface

```
/opt/awsvpnclient/aws-vpn-client
```

Daemon

```
/opt/awsvpnclient/aws-client-vpn-daemon
```
This is the core process that establishes and maintains the VPN tunnel connection.

Device posture agent

```
/opt/awsvpnclient/aws-vpn-client-agent
```
When you connect to an endpoint that has device posture enabled, this process reads the device posture data from your device trust provider.

**Before version 6.0**

VPN client application

```
/opt/awsvpnclient/AWS VPN Client
```

OpenVPN process

```
/opt/awsvpnclient/Resources/openvpn/acvc-openvpn
```
This is the core process that establishes and maintains the VPN tunnel connection.

Privileged service

```
/opt/awsvpnclient/Service/ACVC.GTK.Service
```
Manages VPN connections and routes on behalf of the application.

## Network requirements
<a name="client-vpn-network-requirements"></a>

The AWS provided client requires outbound network access to the Client VPN endpoint to establish a VPN connection. Ensure that your firewall or endpoint security software allows outbound traffic from the VPN tunnel process to the port and protocol configured on your Client VPN endpoint.

**Version 6.0 and later**
+ **Windows:** `aws-client-vpn-daemon.exe`
+ **macOS:** `aws-client-vpn-daemon`
+ **Linux:** `aws-client-vpn-daemon`

**Before version 6.0**
+ **Windows:** `acvc-openvpn.exe`
+ **macOS and Linux:** `acvc-openvpn`

## Configuring endpoint security exclusions
<a name="client-vpn-security-exclusions"></a>

If your endpoint security product interferes with AWS provided client connectivity, review the following exclusion categories with your security administrator:

Process-based exclusions
Add the executables listed in [AWS Client VPN executable paths](#client-vpn-executable-paths) to your endpoint security product's process allowlist or exclusion list.

Network-based exclusions
Allow outbound traffic from the VPN tunnel process to your Client VPN endpoint's port and protocol. For version 6.0 and later, this is `aws-client-vpn-daemon` (or `aws-client-vpn-daemon.exe` on Windows). For earlier versions, this is `acvc-openvpn` (or `acvc-openvpn.exe` on Windows).

Path-based exclusions
Exclude the AWS provided client installation directory from real-time scanning or behavioral analysis:
+ **Windows:** `C:\Program Files\Amazon\AWS VPN Client\`
+ **macOS:** `/Applications/AWS VPN Client/`
+ **Linux:** `/opt/awsvpnclient/`

**Important**
Prescriptive configuration instructions for specific third-party endpoint security products are outside the scope of AWS documentation due to variability across product versions and configurations. Consult your endpoint security vendor's documentation for detailed instructions on configuring exclusions for your specific product.
