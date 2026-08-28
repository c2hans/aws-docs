---
source_url: https://docs.aws.amazon.com/mgn/latest/ug/security-iam-awsmanpol-AWSApplicationMigrationReadOnlyAccess.html
---

NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](https://docs.aws.amazon.com/transform/latest/userguide/getting-started.html) in the *AWS Transform User Guide*.

# AWS managed policy: AWSApplicationMigrationReadOnlyAccess
<a name="security-iam-awsmanpol-AWSApplicationMigrationReadOnlyAccess"></a>

You can attach the `AWSApplicationMigrationReadOnlyAccess` policy to your IAM identities.

This policy provides permissions to all read-only public APIs of AWS Transform MGN, as well as some read-only APIs of other AWS services that are required in order to make full read-only use of the MGN console. It does not allow them to perform any actions, such as initialize the service, replicate servers, or launch servers in AWS. This policy can be granted to a user in a support role.

 Attach this policy to your users or roles.

 **Permissions details**

To view the policy permission details see [AWSApplicationMigrationReadOnlyAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSApplicationMigrationReadOnlyAccess.html) in the AWS Managed Policy Reference Guide.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Transform MGN. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mgn` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
