---
source_url: https://docs.aws.amazon.com/vpn/latest/clientvpn-user/troubleshooting.html
---

# Troubleshooting AWS Client VPN connections
<a name="troubleshooting"></a>

Use the following topics to troubleshoot problems that you might have when using a client application to connect to a Client VPN endpoint.

**Topics**
+ [Client VPN endpoint troubleshooting for administrators](#client-vpn-endpoint-troubleshooting)
+ [Send diagnostic logs to AWS Support in the AWS provided client](#windows-troubleshooting-client-send-diagnostics)
+ [Troubleshooting AWS Client VPN connections with Windows-based clients](windows-troubleshooting.md)
+ [Troubleshooting AWS Client VPN connections with macOS clients](macos-troubleshooting.md)
+ [Troubleshooting AWS Client VPN connections with Linux-based clients](linux-troubleshooting.md)
+ [Troubleshooting common AWS Client VPN problems](common-troubleshooting.md)

## Client VPN endpoint troubleshooting for administrators
<a name="client-vpn-endpoint-troubleshooting"></a>

Some of the steps in this guide can be performed by you. Other steps must be performed by your Client VPN administrator on the Client VPN endpoint itself. The following sections let you know when you need to contact your administrator.

For additional information about troubleshooting Client VPN endpoint issues, see [Troubleshooting Client VPN](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/troubleshooting.html) in the *AWS Client VPN Administrator Guide*.

## Send diagnostic logs to AWS Support in the AWS provided client
<a name="windows-troubleshooting-client-send-diagnostics"></a>

If you have problems with the AWS provided client and you need to contact AWS Support to help troubleshoot, the AWS provided client has an option for sending the diagnostic logs to AWS Support. The option is available on the Windows, macOS and Linux client applications.

After you send the files, we provide you with a reference number that you can give to AWS Support so that they can immediately access the files.

The steps depend on the version of the AWS provided client that you are using. To check your version, open the **About** window. On Windows and Linux, choose **Help**, **About AWS VPN Client**. On macOS, choose **AWS VPN Client**, **About AWS VPN Client**.

### Send diagnostic logs (version 6.0 and later)
<a name="client-vpn-connect-send-diagnostics-6x"></a>

The following steps are the same for Windows, macOS, and Linux.

**To send diagnostic logs using the AWS provided client version 6.0 or later**

1. Open the **AWS VPN Client** app.

1. Choose **Other actions**, **Send diagnostic logs**.

1. On the **Diagnostic Logs** page, choose **Send diagnostic logs**.

1. Note the reference number from the confirmation window. You can copy it to your clipboard from the confirmation window.

   When you contact AWS Support, you will need to provide them with the reference number.

You can also send diagnostic logs by using the `aws-vpn-client send-diagnostic-logs` command. For more information, see [send-diagnostic-logs](cli-command-syntax.md#cli-cmd-send-diagnostic-logs).

### Send diagnostic logs (versions earlier than 6.0)
<a name="client-vpn-connect-macos-connecting"></a>

Before you send the files, you must agree to allow AWS Support to access your diagnostic logs.

The AWS provided client is also referred to as the *AWS VPN Client* in the following steps.

**To send diagnostic logs using the AWS provided client for Windows**

1. Open the **AWS VPN Client** app.

1. Choose **Help**, **Send Diagnostic Logs**.

1. In the **Send Diagnostic Logs** window, choose **Yes**.

1. In the **Send Diagnostic Logs** window, perform one of the following operations:
   + To copy the reference number to the clipboard, choose **Yes**, and then choose **OK**.
   + To manually track the reference number, choose **No**.

   When you contact AWS Support, you will need to provide them with the reference number.

**To send diagnostic logs using the AWS provided client for macOS**

1. Open the **AWS VPN Client** app.

1. Choose **Help**, **Send Diagnostic Logs**.

1. In the **Send Diagnostic Logs** window, choose **Yes**.

1. Note the reference number from the confirmation window, and then choose **OK**.

   When you contact AWS Support, you will need to provide them with the reference number.

**To send diagnostic logs using the AWS provided client for Ubuntu**

1. Open the **AWS VPN Client** app.

1. Choose **Help**, **Send Diagnostic Logs**.

1. In the **Send Diagnostic Logs** window, choose **Send**.

1. Note the reference number from the confirmation window. You are given a choice to copy the information to your clipboard.

   When you contact AWS Support, you will need to provide them with the reference number.
