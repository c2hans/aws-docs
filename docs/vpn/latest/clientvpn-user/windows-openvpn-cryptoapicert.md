---
source_url: https://docs.aws.amazon.com/vpn/latest/clientvpn-user/windows-openvpn-cryptoapicert.html
---

# Use a certificate and establish an AWS Client VPN connection on Windows
<a name="windows-openvpn-cryptoapicert"></a>

You can configure the OpenVPN client to use a certificate and private key from the Windows Certificate System Store. This option is useful when you use a smart card as part of your Client VPN connection. For information about the OpenVPN client cryptoapicert option, see [Reference Manual for OpenVPN ](https://openvpn.net/community-resources/reference-manual-for-openvpn-2-6/) on the OpenVPN website.

**Note**
The certificate must be stored on the local computer.

**To use a certificate and establish a connection**

1. Create a .pfx file that contains the client certificate and the private key.

1. Import the .pfx file to your personal certificate store, on your local computer. For more information, see [How to: View certificates with the MMC snap-in](https://learn.microsoft.com/en-us/dotnet/framework/wcf/feature-details/how-to-view-certificates-with-the-mmc-snap-in#to-view-certificates-for-the-local-device) on the Microsoft website.

1. Verify that your account has permissions to read the local computer certificate. You can use the Microsoft Management Console to modify the permissions. For more information, see [Rights to see the local computer certificates store](https://learn.microsoft.com/en-us/archive/msdn-technet-forums/743d793c-ca94-45b3-88c6-375097eaafc0) on the Microsoft website.

1. Update the OpenVPN configuration file and specify the certificate by using either the certificate subject, or the certificate thumbprint.

   The following is an example of specifying the certificate by using a subject.

   ```
   cryptoapicert “SUBJ:Jane Doe”
   ```

   The following is an example of specifying the certificate by using a thumbprint. You can find the thumbprint by using the Microsoft Management Console. For more information, see [How to: Retrieve the Thumbprint of a Certificate](https://learn.microsoft.com/en-us/dotnet/framework/wcf/feature-details/how-to-retrieve-the-thumbprint-of-a-certificate) on the Microsoft website.

   ```
   cryptoapicert “THUMB:a5 42 00 42 01"
   ```

1.  After you complete the configuration, use OpenVPN to establish a VPN connection by doing one of the following:
   + **Use the OpenVPN GUI client application **

     1. Start the OpenVPN client application.

     1. On the Windows taskbar, choose **Show/Hide icons**. Right-click **OpenVPN GUI**, and then choose **Import file**.

     1. In the Open dialog box, select the configuration file that you received from your Client VPN administrator and choose **Open**.

     1. On the Windows taskbar, choose **Show/Hide icons**. Right-click **OpenVPN GUI**, and then choose **Connect**.
   + **Use the OpenVPN GUI Connect Client **

     1. Start the OpenVPN application, and choose **Import, From local file....**.

     1. Navigate to the configuration file that you received from your VPN administrator, and choose **Open**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS VPN. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vpn` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
