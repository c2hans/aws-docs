---
source_url: https://docs.aws.amazon.com/drs/latest/userguide/security-iam-awsmanpol-AWSElasticDisasterRecoveryReplicationServerPolicy.html
---

# AWS managed policy: AWSElasticDisasterRecoveryReplicationServerPolicy
<a name="security-iam-awsmanpol-AWSElasticDisasterRecoveryReplicationServerPolicy"></a>

This policy is attached to the AWS Elastic Disaster Recovery replication server’s instance role.

This policy allows the AWS Elastic Disaster Recovery (AWS DRS) replication servers, which are Amazon EC2 instances launched by Elastic Disaster Recovery, to communicate with the DRS service, and to create EBS snapshots in your AWS account. An IAM role with this policy is attached (as an EC2 instance profile) by AWS DRS to the AWS DRS replication servers which are automatically launched and terminated by AWS DRS, as needed. AWS DRS replication servers are used to facilitate data replication from your external servers to AWS, as part of the recovery process managed by AWS DRS. We do not recommend that you attach this policy to your users or roles.

 **Permissions details**

To view the policy permission details see [AWSElasticDisasterRecoveryReplicationServerPolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSElasticDisasterRecoveryReplicationServerPolicy.html) in the AWS Managed Policy Reference Guide.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elastic Disaster Recovery. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query drs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
