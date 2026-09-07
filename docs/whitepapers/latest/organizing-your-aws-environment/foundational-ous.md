---
source_url: https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/foundational-ous.html
---

# Foundational OUs
<a name="foundational-ous"></a>

 The Security OU and the Infrastructure OU are categorized as foundational OUs. Foundational OUs are defined as OUs that contain accounts, workloads, and other AWS resources that provide common security and infrastructure capabilities to secure and support your overall AWS environment.

 Accounts, workloads, and data residing in the foundational OUs are typically owned by your centralized Cloud Platform or Cloud Engineering teams made up of cross-functional representatives from your Security, Infrastructure, and Operations teams.

 The majority of your accounts are contained in the other OUs. These OUs are intended to contain your business-related workloads. They also contain tools and services that support the entire lifecycle of your business-related services and data.

## Security OU
<a name="security-ou"></a>

 The Security OU is a foundational OU. Your security organization should own and manage this OU along with any child OUs and associated accounts.

 We recommend that you create the following accounts in the Security OU:
+ Log Archive
+ Security Tooling (Audit)

**Note**
 A default deployment of AWS Control Tower will create a Log Archive and Audit (also referred to as Security Tooling) accounts.

Depending on your initial requirements, you might not need to establish all of these accounts.

### Log Archive account
<a name="log-archive-account"></a>

 The Log Archive is an account that acts as a consolidation point for log data that is gathered from all the accounts in the organization and primarily used by your security, operations, audit, and compliance teams. This account contains a centralized storage location for copies of every account's audit, configuration compliance, and operational logs. It also provides a storage location for any other audit/compliance logs, as well as application/OS logs. For example, in this account, we recommend that you consolidate AWS API access logs recorded in AWS CloudTrail, logs of changes to AWS resources recorded in AWS Config, and other logs that have security implications.

 If you use VPC peering between accounts, then you might also benefit from consolidating [VPC Flow Logs](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html) data in this account. Logs should generally be made directly available for local use by teams working in any account on a shorter-term retention basis. It is common practice to auto- ingest logs from the log archive account into a security information and event management (SIEM) solution.

**Note**
 By utilizing AWS Control Tower for AWS environment management, it automatically enforces best practices, deploying AWS Config and AWS CloudTrail seamlessly across your environment. Their logs are consolidated in an Amazon S3 bucket within the Log Archive account.

### Recommended AWS Organization Integrated Service Delegation
<a name="recommended-integrated-service-delegation"></a>

 ****

| AWS service | Implementation details | AWS Control Tower enabled |
| --- | --- | --- |
| [Amazon Security Lake](https://docs.aws.amazon.com/security-lake/latest/userguide/getting-started.html) | Amazon Security Lake centralizes security data from cloud, on-premises, and custom sources into a data lake that's stored in your account. | No |

### Services in the Log Archive account
<a name="services-in-the-log-archive-account"></a>

 With [Amazon Security Lake](https://docs.aws.amazon.com/security-lake/latest/userguide/what-is-security-lake.html), you can automatically centralize security data from AWS and third-party sources into a data lake that's stored in your [Log Archive account](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/log-archive.html). Review Managing access in this account in the following sections to learn how to grant access to the logs from other accounts in your AWS organization.

 Logs should be available within the workload account for use by teams on short-term retention basis. It is common practice to auto-ingest logs from the log archive account into a security information and event management (SIEM) solution.

 If you are using [AWS Control Tower](https://aws.amazon.com/controltower) to manage your overall AWS environment, then AWS Config is automatically enabled in each Control Tower enrolled account, and AWS CloudTrail Org trail is created for all accounts in the Organization. The AWS CloudTrail logs and AWS Config configuration history are consolidated in an Amazon S3 bucket in the log archive account.

### Operational log data
<a name="operational-log-data"></a>

 Operational log data used by your infrastructure, operations, and workload owning teams often overlaps with the log data used by security, audit, and compliance teams. We recommend that you consolidate your operational log data into the Log Archive account. Based on your specific security and governance requirements, you might need to filter operational log data saved to this account. You might also need to specify who and what has access to the operational log data in the log archive account.

### Immutable log data
<a name="immutable-log-data"></a>

 Log data housed in the Log Archive account is considered immutable in that it is protected from being changed or deleted. Data retention policies and legislation that apply to your organization might also apply to the data in your log archive account.

### Managing access to this account
<a name="managing-access-to-this-account"></a>

 We strongly recommend that you only house log data in this account. By doing so, access to this account can be greatly limited.

 Workloads and tools that need to consume the consolidated log data are typically housed in your other accounts and are granted access through read-only IAM roles to access the log data in a read-only, least privileged manner.

 Additionally, to help ensure that log data is properly protected, we recommend SCPs be applied to the Security OU preventing modification or deletion of files within the centralized logging S3 bucket(s).

 Additionally, the use of S3 bucket versioning provides visibility into the complete history of all log files.

### Security Tooling (Audit) account
<a name="security-tooling-audit-account"></a>

**Note**
 In the context of AWS services, this account is used to provide centralized delegated admin access to AWS security tooling and consoles, as well as provide view-only access for investigative purposes into all accounts in the organization. The security tooling account should be restricted to authorized security and compliance personnel and related security. This account is an aggregation point (or points for organizations that split the functionality across multiple accounts) for AWS security services, including [AWS Security Hub CSPM](https://aws.amazon.com/security-hub/), [Amazon GuardDuty,](https://aws.amazon.com/guardduty/) [Amazon Macie](https://aws.amazon.com/macie/), [AWS AppConfig](https://docs.aws.amazon.com/systems-manager/latest/userguide/appconfig.html), [AWS Firewall Manager](https://aws.amazon.com/firewall-manager/), [Amazon Detective](https://aws.amazon.com/detective/), [Amazon Inspector](https://aws.amazon.com/inspector/), and [IAM Access Analyzer](https://aws.amazon.com/iam/features/analyze-access/).

 `ViewOnlyAccess` and `ReadOnlyAccess` IAM managed policies provide permissions that do not include mutable actions. The `ReadOnlyAccess` grants read access to all AWS services and resources whereas the `ViewOnlyAccess` access provides read-only access and further restricts read operations to view resources and only metadata.

#### Recommended AWS Organization Integrated Service Delegation
<a name="recommended-aws-organization-integrated-service-delegation"></a>

|  AWS service  | Implementation details | AWS Control Tower enabled |
| --- | --- | --- |
|  [AWS Audit Manager](https://docs.aws.amazon.com/organizations/latest/userguide/services-that-can-integrate-audit-manager.html)  |  Continuously audit your AWS use across multiple-accounts in your organization to simplify how you assess risk and compliance. Recommended to be in same AWS account AWS Security Hub CSPM delegated admin exists. <br /> Delegation needs to be done on home and operational AWS Regions.  |  No  |
|  [AWS CloudFormation Stacksets](https://docs.aws.amazon.com/organizations/latest/userguide/services-that-can-integrate-cloudformation.html)  |  CloudFormation Stacksets can be delegated to multiple accounts within your AWS Organization. Delegation of the service needs to be <br /> completed at only one AWS region for the AWS account.  |  Yes, delegation not configured  |
|  [AWS CloudTrail](https://docs.aws.amazon.com/organizations/latest/userguide/services-that-can-integrate-cloudtrail.html)  |  The management of CloudTrail Org Trails can be delegated to one account. It is recommended that the <br /> Security team manages the implementation.  |  Yes, delegation not configured  |
|  [AWS Config](https://docs.aws.amazon.com/organizations/latest/userguide/services-that-can-integrate-config.html)  |  Organization-wide aggregated view of your AWS resources, your AWS Config rules, and the AWS resources' compliance state. Creating an Organization aggregator can be done across multiple AWS regions into the region the aggregator is being deployed to. Multiple accounts can be delegated the AWS Config aggregator.  |  Yes, delegation not configured  |
|  [AWS Detective](https://docs.aws.amazon.com/organizations/latest/userguide/services-that-can-integrate-detective.html)  |  Required to be deployed to same account which is managing Amazon GuardDuty and AWS Security Hub CSPM. <br /> Requires GuardDuty to be enabled on Security Tooling account prior to delegating AWS Detective. Delegation needs to be done on home and operational AWS Regions.  |  No  |
|  [AWS Firewall Manager](https://docs.aws.amazon.com/organizations/latest/userguide/services-that-can-integrate-fms.html)  |  Configure full delegated administration support for Security Tooling account. Firewall Manager delegation is a global configuration for all AWS Regions and only needs to be delegated from your home AWS Region.  |  No  |
|  [Amazon GuardDuty](https://docs.aws.amazon.com/organizations/latest/userguide/services-that-can-integrate-guardduty.html)  |  Amazon GuardDuty allows for one delegated admin per AWS Organization. It is recommended to delegated Amazon GuardDuty to the same account AWS Security Hub CSPM and Amazon Macie are delegated to. Delegation needs to be done on home and operational AWS Regions.  |  No  |
|  [Amazon Inspector](https://docs.aws.amazon.com/organizations/latest/userguide/services-that-can-integrate-inspector2.html)  |  Delegate an administrator to enable or disable scans for member accounts, view aggregated finding data from the entire organization, create and manage suppression rules. Delegation needs to be done on home and operation al AWS Regions.  |  No  |
|  [Amazon Macie](https://docs.aws.amazon.com/organizations/latest/userguide/services-that-can-integrate-macie.html)  |  Amazon Macie allows for one delegated admin per AWS Organization. It is recommended to delegated Amazon Macie to the same account AWS Security Hub CSPM and Amazon GuardDuty are delegated to. Delegation needs to be done on home and operational AWS Regions.  |  No  |
|  [AWS Security Hub CSPM](https://docs.aws.amazon.com/organizations/latest/userguide/services-that-can-integrate-securityhub.html)  |  AWS Security Hub CSPM allows for one delegated admin per AWS Organization. It is recommended to delegated AWS Security Hub CSPM to the same account Amazon GuardDuty and Amazon Macie are delegated to, for ease of pivoting between these services in the AWS Management Console. Delegation needs to be done on each operational Region.  |  Yes — When you activate a Security Hub CSPM detective control within AWS Control Tower, it automatically enables Security Hub CSPM on your behalf.  |
|  [Amazon S3 Storage Lens](https://docs.aws.amazon.com/organizations/latest/userguide/services-that-can-integrate-s3lens.html)  |  Allows for multiple delegated admin accounts per AWS Organization. Service is global and only needs to be delegated from the home AWS Region  |  No  |
|  [AWS Trusted Advisor](https://docs.aws.amazon.com/organizations/latest/userguide/services-that-can-integrate-ta.html)  |  Allows for centralized view of AWS Trusted Advisor information. Requires the management account in your organization must have a Business, Enterprise On- Ramp, or Enterprise Support plan. Service is global and only needs to be delegated from the home AWS Region.  |  No  |
|  [IAM Access Analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-getting-started.html)  |  Configured with the entire AWS organization as the zone of trust so that it's easier for you to quickly look across resource policies and identify resources with public or cross-account access you might not intend. We recommend that you configure this analyzer in one of your security tooling accounts.  |  No  |

#### Additional services and functionalities
<a name="additional-services-and-functionalities"></a>

 Common examples of security capabilities that can be centrally accessed and managed using the Security Tooling account include:
+ **Third-party cloud security monitoring tools** — You can also house third-party cloud security monitoring services and tools in your security tooling accounts. For example, these accounts typically contain security information and event management (SIEM) tools and vulnerability scanners
+ **Automated detection and response workflows** — Automated detection and response workflows that act on data collected through these types of services are normally contained in your security tooling accounts.
+ **Incident response (IR) support** — Tools to support manual incident response (IR) procedures are typically housed in your security tooling accounts. Refer to the [AWS Security Incident Response Guide](https://docs.aws.amazon.com/whitepapers/latest/aws-security-incident-response-guide/welcome.html) for more information.

#### AWS Solutions
<a name="aws-solutions"></a>

|  AWS Solution  |  Description  |
| --- | --- |
|  [Automated Security Response on AWS](https://aws.amazon.com/solutions/implementations/automated-security-response-on-aws/)  |  Add-on that works with AWS Security Hub CSPM and provides predefined response and remediation actions based on industry compliance standards and best practices for security threats. It helps Security Hub CSPM customers to resolve common security findings and to improve their security posture in AWS.  |
|  [Automations for AWS Firewall Manager](https://aws.amazon.com/solutions/implementations/automations-for-aws-firewall-manager/)  |  Allows you to centrally configure, manage, and audit firewall rules across all your accounts and resources in AWS Organizations. This solution is a reference implementation to automate the process to set up AWS Firewall Manager security policies.  |
|  [Security Automations for AWS WAF](https://aws.amazon.com/solutions/implementations/security-automations-for-aws-waf/)  |  Automatically deploys a set of AWS WAF (web application firewall) rules that filter common web-based attacks. Users can select from preconfigured protective features that define the rules included in an AWS WAF web access control list (web ACL).  |

#### Example structure
<a name="example-structure"></a>

 The following example structure represents the recommended Security OU at a basic level. Note that within Control Tower governed environments, the accounts within the Security OU are limited to the Log Archive and Security Tooling (also known as Audit by default for AWS Control Tower deployments).

![Diagram showing example structure of Security OU](https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/images/example-security-ou.png)

## Infrastructure OU
<a name="infrastructure-ou"></a>

 The Infrastructure OU is a foundational OU that is intended to contain infrastructure services. The accounts in this OU are also considered administrative and your infrastructure and operations teams should own and manage this OU, any child OUs, and associated accounts.

 The Infrastructure OU is used to hold AWS accounts containing AWS infrastructure resources that are shared, utilized by, or used to manage accounts in the organization. This includes centralized operations or monitoring of your organization. No application accounts or application workloads are intended to exist within this OU.

 Common use cases for this OU include accounts to centralize management of resources. For example, a Network account might be used to centralize your AWS network, or an Operations Tooling account to centralize your operational tooling.

**Note**
 For guidance on where to contain non-infrastructure shared services, refer to [Workloads OU](application-ous.md#workloads-ou).

 In most cases, given the way most AWS Organization integrated services interact with the accounts within the Infrastructure OU, it does not generally make sense to have production and non-production variants of these accounts within the Infrastructure OU. In situations where non-production accounts are required, these workloads should be treated like any other application and placed in an account within the appropriate Workloads OU corresponding with the non-production phase of the SDLC (Dev OU or Test OU).

### Backup account
<a name="backup-account"></a>

 The Backup account serves as a dedicated and centralized hub for backup and disaster recovery management. It provides a unified platform to orchestrate, monitor, and enforce backup policies across AWS accounts within the AWS Organization.

 By consolidating backup processes in a central account, organizations can achieve several benefits. It simplifies backup management by eliminating the need to configure and maintain backup settings separately in each member account, streamlining operational efficiency and reducing the potential for errors. It ensures consistent and comprehensive data protection across the entire AWS infrastructure, regardless of the specific AWS services and resources in use. This approach also enhances compliance and governance efforts by enabling centralized auditing and reporting on backup and recovery activities, making it easier to track data protection metrics and maintain necessary records for compliance purposes.

### Recommended AWS Organization Integrated Service Delegation
<a name="recommended-aws-organization-integrated-service-delegation-1"></a>

|  AWS service  | Implementation details | AWS Control Tower enabled |
| --- | --- | --- |
|  [AWS Backup](https://docs.aws.amazon.com/organizations/latest/userguide/services-that-can-integrate-backup.html)  |  Register the Backup account as the delegated administrator in the AWS Backup console.  |  Yes  |
|  [AWS Organizations: AWS](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_delegate_policies.html) <br /> [Backup policy administration](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_delegate_policies.html)  |  Delegate AWS Backup Policy administration to the Backup account by enabling delegation of AWS Organizations in the management account and configure a policy that allows the Backup account to create Backup Policies.  |  Yes  |

### Additional services and functionalities
<a name="additional-services-and-functionalities-1"></a>

 Common examples of security capabilities that can be centrally accessed and managed using the Backup account includes:
+ Use centralized AWS KMS customer managed keys for AWS Backup service within the Backup account to centrally manage the encryption for backup operations across accounts.
+  Third-party backup tools that require resources can be created and managed in the Backup account.

### Identity account
<a name="identity-account"></a>

 The Identity account serves as a centralized identity federation account isolated from all other management and workload activities within the AWS Organization. Federated identity management grants you the ability to efficiently manage the access to the accounts in the AWS Organization and authorization to integrated applications. By managing your identities and controlling access to your environment centrally, you can quickly create, update, and delete the permissions and policies you need to meet your business requirements.

### Recommended AWS Organization Integrated Service Delegation
<a name="recommended-aws-organization-integrated-service-delegation-2"></a>

|  AWS service  | Implementation details | AWS Control Tower enabled |
| --- | --- | --- |
|  [IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/delegated-admin.html)  |  You can delegate administration of IAM Identity Center to this account which will allow you to administer IAM Identity Center outside of the management account.  |  Enabled — Yes <br /> Delegated — No  |
|  [IAM Access Analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-settings.html#access-analyzer-delegated-administrator.html)  |  An IAM Access Analyzer can be configured to detect resources that are shared outside of the organization (organization zone of trust). By default, this is managed from the management account. This can be delegated to a member account. This can be delegated to the Identity account or a Security Tooling account depending on who is responsible for auditing external access (Identity Team or Security Team).  |  No  |
|  Policy management for Organizations  |  From the organization's management account, you can delegate policy management for Organizations to specified member accounts to perform policy actions that are by default available only to the management account.  |  No  |
|  Central management root access for member accounts  |  We recommend you centrally secure the root user credentials of AWS accounts managed using AWS Organizations to prevent root user credential recovery and access at scale.  |  No  |

### Additional services and functionalities
<a name="additional-services-and-functionalities-2"></a>

 Common examples of security capabilities that can be centrally accessed and managed using the Identity account includes:
+ **Directory Service** — If you are using an AWS-hosted directory or AWS AD Connector, you can create and managed them in your Identity account alongside of AWS IAM Identity Center.
+ **SAML 2.0 custom managed applications** — With IAM Identity Center, you can create or connect workforce users and centrally manage their access across all their AWS accounts and applications.

### Network account
<a name="network-account"></a>

 The Network account serves as the central hub for your network within your AWS Organization. You can manage your networking resources and route traffic between accounts in your environment, your on-premises, and egress/ingress traffic to the internet. Within this account, your network administrators can manage and build security measures to protect network traffic across your cloud environment.

### Recommended AWS Organization Integrated Service Delegation
<a name="recommended-aws-organization-integrated-service-delegation-3"></a>

|  AWS service  | Implementation details | AWS Control Tower enabled |
| --- | --- | --- |
|  [AWS Network Manager](https://docs.aws.amazon.com/organizations/latest/userguide/services-that-can-integrate-network-manager.html)  |  Centrally manage and monitor your global networks with transit gateways and their attached resources in multiple AWS accounts within your organization.  |  No  |
|  [IPAM](https://docs.aws.amazon.com/vpc/latest/ipam/enable-integ-ipam.html)  |  Delegated to a single account for your entire AWS Organization. IPAM will inventory and track all active IPs across your AWS Organization.  |  No  |
|  [VPC Reachability Analyzer](https://docs.aws.amazon.com/organizations/latest/userguide/services-that-can-integrate-ra.html)  |  Trace paths across accounts in your organizations. You can assign multiple delegated admin accounts as needed.  |  No  |

### Additional services and functionalities
<a name="additional-services-and-functionalities-3"></a>

 Common examples of network capabilities and AWS services that can be centrally accessed and managed via the Network account include:
+ **Amazon VPC** — If you plan to implement centralized networking in your AWS environment, we recommend managing your [VPCs](https://aws.amazon.com/vpc/) within your network account, and sharing resources across your accounts within your AWS organization.
+ **Share your AWS Transit Gateway** — Create an [AWS Transit Gateway](https://aws.amazon.com/transit-gateway/) resource in the networking account and share it across the accounts within your AWS Organization using AWS Resource Access Manager (RAM).
+ **Share your Amazon Route 53 Endpoint Resolvers** — If you plan to use a centralized transitive network with [Amazon Route 53 Public Data Plane](https://aws.amazon.com/route53/) in your AWS Organization, we recommend managing and sharing your Route 53 Endpoint Resolvers in your network account within your AWS organization.
+ **Share your IPAM pools with your organization** — When you delegate an IPAM account, IPAM enables other AWS Organizations member accounts in the organization to allocate CIDRs from IPAM pools that are shared using AWS Resource Access Manager (RAM).
+ **Build centralize [AWS Site-to-Site VPN connections](https://docs.aws.amazon.com/vpn/latest/s2svpn/VPC_VPN.html)** — Using a transitive network architecture centralized in your Network account, a site-to-site VPN can be established and routing enabled across your cloud environment.
+ **Centralize [AWS Direct Connect](https://aws.amazon.com/directconnect/)** — Create and attach AWS Direct Connect to your transitive network with [AWS Transit Gateway.](https://aws.amazon.com/transit-gateway/)
+ **Centralized network inspection point** — Build inbound and outbound network traffic inspection points routing through the Network account.

### AWS Solutions
<a name="aws-solutions-1"></a>

 The following AWS Solutions are commonly deployed or related to the functional operations of the Network account:

|  AWS Solution  |  Description  |
| --- | --- |
|  [Network Orchestration for AWS Transit](https://aws.amazon.com/solutions/implementations/network-orchestration-aws-transit-gateway/) <br /> [Gateway](https://aws.amazon.com/solutions/implementations/network-orchestration-aws-transit-gateway/)  |  Automates the process of setting up and managing transit networks in distributed AWS environments. This solution allows customers to visualize and monitor their global network from a single dashboard rather than toggling between Regions from the AWS console. It creates a web interface to help control, audit, and approve transit network changes.  |
|  [Automations for AWS Firewall Manager](https://aws.amazon.com/solutions/implementations/automations-for-aws-firewall-manager/)  |  Allows you to centrally configure, manage, and audit firewall rules across all your accounts and resources in AWS Organizations. <br /> This solution is a reference implementation to automate the process to set up AWS Firewall Manager security policies.  |
|  [Security Automations for AWS WAF](https://aws.amazon.com/solutions/implementations/security-automations-for-aws-waf/)  |  Automatically deploys a set of AWS WAF (web application firewall) rules that filter common web-based attacks. Users can select from preconfigured protective features that define the rules included in an AWS WAF web access control list (web ACL).  |

### Operations Tooling account
<a name="operations-tooling-account"></a>

 Operations Tooling accounts can be used for day-to-day operational activities across your organization. The operations tooling account hosts tools, dashboards, and services needed to centralize operations where monitoring and metric tracking are hosted. These tools help the central operations team to interact with their environment from a central location.

### Recommended AWS Organization Integrated Service Delegation
<a name="recommended-aws-organization-integrated-service-delegation-4"></a>

|  AWS service  | Implementation details | AWS Control Tower enabled |
| --- | --- | --- |
|  [AWS Account Management](https://docs.aws.amazon.com/organizations/latest/userguide/services-that-can-integrate-account.html)  |  Manage alternate contact information for all of the accounts in your organization. Delegation is done on one region and for one account within your AWS Organizations.  |  No  |
|  [AWS Application Migration](https://docs.aws.amazon.com/organizations/latest/userguide/services-that-can-integrate-application-migration.html) <br /> [Service (AMG)](https://docs.aws.amazon.com/organizations/latest/userguide/services-that-can-integrate-application-migration.html)  |  AWS Application Migration Service simplifies, expedites, and reduces the cost of migrating applications to AWS. By integrating with Organizations, you can use the global view feature to manage large-scale migrations across multiple accounts.  |  No  |
|  [Amazon DevOps Guru](https://docs.aws.amazon.com/organizations/latest/userguide/services-that-can-integrate-devops.html)  |  You can integrate with AWS Organizations to manage insights from all accounts across your entire organization. You delegate an administrator to view, sort, and filter insights from all accounts to obtain organization-wide health of all monitored applications.  |  No  |
|  [AWS Health](https://docs.aws.amazon.com/organizations/latest/userguide/services-that-can-integrate-health.html)  |  Get visibility into events that might affect your resource performance or availability issues for AWS services. You can register up to 5 member accounts in your organization as a delegated administrator.  |  No  |
|  [AWS License Manager](https://docs.aws.amazon.com/organizations/latest/userguide/services-that-can-integrate-license-manager.html)  |  If you are planning to use a centralized model to buy and share licenses across your organization, we recommend you specify one of your Shared Services accounts as the delegated administrator for AWS License Manager.  |  No  |
|  [AWS Systems Manager](https://docs.aws.amazon.com/organizations/latest/userguide/services-that-can-integrate-ssm.html) <br /> [Change Manager](https://docs.aws.amazon.com/organizations/latest/userguide/services-that-can-integrate-ssm.html)  |  You can delegate administration for Systems Manager to the Operations Tooling account to perform administrative tasks for Change Manager, Explorer, and Ops Center.  |  No  |
|  [AWS Systems Manager](https://docs.aws.amazon.com/organizations/latest/userguide/services-that-can-integrate-ssm.html) <br /> [Explorer](https://docs.aws.amazon.com/organizations/latest/userguide/services-that-can-integrate-ssm.html)  |   |  No  |
|  [AWS CloudFormation](https://docs.aws.amazon.com/organizations/latest/userguide/services-that-can-integrate-cloudformation.html) <br /> [Stacksets](https://docs.aws.amazon.com/organizations/latest/userguide/services-that-can-integrate-cloudformation.html)  |  You can register multiple delegated administrator accounts in your AWS Organizations. CloudFormation Stackset delegation will give the AWS account full administrative access to deploy resources in other AWS accounts in your Organization. Delegation needs to be done only at the home region.  |  No  |
|  [VPC Reachability Analyzer](https://docs.aws.amazon.com/organizations/latest/userguide/services-that-can-integrate-ra.html)  |  Trace paths across accounts in your organizations. VPC Reachability Analyzer can have multiple delegated admin accounts.  |  No  |

### AWS Solutions
<a name="aws-solutions-2"></a>

 The following AWS Solutions are commonly deployed or related to the functional operations of the Operations Tooling account:

|  AWS Solution  |  Description  |
| --- | --- |
|  [Account Assessment for AWS Organizations](https://aws.amazon.com/solutions/implementations/account-assessment-for-aws-organizations/)  |  Presented in a web UI, this AWS Solution runs configurable scans on all AWS accounts in your AWS Organizations to help you identify dependencies in your underlying resource-based policies.  |
|  [Instance Scheduler on AWS](https://aws.amazon.com/solutions/implementations/instance-scheduler-on-aws/)  |  Automates the starting and stopping of Amazon Elastic Compute Cloud (Amazon EC2) and Amazon Relational Database Service (Amazon RDS) instances. This solution helps reduce operational costs by stopping resources that are not in use and starting them when they are needed. The cost savings can be significant if you leave all of your instances running at full utilization continuously.  |
|  [Cost Optimizer for Amazon WorkSpaces](https://aws.amazon.com/solutions/implementations/cost-optimizer-for-amazon-workspaces/)  |  Analyzes all of your Amazon WorkSpaces usage data and automatically converts the WorkSpace to the most cost-effective billing option (hourly or monthly), depending on your individual usage. You can use this solution with a single account, or with AWS Organizations across multiple accounts, to help you monitor your WorkSpace usage and optimize costs.  |
|  [Workload Discovery on AWS](https://aws.amazon.com/solutions/implementations/workload-discovery-on-aws/)  |  Workload Discovery on AWS (formerly called Amazon Personalize) is a tool to visualize AWS Cloud workloads. Use Workload Discovery on AWS to build, customize, and share detailed architecture diagrams of your workloads based on live data from AWS.  |

### Monitoring account
<a name="monitoring-account"></a>

 An AWS monitoring account can be used to monitor resources, applications, log data, and performance in other AWS accounts. AWS offers a number of tools and services that can be used to manage and monitor resources and workloads in an AWS account, including CloudWatch, Amazon Managed Service for Prometheus, Amazon Managed Grafana, and Amazon OpenSearch Service. These tools can be used to monitor resource and application usage, performance, review log data, and identify potential issues within the infrastructure or application.

**Note**
 Depending on your business requirements and team structures, you may choose to manage your monitoring resources and services in a single account with your other Operational Tooling services or as a dedicated Monitoring account. The core concept of the Monitoring account is to only give read-only functionality. The account in itself is not intended to have the ability to make changes across account your AWS Organization.

### Recommended AWS Organization Integrated Service Delegation
<a name="recommended-aws-organization-integrated-service-delegation-5"></a>

|  AWS service  | Implementation details | AWS Control Tower enabled |
| --- | --- | --- |
|  [AWS Health](https://docs.aws.amazon.com/organizations/latest/userguide/services-that-can-integrate-health.html)  |  Configure the Monitoring account as the delegated admin for AWS health (in the Management account) for ongoing visibility into your resource performance and the availability of your AWS services and accounts within your organization.  |  No  |
|  [Amazon S3 Storage Lens](https://docs.aws.amazon.com/organizations/latest/userguide/services-that-can-integrate-s3lens.html)  |  Register the Monitoring account as the delegated admin for Amazon S3 storage Lens (in the Management account) for organization-wide visibility into object-storage usage and activity. <br />You can use S3 Storage Lens metrics to generate summary insights, such as finding out how much storage you have across your entire organization or which are the fastest-growing buckets and prefixes.  |  No  |

### Additional services and functionalities
<a name="additional-services-and-functionalities-4"></a>

 Common examples of monitoring capabilities that can be centrally accessed and managed using the Monitoring account includes:
+ **AWS CloudWatch** — Configure [AWS CloudWatch Cross Account observability](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Unified-Cross-Account.html) and configure as the *monitoring account* or hub account.
+  **CloudWatch dashboards** that are created at the account level can be shared with the monitoring account which allows for distributed management with centralized monitoring.
+ **Third-party monitoring tools** (such as ElasticSearch, Splunk, Prometheus, and Grafana) that require resources can be created and managed in the Monitoring account.
+ **Customer created automations and reports** can be run from and stored in the Monitoring account.
+ **Log Archive log analysis**. In order to analyze Log data stored in the Log Archive account, Amazon Managed Grafana or Quick can be used in the Monitoring account to analyze Log data in an S3 bucket in the Log Archive account by connecting to Amazon Athena in the Log Archive account.
+ **Amazon OpenSearch Service** can be deployed and managed in the Monitoring account to analyze logs, monitor applications, and analyze clickstreams.
+ **Quick** can be deployed and managed in the Monitoring account and cross account data sources can be used to centrally monitor or report organization data.
+  **Amazon Managed Grafana** can be deployed into the monitoring account for centralized monitoring of resources, containers, CloudWatch logs, and applications by connecting to data sources in different accounts or to centralized CloudWatch metrics, logs, and traces.

### AWS Solutions
<a name="aws-solutions-x"></a>

 The following AWS solutions are commonly deployed or related to the functional operations of the Monitoring account:

|  AWS Solution  |  Description  |
| --- | --- |
|  [Centralized Logging with OpenSearch](https://aws.amazon.com/solutions/implementations/centralized-logging-with-opensearch/)  |  Helps organizations collect, ingest, and visualize log data from various sources using Amazon OpenSearch Service. This solution provides a web-based console, which you can use to create log ingestion pipelines with a few clicks.  |

### Shared Services accounts
<a name="shared-services-accounts"></a>

 A Shared Services account is an AWS account created and dedicated to hosting and managing centralized IT services and resources that are shared across multiple other AWS accounts within an AWS Organization. The primary purpose of a Shared Services account is to consolidate similar shared services to give a single access point to manage, interface and consume. You may create multiple Shared Service accounts depending on your need to securely isolate the functionality of the grouped services in the account.

**Note**
 AWS account workload isolation is a best practice for enhancing security and operational efficiency in cloud environments. It involves grouping AWS resources and workloads into separate AWS accounts based on their functionality and security requirements. A Shared Service account should contain resources and workloads that can be grouped together in order to ensure security, compliance, and operational separation of duties.

### Recommended AWS Organization Integrated Service Delegation
<a name="recommended-aws-organization-integrated-service-delegation-6"></a>

|  AWS service  |  Implementation Details  |  Control Tower Enabled  |
| --- | --- | --- |
|  [Service Catalog](https://docs.aws.amazon.com/organizations/latest/userguide/services-that-can-integrate-servicecatalog.html)  |  Create and manage catalogs of IT services that are approved for use on AWS.  |  Yes — AWS Control Tower automatically sets up Service Catalog to provision new accounts through Account Factory.  |
|  [AWS Compute Optimizer](https://docs.aws.amazon.com/organizations/latest/userguide/services-that-can-integrate-compute-optimizer.html)  |  AWS Compute Optimizer can be delegated to one AWS account in your AWS Organization. It is recommended to deploy to a Shared Services account or the Monitoring account.  |  No  |

### Additional services and functionalities
<a name="additional-services-and-functionalities-5"></a>

 Common examples of security capabilities that can be centrally accessed and managed using the Shared Services account includes:
+ **EC2 Image Builder** — EC2 Image Builder integrates with AWS Resource Access Manager (AWS RAM) to allow you to share certain resources with any AWS account or through AWS Organizations.

### Example structure
<a name="example-structure-1"></a>

 The following example structure represents the recommended Infrastructure OU at a basic level. For general guidance on separating production and non-production workloads, refer to [Organizing workload-oriented OUs](advanced-ous.md#organizing-workload-oriented-ous).

![Diagram showing an example structure of Infrastructure OU](https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/images/example-infrastructure-ou.png)
