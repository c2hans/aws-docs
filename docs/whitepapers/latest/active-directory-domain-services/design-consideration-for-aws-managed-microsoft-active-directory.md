---
source_url: https://docs.aws.amazon.com/whitepapers/latest/active-directory-domain-services/design-consideration-for-aws-managed-microsoft-active-directory.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Design consideration for AWS Managed Microsoft Active Directory
<a name="design-consideration-for-aws-managed-microsoft-active-directory"></a>

 Active Directory depends on the network and accounts design. Before you select the right Active Directory topology, you must choose your network and organizational design.

 Although there is no one-size-fits-all answer for how many AWS accounts a particular customer should have, most companies create more than one AWS account, as multiple accounts provide the highest level of resource and billing isolation in the following cases:
+  The business requires strong fiscal and budgetary billing isolation between specific workloads, business units, or cost centers.
+  The business requires administrative isolation between workloads.
+  The business requires a particular workload to operate within specific AWS service limits and not impact the limits of another workload.
+  The business’s workloads depend on specific instance reservations to support high availability (HA) or disaster recovery (DR) capacity requirements.

## Single account, AWS Region, and VPC
<a name="single-account-aws-region-and-vpc"></a>

 The simplest case is when you need to deploy a new solution in the cloud from scratch. You can deploy AWS Managed Microsoft AD in minutes and use it for most of the services and applications that require Active Directory. This solution is ideal for scenarios with no additional requirements for logical isolation between application tiers or administrators.

![Diagram showing Managed Active Directory architecture deployed by Quick Start](http://docs.aws.amazon.com/whitepapers/latest/active-directory-domain-services/images/managed-ad-deployed-by-quick-start.png)

## Multiple accounts and VPCs in one AWS Region
<a name="multiple-accounts-and-vpcs-in-one-aws-region"></a>

 Large organizations use multiple AWS accounts for administrative delegation and billing purposes. You can share a single AWS Managed Microsoft AD with multiple AWS accounts within one AWS Region. This capability makes it easier and more cost-effective for you to manage directory-aware workloads from a single directory across accounts and VPCs. This option also allows you seamlessly join your Amazon EC2 Windows instances to AWS Managed Microsoft AD.

![Diagram showing sharing single AWS Managed Microsoft AD with another account](http://docs.aws.amazon.com/whitepapers/latest/active-directory-domain-services/images/sharing-single-managed-ad-with-another-account.png)

 AWS recommends that you create a separate account for identity services like Active Directory and only allow a very limited group of administrators to have access to this account. Generally, you should treat Active Directory in the cloud in the same manner as on-premises Active Directory. Just as you would limit access to a physical data center, make sure to limit administrative access to the AWS account control.

 Create additional AWS accounts as necessary in your organization and share the AWS Managed Microsoft AD with them. After you have shared the service and configured routing, these users can use Active Directory to join EC2 Windows instances, but you maintain control of all administrative tasks.

 Deploy AWS Managed AD in your management account of AWS Organizations. This allows you to use Managed AD for authentication with AWS Identity and Access Management (IAM) to access the AWS Management Console and other AWS applications using your Active Directory credentials.

## Multiple AWS Regions deployment
<a name="multiple-aws-regions-deployment"></a>

 AWS Managed Microsoft AD Enterprise Edition supports Multi-Region deployment. You can use automated multi-Region replication in all Regions where AWS Managed Microsoft AD is available.

 AWS services such as Amazon RDS for SQL Server and Amazon FSx connect to the local instances of the global directory. This allows your users to sign-in once to AD-aware applications running in AWS as well as AWS services like Amazon RDS for SQL Server in any AWS Region – using credentials from AWS Managed Microsoft AD or a trusted AD domain or forest. Refer to [AWS Directory Service documentation](https://docs.aws.amazon.com/directory-service/) for the current list of AWS Services supporting Multi-Region replication feature.

 With multi-Region replication in AWS Managed Microsoft AD, AD-aware applications such as SharePoint, SQL Server Always On, AWS services such as Amazon RDS for SQL Server, and Amazon FSx for Windows File Server, use the directory locally for high performance and are multi-Region for high resiliency. The following list comprises additional benefits of Multi-Region replication.
+  It enables you to deploy a single AWS Managed Microsoft AD instance globally, quickly, and eliminates the heavy lifting of self-managing a global AD infrastructure.
+  Optimal performance for workloads deployed in multiple regions.
+  Multi-Region resiliency. AWS Managed Microsoft AD handles automated software updates, monitoring, recovery, and the security of the underlying AD infrastructure across all Regions.
+  Disaster recovery. In the event that all domain controllers in one Region are down, AWS Managed Microsoft AD recovers the domain controllers and replicates the directory data automatically. Meanwhile domain controllers in other Regions are up and running.

   To deploy AWS Managed Microsoft AD across multiple Regions, you must create it in Primary region and after that add one or more Replicated regions. Consider following factors for your Active Directory design:
+  When you deploy a new Region, AWS Managed Microsoft AD creates two domain controllers in the selected VPC in the new Region. You can add more domains controllers later for scalability.
+  AWS Managed Microsoft AD uses a backend network for replication and communications between domain controllers.
+  AWS Managed Microsoft AD creates a new Active Directory Site and names it the same name of the Region. For example, us-east-1. You can also rename this later using the Active Directory Sites & Services tool
+  AWS Managed AD is configured to use change notifications for inter-site replications to eliminate replication delays.

 After you add your new Region, you can do any of the following tasks:
+  Add more domain controllers to the new Region for horizontal scalability.
+  Share your directory with more AWS accounts per Region. Directory sharing configurations are not replicated from the primary Region and you may have different sharing configuration in different region based on your security requirements.
+  Enable log forwarding to retrieve your directory’s security logs using Amazon CloudWatch Logs from the new Region. When you enable log forwarding, you must provide a log group name in each Region where you replicated your directory.
+  Enable Amazon Simple Notification Service (Amazon SNS) monitoring for the new Region to track your directory health status per Region.

## Enable Multi-Factor Authentication for AWS Managed Microsoft AD
<a name="enable-multi-factor-authentication-for-aws-managed-microsoft-ad"></a>

 You can enable multi-factor authentication (MFA) for your AWS Managed Microsoft AD to increase security when your users specify their Active Directory credentials to access [supported Amazon enterprise applications.](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_mfa.html#supportedamazonapps) When you enable MFA, your users enter their sign-in credentials (first factor), and then enter an authentication code (second factor) that they obtain from your virtual or hardware MFA solution. These factors together provide additional security by preventing access to your Amazon enterprise applications, unless users supply valid user credentials and a valid MFA code.

 To enable MFA, you must have an MFA solution that is a remote authentication dial-in user service (RADIUS) server, or you must have an MFA plugin to a RADIUS server already implemented in your on-premises infrastructure. Your MFA solution should implement one-time passcodes (OTP) that users obtain from a hardware device or from software running on a device (such as a mobile phone).

![Diagram showing using AWS Managed Microsoft Active Directory with MFA for access to Amazon WorkSpaces](http://docs.aws.amazon.com/whitepapers/latest/active-directory-domain-services/images/managed-microsoft-ad-with-mfa.png)

 A more detailed description of [this solution](https://aws.amazon.com/blogs/security/how-to-enable-multi-factor-authentication-for-amazon-workspaces-and-amazon-quicksight-by-using-microsoft-ad-and-on-premises-credentials/) is available on the AWS Security Blog.

## Active Directory permissions delegation
<a name="active-directory-permissions-delegation"></a>

 When you use AWS Managed Microsoft AD, AWS assumes responsibility for some of the service level tasks so that you may focus on other business critical tasks.

 The following service-level tasks are automatically performed by AWS
+  Taking snapshots of the Directory Service and providing the ability to recover data.
+  Creating trusts by administrator request.
+  Extending Active Directory schema by administrator request.
+  Managing Active Directory forest configuration.
+  Managing, monitoring, and updating domain controllers.
+  Managing and monitoring DNS service for Active Directory.
+  Managing and monitoring Active Directory replication.
+  Managing Active Directory sites and networks configuration.

 With AWS Managed Microsoft AD, you also may delegate administrative permissions to some groups in your organization. These permissions include managing users, joining computers to the domain, managing group policies and password policies, managing DNS, DHCP, DFS, RAS, CA and other services. The full list of permissions that can be delegated is described in the [AWS Directory Service Administration Guide.](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_getting_started_what_gets_created.html)

 Work with all teams that are using Active Directory services in your organization and create a list with all of the permissions that must be delegated. Plan security groups for different administrative roles and use AWS Managed Microsoft AD delegated groups to assign permissions. Check the [AWS Directory Service Administration Guide](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_getting_started_what_gets_created.html) to make sure that it is possible to delegate all of the required permissions.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
