---
source_url: https://docs.aws.amazon.com/vpn/latest/clientvpn-user/windows-troubleshooting.html
---

# Troubleshooting AWS Client VPN connections with Windows-based clients
<a name="windows-troubleshooting"></a>

The following sections contain information about problems that you might have when using Windows-based clients to connect to a Client VPN endpoint.

## AWS provided client event logs
<a name="aws-provided-client"></a>

The AWS provided client creates event logs and stores them in the following location on your computer.

```
C:\Users\{{User}}\AppData\Roaming\AWSVPNClient\logs
```

**Note**
For version 6.0 and later, the logs are stored in the following location.

```
%USERPROFILE%\AppData\Roaming\AWSVPNClient\logs\
```

The following types of logs are available:
+ **Application logs**: Contain information about the application. These logs are prefixed with 'aws\_vpn\_client\_'.
+ **OpenVPN logs**: Contain information about OpenVPN processes. These logs are prefixed with 'ovpn\_aws\_vpn\_client\_'.

The AWS provided client uses the Windows service to perform root operations. Windows service logs are stored in the following location on your computer.

```
C:\Program Files\Amazon\AWS VPN Client\WinServiceLogs\{{username}}
```

**Note**
For version 6.0 and later, the service logs are stored in the following location.

```
C:\ProgramData\Amazon\AWSVPNClient\logs\
```

**Topics**
+ [AWS provided client event logs](#aws-provided-client)
+ [Client cannot connect](#windows-troubleshooting-client-vpn-cannot-connect)
+ [Client cannot connect with "no TAP-Windows adapters" log message](#windows-troubleshooting-client-vpn-cannot-connect-tap-driver)
+ [Client is stuck in a reconnecting state](#windows-troubleshooting-client-vpn-stuck)
+ [VPN connection process quits unexpectedly](#windows-troubleshooting-client-vpn-quits)
+ [Application fails to launch](#windows-troubleshooting-client-vpn-cannot-launch)
+ [Client cannot create profile](#windows-troubleshooting-client-vpn-cannot-create-profile)
+ [Profiles or preferences missing after upgrade to version 6.0](#windows-troubleshooting-profiles-missing)
+ [VPN disconnects with a pop up message](#windows-troubleshooting-client-vpn-connection-terminated)
+ [Client crash occurs on Dell PCs using Windows 10 or 11](#windows-troubleshooting-client-vpn-crash-dell)
+ [OpenVPN GUI](#windows-troubleshooting-openvpn-gui)
+ [OpenVPN connect client](#windows-troubleshooting-openvpn-connect)
+ [Unable to resolve DNS](#windows-troubleshooting-openvpn-connect-dns)
+ [Missing PKI alias](#windows-troubleshooting-openvpn-connect-pki)

## Client cannot connect
<a name="windows-troubleshooting-client-vpn-cannot-connect"></a>

**Problem**
The AWS provided client cannot connect to the Client VPN endpoint.

**Cause**
The cause of this problem might be one of the following:
+ Another OpenVPN process is already running on your computer, which prevents the client from connecting.
+ Your configuration (.ovpn) file is not valid.

**Solution**
Check to see if there are other OpenVPN applications running on your computer. If there are, stop or quit these processes and try connecting to the Client VPN endpoint again. Check the OpenVPN logs for errors, and ask your Client VPN administrator to verify the following information:
+ That the configuration file contains the correct client key and certificate. For more information, see [Export Client Configuration](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/cvpn-working-endpoint-export.html) in the *AWS Client VPN Administrator Guide*.
+ That the CRL is still valid. For more information, see [Clients Unable to Connect to a Client VPN Endpoint](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/troubleshooting.html#client-cannot-connect) in the *AWS Client VPN Administrator Guide*.

## Client cannot connect with "no TAP-Windows adapters" log message
<a name="windows-troubleshooting-client-vpn-cannot-connect-tap-driver"></a>

**Problem**
The AWS provided client cannot connect to the Client VPN endpoint *and* the following error message appears in the application logs: "There are no TAP-Windows adapters on this system. You should be able to create a TAP-Windows adapter by going to Start -> All Programs -> TAP-Windows -> Utilities -> Add a new TAP-Windows virtual ethernet adapter".

**Solution**
You can remediate this problem by taking one or more of the following actions:
+ Restart the TAP-Windows adapter.
+ Reinstall the TAP-Windows driver.
+ Create a new TAP-Windows adapter.

## Client is stuck in a reconnecting state
<a name="windows-troubleshooting-client-vpn-stuck"></a>

**Problem**
The AWS provided client is trying to connect to the Client VPN endpoint, but is stuck in a reconnecting state.

**Cause**
The cause of this problem might be one of the following:
+ Your computer is not connected to the internet.
+ The DNS hostname does not resolve to an IP address.
+ An OpenVPN process is indefinitely trying to connect to the endpoint.

**Solution**
Verify that your computer is connected to the internet. Ask your Client VPN administrator to verify that the `remote` directive in the configuration file resolves to a valid IP address. You can also disconnect the VPN session by choosing **Disconnect** in the AWS VPN Client window, and try connecting again.

## VPN connection process quits unexpectedly
<a name="windows-troubleshooting-client-vpn-quits"></a>

**Problem**
While connecting to a Client VPN endpoint, the client quits unexpectedly.

**Cause**
TAP-Windows is not installed on your computer. This software is required to run the client.

**Solution**
Rerun the AWS provided client installer to install all of the required dependencies.

## Application fails to launch
<a name="windows-troubleshooting-client-vpn-cannot-launch"></a>

**Problem**
On Windows 7, the AWS provided client does not launch when you try to open it.

**Cause**
.NET Framework 4.7.2 or higher is not installed on your computer. This is required to run the client.

**Solution**
Rerun the AWS provided client installer to install all of the required dependencies.

## Client cannot create profile
<a name="windows-troubleshooting-client-vpn-cannot-create-profile"></a>

**Problem**
You get the following error when you try to create a profile using the AWS provided client.

```
The config should have either cert and key or auth-user-pass specified.
```

**Cause**
If the Client VPN endpoint uses mutual authentication, the configuration (.ovpn) file does not contain the client certificate and key.

**Solution**
Ensure that your Client VPN administrator adds the client certificate and key to the configuration file. For more information, see [Export Client Configuration](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/cvpn-working-endpoint-export.html) in the *AWS Client VPN Administrator Guide*.

## Profiles or preferences missing after upgrade to version 6.0
<a name="windows-troubleshooting-profiles-missing"></a>

**Problem**
After upgrading the AWS provided client to version 6.0 or later, previously configured VPN profiles do not appear in the client, and preferences might be reset to their defaults.

**Cause**
Version 6.0 introduced a new architecture that stores configuration data in a new system-wide location. On first launch, the client attempts to automatically migrate profiles and preferences from the previous location, but this migration can fail in some cases. The client does not delete your original `.ovpn` configuration files.

**Solution**
Download a new endpoint configuration file from your Client VPN endpoint and re-import it. For instructions on how to download the configuration file, see [Export Client Configuration](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/cvpn-working-endpoint-export.html) in the *AWS Client VPN Administrator Guide*. For instructions on how to add a profile, see [Connect to AWS Client VPN with an AWS provided client for Windows](client-vpn-connect-windows-connecting-how.md).

If you cannot locate your endpoint or do not have access to the self-service portal, contact your VPN administrator to obtain a new configuration file.

## VPN disconnects with a pop up message
<a name="windows-troubleshooting-client-vpn-connection-terminated"></a>

**Problem**
The VPN disconnects with a pop up message that says: "The VPN connection is being terminated because the address space of the local network your device is connected to has changed. Please establish a new VPN connection."

**Cause**
TAP-Windows adapter does not contain the required description.

**Solution**
If the `Description` field does not match below, first remove the TAP-Windows adapter, then rerun the AWS provided client installer to install all of the required dependencies.

```
C:\Users\jdoe> ipconfig /all

Ethernet adapter Ethernet 2:

Media State . . . . . . . . . . . : Media disconnected
Connection-specific DNS Suffix  . :
Description . . . . . . . . . . . : AWS VPN Client TAP-Windows Adapter V9
Physical Address. . . . . . . . . : 00-FF-50-ED-5A-DE
DHCP Enabled. . . . . . . . . . . : Yes
Autoconfiguration Enabled . . . . : Yes
```

## Client crash occurs on Dell PCs using Windows 10 or 11
<a name="windows-troubleshooting-client-vpn-crash-dell"></a>

**Problem**
On certain Dell PCs (desktop and laptop) that are running Windows 10 or 11, a crash can occur when you're browsing your file system to import a VPN configuration file. If this issue occurs, you'll see messages like the following in the logs of the AWS provided client:

```
System.AccessViolationException: Attempted to read or write protected memory. This is often an indication that other memory is corrupt.
   at System.Data.SQLite.UnsafeNativeMethods.sqlite3_open_interop(Byte[] utf8Filename, Int32 flags, IntPtr& db)
   at System.Data.SQLite.SQLite3.Open(String strFilename, SQLiteConnectionFlags connectionFlags, SQLiteOpenFlagsEnum openFlags, Int32 maxPoolSize, Boolean usePool)
   at System.Data.SQLite.SQLiteConnection.Open()
   at STCommonShellIntegration.DataShellManagement.CreateNewConnection(SQLiteConnection& newConnection)
   at STCommonShellIntegration.DataShellManagement.InitConfiguration(Dictionary`2 targetSettings)
   at DBROverlayIcon.DBRBackupOverlayIcon.initComponent()
```

**Cause**
The Dell Backup and Recovery system in Windows 10 and 11 might cause conflicts with the AWS provided client, particularly with the following three DLLs:
+ DBRShellExtension.dll
+ DBROverlayIconBackuped.dll
+ DBROverlayIconNotBackuped.dll

**Solution**
To avoid this problem, first make sure that your client is up to date with the latest version of the AWS provided client. Go to [AWS Client VPN download](https://aws.amazon.com/vpn/client-vpn-download/) and if a newer version is available, upgrade to the latest version.

**In addition, do one of the following:**
+ If you are using the Dell Backup and Recovery application, make sure that it's up to date. A [Dell forum post](https://www.dell.com/community/en/conversations/productivity-software/backup-and-recovery-causing-applications-using-qt5-dlls-to-crash/647f54c6f4ccf8a8dee57b89?commentId=647f6c00f4ccf8a8de92b263#M35007) states that this issue is resolved in newer versions of the application.
+ If you're not using the Dell Backup and Recovery application, some action will still need to be taken if you are experiencing this problem. If you do not wish to upgrade the application, as an alternative, you can delete or rename the DLL files. However, note that this will prevent the Dell Backup and Recovery application from functioning completely.

**Delete or rename the DLL files**

1. Go to Windows Explorer and browse to the location where Dell Backup and Recovery is installed. It typically is installed in the following location, but you might need to search to find it.

   ```
   C:\Program Files (x86)\Dell Backup and Recovery\Components\Shell
   ```

1. Manually delete the following DLL files from the installation directory, or rename them. Either action will prevent them from being loaded.
   + DBRShellExtension.dll
   + DBROverlayIconBackuped.dll
   + DBROverlayIconNotBackuped.dll

   You can rename the files by adding ".bak" to the end of the file name, for example, **DBROverlayIconBackuped.dll.bak**.

## OpenVPN GUI
<a name="windows-troubleshooting-openvpn-gui"></a>

The following troubleshooting information was tested on versions 11.10.0.0 and 11.11.0.0 of the OpenVPN GUI software on Windows 10 Home (64-bit) and Windows Server 2016 (64-bit).

The configuration file is stored in the following location on your computer.

```
C:\Users\{{User}}\OpenVPN\config
```

The connection logs are stored in the following location on your computer.

```
C:\Users\{{User}}\OpenVPN\log
```

## OpenVPN connect client
<a name="windows-troubleshooting-openvpn-connect"></a>

The following troubleshooting information was tested on versions 2.6.0.100 and 2.7.1.101 of the OpenVPN Connect Client software on Windows 10 Home (64-bit) and Windows Server 2016 (64-bit).

The configuration file is stored in the following location on your computer.

```
C:\Users\{{User}}\AppData\Roaming\OpenVPN Connect\profile
```

The connection logs are stored in the following location on your computer.

```
C:\Users\{{User}}\AppData\Roaming\OpenVPN Connect\logs
```

## Unable to resolve DNS
<a name="windows-troubleshooting-openvpn-connect-dns"></a>

**Problem**
The connection fails with the following error.

```
Transport Error: DNS resolve error on 'cvpn-endpoint-xyz123.prod.clientvpn.us-east-1.amazonaws.com (http://cvpn-endpoint-xyz123.prod.clientvpn.us-east-1.amazonaws.com/)' for UDP session: No such host is known.
```

**Cause**
The DNS name cannot be resolved. The client must prepend a random string to the DNS name to prevent DNS caching; however, some clients do not do this.

**Solution**
See the solution for [Unable to Resolve Client VPN Endpoint DNS Name](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/troubleshooting.html#resolve-host-name) in the *AWS Client VPN Administrator Guide*.

## Missing PKI alias
<a name="windows-troubleshooting-openvpn-connect-pki"></a>

**Problem**
A connection to a Client VPN endpoint that does not use mutual authentication fails with the following error.

```
FATAL:CLIENT_EXCEPTION: connect error: Missing External PKI alias
```

**Cause**
The OpenVPN Connect Client software has a known issue where it attempts to authenticate using mutual authentication. If the configuration file does not contain a client key and certificate, authentication fails.

**Solution**
Specify a random client key and certificate in the Client VPN configuration file and import the new configuration into the OpenVPN Connect Client software. Alternatively, use a different client, such as the OpenVPN GUI client (v11.12.0.0) or the Viscosity client (v.1.7.14).
