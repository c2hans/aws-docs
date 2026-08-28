---
source_url: https://docs.aws.amazon.com/drs/latest/userguide/security-iam-awsmanpol-AWSElasticDisasterRecoveryRecoveryInstancePolicy.html
---

# AWS managed policy: AWSElasticDisasterRecoveryRecoveryInstancePolicy
<a name="security-iam-awsmanpol-AWSElasticDisasterRecoveryRecoveryInstancePolicy"></a>

This policy is attached to the instance role of AWS Elastic Disaster Recovery's recovery instance.

This policy allows the AWS Elastic Disaster Recovery (AWS DRS) recovery instances, which are EC2 instances launched by AWS DRS - to communicate with the AWS DRS service, and to be able to failback to their original source infrastructure. An IAM role with this policy is attached (as an Amazon EC2 Instance Profile) by AWS DRS to the AWS DRS recovery instances. We do not recommend that you attach this policy to your users or roles.

 **Permissions details**

To view the policy permission details see [AWSElasticDisasterRecoveryRecoveryInstancePolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSElasticDisasterRecoveryRecoveryInstancePolicy.html) in the AWS Managed Policy Reference Guide.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elastic Disaster Recovery. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query drs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
