---
source_url: https://docs.aws.amazon.com/vpn/latest/clientvpn-user/connect.html
---

# Connect to an AWS Client VPN endpoint using an OpenVPN client
<a name="connect"></a>

You can establish a connection to a Client VPN endpoint using common Open VPN client applications. Client VPN is supported on the following operating systems:
+ **Windows**

  Use a certificate and private key from the Windows Certificate Store. Once you've generated the certificate and key you can establish an AWS Client connection using either the OpenVPN GUI client application or the OpenVPN GUI Connect Client. For the steps to create the certificate and key, see [Establish a VPN connection using a certificate on Windows](windows-openvpn-cryptoapicert.md).
+ **macOS**

  Establish a VPN connection using a configuration file for macOS-based Tunnelblick or for AWS Client VPN. For more information, see [Establish a VPN connection on macOS](macos-tunnelblick.md).
+ **Linux**

  Establish a VPN connection on Linux using either the** OpenVPN - Network Manager** interface or the OpenVPN application. To use the **OpenVPN - Network Manager** interface you'll first need to install the network manager module if it's not already installed. For more information, see [Establish a VPN connection on Linux](ubuntu-network-manager-openvpn.md).
+ **Android and iOS**

  Establish a VPN connection using the OpenVPN client application on an Android or iOS device. For more information see [Client VPN connections on Android and iOS](android.md).

**Important**
If the Client VPN endpoint has been configured to use [SAML-based federated authentication](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/client-authentication.html#federated-authentication), you cannot use the OpenVPN-based VPN client to connect to a Client VPN endpoint. This includes any ARM-based architectures. If you are using a device with an ARM processor (such as Apple Silicon Macs or ARM-based Windows devices), you must use SAML-based VPN endpoints with the AWS provided client instead of OpenVPN clients.

**Topics**
+ [Windows](windows.md)
+ [macOS](macos.md)
+ [Linux](linux.md)
+ [Client VPN connections on Android and iOS](android.md)
