---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/transitioning-to-multiple-aws-accounts/introduction.html
---

# Transitioning to multiple AWS accounts
<a name="introduction"></a>

*Justin Plock, Amazon Web Services*

Many companies begin their journey by using a single Amazon Web Services (AWS) account. Multiple roles within a company use this account to operate the business. Engineers develop code, deploy to development and test environments, and promote changes to production. Product managers query data sources to gather insights into business performance. The sales team is conducting demos from the production environment to attract new customers. The finance team is monitoring cloud spending from the AWS Billing console.

When all of these separate roles use a single AWS account, it can become difficult to enforce the security best practice of [Applying the least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#grant-least-privilege), which means you grant only the minimum permissions necessary to do the job. At a certain stage in a startup's development, someone will ask the question *Do all of our engineers need access to production?* The answer is almost always *no*, but many companies struggle with how to unwind their existing single-account environment into a multi-account environment without slowing down business.

This guide includes best practices to help you transition from a single-account environment to a multi-account environment. It discusses the decisions you need to make about account migration, user management, networking, security, and architecture. It is designed to help you succeed with minimal or no downtime for your business and daily operations. This guide focuses on the following capabilities as you transition from a single AWS account to a multi-account environment:
+ [Identity management and access control](identity-management.md)
+ [Managing permissions and access](managing-permissions.md)
+ [Network connectivity](network-connectivity.md)
+ [Security incident response](security-incident-response.md)
+ [Backups](backups.md)
+ [Account migration](account-migration.md)
+ [Resource migration](resource-migration.md)
+ [Billing considerations](billing-considerations.md)

For more information about capabilities, see [Cloud Foundation on AWS](framework.md#cloud-foundation-on-aws).

This guide is aligned to existing resources related to this topic, including the [Organizing Your AWS Environment Using Multiple Accounts](https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/organizing-your-aws-environment.html) whitepaper, the [AWS Security Reference Architecture](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/welcome.html) (AWS SRA), and the [Establishing Your Cloud Foundation on AWS](https://docs.aws.amazon.com/whitepapers/latest/establishing-your-cloud-foundation-on-aws/welcome.html) whitepaper. You should continue to use those resources for more specific guidance not covered in this guide.

## Intended audience
<a name="intended-audience"></a>

This guide is best suited for company that wants or needs to transition to multiple AWS accounts. For startups, this need typically arises when you have found product-market fit, raised a round of funding, and are beginning to hire distinct engineering disciplines, such as infrastructure, development operations (DevOps), or security.

Even if your company isn't ready to make this transition, you can still use this guide to understand the decisions that need to be made during the transition and begin to prepare.
