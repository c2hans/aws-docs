---
source_url: https://docs.aws.amazon.com/whitepapers/latest/access-workspaces-with-access-cards/aws-directory-service-active-directory-connector.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# AWS Directory Service Active Directory Connector
<a name="aws-directory-service-active-directory-connector"></a>

## Create an AD Connector
<a name="create-an-ad-connector"></a>

Before starting this procedure, make sure you have completed the prerequisites identified in [AD Connector Prerequisites](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/prereq_connector.html).

 **To connect to your existing directory with AD Connector**:

1.  In the [AWS Directory Service console](https://console.aws.amazon.com/directoryservicev2/) navigation pane, choose **Directories** and then choose **Set up directory**.

1.  On the **Select directory type page**, choose **AD Connector**, and then choose **Next**.

1.  On the **Enter AD Connector information** page, provide the following information:
   +  Select **Directory size**. Choose either the **Small or Large** size option. For more information about sizes, see [Active Directory Connector](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/directory_ad_connector.html).
   +  Enter **Directory description** information.
   +  Click **Next**.

1.  On the **Choose VPC and subnets** page, select the following information:
   +  Select **VPC** from the VPC dropdown.
   +  Select two **subnets** for the domain controllers from the subnet dropdowns. The two selected subnets must be in different Availability Zones.
   +  Click **Next**.

1.  On the **Connect to AD** page, provide the following information:
   +  **Directory DNS name** — The fully qualified name of your existing directory, such as corp.example.com.
   +  **Directory NetBIOS name** — The short name of your existing directory, such as `CORP`.
   +  **DNS IP addresses** — The IP address of at least one DNS server in your existing directory. These servers must be accessible from each subnet specified in the next section.
   +  **Service account username** — The user name of a user in the existing directory. This service account name was created in the [Create service account and delegate privileges section](create-a-service-account-and-delegate-privileges.md). For more information about this service account, see [AD Connector Prerequisites](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/prereq_connector.html).
   +  **Service account password** — The password for the existing user.
   +  **Confirm password** — Retype the password for the existing user.

1.  Click **Next**.

1.  On the **Review & create** page, review the directory information and make any necessary changes. When the information is correct, choose **Create directory**. It takes several minutes for the directory to be created. When the directory is created, the **Status** value changes to **Active**.
