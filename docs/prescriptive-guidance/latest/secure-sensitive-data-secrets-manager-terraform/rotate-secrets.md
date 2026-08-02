---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/secure-sensitive-data-secrets-manager-terraform/rotate-secrets.html
---

# Using AWS Lambda to rotate secrets
<a name="rotate-secrets"></a>

The AWS Well-Architected Framework recommends that you [store and use secrets securely](https://docs.aws.amazon.com/wellarchitected/latest/framework/sec_identities_secrets.html). This best practice recommends that you automate the rotation of credentials at regular intervals. *Rotation* is the process of periodically updating a secret to make it more difficult for an attacker to access the credentials. Many compliance frameworks and regulations also require that you rotate secrets.

For Terraform IaC, you can use AWS Secrets Manager and [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) to establish automated rotation. In Secrets Manager, you can set up automatic rotation for your secrets. When Secrets Manager rotates a secret, it updates the credentials in both the secret and the database or service.

For databases, we recommend that you manage the primary credentials in Secrets Manager and rotate the secrets at a regular interval. Secrets Manager provides rotation function templates for Lambda for several types of database credentials. For more information, see [AWS Secrets Manager rotation function templates](https://docs.aws.amazon.com/secretsmanager/latest/userguide/reference_available-rotation-templates.html) in the Secrets Manager documentation and see the [code samples](https://github.com/aws-samples/aws-secrets-manager-rotation-lambdas/blob/master/README.md) in GitHub. The following is an example of a Terraform IaC that you can use to rotate secrets or sensitive data.

```
resource "aws_secretsmanager_secret_rotation" "createrotation" {
  count               = var.needrotation == true ? 1 : 0
  secret_id           = aws_secretsmanager_secret.initiatesecret.id
  rotation_lambda_arn = aws_lambda_function.rotationlambda.arn

  rotation_rules {
    automatically_after_days = 1
  }
}
```

The following architecture diagram shows how you can use Secrets Manager, an Amazon VPC endpoint, and a Lambda function to rotate sensitive data in an AWS account.

![Automatically schedule an AWS Lambda function that rotates secrets on a regular schedule.](http://docs.aws.amazon.com/prescriptive-guidance/latest/secure-sensitive-data-secrets-manager-terraform/images/guide-img/e6185df2-3707-4018-a94c-6edc793f0353/images/37a32a01-6350-41b2-a7fb-2e54fa1c45dc.png)
