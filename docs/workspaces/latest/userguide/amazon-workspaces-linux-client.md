---
source_url: https://docs.aws.amazon.com/workspaces/latest/userguide/amazon-workspaces-linux-client.html
---

# WorkSpaces Linux client application
<a name="amazon-workspaces-linux-client"></a>

The following information will help you get started with the WorkSpaces Linux client application.

**Topics**
+ [Requirements](#linux-requirements)
+ [Setup and installation](#linux_setup)
+ [Connecting to your WorkSpace](#linux_connecting)
+ [Manage your login information](#manage-login-info-linx)
+ [Client views](#linux_views)
+ [Client language](#linux_client_lang)
+ [Display support](#linux-display-support)
+ [Proxy servers](#linux_proxy_server)
+ [Command shortcuts](#linux_shortcuts)
+ [Clipboard redirection](#linux_clipboard)
+ [Disconnect](#linux_disconnect)
+ [Release notes](#linux-release-notes)

## Requirements
<a name="linux-requirements"></a>

For the WorkSpaces Linux client version 2023.x to be able to access the WorkSpaces service, you must add the WorkSpaces Web Access domain (https://webclient.amazonworkspaces.com/) to the allowlist on the network from which the client is trying to access the service.

**Note**
By default, Linux client access is disabled. To use this client with your WorkSpace, your Amazon WorkSpaces administrator must enable Linux client access for your WorkSpaces directory. For more information, see [ Control Device Access](https://docs.aws.amazon.com/workspaces/latest/adminguide/update-directory-details.html#control-device-access) in the *Amazon WorkSpaces Administration Guide*.
If your WorkSpace is located in the Asia Pacific (Mumbai) Region, you must use version 3.1.3 or later of the Amazon WorkSpaces Linux client application.
The WorkSpaces Linux client version 2023.0.4395 for Ubuntu 22.04 is only available for the DCV.

## Setup and installation
<a name="linux_setup"></a>

Download and install the WorkSpaces Linux client application from [Amazon WorkSpaces Client Downloads](https://clients.amazonworkspaces.com/). Detailed installation instructions are included on the Linux client page on the Client Downloads site.

### 2023.x clients
<a name="w2aab9c14b9c13b1"></a>

To launch the Linux client from the command line, use:

`workspacesclient`

**Note**
When running a new client application, you will be prompted for your registration code, which is can be found in your welcome email. For existing customers, you can find the registration code under `/home/UserName/.local/share/Amazon Web Services/Amazon WorkSpaces/RegisterationList.json`.

### 3.x and 4.x clients
<a name="w2aab9c14b9c13b3"></a>

To launch the Linux client from the command line, use:

`/opt/workspacesclient/workspacesclient`

## Connecting to your WorkSpace
<a name="linux_connecting"></a>

To connect to your WorkSpace, complete the following procedure.

**To connect to your WorkSpace**

1. The first time that you run the client application, you are prompted for your registration code, which is contained in your welcome email. The WorkSpaces client application uses the registration code and user name to identify which WorkSpace to connect to. When you launch the client application later, the same registration code is used. To enter a different registration code, launch the client application, and then choose **Change Registration Code** at the bottom of the login page.

1. Enter your sign-in credentials in the login screen and choose **Sign In**. If your WorkSpaces administrator has enabled multi-factor authentication for your organization's WorkSpaces, you are prompted for a passcode to complete your login. Your WorkSpaces administrator will provide more information about how to obtain your passcode.

1. If your WorkSpaces administrator has not disabled the **Keep me logged in** feature, you can select the **Keep me logged in** check box at the bottom of the login screen to save your credentials securely so that you can connect to your WorkSpace easily while the client application remains running. Your credentials are securely cached up to the maximum lifetime of your Kerberos ticket.

   After the client application connects to your WorkSpace, your WorkSpace desktop is displayed.

An interruption of network connectivity causes an active session to be disconnected. This can be caused by events such as closing the laptop lid, or the loss of your wireless network connection. The WorkSpaces client application for Linux attempts to reconnect the session automatically if network connectivity is regained within a certain amount of time. The default session resume timeout is 20 minutes, but this timeout can be modified by your network administrator.

## Manage your login information
<a name="manage-login-info-linx"></a>

You can view your registration code and what Region your WorkSpace is in. You can specify whether you want the WorkSpaces client application to save your current registration code, and you can assign a name to your WorkSpace. You can also specify if you want Amazon WorkSpaces to keep you logged in to a WorkSpace until you quit or your login period expires.

### 2023.x clients
<a name="w2aab9c14c13b5b1"></a>

**To manage your login information for a WorkSpace**

1. In the WorkSpaces client application, go to **Settings**, **Manage Login Information**.

1. In the **Settings** dialog box, you can see the registration code and Region information for your WorkSpace.

1. (Optional) If you want the WorkSpaces client to remember your current registration code, enable **Save registration code**.

1. Under **Saved registration codes**, select the WorkSpace you want to name.

1. In the **WorkSpace name** box, enter a name for the WorkSpace.

1. (Optional) If you want WorkSpaces to keep you logged in until you quit or your login period expires, select the **Keep me logged in** check box.

1. Choose **Save**.

### 3.x and 4.x clients
<a name="w2aab9c14c13b5b3"></a>

**To manage your login information for a WorkSpace**

1. In the WorkSpaces client application, go to **Settings**, **Manage Login Information**.

1. In the **Manage Login Information** dialog box, you can see the registration code and Region information for your WorkSpace.

1. (Optional) If you want the WorkSpaces client to remember your current registration code, select the **Remember Registration Code** check box.

1. Under **Saved registration codes**, select the WorkSpace you want to name.

1. In the **WorkSpace name** box, enter a name for the WorkSpace.

1. (Optional) If you want WorkSpaces to keep you logged in until you quit or your login period expires, select the **Keep me logged in** check box.

1. Choose **Save**.

## Client views
<a name="linux_views"></a>

### Full screen mode for 2023.x clients
<a name="w2aab9c14c15b3b1"></a>

You can switch to full screen mode by selecting the full screen icon in the client application menu. While in full screen mode, you can switch back to window mode by moving the pointer to the top of the screen. The client application menu is displayed, and you can choose **Leave Full Screen** in the client application menu.

### Full screen mode for 3.x and 4.x clients
<a name="w2aab9c14c15b3b3"></a>

You can switch to full screen mode by choosing **View**, **Enter Full Screen** in the client application menu.

While in full screen mode, you can switch back to window mode by moving the pointer to the top of the screen. The client application menu is displayed, and you can choose **View**, **Leave Full Screen** in the client application menu.

You can also toggle full screen mode by pressing Ctrl\+Alt\+Enter.

## Client language
<a name="linux_client_lang"></a>

### 2023.x clients
<a name="w2aab9c14c17b3b1"></a>

The WorkSpaces client automatically selects the default display language used by the operating system on your computer.

### 3.x and 4.x clients
<a name="w2aab9c14c17b3b3"></a>

You can select the language displayed by the client by performing the following steps.

**Note**
In the client, Japanese is available in all Regions. However, Japanese is only available in Tokyo for individual WorkSpaces.

**To select the client language**

1. In the WorkSpaces client application, go to **Settings**, **Change Language**.

1. Enter your desired language in the **Select a language** list and choose **Save**.

1. Restart the client.

## Display support
<a name="linux-display-support"></a>

WorkSpaces WorkSpaces Value, Standard, Performance, Power, PowerPro, and GPU-enabled bundles support a maximum of four displays and a maximum resolution of 3840x2160 (ultra-high definition, or UHD). The maximum supported resolution depends on the number of displays, as shown in the following table.

| Displays | Resolution |
| --- | --- |
| 2 | 3840x2160 |
| 4 | 1920x1200 |

**Note**
You can only extend the display. You cannot duplicate the display. Duplicating the display will cause your session to be disconnected.

The WorkSpaces client application extracts the Extended Display Information Data (EDID) of all attached displays and determines the best compatibility match before starting the session. If you have a high pixel density (high DPI) display, the client application automatically scales the streaming window according to your local DPI settings. For better maximum resolution with high DPI displays, see [Enabling high DPI display for WorkSpaces](high_dpi_support.md).

**To use multiple monitors with WorkSpaces**

1. Configure your local machine to use multiple monitors.

1. Start the WorkSpaces client application and log in to your WorkSpace.

1. Depending on which client you're using, do one of the following:
**Note**
If you are using client version is 2023.x with DCV WorkSpaces, and if there are three or more monitors connected, your WorkSpace can also extend full-screen across a selection of those available monitors. Selected monitors must be set adjacent or sharing a side with each other, in your display setting. DCV multi-monitor support is built using DCV technology. For more information about requirements and troubleshooting, see [ Extending full-screen across selected monitors](https://docs.aws.amazon.com/dcv/latest/userguide/full-screen-selected-monitors.html).
[See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/userguide/amazon-workspaces-linux-client.html)

Your WorkSpace should now be extended across your displays. Whichever display you have designated as your primary display is also the primary display in WorkSpaces when you enter full screen mode.

**Note**
Using full screen mode on only some of the displays in a multiple monitor setup isn't possible. You can, however, press Alt\+F10 or double-click the title bar to maximize the WorkSpaces client window on a display without extending the WorkSpace to the other displays.

## Proxy servers
<a name="linux_proxy_server"></a>

If your network requires you to use a proxy server to access the internet, you can enable your WorkSpaces client application to use a proxy for HTTPS (port 443) traffic. The WorkSpaces client applications use the HTTPS port for updates, registration, and authentication.

**Note**
The desktop streaming connections to the WorkSpace require ports 4172 and 4195 to be enabled, and do not go through the proxy server.
Proxy servers that require authentication with a sign-in credentials are not supported.

### Using a proxy server
<a name="w2aab9c14c21b7"></a>

By default, the Linux client uses the proxy server that's specified in the device operating system settings. The first time the client is launched, the device operating system proxy server setting is used. If you select another option for the proxy server, that setting is used for subsequent launches of the client.

**Note**
In versions 3.0.0 through 3.1.4, if you specify a custom proxy server, a "No network" error might appear when you attempt to log in to your WorkSpace. If you want to use a custom proxy server with the Linux client, we recommend upgrading to version 3.1.5. If you can't upgrade, you can work around the issue by using the default operating system proxy server instead of specifying a custom proxy server in the Linux client.

#### 2023.x clients
<a name="w2aab9c14c21b7b7b1"></a>

#### To use a proxy server

1. In the WorkSpaces client application, from the login page, choose the three-line menu icon, **Connection Settings**.

1. In the **Connection Settings** dialog box, choose **Customize proxy server for WorkSpaces** , enter the proxy server URL or IP address, enter the port, and choose **Save**.

#### 3.x and 4.x clients
<a name="w2aab9c14c21b7b7b3"></a>

#### To use a proxy server

1. In the WorkSpaces client application, go to **Settings**, **Manage Proxy Server**.

1. In the **Set Proxy** dialog box, select **Use proxy server**, enter the proxy server URL or IP address and the port, and choose **Save**.

## Command shortcuts
<a name="linux_shortcuts"></a>

The PCoIP WorkSpaces Linux client supports the following command shortcuts:
+ Ctrl\+Alt\+Enter—Toggle full screen display (PCoIP only)

## Clipboard redirection
<a name="linux_clipboard"></a>

Clipboard supports a maximum uncompressed object size of 20 MB. For more information, see [ I'm having trouble copying and pasting](https://docs.aws.amazon.com/workspaces/latest/userguide/client_troubleshooting.html).

## Disconnect
<a name="linux_disconnect"></a>

To disconnect the Linux client application, you have several options.

### 2023.x clients
<a name="w2aab9c14c27b5b1"></a>
+ In theWorkSpaces streaming session, end the WorkSpace session by closing the window. In the dialog box, choose **Disconnect** to end your WorkSpace session. The client application will continue running if you want to login again.
+ In the WorkSpaces streaming session, end your WorkSpace session by clicking on the three-line menu icon and choosing **Disconnect**. The client application will continue running, which allows you to login again.

### 3.x and 4.x clients
<a name="w2aab9c14c27b5b3"></a>
+ In the Amazon WorkSpaces client application, go to **Amazon WorkSpaces**, and then choose **Disconnect WorkSpace**. Your WorkSpace session ends, but the client application continues running in case you want to log in again.
+ In the Amazon WorkSpaces client application, go to **Amazon WorkSpaces**, and then choose **Quit Amazon WorkSpaces**. Your WorkSpace session ends, and the client application closes.
+ In the Amazon WorkSpaces client application, close the WorkSpaces client window by clicking the close (X) button in the upper-right corner.
+ In the Amazon WorkSpaces client application, go to **Amazon WorkSpaces**, and then choose **Disconnect WorkSpace**. Your WorkSpace session ends, but the client application continues running in case you want to log in again.
+ In the Amazon WorkSpaces client application, go to **Amazon WorkSpaces**, and then choose **Quit Amazon WorkSpaces**. Your WorkSpace session ends, and the client application closes.
+ In the Amazon WorkSpaces client application, close the WorkSpaces client window by clicking the close (X) button in the upper-right corner. In the prompt choose **End Session **, this disconnects you from the Amazon WorkSpaces and closes the client application.

### Diagnostic log upload
<a name="linux-disconnect-diagnostic-log-upload"></a>

To troubleshoot issues with the WorkSpaces client, ensure that diagnostic logging is enabled for your client. The log files that are sent to WorkSpaces include detailed information about your device and connection to the AWS network. You can enable diagnostic log uploads before or during WorkSpace streaming sessions so that these files are sent to WorkSpaces automatically.

**Note**
You can send log files before and during WorkSpaces streaming sessions. Log upload is supported only on Linux Ubuntu 20.04 and Ubuntu 22.04 clients.

**To send log files**

1. Open your Amazon WorkSpaces client.

1. In the top right of the WorkSpaces sign-in page after registration, choose **Settings** and then **Diagnostic logging**.

1. In the pop-up dialog box, set the toggle under **Diagnostic Logging** to your desired preference and choose **Save**.

1. You can choose the amount of data you want to provide in your session logs by selecting a radio button under **Log Level**. You can choose either **Standard logging (default)** or **Advance logging**.
**Important**
When you report an issue to Support, ensure you keep track of the device ID of the client that is experiencing the issue. The device ID can be found in the settings diagnostics logging menu on the client login page after entering a registration code. This helps the support team identify logs associated with your specific device. Include the device ID in the tickets that you create regarding your specific issue.

## Release notes
<a name="linux-release-notes"></a>

### WorkSpaces client application for Ubuntu 24.04 release notes
<a name="linux-2404-client-release-notes"></a>

The following table describes the changes to each release of the Ubuntu 24.04 client application.

| Release | Date | Changes |
| --- | --- | --- |
| 2026.0 | June 10, 2026 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/userguide/amazon-workspaces-linux-client.html)  |
| 2025.1 | December 12, 2025 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/userguide/amazon-workspaces-linux-client.html)  |

### WorkSpaces client application for Ubuntu 22.04 release notes
<a name="linux-2204-client-release-notes"></a>

The following table describes the changes to each release of the Ubuntu 22.04 client application.

| Release | Date | Changes |
| --- | --- | --- |
| 2026.0 | June 10, 2026 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/userguide/amazon-workspaces-linux-client.html)  |
| 2025.1 | December 12, 2025 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/userguide/amazon-workspaces-linux-client.html)  |
| 2025.0 | May 28, 2025 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/userguide/amazon-workspaces-linux-client.html)  |
| 2024.8 | December 11, 2024 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/userguide/amazon-workspaces-linux-client.html)  |
| 2024.7 | October 10, 2024 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/userguide/amazon-workspaces-linux-client.html)  |
| 2024.5 | August 26, 2024 | Bug fixes and enhancements. |
| 2024.4 | August 15, 2024 | Bug fixes and enhancements. |
| 2024.3 | August 8, 2024 | [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/userguide/amazon-workspaces-linux-client.html) |
| 2024.2 | July 3, 2024 | Bug fixes and enhancements. |
| 2024.1 | June 11, 2024 | [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/userguide/amazon-workspaces-linux-client.html) |
| 2024.0 | February 28, 2024 | [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/userguide/amazon-workspaces-linux-client.html) |
| 2023.2 | December 19, 2023 | [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/userguide/amazon-workspaces-linux-client.html) |
| 2023.1 | November 12, 2023 | [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/userguide/amazon-workspaces-linux-client.html) |
| 2023.0.4395 | August 24, 2023 | [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/userguide/amazon-workspaces-linux-client.html) Uniform Resource Identifier (URI) is not supported in this version. For more information, see [ Customize how users log in to their WorkSpaces](https://docs.aws.amazon.com/workspaces/latest/adminguide/customize-workspaces-user-login.html) |

### WorkSpaces client application for Ubuntu 20.04 release notes
<a name="linux-2004-client-release-notes"></a>

The following table describes the changes to each release of the Ubuntu 20.04 client application.

| Release | Date | Changes |
| --- | --- | --- |
| 2025.1 | December 12, 2025 | Bug fixes and enhancements. |
| 2025.0 | May 28, 2025 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/userguide/amazon-workspaces-linux-client.html)  |
| 2024.8 | December 11, 2024 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/userguide/amazon-workspaces-linux-client.html)  |
| 2024.7 | October 10, 2024 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/userguide/amazon-workspaces-linux-client.html)  |
| 2024.6 | September 5, 2024 | Bug fixes and enhancements. |
| 2024.5 | August 26, 2024 | Bug fixes and enhancements. |
| 2024.4 | August 15, 2024 | Bug fixes and enhancements. |
| 2024.3 | August 8, 2024 | [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/userguide/amazon-workspaces-linux-client.html) |
| 2024.2 | July 3, 2024 | Bug fixes and enhancements. |
| 2024.1 | June 11, 2024 | [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/userguide/amazon-workspaces-linux-client.html) |
| 2024.0 | February 28, 2024 | [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/userguide/amazon-workspaces-linux-client.html) |
| 2023.2 | December 19, 2023 | [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/userguide/amazon-workspaces-linux-client.html) |
| 2023.1 | November 12, 2023 | [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/userguide/amazon-workspaces-linux-client.html) |
| 4.7.0 | November 1, 2023 | [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/userguide/amazon-workspaces-linux-client.html) |
| 2023.0.4430 | August 24, 2023 | [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/userguide/amazon-workspaces-linux-client.html) Uniform Resource Identifier (URI) is not supported in this version. For more information, see [ Customize how users log in to their WorkSpaces](https://docs.aws.amazon.com/workspaces/latest/adminguide/customize-workspaces-user-login.html) |
| 4.6.0 | June 21, 2023 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/userguide/amazon-workspaces-linux-client.html)  |
| 4.5.0 | December 27, 2022 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/userguide/amazon-workspaces-linux-client.html)  |
| 4.4.0 | October 27, 2022 | Ubuntu 20.04 support. |
