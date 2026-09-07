---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/designing-control-tower-landing-zone/account-structure.html
---

# Configuring acount structure and OUs
<a name="account-structure"></a>

You can achieve both speed and security in the cloud by using AWS accounts. AWS accounts are resource containers that assist users in managing AWS resources. As needs and demands grow, environments scale through the addition of new accounts. The use of multiple accounts is a best practice because it enables rapid innovation across distributed teams and individuals, reduces the scope of impact through isolation, and can be adjusted to meet new business processes based on operational, regulatory, and budgetary requirements. Lastly, costs are incurred at the account level, so activity and costs can be identified with each account.

One of the key principles of account structure design is to start with a basic structure and expand it as your needs evolve. For an example of an incremental approach for account structure design, see the section [Patterns for organizing your AWS accounts](https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/patterns-for-organizing-your-aws-accounts.html) in the AWS whitepaper *Organizing Your AWS Environment Using Multiple Accounts*. Your account structure might have to be tailored based on your industry. For examples, see the AWS blog post [Defining an AWS multi-account strategy for a digital bank](https://aws.amazon.com/blogs/industries/defining-an-aws-multi-account-strategy-for-a-digital-bank/) and the AWS Prescriptive Guidance guide [OU structure in regulated AWS landing zones: an example from the pharmaceutical industry](https://docs.aws.amazon.com/prescriptive-guidance/latest/ou-structure-landing-zone/introduction.html). Let's look at some key considerations for OU design.
+ **Preventive and detective controls**. A key consideration for defining a separate OU for a group of accounts is whether there are a set of controls you would like to apply to that OU. If you are planning to use custom controls, specifically SCPs, consider the [quota](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_reference_limits.html) on the number of SCPs that you can attach to an OU. If you need more custom SCPs for an OU than the quota permits, you can design your account structure to apply some of those SCPs at an OU that's one level higher or lower to achieve the desired outcome.
+ **Shared resources**. Another consideration is whether there are any AWS resources (such as transit gateways or Amazon Route 53 forwarding rules) that you would like to share with all the accounts in the OU by using [AWS Resource Access Manager](https://docs.aws.amazon.com/ram/latest/userguide/what-is.html).
+ **Automation**. This can be an important consideration for OU design. For example, [AWS CloudFormation StackSets](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/what-is-cfnstacksets.html) supports deploying resources to all accounts within an OU, so you can group accounts that have common AWS resource requirements in an OU to automate deployments.

The following diagram provides an example of an AWS Control Tower‒based account structure that includes various accounts and OUs and follows AWS best practices. You can customize this architecture based on the account structure that's suitable for your enterprise.

![AWS Control Tower-based account structure for a landing zone](https://docs.aws.amazon.com/prescriptive-guidance/latest/designing-control-tower-landing-zone/images/guide-img/156d118c-ed00-4c5b-9a02-63c2673a3342/images/101dd11a-d8b3-49fd-ae5f-5480a1c91607.png)

The account in which AWS Control Tower is deployed is automatically configured as the AWS Control Tower management account. The management account consolidates billing of all accounts in the landing zone. This account is used to [provision new AWS accounts with AWS Control Tower Account Factory](https://docs.aws.amazon.com/controltower/latest/userguide/account-factory.html), manage OUs and controls, and manage user access and permissions by using IAM Identity Center.

AWS Control Tower sets up the Security OU that contains the Log Archive and Audit accounts, and provides an option to create an additional OU. You can change the names of these accounts during AWS Control Tower setup but not later. If required, you can specify an existing AWS account as the Log Archive or Audit account during the setup process. You have to provision all additional OUs and member accounts. You might decide to start with a subset of OUs at their beginning of your landing zone implementation and add OUs later.

The diagram includes the following key OUs.

|
|
| OU | Description |
| --- |--- |
| **Security OU** | Automatically set up by AWS Control Tower to host the Log Archive and Audit accounts.+ **Log Archive account** – AWS Control Tower centralizes all AWS CloudTrail and AWS Config logs into a centralized S3 bucket. You can also centralize other logs from across your organization, such as Amazon CloudWatch logs, Amazon S3 access logs, and VPC Flow Logs, in this account.<br />+ **Audit account** – Provides read and write access to all accounts in your landing zone. From the Audit account, you can programmatically review accounts by using a role that is granted only to AWS Lambda functions. Your security and compliance teams can use the Audit account to audit and review the accounts in your organization. |
| **Sandbox OU** | Set up by AWS Control Tower to host sandbox accounts that help you safely test and develop new services, processes, and templates. |
| **Infrastructure OU** | Contains the following accounts that are required for shared infrastructure services for your production and non-production workloads:+ Backup account<br />+ Identity account<br />+ Monitoring account<br />+ Network account<br />+ Operations Tooling account<br />+ Shared Services account<br />For details of the recommended AWS services and the AWS solutions that you can host in each account, see [Infrastructure OU](https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/infrastructure-ou-and-accounts.html) in the AWS whitepaper *Organizing Your AWS Environment Using Multiple Accounts*. |
| **Policy Staging OU** | Helps you safely test policy changes such as detective and preventive controls before applying them to OUs or accounts. |
| **Individual Business Users OU** | Hosts accounts for individual business users and teams who want to internally use AWS resources that aren't classified as workloads. |
| **Exceptions OU** | Hosts accounts that require exceptions to the default security policies that are applied to the Workloads OU. |
| **Workloads OU** | Hosts business workloads for both production and non-production environments. |
| **Deployments OU** | Hosts resources for building, validating, and promoting releases to your environments. Includes continuous integration and continuous delivery (CI/CD) tooling. |
| **Transitional OU** | Provides a holding area for accounts that are being moved to the landing zone before formally integrating them into the standardized OUs in the account structure. |
| **Suspended OU** | Provides a locked and extremely restricted environment to host suspended, deleted, and reused accounts. This is useful if you suspect that an account has been breached or compromised. |

For further guidance on defining a multi-account strategy, see the AWS whitepaper [Organizing Your AWS Environment Using Multiple Accounts.](https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/organizing-your-aws-environment.html)

You can automatically provision new AWS accounts by using [AWS Control Tower Account Factory](https://docs.aws.amazon.com/controltower/latest/userguide/account-factory.html) or [AWS Control Tower Account Factory for Terraform (AFT)](https://docs.aws.amazon.com/controltower/latest/userguide/aft-overview.html), as described in the following sections.

## AWS Control Tower Account Factory
<a name="account-factory"></a>

[AWS Control Tower Account Factory](https://docs.aws.amazon.com/controltower/latest/userguide/account-factory.html) is a console-based AWS Control Tower feature that you can use to provision new accounts in your organization. Account Factory functions as a UI for an AWS Service Catalog product and provisions custom accounts by using CloudFormation. You can also configure Account Factory to optionally create VPCs and a NAT gateway in the new accounts. This configuration automatically provisions a VPC with up to two subnets and a defined Classless InterDomain Routing (CIDR) range in the AWS Regions that you specify.

**Note**
The subnet IP address ranges in the VPCs of the accounts provisioned by Account Factory might [overlap](https://docs.aws.amazon.com/controltower/latest/userguide/configuring-account-factory-with-VPC-settings.html).

## AWS Control Tower add-ons
<a name="add-ons"></a>

AWS Control Tower add-on solutions deliver enhanced features and customizations provided by AWS to augment the capabilities of AWS Control Tower. These enhancements are designed to seamlessly elevate the functionality of AWS Control Tower to help meet organizational requirements for increased efficiency, security, and compliance within the AWS environment. Examples include the following:
+ [Landing Zone Accelerator (LZA)](https://aws.amazon.com/solutions/implementations/landing-zone-accelerator-on-aws/) is an open source solution from AWS that's designed to expedite the setup of a secure, multi-account AWS environment based on AWS best practices. It streamlines the deployment of a landing zone and offers automated processes for account creation, configurable security and compliance guardrails, and customizations to align with your organization's policies.
+ [Account Factory for Terraform (AFT)](https://docs.aws.amazon.com/controltower/latest/userguide/aft-overview.html) is a Terraform module from AWS that extends the capabilities of the AWS Control Tower Account Factory. It enables organizations to create and manage AWS accounts by using infrastructure as code (IaC). AFT facilitates the definition of account configurations and resources through version-controlled code, which helps ensure consistency and repeatability in the account creation process.
+ [Customizations for Control Tower (CfCT)](https://docs.aws.amazon.com/controltower/latest/userguide/cfct-overview.html) is a solution by AWS that supports the deployment of resources by using CloudFormation templates and service control policies (SCPs). CfCT is integrated with AWS Control Tower lifecycle events and ensures that your deployments are synchronized with landing zone events. For example, it ensures that newly provisioned accounts are equipped with the correct infrastructure and automatically deploys domain-specific resources for accounts that are placed within OUs.
