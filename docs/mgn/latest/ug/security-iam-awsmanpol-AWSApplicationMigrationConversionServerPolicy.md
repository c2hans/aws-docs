---
source_url: https://docs.aws.amazon.com/mgn/latest/ug/security-iam-awsmanpol-AWSApplicationMigrationConversionServerPolicy.html
---

NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](https://docs.aws.amazon.com/transform/latest/userguide/getting-started.html) in the *AWS Transform User Guide*.

# AWS managed policy: AWSApplicationMigrationConversionServerPolicy
<a name="security-iam-awsmanpol-AWSApplicationMigrationConversionServerPolicy"></a>

This policy is attached to the AWS Transform MGN conversion server’s instance role.

This policy allows the AWS Transform MGN conversion servers, which are EC2 instances launched by AWS Transform MGN, to communicate with the MGN service. An IAM role with this policy is attached (as an EC2 Instance Profile) by MGN to the MGN Conversion Servers, which are automatically launched and terminated by MGN, when needed. We do not recommend that you attach this policy to your users or roles. MGN conversion servers are used by AWS Transform MGN when users choose to launch test or cutover instances using the MGN console, CLI, or API.

 **Permissions details**

To view the policy permission details see [AWSApplicationMigrationConversionServerPolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSApplicationMigrationConversionServerPolicy.html) in the AWS Managed Policy Reference Guide.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Transform MGN. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mgn` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
