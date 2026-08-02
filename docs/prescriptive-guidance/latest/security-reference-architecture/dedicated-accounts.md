---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/dedicated-accounts.html
---

# Dedicated accounts structure
<a name="dedicated-accounts"></a>

An AWS account provides security, access, and billing boundaries for your AWS resources, and enables you to achieve resource independence and isolation. By default, no access is allowed between accounts.

When designing your OU and account structure, start with security and infrastructure in mind. We recommend creating a set of foundational OUs for these specific functions, split into Infrastructure and Security OUs. These OU and account recommendations capture a subset of our broader, more comprehensive guidelines for AWS Organizations and multi-account structure design. For a full set of recommendations, see [Organizing your AWS environment using multiple accounts](https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/organizing-your-aws-environment.html) in the AWS documentation and the blog post [Best practices for organizational units with AWS Organizations](https://aws.amazon.com/blogs/mt/best-practices-for-organizational-units-with-aws-organizations/).

The AWS SRA utilizes the following accounts to achieve effective security operations on AWS. These dedicated accounts help ensure separation of duties, support different governance and access policies for different sensitives of applications and data, and help mitigate the impact of a security event. In the discussions that follow, we are focused on production (*prod*) accounts and their associated workloads. Software development lifecycle (SDLC) accounts (often called *dev* and *test* accounts) are intended for staging deliverables and can operate under a different security policy set from that of production accounts.

|
|
| Account | OU | Security role |
| --- |--- |--- |
| Management<br />  | — | Central governance and management of all AWS Regions and accounts. The AWS account that hosts the root of the AWS organization. |
| Security Tooling | Security | Dedicated AWS accounts for operating broadly applicable security services (such as GuardDuty, AWS Security Hub CSPM, Audit Manager, Detective, Amazon Inspector, and AWS Config), monitoring AWS accounts, and automating security alerting and response. (In AWS Control Tower, the default name for the account under the Security OU is *Audit account*.) |
| Log Archive | Security | Dedicated AWS accounts for ingesting and archiving all logging and backups for all AWS Regions and AWS accounts. This should be designed as immutable storage. |
| Network | Infrastructure | The gateway between your application and the broader internet. The Network account isolates the broader networking services, configuration, and operation from the individual application workloads, security, and other infrastructure. |
| Shared Services | Infrastructure | This account supports the services that multiple applications and teams use to deliver their outcomes. Examples include Identity Center directory services (Active Directory), messaging services, and metadata services. |
| Application | Workloads | AWS accounts that host the AWS organization's applications and perform the workloads. (These are sometimes called *Workload accounts*.) Application accounts should be created to isolate software services instead of being mapped to your teams. This makes the deployed application more resilient to organizational change. |
