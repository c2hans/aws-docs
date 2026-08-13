---
source_url: https://docs.aws.amazon.com/vpn/latest/clientvpn-user/client-vpn-connect-linux-release-notes.html
---

# AWS Client VPN for Linux release notes
<a name="client-vpn-connect-linux-release-notes"></a>

The following table contains the release notes and download links for the current and previous versions of AWS Client VPN for Linux.

**Note**
We continue to provide usability and security fixes with every release. We strongly recommend that you use the latest version for every platform. Previous versions may be affected by usability and/or security issues. See release notes for details.

| Version | Changes | Date | Download link |
| --- | --- | --- | --- |
| 6.0.1 |  +  Added support for command-line interface (CLI) <br />+  Added support for enterprise administrative controls <br />+  Redesigned graphical user interface (GUI) <br />+  Modernized connectivity architecture and improved security posture <br />+  Improved connection establishment time <br />+  Relocated configuration files to a system-wide admin-protected location. If profiles or preferences are missing after the upgrade, see [Profiles or preferences missing after upgrade to version 6.0](linux-troubleshooting.md#linux-troubleshooting-profiles-missing) for resolution steps.   | August 12, 2026 | [Download version 6.0.1](https://d20adtppz83p9s.cloudfront.net/GTK/6.0.1/awsvpnclient_amd64.deb)sha256: c3c10d91693efa2800c4812afa7cdb0be22181fa9a2d551030fa6f4c819e8cc9 |
| 5.4.0 |  +  Improved security posture   | June 22, 2026 | [Download version 5.4.0](https://d20adtppz83p9s.cloudfront.net/GTK/5.4.0/awsvpnclient_amd64.deb)sha256: 7dd9e28962bf64bf94ef41b8e1f68de5e0d0393d71300767698fb336c69276cc |
| 5.3.3 |  +  Minor bug fixes and enhancements <br />+  Improved security posture   | May 18, 2026 | [Download version 5.3.3](https://d20adtppz83p9s.cloudfront.net/GTK/5.3.3/awsvpnclient_amd64.deb)sha256: d0096c934b36122c245d8c2243d4146cdac67125c7421c4e1e6ad430eb3adfcf |
| 5.3.2 |  +  Minor bug fixes and enhancements. <br />+  Improved security posture.   | December 17, 2025 | No longer supported. |
| 5.3.1 |  +  Minor enhancements.   | September 25, 2025 | No longer supported. |
| 5.3.0 |  +  Minor enhancements. <br />+  Added support for IPv6 connections.   | August 14, 2025 | No longer supported. |
| 5.2.0 |  +  Minor enhancements. <br />+  Added support for Client Route Enforcement.   | April 8, 2025 | No longer supported. |
| 5.1.0 |  +  Fixed an issue that caused AWS Client VPN version 5.0.x to automatically reconnect to VPN after an inactivity timeout disconnect. <br />+  Minor bug fixes and enhancements.   | March 17, 2025 | No longer supported. |
| 5.0.0 |  +  Added support for multiple concurrent connections. <br />+  Updated the graphical user interface. <br />+  Minor bug fixes and enhancements.   | January 21, 2025 | No longer supported. |
| 4.1.0 |  +  Added support for Ubuntu 22.04 and 24.04. <br />+  Bug fixes.   | November 12, 2024 | No longer supported. |
| 4.0.0 | Minor enhancements. | September 25, 2024 | No longer supported. |
| 3.15.1 | Added support for the `mssfix` OpenVPN flag. | September 4, 2024 | No longer supported. |
| 3.15.0 |  + Added support for the `tap-sleep` OpenVPN flag.<br />+ Updated the OpenVPN and OpenSSL libraries.  | August 12, 2024 | No longer supported. |
| 3.14.0 |  +  Updated the OpenVPN and OpenSSL libraries.   | July 29, 2024 | No longer supported. |
| 3.13.0 |  +  Automatically reconnect when local area network ranges change.   | May 21, 2024 | No longer supported. |
| 3.12.2 |  +  Resolved a SAML authentication issue with Chromium-based browsers since version 123.   | April 11, 2024 | No longer supported. |
| 3.12.1 |  +  Fixed a buffer overflow action that could potentially allow a local actor to execute arbitrary commands with elevated permissions. <br />+  Improved security posture.   | February 16, 2024 | No longer supported. |
| 3.12.0 |  +  Fixed connectivity issues for some LAN configurations.   | December 19, 2023 | No longer supported. |
| 3.11.0 |  +  Rollback for "Fixed connectivity issues for some LAN configurations". <br />+  Improved accessibility.   | December 6, 2023 | No longer supported. |
| 3.10.0 |  +  Fixed connectivity issues for some LAN configurations. <br />+  Improved accessibility.   | December 6, 2023 | No longer supported. |
| 3.9.0 |  +  Fixed a connectivity issue when NAT64 is enabled in the client network. <br />+  Minor bug fixes and enhancements.   | August 24, 2023 | No longer supported. |
| 3.8.0 |  +  Improved security posture.   | August 3, 2023 | No longer supported. |
| 3.7.0 |  +  Improved security posture.   | July 15, 2023 | No longer supported. |
| 3.6.0 |  +  Rolled back changes from 3.5.0.   | July 15, 2023 | No longer supported. |
| 3.5.0 |  +  Improved security posture.   | July 14, 2023 | No longer supported. |
| 3.4.0 |  +  Added support for "verify-x509-name" OpenVPN flag.   | February 14, 2023 | No longer supported. |
| 3.1.0 |  +  Fixed issue for drive type detection. <br />+  Improved security posture.   | May 23, 2022 | No longer supported. |
| 3.0.0 |  +  Fixed the banner message not being displayed when using federated authentication. <br />+  Fixed banner text display for longer text and specific character sequences. <br />+  Enhanced security posture.   | March 3, 2022 | No longer supported. |
| 2.0.0 |  +  Added support for banner text after new connection is established. <br />+  Removed ability to use pull-filter in relation to echo. i.e. pull-filter \* echo <br />+  Minor bug fixes and enhancements.   | January 20, 2022 | No longer supported. |
| 1.0.3 |  +  Fixed federated authentication connection attempt in some cases. <br />+  Minor bug fixes and enhancements.   | November 8, 2021 | No longer supported. |
| 1.0.2 |  +  Added support for OpenVPN flags: connect-retry-max, dev-type, keepalive, ping, ping-restart, pull, rcvbuf, server-poll-timeout. <br />+  Minor bug fixes and enhancements.   | September 28, 2021 | No longer supported. |
| 1.0.1 |  +  Enabled option to quit from Ubuntu application bar. <br />+  Added support for OpenVPN flags: inactive, pull-filter, route. <br />+  Minor bug fixes and enhancements.   | August 4, 2021 | No longer supported. |
| 1.0.0 | The initial release. | June 11, 2021 | No longer supported. |
