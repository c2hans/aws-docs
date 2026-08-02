---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/microsoft-sql-failover-cluster-on-amazon-ec2.html
---

# Set up a Microsoft SQL Server failover cluster on Amazon EC2 by using FSx for Windows File Server
<a name="microsoft-sql-failover-cluster-on-amazon-ec2"></a>

*Sweta Krishna and Ramesh Babu Donti, Amazon Web Services*

## Summary
<a name="microsoft-sql-failover-cluster-on-amazon-ec2-summary"></a>

Microsoft SQL Server Standard edition with a failover cluster instance (FCI) can provide a more cost-effective alternative to SQL Server Enterprise. Setting up SQL FCI requires shared file storage between nodes, and [Amazon FSx for Windows File Server](https://aws.amazon.com/fsx/windows/) provides fully managed storage that automatically replicates synchronously across Availability Zones. Amazon FSx reduces storage costs by using built-in data deduplication for general-purpose file shares, which eliminates the need to maintain third-party solutions. Amazon FSx also supports the following:
+ Pay only for what you use with no upfront fees or commitments.
+ Set up FCI manually with Amazon FSx as your shared storage.
+ Use Amazon FSx as the file share witness for your SQL cluster.
+ Amazon FSx for Windows File Server supports Server Message Block (SMB) 3.0 for continuously available file shares, making it suitable for SQL Server FCI deployments.

## Prerequisites and limitations
<a name="microsoft-sql-failover-cluster-on-amazon-ec2-prereqs"></a>

**Prerequisites**
+ Active [AWS account](https://aws.amazon.com/account/).
+ Permissions to create and manage Amazon Virtual Private Cloud (Amazon VPC) resources, Amazon Elastic Compute Cloud (Amazon EC2) instance, security groups, and AWS Identity and Access Management (IAM) roles.
+ AWS Managed Microsoft AD or your own on-premises Active Directory.
+ An Active Directory domain user with [necessary permission](https://learn.microsoft.com/en-us/windows-server/failover-clustering/configure-failover-cluster-accounts) to set up a failover cluster.
+ Security group rules for SQL Server FCI and [Microsoft Active Directory ports](https://docs.aws.amazon.com/whitepapers/latest/access-workspaces-with-access-cards/ip-address-and-port-requirements.html) for secure hybrid connectivity.
+ A [service account](https://learn.microsoft.com/en-us/sql/database-engine/configure-windows/configure-windows-service-accounts-and-permissions?view=sql-server-ver16#sql-server-failover-cluster-instance) in Active Directory for SQL Server that’s configured with appropriate permissions across SQL nodes.
+ Amazon FSx for Windows File Server in a failover cluster.
+ SQL Server installation binaries.

**Limitations**
+ Some AWS services aren’t available in all AWS Regions. For Region availability, see [AWS services by Region](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/). For specific endpoints, see the [Service endpoints and quotas page](https://docs.aws.amazon.com/general/latest/gr/aws-service-information.html), and choose the link for the service.

**Product versions**
+ Amazon EC2 for Windows Server 2012 R2 or later
+ Amazon FSx for Windows File Server with all current Windows Server versions
+ Amazon FSx for NetApp ONTAP as an alternative for shared storage
+ SQL Server 2012/2016/2019/2022

## Architecture
<a name="microsoft-sql-failover-cluster-on-amazon-ec2-architecture"></a>

**Technology stack**
+ Amazon EC2
+ Amazon FSx for Windows File Server
+ Amazon VPC
+ AWS Directory Service
+ AWS Systems Manager
+ IAM

**Target architecture**

The following diagram shows the high-level architecture of Microsoft SQL Server FCI on Amazon EC2 using Amazon FSx for Windows File Server.

![Architecture diagram for Microsoft Server FCI on Amazon EC2 using Amazon FSx for Windows File Server.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/208bf64a-8fef-4019-944a-723372450885/images/ba0c9169-9536-41c3-ae8e-7264dcc3e1ad.png)

**Network infrastructure**
+ Amazon VPC provides a network container that spans three Availability Zones.
+ Private subnets provide isolated subnets in each Availability Zones for deploying resources.

**Compute layer**
+ Amazon EC2 contains an SQL Server cluster node 1, deployed in Availability Zone 1 as part of the Windows Server Failover Cluster (WSFC).
+ Amazon EC2 contains an SQL Server cluster node 2, deployed in Availability Zone 2 as part of the WSFC.
+ The WSFC cluster connects both SQL Server nodes for failover capability.

**Storage layer for Amazon FSx for Windows File Server**

**Multi-AZ FSx deployment (spanning Availability Zones 1 and 2)**
+ A primary FSx file system in Availability Zone 1 hosts active SQL Server data and log files.
+ A secondary FSx file system in Availability Zone 2 provides automatic failover capability.
+ A shared SMB file share (\\\\fsx.domain\\sqlshare), accessible by both cluster nodes for SQL Server databases.

**Single-AZ FSx deployment (in AZ3)**
+ Amazon FSx file server witness in Availability Zone 3 serves as the cluster quorum witness.
+ The file share witness (`\\fsx.domain\witness`) maintains the cluster quorum and prevents split-brain scenarios.

**Directory services**
+ AWS Managed Microsoft AD provides Windows authentication and domain services that are required for cluster functionality.

**High availability features**
+ Multi-AZ components provide fault tolerance across Availability Zones.
+ FSx standby file server provides automatic failover if the primary server fails.
+ File share witness provides cluster quorum management in Availability Zone 3 to help ensure proper cluster operation during failures.
+ Domain is integrated with AWS Managed Microsoft AD for seamless Windows authentication.

## Tools
<a name="microsoft-sql-failover-cluster-on-amazon-ec2-tools"></a>

**AWS services**
+ [Amazon Elastic Compute Cloud (Amazon EC2)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html) provides scalable computing capacity in the AWS Cloud. You can launch as many virtual servers as you need and quickly scale them up or down.
+ [Amazon FSx](https://docs.aws.amazon.com/fsx/?id=docs_gateway) provides file systems that support industry-standard connectivity protocols and offer high availability and replication across AWS Regions.
+ [Amazon Virtual Private Cloud (Amazon VPC)](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html) helps you launch AWS resources into a virtual network that you’ve defined. This virtual network resembles a traditional network that you’d operate in your own data center, with the benefits of using the scalable infrastructure of AWS.
+ [AWS Directory Service for Microsoft Active Directory](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/directory_microsoft_ad.html) enables your directory-aware workloads and AWS resources to use Microsoft Active Directory in the AWS Cloud.
+ [AWS Identity and Access Management (IAM)](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) helps you securely manage access to your AWS resources by controlling who is authenticated and authorized to use them.
+ [AWS Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/what-is-systems-manager.html) helps you manage your applications and infrastructure running in the AWS Cloud. It simplifies application and resource management, shortens the time to detect and resolve operational problems, and helps you manage your AWS resources securely at scale.

## Best practices
<a name="microsoft-sql-failover-cluster-on-amazon-ec2-best-practices"></a>
+ Place database instances in private subnets to protect them from being publicly accessible from the internet while still allowing them to connect to AWS services and perform updates.
+ To use PowerShell to administer your Amazon FSx for Windows File Server, see [Administering FSx for Windows file systems](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/administering-file-systems.html).

## Epics
<a name="microsoft-sql-failover-cluster-on-amazon-ec2-epics"></a>

### Create and configure Amazon EC2 nodes for SQL Server
<a name="create-and-configure-ec2-nodes-for-sql-server"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Add names and tags. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/microsoft-sql-failover-cluster-on-amazon-ec2.html) | DBA |
| Choose a Windows AMI. | Choose an Amazon Machine Image (AMI) for Windows that meets your SQL Server requirements. | DBA |
| Select an instance type. | Select an Amazon EC2 instance type that meets your requirements. | DBA |
| Use a key pair. | You can use a key pair to securely connect to your instance. Ensure that you have access to the selected key pair before you launch the instance. | DBA |
| Configure network settings. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/microsoft-sql-failover-cluster-on-amazon-ec2.html) | DBA |
| Configure advanced network settings. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/microsoft-sql-failover-cluster-on-amazon-ec2.html) | DBA |
| Configure storage. | Configure the required total storage and choose the required storage type. | DBA |
| Configure advanced details and launch the instance. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/microsoft-sql-failover-cluster-on-amazon-ec2.html) | DBA |
| Create node 2. | Repeat these steps to create and configure node 2. | DBA |

### Install and configure Windows Server failover cluster on nodes 1 and 2
<a name="install-and-configure-windows-server-failover-cluster-on-nodes-1-and-2"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Log in to node 1. | Log in to the Windows Amazon EC2 instance as an administrator. | DBA |
| Install FCI features on node 1. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/microsoft-sql-failover-cluster-on-amazon-ec2.html)<pre>Install-WindowsFeature -Name Failover-Clustering -IncludeManagementTools</pre>[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/microsoft-sql-failover-cluster-on-amazon-ec2.html) | DBA |
| Log in to node 2. | Log in to the Windows Amazon EC2 instance as an administrator. | DBA |
| Install FCI features on node 2. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/microsoft-sql-failover-cluster-on-amazon-ec2.html)<pre>Install-WindowsFeature -Name Failover-Clustering -IncludeManagementTools</pre>[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/microsoft-sql-failover-cluster-on-amazon-ec2.html) | DBA |
| Add nodes to the cluster. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/microsoft-sql-failover-cluster-on-amazon-ec2.html) | DBA |
| Bring the cluster online. | To bring the cluster online, update the static IP addresses of both nodes:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/microsoft-sql-failover-cluster-on-amazon-ec2.html) | DBA |
| Validate the cluster. | Navigate to **Failover cluster manager** and verify that the cluster core resources are online. | DBA |

### Install SQL Server on nodes 1 and 2
<a name="install-sql-server-on-nodes-1-and-2"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Log in to the server. | Log in to the Amazon EC2 instance as an administrator. | DBA |
| Mount the SQL binaries. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/microsoft-sql-failover-cluster-on-amazon-ec2.html) |  |
| Add node 2 to the failover cluster. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/microsoft-sql-failover-cluster-on-amazon-ec2.html) | DBA |

### Configure the Amazon FSx file share witness
<a name="configure-the-fsx-file-share-witness"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Configure quorum settings. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/microsoft-sql-failover-cluster-on-amazon-ec2.html) | DBA |
| Retrieve DNS details. | In the Amazon FSx console, choose **Managed AD** and then **Attach**. The DNS should have the following format: `\\example.example.net\share` | DBA |
| Configure the file share witness. | Choose **Amazon FSx file share path** and then **Finish**. | DBA |

## Related resources
<a name="microsoft-sql-failover-cluster-on-amazon-ec2-resources"></a>

**AWS resources**
+ [Amazon FSx for Windows File Server](https://www.youtube.com/watch?v=IMDWTIShlyI) (video)
+ [Deep dive on Amazon FSx for Windows File Server](https://www.youtube.com/watch?v=_x_Geur93oc) (video)
+ [How to deploy a SQL Server failover cluster with Amazon EBS Multi-Attach on Windows Server](https://aws.amazon.com/blogs/modernizing-with-aws/how-to-deploy-a-sql-server-failover-cluster-with-amazon-ebs-multi-attach-on-windows-server/) (AWS blog post)
+ [Simplify your Microsoft SQL Server high availability deployments using Amazon FSx for Windows File Server](https://aws.amazon.com/blogs/storage/simplify-your-microsoft-sql-server-high-availability-deployments-using-amazon-fsx-for-windows-file-server/) (AWS blog post)
+ [SQL Server high availability deployments using Amazon FSx for NetApp ONTAP](https://aws.amazon.com/blogs/modernizing-with-aws/sql-server-high-availability-amazon-fsx-for-netapp-ontap/) (AWS blog post)
+ [Using FSx for Windows File Server with Microsoft SQL Server](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/sql-server.html)
+ [What is FSx for Windows File Server?](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/what-is.html)

**Other resources**
+ [Create a failover cluster](https://learn.microsoft.com/en-us/windows-server/failover-clustering/create-failover-cluster?pivots=windows-admin-center)

## Additional information
<a name="microsoft-sql-failover-cluster-on-amazon-ec2-additional"></a>

**Configuring the file share witness**

Ensure that you’re connected to the file system from both nodes by adding rules in the Amazon FSx security group that allow inbound connections. The SMB port should be allowed. For example, if the DNS name is `\\example.example.com\share`, use `\\example.example.com\share`. Use the same value for the file share witness in the Always On availability cluster. Complete the following steps to configure the file share witness:

1. Use RDP to connect to your Amazon EC2 instance.

1. Navigate to **Failover cluster manager**.

1. Open the context (right-click) menu and choose **More actions**.

1. Choose **Configure cluster quorum settings**.

1. Choose **Next**.

1. Select **Quorum configuration** and configure a file share witness.

1. Provide the DNS name.

1. Review the summary and then choose **Finish**. The file share witness should be online in the **Cluster core** resources section.
