---
source_url: https://docs.aws.amazon.com/vpn/latest/clientvpn-user/client-vpn-connect-windows-release-notes.html
---

# AWS Client VPN for Windows release notes
<a name="client-vpn-connect-windows-release-notes"></a>

The following table contains the release notes and download links for the current and previous versions of AWS Client VPN for Windows x64-based and Windows Arm64-based systems.

**Note**
We continue to provide usability and security fixes with every release. We strongly recommend that you use the latest version for every platform. Previous versions might be affected by usability or security issues. See individual version entries below for details.

| Version | Changes | Date | Download link and SHA256 |
| --- | --- | --- | --- |
| 6.2.1 | This release includes minor enhancements and fixes the following issues present in earlier 6.x versions:+  Loss of network access after resuming from hibernation while connected <br />+  Short host names failing to resolve when a Client VPN endpoint pushed a duplicate DNS server address <br />+  Internal name resolution failing when a physical network adapter used the same DNS suffix as the internal domain <br />+  A missing `platform-version` value in the client connect handler event, which could cause connections to be denied by authorization handlers that explicitly rely on this field <br />+  Import failures for `.ovpn` profiles whose certificate or key paths used double backslash separators <br />+  GUI and CLI crashes that occurred when the user's configuration directory is a symbolic link <br />+  Custom error messages from the authorization Lambda not displaying in some scenarios <br />+  Installation failures on machines without the Microsoft Visual C\+\+ Runtime libraries <br />+  Added support for the `remote` host keyword in the `route` OpenVPN directive  | October 16, 2026 |  +   [Download Windows x64 version 6.2.1](https://d3c4iklh14o4hj.cloudfront.net/WPF/6.2.1/AWS_VPN_Client.msi)  <br />sha256: 89b9522c723b2be6d4366ab78a592a60f7b86243edfa67bbb4977d0c4a5215ba <br />+   [Download Windows Arm64 version 6.2.1](https://d3c4iklh14o4hj.cloudfront.net/WPF_ARM64/6.2.1/AWS_VPN_Client_ARM64.msi)  <br />sha256: 3254a8832760373dab5ac0958d4bc23145434e50d675c7595f8b2b265f41e8a9   |
| 6.2.0 |  +  Support for Device Posture <br />+  Minor bug fixes and enhancements   | September 28, 2026 |  +   [Download Windows x64 version 6.2.0](https://d3c4iklh14o4hj.cloudfront.net/WPF/6.2.0/AWS_VPN_Client.msi)  <br />sha256: 729d438555bf2ff671ea078c4325de7475718bee8b7b8acdf3f669bf2fb74641 <br />+   [Download Windows Arm64 version 6.2.0](https://d3c4iklh14o4hj.cloudfront.net/WPF_ARM64/6.2.0/AWS_VPN_Client_ARM64.msi)  <br />sha256: 6bc448d8ef61ea274fa9167654a65e60b3b580642405aef81f52224d1a6d7bca   |
| 6.1.1 |  +  Fixed a bug that blocked automatic upgrades in version 6.0.3   | September 25, 2026 |  +   [Download Windows x64 version 6.1.1](https://d3c4iklh14o4hj.cloudfront.net/WPF/6.1.1/AWS_VPN_Client.msi)  <br />sha256: 8f57525c843ea94cbd835b45298f2ce3cbdb62fc331b40139c4785af4e8ba51b <br />+   [Download Windows Arm64 version 6.1.1](https://d3c4iklh14o4hj.cloudfront.net/WPF_ARM64/6.1.1/AWS_VPN_Client_ARM64.msi)  <br />sha256: 1fa1e6d2b5f9914d93bd0898b32c3b36692772dd4c65a52a49d231c8d4ce05b6   |
| 6.1.0 |  +  Minor bug fixes and enhancements   | September 24, 2026 | No longer supported. |
| 6.0.3 |  +  Enabled upgrade notifications prompting pre-6.x users to move to 6.x <br />+  Prompt to disconnect on GUI app quit <br />+  Improved security posture <br />+  Minor bug fixes and enhancements   | September 14, 2026 | No longer supported. |
| 6.0.2 |  +  Fixed TAP adapter installation issue due to name conflicts <br />+  Fixed duplicate profile name during migration by adding suffix <br />+  Minor bug fixes and enhancements   | August 12, 2026 |  +   [Download Windows x64 version 6.0.2](https://d20adtppz83p9s.cloudfront.net/WPF/6.0.2/AWS_VPN_Client.msi)  <br />sha256: 519e5d3e62dbe438f501f0da226ec386216df54be4a31f9d349731d7dda080aa <br />+   [Download Windows Arm64 version 6.0.2](https://d20adtppz83p9s.cloudfront.net/WPF_ARM64/6.0.2/AWS_VPN_Client_ARM64.msi)  <br />sha256: 4e8466dafd71f3a16e56a6caa316942f1c4320fc50912fb0091441f0bb7ffc7d   |
| 6.0.1 |  +  Fixed a SAML authentication issue that led to sporadic VPN connection errors in version 6.0.0 <br />+  Minor bug fixes and enhancements   | August 7, 2026 |  +   [Download Windows x64 version 6.0.1](https://d20adtppz83p9s.cloudfront.net/WPF/6.0.1/AWS_VPN_Client.msi)  <br />sha256: 23a008656f10f3af28951fe3ae69da46117f0f50e86cbc25490a4f50374f3b5b <br />+   [Download Windows Arm64 version 6.0.1](https://d20adtppz83p9s.cloudfront.net/WPF_ARM64/6.0.1/AWS_VPN_Client_ARM64.msi)  <br />sha256: 2a531aa5c7a525be24b6361127df66e8d8bfce2da8d5cb32bc333ec27cd228a6   |
| 6.0.0 |  +  Added support for command-line interface (CLI) <br />+  Added support for enterprise administrative controls <br />+  Redesigned AWS Client VPN graphical user interface (GUI) <br />+  Modernized connectivity architecture and improved security posture <br />+  Improved connection establishment time <br />+  Relocated configuration files to a system-wide admin-protected location. If profiles or preferences are missing after the upgrade, see [Profiles or preferences missing after upgrade to version 6.0](windows-troubleshooting.md#windows-troubleshooting-profiles-missing) for resolution steps.   | August 4, 2026 |  +   [Download Windows x64 version 6.0.0](https://d20adtppz83p9s.cloudfront.net/WPF/6.0.0/AWS_VPN_Client.msi)  <br />sha256: 76a4d2b76e95a5b43b6f0d0e212ef7bba20660ac9390766555414abc30fe4cb3 <br />+   [Download Windows Arm64 version 6.0.0](https://d20adtppz83p9s.cloudfront.net/WPF_ARM64/6.0.0/AWS_VPN_Client_ARM64.msi)  <br />sha256: a8f47e4010de34dd720f22e8c754c98e45ea1c1c63b00bbb00259804069314ea   |
| 5.4.3 |  +  Minor enhancements   | July 23, 2026 |  +   [Download Windows x64 version 5.4.3](https://d20adtppz83p9s.cloudfront.net/WPF/5.4.3/AWS_VPN_Client.msi)  <br />sha256: eaa60ff88478745604c500020d824bfdd361a739b5021db0378ece4c3f4d60b1 <br />+   [Download Windows Arm64 version 5.4.3](https://d20adtppz83p9s.cloudfront.net/WPF_ARM64/5.4.3/AWS_VPN_Client_ARM64.msi)  <br />sha256: bdcb1a5acff49770dff48d2aa8dce3ca60531cd04c1d749c518ef5567e0231b0   |
| 5.4.2 |  +  Minor enhancements.   | July 20, 2026 | No longer supported. |
| 5.4.1 |  +  Minor enhancements.   | July 9, 2026 | No longer supported. |
| 5.4.0 |  +  Improved security posture.   | June 22, 2026 | No longer supported. |
| 5.3.7 |  +  Minor bug fixes and enhancements.   | June 15, 2026 | No longer supported. |
| 5.3.6 |  +  Rolled back changes from 5.3.5   | May 28, 2026 | No longer supported. |
| 5.3.5 |  +  Minor bug fixes and enhancements. <br />+  Improved security posture.   | May 27, 2026 | No longer supported. |
| 5.3.4 |  +  Minor bug fixes and enhancements. <br />+  Improved security posture.   | March 27, 2026 | No longer supported. |
| 5.3.3 |  +  Fixed connection failures in version 5.3.2   | February 28, 2026 | No longer supported. |
| 5.3.2 |  +  Minor bug fixes and enhancements. <br />+  Improved security posture.   | February 17, 2026 | No longer supported. |
| 5.3.1 | Minor bug fixes and enhancements. | September 30, 2025 | No longer supported. |
| 5.3.0 (Arm64) | New AWS Client VPN support for Windows Arm64-based operating systems. <br />This release includes all updates from the Windows (x64) 5.3.0 release. | August 26, 2025 | No longer supported. |
| 5.3.0  |  +  Minor enhancements. <br />+  Added support for IPv6 connections   | August 14, 2025 | No longer supported. |
| 5.2.2 | Improved security posture. | June 2, 2025 | No longer supported. |
| 5.2.1 |  +  Added support for the `ping-exit` OpenVPN flag. <br />+  Updated the OpenSSL library. <br />+  Minor bug fixes and enhancements.   | April 21, 2025 | No longer supported. |
| 5.2.0 |  +  Minor enhancements. <br />+  Added support for Client Route Enforcement.    | April 8, 2025 | No longer supported. |
| 5.1.0 |  +  Fixed an issue that caused AWS Client VPN version 5.0.x to automatically reconnect to VPN after an inactivity timeout disconnect. <br />+  Minor bug fixes and enhancements.   | March 17, 2025 | No longer supported. |
| 5.0.2 |  +  Fixed a DNS issue for concurrent connections. <br />+  Fixed sporadic issues when installing new TAP adapters.   | February 24, 2025 | No longer supported. |
| 5.0.1 | Fixed an issue that led to sporadic VPN connection errors on Windows client version 5.0.0. | January 30, 2025 | No longer supported. |
| 5.0.0 |  +  Added support for concurrent connections. <br />+  Updated the TAP driver version. <br />+  Updated the graphical user interface. <br />+  Minor bug fixes and enhancements.   | January 21, 2025 | No longer supported. |
| 4.1.0 | Minor bug fixes and enhancements. | November 12, 2024 | No longer supported. |
| 4.0.0 | Minor enhancements. | September 25, 2024 | No longer supported. |
| 3.14.2 | Added support for the `mssfix` OpenVPN flag. | September 4, 2024 | No longer supported. |
| 3.14.1 | Minor bug fixes and enhancements. | August 22, 2024 | No longer supported. |
| 3.14.0 |  +  Added support for the `tap-sleep` OpenVPN flag. <br />+  Updated the OpenVPN and OpenSSL libraries.   | August 12, 2024 | No longer supported. |
| 3.13.0 | Updated the OpenVPN and OpenSSL libraries. | July 29, 2024 | No longer supported. |
| 3.12.1 | Fixed an issue that prevented Windows client version 3.12.0 from establishing VPN connection for some users. | July 18, 2024 | No longer supported. |
| 3.12.0 |  +  Automatically reconnect when local area network ranges change. <br />+  Removed automatic application focus when connected with SAML endpoints.   | May 21, 2024 | No longer supported |
| 3.11.2 | Resolved a SAML authentication issue with Chromium-based browsers since version 123. | April 11, 2024 | No longer supported. |
| 3.11.1 |  +  Fixed a buffer overflow action that could potentially allow a local actor to execute arbitrary commands with elevated permissions. <br />+  Improved security posture.   | February 16, 2024 | No longer supported. |
| 3.11.0 |  +  Fixed a connectivity issue caused by Windows VMs. <br />+  Fixed connectivity issues for some LAN configurations. <br />+  Improved accessibility.   | December 6, 2023 | No longer supported. |
| 3.10.0 |  +  Fixed a connectivity issue when NAT64 is enabled in the client network. <br />+  Fixed a connectivity issue when Hyper-V network adapters are installed on the client machine. <br />+  Minor bug fixes and enhancements.   | August 24, 2023 | No longer supported. |
| 3.9.0 | Improved security posture. | August 3, 2023 | No longer supported. |
| 3.8.0 | Improved security posture. | July 15, 2023 | No longer supported |
| 3.7.0 | Rolled back changes from 3.6.0. | July 15, 2023 | No longer supported |
| 3.6.0 | Improved security posture. | July 14, 2023 | No longer supported |
| 3.5.0 | Minor bug fixes and enhancements. | April 3, 2023 | No longer supported |
| 3.4.0 | Rolled back the changes from version 3.3.0. | March 28, 2023 | No longer supported |
| 3.3.0 | Minor bug fixes and enhancements. | March 17, 2023 | No longer supported |
| 3.2.0 |  +  Added support for "verify-x509-name" OpenVPN flag. <br />+  Automatically detect when updated versions of the client are available. <br />+  Added the ability to automatically install new client versions when available.   | January 23, 2023 | No longer supported |
| 3.1.0 | Improved security posture. | May 23, 2022 | No longer supported |
| 3.0.0 |  +  Added Windows 11 support. <br />+  Fixed TAP Windows driver naming causing other driver names to be affected. <br />+  Fixed the banner message not being displayed when using federated authentication. <br />+  Fixed banner text display for longer text. <br />+  Enhanced security posture.   | March 3, 2022 | No longer supported |
| 2.0.0 |  +  Added support for banner text after new connection is established. <br />+  Removed ability to use pull-filter in relation to echo. i.e. pull-filter \* echo <br />+  Minor bug fixes and enhancements.   | January 20, 2022 | No longer supported |
| 1.3.7 |  +  Fixed federated authentication connection attempt in some cases. <br />+  Minor bug fixes and enhancements.   | November 8, 2021 | No longer supported |
| 1.3.6 |  +  Added support for OpenVPN flags: connect-retry-max, dev-type, keepalive, ping, ping-restart, pull, rcvbuf, server-poll-timeout. <br />+  Minor bug fixes and enhancements.   | September 20, 2021 | No longer supported |
| 1.3.5 | Patch to delete large windows log files. | August 16, 2021 | No longer supported |
| 1.3.4 |  +  Added support for OpenVPN flag: dhcp-option. <br />+  Minor bug fixes and enhancements.   | August 4, 2021 | No longer supported |
| 1.3.3 |  +  Added support for OpenVPN flags: inactive, pull-filter, route. <br />+  Fixed an issue that caused app crashes on disconnect or exit. <br />+  Fixed an issue with Active Directory usernames with backslash. <br />+  Fixed app crash when manipulating profile list outside of app. <br />+  Minor bug fixes and enhancements.   | July 1, 2021 | No longer supported |
| 1.3.2 |  +   Add IPv6 leak prevention, when it is configured. <br />+  Fixed a potential crash when you use the **Show Details** option under **Connection**.   | May 12, 2021 | No longer supported |
| 1.3.1 |  +   Added support for multiple client certificates with same subject. Expired certificates will be ignored. <br />+  Fixed local log retention to reduce disk usage. <br />+  Added support for 'route-ipv6' OpenVPN directive. <br />+  Minor bug fixes and enhancements.   | April 5, 2021 | No longer supported |
| 1.3.0 | Added support features such as error reporting, sending diagnostic logs, and analytics. | March 8, 2021 | No longer supported |
| 1.2.7 |  +  Added support for the cryptoapicert OpenVPN directive. <br />+  Fixed stale routes between connections. <br />+  Minor bug fixes and enhancements.   | February 25, 2021 | No longer supported |
| 1.2.6 | Minor bug fixes and enhancements. | October 26, 2020 | No longer supported |
| 1.2.5 |  +  Added support for comments in the OpenVPN configuration. <br />+  Added an error message for TLS handshake errors.   | October 8, 2020 | No longer supported |
| 1.2.4 | Minor bug fixes and enhancements. | September 1, 2020 | No longer supported |
| 1.2.3 | Roll back changes in version 1.2.2. | August 20, 2020 | No longer supported |
| 1.2.1 | Minor bug fixes and enhancements. | July 1, 2020 | No longer supported |
| 1.2.0 |  +  Added support for [SAML 2.0-based federated authentication](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/client-authentication.html#federated-authentication). <br />+  Deprecated support for the Windows 7 platform.   | May 19, 2020 | No longer supported |
| 1.1.1 | Minor bug fixes and enhancements. | April 21, 2020 | No longer supported |
| 1.1.0 |  +  Added support for OpenVPN static challenge echo functionality to hide or show the text displayed in the user interface. <br />+  Minor bug fixes and enhancements.   | March 9, 2020 | No longer supported |
| 1.0.0 | The initial release. | February 4, 2020 | No longer supported |
