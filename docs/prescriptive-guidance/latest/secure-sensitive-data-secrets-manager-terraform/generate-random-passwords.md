---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/secure-sensitive-data-secrets-manager-terraform/generate-random-passwords.html
---

# Generating random passwords by using AWS Secrets Manager
<a name="generate-random-passwords"></a>

The AWS Well-Architected Framework recommends that you [store and use secrets securely](https://docs.aws.amazon.com/wellarchitected/latest/framework/sec_identities_secrets.html). You can use the AWS Secrets Manager API to generate random passwords, and you can customize the password complexity requirements. The `GetRandomPassword` action supports password string lengths between 1 and 4,096 characters. For more information, see [GetRandomPassword](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetRandomPassword.html) in the *AWS Secrets Manager API Reference*. We recommend that you use this approach to generate secrets instead of allowing users to manually define secrets.

The following code sample shows how you can generate random passwords that are 20 characters long and that include numbers, exclude punctuation characters, and exclude spaces. You can modify this code example to meet the password security requirements for your organization.

```
data "aws_secretsmanager_random_password" "test" {
password_length = 20
exclude_numbers = false
exclude_punctuation = true
include_space = false
}
```

Using random secrets generation when you deploy IaC help you protect sensitive data from the very start, known as *zero hours*. The sensitive data is never known to anyone, right from the deployment phase.

![Terraform using AWS Secrets Manager to create and use a random secret.](http://docs.aws.amazon.com/prescriptive-guidance/latest/secure-sensitive-data-secrets-manager-terraform/images/guide-img/e6185df2-3707-4018-a94c-6edc793f0353/images/3b1be47e-430d-4226-a46c-76070a44636b.png)

1. Through Terraform, use AWS Secrets Manager to generate a random password secret.

1. Terraform uses this random password secret, which is stored in AWS Secrets Manager, to access the database.

**Important**
When you use Terraform as a data source, secrets are not stored in the [state file](https://developer.hashicorp.com/terraform/language/state). But after you use that secret in a database or any service, then it is stored in the state file. We recommend that you rotate the secrets immediately or create very restrictive permissions to access the state file. For more information, see [Protecting sensitive data in the Terraform state file](terraform-state-file.md) in this guide.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
