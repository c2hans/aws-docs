---
source_url: https://docs.aws.amazon.com/whitepapers/latest/access-workspaces-with-access-cards/create-a-service-account-and-delegate-privileges.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Create a service account and delegate privileges
<a name="create-a-service-account-and-delegate-privileges"></a>

 To connect to your existing directory, you must have the credentials for your AD Connector service account in the existing directory that has been delegated certain privileges. While members of the “Domain Admins” group have sufficient privileges to connect to the directory, as a best practice, you should use a service account that has only the minimum privileges necessary to connect to the directory. The following procedure demonstrates how to create a new group called “Connectors”, delegate the necessary privileges needed to connect AWS Directory Service to this group, and then add a new service account to this group.

 This procedure must be performed on a machine that is joined to your directory and has the “Active Directory User and Computers MMC” snap-in installed. You must also be logged in as a domain administrator.

 **To delegate privileges to your service account**:

1.  Open **Active Directory User and Computers** and select your domain root in the navigation tree.

1.  In the list in the left-hand pane, right-click **Users**, select **New**, and then select **Group**.

1.  Locate the **New Object - Group** dialog box.

1.  For **Group name**, enter Connectors.

1.  For **Group scope**, choose **Global**.

1.  For **Group type**, enter Security.

1.  Choose **OK**.

1.  In the **Active Directory User** and **Computers** navigation tree, choose your domain root.

1.  In the menu, choose **Action**, and then **Delegate Control**.

1.  On the **Delegation of Control Wizard** page, select **Next**, then select **Add**.

1.  In the **Select Users, Computers, or Groups** dialog box, enter **Connectors** and select **OK**. If more than one object is found, choose the **Connectors** group created above. Choose **Next**.

1.  On the **Tasks to Delegate** page, select **Create a custom task to delegate**. Choose **Next**.

1.  Choose **Only the following objects in the folder**, and then choose **Computer objects and User objects**.

1.  Choose **Create selected objects in this folder** and **Delete selected objects in this folder**. Choose **Next**.

1.  Choose **General** and **Property-specific**, **Read** and **Write**. Choose **Next**.

1.  Verify the information on the **Completing the Delegation of Control Wizard** page, and select **Finish**.

1.  Create a user with a strong password and add that user to the “Connectors” group. This user will be known as your AD Connector service account. Because this user it is now a member of the “Connectors” group, they now have sufficient privileges to connect AWS Directory Service to the directory.
