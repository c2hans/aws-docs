---
source_url: https://docs.aws.amazon.com/vpn/latest/clientvpn-user/connect-aws-client-vpn-connect.html
---

# Connect to an AWS Client VPN endpoint using an AWS provided client
<a name="connect-aws-client-vpn-connect"></a>

You can connect to a Client VPN endpoint using the AWS provided client, which is supported on Windows, macOS, and Ubuntu. You can use the client in two ways — through the graphical user interface (GUI) or the command line interface (CLI). The AWS provided client also supports up to five concurrent connections as well as OpenVPN directives.

**Topics**
+ [Updates](#support-updates)
+ [CLI commands](#cli-commands)
+ [Admin controls](#admin-controls)
+ [Support for concurrent connections](#support-multi)
+ [Connecting with device posture](#connect-device-posture)
+ [OpenVPN directives](#support-openvpn)

## Security
<a name="support-security"></a>

Security is the highest priority in the AWS provided client. We regularly release patches to improve the security posture of the application. The AWS provided client includes several unique security features compared to other OpenVPN clients, including SAML authentication, Client Routes Enforcement, and device settings monitoring.

While the AWS provided client is designed to mitigate threats originating from misconfigured or compromised network environment, it is not responsible for modifying the environment or eliminating the external threats at their source. The AWS provided client relies on the customers to maintain a secure and well-configured environment. This includes:
+ Preventing unauthorized modification or abuse by local users
+ Restricting administrative privileges to trusted users
+ Maintaining up-to-date security patches

## Software updates
<a name="support-updates"></a>

We recommend that you always run the latest version of the AWS provided client to receive the newest features and security patches.

On Windows and macOS, the AWS provided client automatically checks for a newer version and, when one is available, displays a notification that prompts you to update. Follow the prompt to install the update.

On Ubuntu, the AWS provided client for Linux does not automatically check for updates. We recommend that you install the client through the package repository and keep it current from there. For more information, see [Install the provided AWS Client VPN for Linux](client-vpn-connect-linux-install.md).

## Connect using the command line interface
<a name="cli-commands"></a>

The AWS Client VPN Command Line Interface (CLI) provides a lightweight, scriptable interface to manage VPN profiles and connections. The CLI is available on Windows, macOS, and Linux, and enables enterprise administrators to automate VPN deployments, manage profiles at scale, and integrate Client VPN with existing management infrastructure.

The CLI tool is named `aws-vpn-client` and is installed alongside the AWS provided client from version 6.0 onwards.

The CLI provides access to all features of the client application, including profile management, connection management, and administrative configuration.

For details on CLI commands and syntax, see [CLI command syntax](cli-command-syntax.md).

## Administrative controls
<a name="admin-controls"></a>

AWS Client VPN administrative controls provide global configuration settings and profile management capabilities that enable administrators to manage VPN client deployments at scale.

With administrative controls, administrators can:
+ Control profile management permissions for end users
+ Set the maximum number of concurrent connections
+ Import profiles globally for all users on a device
+ Manage telemetry settings

To run administrative commands, you need elevated privileges (sudo on macOS/Linux, administrator on Windows).

You can use the following preference settings with `aws-vpn-client put-preference`:

Manage preferences
Use `aws-vpn-client put-preference` with elevated privileges to set global configuration values such as `max-connections`, `enable-user-profile-management`, and `enable-telemetry`.

In addition, you can import profiles globally for all users on a device by using `aws-vpn-client import-profile` with the `--global` flag and elevated privileges.

For the full list of CLI commands and syntax, see [CLI command syntax](cli-command-syntax.md).

## Support for concurrent connections using an AWS provided client
<a name="support-multi"></a>

The AWS provided client supports connecting to multiple concurrent sessions. This is helpful if you need access to resources across multiple AWS environments and have different endpoints for those resources. For example, you might need access to a database in an environment at an endpoint that's different from the endpoint you're currently connected to, but you don't want to disconnect the current connection. To enable your AWS provided client to connect to multiple sessions, download the configuration file that your administrator created for each endpoint, and then create a connection profile for each file. Using the AWS provided client, you can then connect to multiple sessions without disconnecting from any session currently open. This is supported for AWS provided clients only. For the steps to connect to concurrent sessions, see [Connect using the AWS provided client](client-vpn-connect-how.md).

When connecting to multiple endpoints, Client VPN checks for conflicts with other open endpoint connections — for example, if two sessions have conflicting CIDR blocks or routing policies, or if you're already connected with a full tunnel connection. If the check finds conflicts, the connection fails. You must either choose a different connection that doesn't conflict with the open connection, or disconnect from the open session that's causing the conflict.

Concurrent DNS connections are allowed. The DNS server of one of the DNS-enabled connections is applied. Depending on the DNS server, you might be prompted for authentication during that reconnection.

**Note**
The maximum number of allowed concurrent sessions is five.

## Connecting to an endpoint that requires device posture
<a name="connect-device-posture"></a>

If your administrator has enabled device posture on an endpoint, the AWS provided client collects device posture data from your device trust provider when you connect and sends it to the endpoint for evaluation. To connect to an endpoint that requires device posture, you must meet the following requirements:
+ Use the AWS provided client, version 6.2.0 or later. Device posture is not supported with other OpenVPN clients.
+ Your device trust provider must be set up on your device. The following providers are supported by operating system: CrowdStrike (macOS, Windows), Jamf (macOS), and JumpCloud (macOS, Windows, Ubuntu).
+ The profile you import includes an `aws-auth-device-posture <provider>` directive in its configuration. Do not remove this line.

If your device does not meet the policy, the connection is refused. Your session can also end mid-session if your device later falls out of compliance. If you are denied unexpectedly, confirm your device trust provider is set up and your device is compliant with your organization's requirements, then try again.

## OpenVPN directives
<a name="support-openvpn"></a>

The AWS provided client supports the following OpenVPN directives. For more information about these directives, see the documentation at the [OpenVPN website](https://openvpn.net/).
+ auth-federate
+ auth-nocache
+ auth-retry
+ auth-user-pass
+ aws-auth-device-posture
+ block-outside-dns
+ ca
+ cert
+ cipher
+ client
+ connect-retry
+ connect-retry-max
+ cryptoapicert
+ dev
+ dev-type
+ dhcp-option
+ ifconfig-ipv6
+ inactive
+ keepalive
+ key
+ mssfix
+ nobind
+ persist-key
+ persist-tun
+ ping
+ ping-exit
+ ping-restart
+ proto
+ pull
+ pull-filter
+ remote
+ remote-cert-tls
+ remote-random-hostname
+ reneg-sec
+ resolv-retry
+ route
+ route-ipv6
+ server-poll-timeout
+ static-challenge
+ tun-mtu
+ verb
+ verify-x509-name

**Note**
Starting with version 6.0, the AWS provided client no longer supports the `rcvbuf`, `tap-sleep`, and `tun-mtu-extra` directives. When you upgrade from an earlier version, these directives are automatically removed from your existing profiles. Do not include them in profiles that you import in version 6.0 or later; otherwise the import fails.
