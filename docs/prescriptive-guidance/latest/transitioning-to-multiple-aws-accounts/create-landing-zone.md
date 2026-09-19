---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/transitioning-to-multiple-aws-accounts/create-landing-zone.html
---

# Create a landing zone
<a name="create-landing-zone"></a>

A *landing zone* is a well-architected, multi-account AWS environment that is a starting point from which you can deploy workloads and applications. It provides a baseline to get started with multi-account architecture, identity and access management, governance, data security, network design, and logging. [AWS Control Tower](https://docs.aws.amazon.com/controltower/latest/userguide/what-is-control-tower.html) is a service that simplifies the maintenance and governance of a multi-account environment by providing automated guardrails. Typically, you provision a single AWS Control Tower landing zone that manages your environment across all AWS Regions. AWS Control Tower works by orchestrating other AWS services within your account. For more information, see [What happens when you set up a landing zone](https://docs.aws.amazon.com/controltower/latest/userguide/how-control-tower-works.html#how-it-works-setup) (AWS Control Tower documentation).

When you set up a landing zone with AWS Control Tower, you identify three shared accounts: the management account, the log archive account, and the audit account. For more information, see [What are the shared accounts](https://docs.aws.amazon.com/controltower/latest/userguide/how-control-tower-works.html#what-shared) (AWS Control Tower documentation). For the management account, you must use an existing account that isn't hosting any workloads to set up the landing zone. For the log archive and audit accounts, you can choose to reuse existing AWS accounts, or AWS Control Tower can create them for you.

For instructions about how to set up your AWS Control Tower landing zone, see [Getting started](https://docs.aws.amazon.com/controltower/latest/userguide/getting-started-with-control-tower.html) (AWS Control Tower documentation).

## Best practices
<a name="landing-zone-best-practices"></a>
+ Adhere to the best practices in [Design principles for your multi-account strategy](https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/design-principles-for-your-multi-account-strategy.html) (AWS Whitepaper).
+ Adhere to the [Best practices for AWS Control Tower administrators](https://docs.aws.amazon.com/controltower/latest/userguide/best-practices.html) (AWS Control Tower documentation).
+ Create your landing zone in the AWS Region that hosts the majority of your workloads.

<table>
<tbody>
</tbody>
</table>

+ When determining which Regions AWS Control Tower will govern, select only the Regions in which you expect to immediately deploy workloads. You can change these Regions or add more later. If AWS Control Tower governs a Region, it will deploy its detective guardrails into that Region as [AWS Config Rules](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config.html).
+ After determining which Regions AWS Control Tower will govern, deny access to all ungoverned Regions. This helps ensure that your workloads and developers can only use approved AWS Regions. This is implemented as a service control policy (SCP) in the organization. For more information, see [Configure the AWS Region deny control](https://docs.aws.amazon.com/controltower/latest/userguide/region-deny.html) (AWS Control Tower documentation).
+ When setting up your landing zone in AWS Control Tower, we recommend you rename the following OUs and accounts:
  + We recommend that you rename the **Security** OU to **Security\_Prod** to signify that this OU will be used for production security-related AWS accounts.
  + We recommend that you allow AWS Control Tower to create an additional OU and then rename it from **Sandbox** to **Workloads**. In the next section, you create additional OUs within the **Workloads** OU, which you use to organize your AWS accounts.
  + We recommend that you rename the centralized logging AWS account from **Log Archive** to **log-archive-prod**.
  + We recommend that you rename the audit account from **Audit** to **security-tooling-prod**.
+ To help prevent fraud, AWS requires that AWS accounts have a history of use before they can be added to an AWS Control Tower landing zone. If you are using a new AWS account without any usage history, in the new account, you can launch an Amazon Elastic Compute Cloud (Amazon EC2) instance that is not in the AWS Free Tier. Let the instance run for a few minutes and then terminate it.
