---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/secure-sensitive-data-secrets-manager-terraform/limiting-access.html
---

# Limiting access to secrets
<a name="limiting-access"></a>

Security is the top priority at AWS. In the AWS Well-Architected Framework, the [Store and use secrets securely](https://docs.aws.amazon.com/wellarchitected/latest/framework/sec_identities_secrets.html) best practice recommends that you limit access to secrets, log and audit access to secrets, and that you get access through an API instead of granting access to a person. This is related to [Generating random passwords by using AWS Secrets Manager](generate-random-passwords.md), previously discussed in this guide.

In the past, credentials used to authenticate to databases, third-party APIs, tokens, and other secrets might have been embedded in source code or in environment files. In many organizations, database administrators still can access all database user credentials. However, it's more secure if they don't. We recommend that you:
+ Limit access to Secrets Manager through an AWS Identity and Access Management (IAM) policy that is attached to an [AWS service role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-service.html) or to an [IAM role for users](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-user.html).
+ Extend programmatic access to secrets in Secrets Manager only through API calls to Secrets Manager.
+ Avoid using hard-coded secrets.
+ Don't pass credential values in variables.
+ Make sure that secrets are directly used by the application or infrastructure, rather than by a human user.

The following code sample shows an approach you can use to protect sensitive data when creating a database. When you create the database, you can require user input as a password and then rotate the password, or you can use a random password from the start. Generating a random password from the start can help you more securely handle and manage credentials.

The following code snippet creates a database resource, and `password = local.passwddata` fetches the password from a local variable.

```
resource "aws_db_instance" "default" {
  count                  = var.createdb == true ? 1 : 0
  allocated_storage      = 20
  identifier             = var.identifier
  db_name                = var.databasename
  engine                 = "mysql"
  engine_version         = "8.0.32"
  instance_class         = "db.t3.micro"
  username               = "admin"
  password               = local.passwddata
  skip_final_snapshot    = true
  publicly_accessible    = false
  vpc_security_group_ids = [aws_security_group.db.id]
  db_subnet_group_name   = aws_db_subnet_group.db.0.name
}
```

The following code snippet creates a random password or accepts the user-provided password. Terraform stores this password as a local variable so that you can use this password variable later in the code.

```
locals {
  passwddata = var.passwddata != null ? var.passwddata : data.aws_secretsmanager_random_password.test.random_secrets
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
