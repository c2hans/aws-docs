---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/account-structure.html
---

# AWS organization and account structure of the AWS SRA
<a name="account-structure"></a>

The following diagram captures the high-level structure of the AWS SRA without displaying specific services. It reflects the dedicated accounts structure discussed in the previous section, and we include the diagram here to orient the discussion around the primary components of the architecture:
+ All accounts that are shown in the diagram are part of a single AWS organization.
+ At the upper left of the diagram is the Org Management account, which is used to create the AWS organization.
+ Below the Org Management account is the Security OU with two specific accounts: one for Security Tooling and the other for Log Archive.
+ Along the right side is the Infrastructure OU with the Network account and Shared Services account.
+ At the bottom of the diagram is the Workloads OU, which is associated with an Application account that houses the enterprise application.

For this guidance, all accounts are considered production (prod) accounts that operate in a single AWS Region. Most AWS services (except for [global services](https://docs.aws.amazon.com/whitepapers/latest/aws-fault-isolation-boundaries/global-services.html)) are regionally scoped, which means that the control and data planes for the service exist independently in each AWS Region. For this reason, you must replicate this architecture across all AWS Regions that you plan to use, to ensure coverage for your entire AWS landscape. If you don't have any workloads in a specific AWS Region, you should disable the Region by using [SCPs](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps_examples_general.html#example-scp-deny-region) or by using logging and monitoring mechanisms. You can use Security Hub CSPM to aggregate findings and security scores from multiple AWS Regions to a single aggregation Region for centralized visibility.

When hosting an AWS organization with a large set of accounts, it's beneficial to have an orchestration layer that facilitates account deployment and account governance. AWS Control Tower offers a straightforward way to set up and govern an AWS multi-account environment. The AWS SRA code samples in the [GitHub repository](https://github.com/aws-samples/aws-security-reference-architecture-examples) demonstrate how you can use the [Customizations for AWS Control Tower (CfCT)](https://aws.amazon.com/solutions/implementations/customizations-for-aws-control-tower/) solution to deploy AWS SRA recommended structures.

![High-level structure of the AWS SRA (without services).](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/images/guide-img/91d313fc-d5f1-45a8-a5a6-2f4fc7abc93a/images/de6cd2fe-0a9a-4c78-81c5-b6d8fb3c891d.png)
