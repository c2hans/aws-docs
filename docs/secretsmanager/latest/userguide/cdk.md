---
source_url: https://docs.aws.amazon.com/secretsmanager/latest/userguide/cdk.html
---

# Create AWS Secrets Manager secrets in AWS Cloud Development Kit (AWS CDK)
<a name="cdk"></a>

To create, manage, and retrieve secrets in a CDK app, you can use the [AWS Secrets Manager Construct Library](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_secretsmanager-readme.html), which contains [`ResourcePolicy`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_secretsmanager.ResourcePolicy.html), [`RotationSchedule`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_secretsmanager.RotationSchedule.html), [`Secret`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_secretsmanager.Secret.html), [`SecretRotation`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_secretsmanager.SecretRotation.html), and [`SecretTargetAttachment`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_secretsmanager.SecretTargetAttachment.html) constructs.

A good practice for using secrets in CDK applications is to first [create the secret by using console or the CLI](create_secret.md), and then import the secret into your CDK application.

For examples, see:
+ [Create a secret](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_secretsmanager-readme.html#creating-json-secrets)
+ [Import a secret](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_secretsmanager-readme.html#importing-secrets)
+ [Retrieve a secret](https://docs.aws.amazon.com/cdk/v2/guide/get-secrets-manager-value.html)
+ [Grant permission to use the secret](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_secretsmanager-readme.html#grant-permission-to-use-the-secret-to-a-role)
+ [Rotate a secret ](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_secretsmanager-readme.html#rotating-a-secret)
+ [Rotate a database secret](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_secretsmanager-readme.html#rotating-database-credentials)
+ [Replicate a secret to other Regions](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_secretsmanager-readme.html#replicating-secrets)

For more information about the CDK, see the [AWS Cloud Development Kit (AWS CDK) v2 Developer Guide](https://docs.aws.amazon.com/cdk/v2/guide/home.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Secrets Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query secretsmanager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
