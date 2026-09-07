---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/transitioning-to-multiple-aws-accounts/targeted-business-outcomes.html
---

# Objectives
<a name="targeted-business-outcomes"></a>

The transition to a multi-account architecture is usually driven by a business need for one or more of the following benefits:
+ Grouping workloads based on business purpose or ownership
+ Applying distinct security controls by environment
+ Constraining access to sensitive data
+ Promoting innovation and agility
+ Limiting scope of impact from adverse events
+ Supporting multiple IT operating models
+ Managing costs
+ Distributing AWS service quotas and API request rate limits

For more information about the many benefits of using a multi-account architecture, see [Organizing Your AWS Environment Using Multiple Accounts](https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/benefits-of-using-multiple-aws-accounts.html) (AWS whitepaper) and [Guidelines to set up a well-architected environment](https://docs.aws.amazon.com/controltower/latest/userguide/aws-multi-account-landing-zone.html#guidelines-for-multi-account-setup) (AWS Control Tower documentation).

## Sample single-account architecture
<a name="sample-architecture"></a>

As a starting point, it is common for startup or small companies to use a single AWS Region and have two virtual private clouds (VPCs) that are connected by [VPC peering](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-peering.html). Each VPC contains compute resources, such as Amazon Elastic Compute Cloud (Amazon EC2) instances. The engineering team develops code directly in the **Development VPC**. The product team reviews the changes, and then the engineering team manually promotes the changes to the **Production VPC**. The finance team has access to the AWS account so they can review the AWS Billing and Cost Management console.

![](https://docs.aws.amazon.com/prescriptive-guidance/latest/transitioning-to-multiple-aws-accounts/images/guide-img/b35f7443-fbaf-4ce8-bb48-32b6441d573f/images/743baaf6-1cf2-493c-9cb4-6ffedff927eb.png)

The following are a few examples of challenges that a company might experience with this environment:
+ An engineer mistakenly deleted production data when they thought they were accessing a development database.
+ A sales demo was impacted when a production deployment took longer than expected.
+ When development code was being load tested, the **Production VPC** became slow and generated error messages about throttling.
+ The finance team can't differentiate costs for production and development environments.
+ The CEO is concerned that some newly hired offshore contractors have access to customer data though the **Production VPC**.
+ The finance team can't disallow access to specific AWS services that might incur high costs.

Adopting a multi-account strategy addresses all of these challenges by using compartmentalized AWS accounts to separate workloads and access.
