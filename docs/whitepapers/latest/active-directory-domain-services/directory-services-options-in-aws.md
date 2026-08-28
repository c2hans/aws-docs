---
source_url: https://docs.aws.amazon.com/whitepapers/latest/active-directory-domain-services/directory-services-options-in-aws.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Directory services options in AWS
<a name="directory-services-options-in-aws"></a>

 AWS provides a comprehensive set of services and tools for deploying Microsoft Windows workloads on its reliable and secure cloud infrastructure. AWS Active Directory Connector (AD Connector) and AWS Managed Microsoft AD are fully managed services that allow you to connect AWS applications to an existing Active Directory or host a new Active Directory in the cloud. Together, with the ability to deploy self-managed Active Directory in Amazon EC2 instances, these services cover all cloud and hybrid scenarios for enterprise identity services.

## AD Connector
<a name="ad-connector"></a>

 AD Connector can be used in the following scenarios:
+  Sign in to AWS applications, such as [Amazon Chime,](https://docs.aws.amazon.com/chime/latest/ag/active_directory.html) [Amazon WorkDocs](https://docs.aws.amazon.com/workdocs/latest/adminguide/connect_directory_connector.html), [Amazon WorkMail,](https://docs.aws.amazon.com/workmail/latest/adminguide/premises_directory.html) or [Amazon WorkSpaces](https://docs.aws.amazon.com/workspaces/latest/adminguide/launch-workspace-ad-connector.html) using corporate credentials. (See the [list of compatible applications](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ad_connector_app_compatibility.html) on the AWS Documentation site.)
+  [Enable Access to the AWS Management Console with AD Credentials](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_management_console_access.html). For large enterprises, AWS recommends using [AWS Single Sign-On](https://aws.amazon.com/single-sign-on).
+  Enable multi-factor authentication by [integrating with your existing RADIUS-based MFA infrastructure](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ad_connector_mfa.html).
+  [Join Windows EC2 instances](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/launching_instance.html) to your on-premises Active Directory.

 **Note:** Amazon RDS for SQL Server and Amazon FSx for Windows File Server are not compatible with AD Connector. Amazon RDS for SQL Server compatible with AWS Managed Microsoft AD only. Amazon FSx for Windows File Server can be deployed with AWS Managed Microsoft AD or self-managed Active Directory.

## AWS Managed Microsoft Active Directory
<a name="aws-managed-microsoft-active-directory"></a>

 AWS Directory Service lets you run Microsoft Active Directory as a managed service. By default, each AWS Managed Microsoft AD has a minimum of two domain controllers, each deployed in a separate Availability Zone (AZ) for resiliency and fault tolerance. All domain controllers are exclusively yours with nothing shared with any other AWS customer. AWS provides operational management to monitor, update, backup, and recover domain controller instances. You administer users, groups, computer and group policies using standard Active Directory tools from a Windows computer joined to the AWS Managed Microsoft AD domain.

 AWS Managed Microsoft AD preserves the Windows single sign-on (SSO) experience for users who access AD DS integrated applications in a hybrid IT environment. With AD DS trust support, your users can sign in once on-premises and access Windows workloads running on-premises and in the cloud. You can optionally expand the scale of the directory by adding domain controllers, thereby enabling you to distribute requests to meet your performance requirements. You can also share the directory with any account and VPC. Multi-Region replication can be used to automatically replicate your AWS Managed Microsoft AD directory data across multiple Regions so you can improve performance for users and applications in disperse geographic locations. AWS Managed Microsoft AD uses native AD replication to replicate your directory’s data securely to the new Region. Multi-Region replication is only supported for the Enterprise Edition of AWS Managed Microsoft AD.

 AWS Managed Microsoft AD enables you to forward all domain controller’s Windows Security event log to Amazon CloudWatch, giving you the ability to monitor your use of the directory and any administrative intervention performed in the course of AWS operating the service. It is also approved for applications in the AWS Cloud that are subject to compliance by the [U.S. Health Insurance Portability and Accountability Act](https://aws.amazon.com/compliance/hipaa-compliance/) (HIPAA), [Payment Card](https://aws.amazon.com/compliance/pci-dss-level-1-faqs/) [Industry Data Security Standard](https://aws.amazon.com/compliance/pci-dss-level-1-faqs/) (PCI DSS), [Federal Risk and Authorization Management](https://aws.amazon.com/compliance/fedramp/) (FedRAMP), or [Service Organizational Control](https://aws.amazon.com/compliance/soc-faqs/) (SOC), when you [enable compliance for your directory](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_compliance.html). You can also tailor security with features that enable you to [manage](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_password_policies.html) [password policies,](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_password_policies.html) and [enable secure LDAP communications](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_ldap.html) through Secure Socket Layer (SSL)/Transport Layer Security (TLS). You can also [enable multi-factor](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_mfa.html) [authentication (MFA) for AWS Managed Microsoft AD](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_mfa.html). This authentication provides an additional layer of security when users access AWS applications from the internet, such as Amazon WorkSpaces or Quick.

 AWS Managed Microsoft AD enables you to [extend your schema](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_schema_extensions.html) and perform LDAP write operations. These features, combined with advanced security features, such as Kerberos Constrained Delegation and Group Managed Service Account, provide the greatest degree of compatibility for Active Directory aware applications, like Microsoft SharePoint, Microsoft SQL Server Always On Availability Groups, and many .NET applications. Because Active Directory is an LDAP directory, you can also use AWS Managed Microsoft AD for Linux Secure Shell (SSH) authentication and other LDAP-enabled applications. The full [list of supported](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_mfa.html#supportedamazonapps) [AWS applications](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_mfa.html#supportedamazonapps) is available on the AWS Documentation site.

 AWS Managed Microsoft AD runs actual Windows Server 2012 R2 Active Directory Domain Services and operates at the 2012 R2 functional level. AWS Managed Microsoft AD is available in two editions: Standard and Enterprise. These editions have different storage capacity; Enterprise Edition also has multi-region features.

All new AWS Directory Service for Microsoft AD (AWS Managed Microsoft AD) directories run on Windows Server 2019. For current customers with existing directories, you can simply update with just a few clicks or programmatically via API. With this feature, you can initiate updates for existing directories when it’s most convenient, avoiding peak business hours, for example. Additionally, starting in March 2023, AWS will begin automatically updating any AWS Managed Microsoft AD directories to Windows Server 2019.

|  Edition  |  Storage capacity  |  Approximate number of objects that can be stored\*  |  Approximate number of users in domain\*  |
| --- | --- | --- | --- |
|  Standard  |  1 GB  |  \~30,000  |  Up to \~5,000 users  |
|  Enterprise  |  17 GB  |  \~500,000  |  Over 5,000 users  |

 **\*** The number of objects varies based on type of objects, schema extensions, number of attributes, and data stored in attributes.

**Note**
AWS Domain Administrators have full administrative access to all domains hosted on AWS. See your agreement with AWS and the AWS Data Privacy FAQ for more information about how AWS handles content that you store on AWS systems, including directory information. You do not have Domain or Enterprise Admin permissions and rely on delegated groups for administration.

 AWS Managed Microsoft AD can be used for following scenarios: managing access to AWS Management Console and cloud services, joining EC2 Windows instances to Active Directory, deploying Amazon RDS databases with Windows authentication, using FSx for Windows File Services, and signing in to productivity tools like Amazon Chime and Amazon WorkSpaces. For more information on this solution, see [Design consideration for AWS Managed Microsoft Active Directory](design-consideration-for-aws-managed-microsoft-active-directory.md) in this document.

## Active Directory on EC2
<a name="active-directory-on-ec2"></a>

 If you prefer to extend your Active Directory to AWS and manage it yourself for flexibility or other reasons, you have the option of running Active Directory on EC2. For more information, see [Design considerations for running Active Directory on EC2 instances](design-considerations-for-running-active-directory-on-ec2-instances.md) in this document.

## Comparison of Active Directory Services on AWS
<a name="comparison-of-active-directory-services-on-aws"></a>

 The following table compares the features and functions between various Directory Services options available on AWS. Many features are not applicable directly to AWS AD Connector, because it is acting only as a proxy to the existing Active Directory domain.

|  Function  |  AWS AD Connector  |  AWS Managed Microsoft AD  |  Active Directory on EC2  |
| --- | --- | --- | --- |
|  Managed service  |  yes  |  yes  |  no  |
|  Multi-Region deployment  |  n/a  |  yes, Enterprise Edition  |  yes  |
|  Share directory with multiple accounts  |  no  |  yes  |  no  |
|  Supported by AWS applications (Amazon Chime, Amazon WorkSpaces, AWS Single Sign-On & etc.)  |  yes  |  yes  |  yes (through federation or AD Connector)  |
|  Supported by RDS (SQL Server, Oracle, MySQL, PostgreSQL, and MariaDB)  |  n/a  |  yes  |  no  |
|  Supported by FSx for Windows File Server  |  n/a  |  yes  |  yes  |
|  Creating users and groups  |  yes  |  yes  |  yes  |
|  Joining computers to the domain  |  yes  |  yes  |  yes  |
|  Create trusts with existing Active Directory domains and forests  |  n/a  |  yes  |  yes  |
|  Seamless domain join for Windows and Linux EC2 instances  |  yes  |  yes  |  yes, with AWS AD Connector  |
|  Schema extensions  |  n/a  |  yes  |  yes  |
|  Add domain controllers  |  n/a  |  yes  |  yes  |
|  Group Managed Service Accounts  |  n/a  |  yes  |  Depends on the Windows Server version  |
|  Kerberos constrained delegation  |  n/a  |  yes  |  yes  |
|  Support Microsoft Enterprise CA  |  n/a  |  yes  |  yes  |
|  Multi-Factor Authentication  |  yes, through RADIUS  |  yes, through RADIUS  |  yes, with AD Connector  |
|  Group policy  |  n/a  |  yes  |  yes  |
|  Active Directory Recycle bin  |  n/a  |  yes  |  yes  |
|  PowerShell support  |  n/a  |  yes  |  yes  |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
