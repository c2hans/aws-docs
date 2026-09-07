---
source_url: https://docs.aws.amazon.com/whitepapers/latest/access-workspaces-with-access-cards/configure-active-directory.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Configure Active Directory
<a name="configure-active-directory"></a>

 After you have installed the AD DS role, you must configure the server for your domain.

**To configure the server**:

1.  From the task bar, open the **Server Manager**.

1.  Choose the triangular yellow notifications icon in the top navigation bar of the Server Manager window. The **Notifications** pane opens and displays a **Post-deployment Configuration** notification. Choose the **Promote this server to a domain controller** link that appears in the notification.
![A screenshot showing post-deployment configuration](https://docs.aws.amazon.com/whitepapers/latest/access-workspaces-with-access-cards/images/workspaces-smartcard6.png)

    *Active Directory post-deployment configuration *

1.  From the **Deployment Configuration** tab, choose **Radial options** > **Add a new forest**. Enter your root domain name in the **Root domain name** field and select **Next**.

1.  Choose a **Domain** and a **Forest functional level**. (These selections affect features and server domain controller eligibility. For further information on domains and forest functional levels, see the official Microsoft documentation.)

1.  Enter a password for Directory Services Restore Mode (DSRM) in the **Password** field. (The DSRM password is used when booting the Domain Controller into recovery mode.)

1.  Review the warning on the **DNS Options** tab and select **Next**.

1.  Confirm or enter a **NetBIOS name** and select **Next**.

1.  Specify the locations of the **Database**, **Log files**, and **SYSVOL folders**, then select **Next**.

1.  Review the configuration options and select **Next**.

1.  The system checks if all of the necessary prerequisites are installed on the system. If the system passes these checks, select **Install**. The server automatically reboots after the installation is complete.

1.  After the server reboots, reconnect to it by using Microsoft Remote Desktop Protocol (RDP).
