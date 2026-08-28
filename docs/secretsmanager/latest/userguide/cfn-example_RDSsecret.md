---
source_url: https://docs.aws.amazon.com/secretsmanager/latest/userguide/cfn-example_RDSsecret.html
---

# Create an AWS Secrets Manager secret with automatic rotation and an Amazon RDS MySQL DB instance with CloudFormation
<a name="cfn-example_RDSsecret"></a>

To create an admin secret for Amazon RDS or Aurora, we recommend you use `ManageMasterUserPassword`, as shown in the example *Create a Secrets Manager secret for a master password* in [`AWS::RDS::DBCluster`](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbcluster.html). Then Amazon RDS creates the secret and manages rotation for you. For more information, see [Managed rotation](rotate-secrets_managed.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Secrets Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query secretsmanager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
