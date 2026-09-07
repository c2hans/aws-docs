---
source_url: https://docs.aws.amazon.com/whitepapers/latest/access-workspaces-with-access-cards/install-and-configure-active-directory-and-certificate-authority.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Install and configure Active Directory and Certificate Authority
<a name="install-and-configure-active-directory-and-certificate-authority"></a>

 **To install Active Directory on the server**:

1.  From the task bar, open the **Server Manager**.

1.  From the **Server Manager** dashboard, select **Manage** and then **Add roles and features**. The Roles and Features Wizard launches. This wizard enables you to make modifications to the Windows Server instance.

1.  On the **Installation Type** screen, select **Role-based or features-based** and select **Next**.

1.  By default, the current server is selected. Choose **Next**.

1.  On the **Server Roles** screen, choose the check box next to **Active Directory Domain Services**. A notice explains that you must also install additional roles, services, or features to install Domain Services. These additional capabilities include certificate services, federation services, lightweight directory services, and rights management.

1.  To select additional capabilities, select **Add Features**. Choose **Next**.

1.  On the **Select features** screen, select the check boxes next to the features that you want to install during the AD DS installation process. Choose **Next**.
![A diagram depicting Active Directory feature installation.](https://docs.aws.amazon.com/whitepapers/latest/access-workspaces-with-access-cards/images/workspaces-smartcard5.png)

   *Active Directory feature installation *

1.  Review the information on the **AD DS** tab, then select **Next**.

1.  Review the information on the **Confirm installation selections** screen, then select **Install**. Information on the progress of the installation displays. After the installation is complete, the AD DS role displays on the "Server Manager" landing page.
