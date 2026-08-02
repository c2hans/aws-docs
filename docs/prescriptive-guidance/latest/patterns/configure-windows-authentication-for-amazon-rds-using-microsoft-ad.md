---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/configure-windows-authentication-for-amazon-rds-using-microsoft-ad.html
---

# Configure Windows authentication for Amazon RDS for Microsoft SQL Server using AWS Managed Microsoft AD
<a name="configure-windows-authentication-for-amazon-rds-using-microsoft-ad"></a>

*Ramesh Babu Donti, Amazon Web Services*

## Summary
<a name="configure-windows-authentication-for-amazon-rds-using-microsoft-ad-summary"></a>

This pattern shows how to configure Windows authentication for an Amazon Relational Database Service (Amazon RDS) for SQL Server instances using AWS Directory Service for Microsoft Active Directory (AWS Managed Microsoft AD). Windows authentication allows users to connect to the RDS instance using their domain credentials instead of database-specific usernames and passwords.

You can enable Windows authentication either when creating a new RDS SQL Server database or by adding it to an existing database instance. The database instance integrates with AWS Managed Microsoft AD to provide centralized authentication and authorization for domain users accessing the SQL Server database.

This configuration enhances security by leveraging existing Active Directory infrastructure and eliminates the need to manage separate database credentials for domain users.

## Prerequisites and limitations
<a name="configure-windows-authentication-for-amazon-rds-using-microsoft-ad-prereqs"></a>

**Prerequisites**
+ An active AWS account with appropriate permissions
+ A virtual private cloud (VPC) with the following:
  + Configured Internet gateways and route tables
  + NAT gateways in public subnets (if internet access is required for instances)
+ AWS Identity and Access Management (IAM) roles:
  + A domain role with the following AWS managed policies:
    + `AmazonSSMManagedInstanceCore` to enable AWS Systems Manager
    + `AmazonSSMDirectoryServiceAccess` to provide permissions to join instances to directories
  + An RDS enhanced monitoring role (if enhanced monitoring is enabled)
+ Security groups:
  + Directory service security group to allow Active Directory communication ports
  + An Amazon Elastic Compute Cloud (Amazon EC2) security group to allow RDP `3389` and domain communications
  + An RDS security group to allow SQL Server port `1433` from authorized sources
+ Network connectivity:
  + Proper DNS resolution and network connectivity between subnets

**Limitations**
+ For information about AWS Regions that support AWS Managed Microsoft AD with RDS for SQL Server, see [Region and version availability](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_SQLServerWinAuth.html#USER_SQLServerWinAuth.RegionVersionAvailability).
+ Some AWS services aren’t available in all AWS Regions. For Region availability, see [AWS services by Region](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/). For specific endpoints, see the [Service endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/aws-service-information.html) page, and choose the link for the service.

## Architecture
<a name="configure-windows-authentication-for-amazon-rds-using-microsoft-ad-architecture"></a>

**Source technology stack**
+ An on-premises Active Directory or AWS Managed Microsoft AD

**Target technology stack**
+ Amazon EC2
+ Amazon RDS for Microsoft SQL Server
+ AWS Managed Microsoft AD

**Target architecture**

![](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/e02f6059-6631-46f6-819c-5961af7ba4ae/images/1aa50e3b-b4f6-4d44-9f9e-6cbb248a159c.png)

The architecture includes the following:
+ An IAM role that joins the Amazon EC2 instance to the AWS Managed Microsoft AD domain.
+ An Amazon EC2 Windows instance for database administration and testing.
+ An Amazon VPC with a private subnet to host the Amazon RDS instance and internal resources across Availability Zones.
+ Security groups for network access control:
  + An Amazon RDS security group to control inbound access to SQL Server port `1433` from authorized sources.
  + An Amazon EC2 security group to manage RDP access through port `3389` and domain communication ports.
  + A Directory Services security group for Active Directory communications through ports `53`, `88`, `389`, and `445`.
+ AWS Managed Microsoft AD to provide centralized authentication and authorization services for Windows resources.
+ An Amazon RDS for SQL Server database instance in the private subnet with Windows authentication enabled.

## Tools
<a name="configure-windows-authentication-for-amazon-rds-using-microsoft-ad-tools"></a>

**AWS services**
+ [Amazon Elastic Compute Cloud (Amazon EC2)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html) provides scalable computing capacity in the AWS Cloud. You can launch as many virtual servers as you need and quickly scale them up or down.
+ Amazon Relational Database Service (Amazon RDS) helps you set up, operate, and scale a relational database in the AWS Cloud.
+ [AWS Directory Service](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/what_is.html) provides multiple ways to use Microsoft Active Directory (AD) with other AWS services such as Amazon Elastic Compute Cloud (Amazon EC2), Amazon Relational Database Service (Amazon RDS) for SQL Server, and Amazon FSx for Windows File Server.
+ [AWS Directory Service for Microsoft Active Directory](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/directory_microsoft_ad.html) enables your directory-aware workloads and AWS resources to use Microsoft Active Directory in the AWS Cloud.
+ [AWS Identity and Access Management (IAM)](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) helps you securely manage access to your AWS resources by controlling who is authenticated and authorized to use them.

**Other services**
+ [Microsoft SQL Server Management Studio (SSMS)](https://learn.microsoft.com/en-us/sql/ssms/download-sql-server-management-studio-ssms) is a tool for managing SQL Server, including accessing, configuring, and administering SQL Server components.

## Best practices
<a name="configure-windows-authentication-for-amazon-rds-using-microsoft-ad-best-practices"></a>
+ For general best practices, see [Best practices for Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_BestPractices.html).

## Epics
<a name="configure-windows-authentication-for-amazon-rds-using-microsoft-ad-epics"></a>

### Configure AWS Managed Microsoft AD
<a name="configure-managed-ad"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Set up the directory type. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/configure-windows-authentication-for-amazon-rds-using-microsoft-ad.html) | DBA, DevOps engineer |
| Configure directory information. | In the **Directory information** section, enter the required information, and keep the optional values:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/configure-windows-authentication-for-amazon-rds-using-microsoft-ad.html) | DBA, DevOps engineer |
| Configure the VPC and subnets. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/configure-windows-authentication-for-amazon-rds-using-microsoft-ad.html) | DBA, DevOps engineer |
| Review and create the directory. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/configure-windows-authentication-for-amazon-rds-using-microsoft-ad.html) | DBA, DevOps engineer |

### Create and configure an Amazon EC2 instance
<a name="create-and-configure-an-ec2-instance"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Configure an AMI for Windows. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/configure-windows-authentication-for-amazon-rds-using-microsoft-ad.html) | DBA, DevOps engineer |
| Configure network settings. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/configure-windows-authentication-for-amazon-rds-using-microsoft-ad.html) | DBA, DevOps engineer |
| Configure storage. | Configure the Amazon EBS volumes as needed. | DBA, DevOps engineer |
| Configure advanced details and launch the instance. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/configure-windows-authentication-for-amazon-rds-using-microsoft-ad.html) | DBA, DevOps engineer |

### Create and configure RDS for SQL Server with Windows authentication
<a name="create-and-configure-rds-for-sql-server-with-windows-authentication"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a database and configure engine options. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/configure-windows-authentication-for-amazon-rds-using-microsoft-ad.html) | DBA, DevOps engineer |
| Choose a template. | Choose a sample template that meets your requirements. | DBA, DevOps engineer |
| Configure database settings. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/configure-windows-authentication-for-amazon-rds-using-microsoft-ad.html) | DBA, DevOps engineer |
| Configure the instance. | In the **Instance configuration** section, under **DB instance class**, select an instance size that meets your requirements. | DBA, DevOps engineer |
| Configure storage. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/configure-windows-authentication-for-amazon-rds-using-microsoft-ad.html) | DBA, DevOps engineer |
| Configure connectivity. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/configure-windows-authentication-for-amazon-rds-using-microsoft-ad.html) | DBA, DevOps engineer |
| Configure Windows authentication. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/configure-windows-authentication-for-amazon-rds-using-microsoft-ad.html) | DBA, DevOps engineer |
| Configure monitoring. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/configure-windows-authentication-for-amazon-rds-using-microsoft-ad.html)Note: Metrics are useful when you want to see how different processes or threads use the CPU. You can also export error logs to Amazon CloudWatch if **Error log** is enabled. | DBA, DevOps engineer |
| Configure additional settings. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/configure-windows-authentication-for-amazon-rds-using-microsoft-ad.html) | DBA, DevOps engineer |
| Review costs and create database. | Review the **Estimated monthly costs** section, and then choose **Create database**. | DBA, DevOps engineer |

### Configure database access and test connections
<a name="configure-database-access-and-test-connections"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Connect to the Windows machine. | Connect to your Windows machine and launch SQL Server Management Studio.[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/configure-windows-authentication-for-amazon-rds-using-microsoft-ad.html) | DBA, DevOps engineer |
| Configure the SSMS connection. | Set up the database connection using Windows authentication.[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/configure-windows-authentication-for-amazon-rds-using-microsoft-ad.html) | DBA, DevOps engineer |
| Configure security settings. | Set the required security parameters for SSMS version 20 or later.[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/configure-windows-authentication-for-amazon-rds-using-microsoft-ad.html) | DBA, DevOps engineer |
| Create a Windows login. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/configure-windows-authentication-for-amazon-rds-using-microsoft-ad.html)<pre>CREATE LOGIN [<domainName>\<user_name>] FROM WINDOWS;<br />GO</pre> | DBA, DevOps engineer |
| Test Windows authentication. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/configure-windows-authentication-for-amazon-rds-using-microsoft-ad.html) | DBA, DevOps engineer |

## Related resources
<a name="configure-windows-authentication-for-amazon-rds-using-microsoft-ad-resources"></a>
+ [Creating your AWS Managed Microsoft AD](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_getting_started_create_directory.html)
+ [Joining an Amazon EC2 Windows instance to your AWS Managed Microsoft AD](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/launching_instance.html)
+ [Supported Regions and DB engines for Kerberos authentication in Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.RDS_Fea_Regions_DB-eng.Feature.KerberosAuthentication.html)
+ [What is SQL Server Management Studio (SSMS)?](https://learn.microsoft.com/en-us/ssms/sql-server-management-studio-ssms)
