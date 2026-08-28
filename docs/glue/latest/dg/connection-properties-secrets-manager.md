---
source_url: https://docs.aws.amazon.com/glue/latest/dg/connection-properties-secrets-manager.html
---

# Storing connection credentials in AWS Secrets Manager
<a name="connection-properties-secrets-manager"></a>

We recommend that you use AWS Secrets Manager to supply connection credentials for your data store. Using Secrets Manager this way lets AWS Glue access your secret at runtime for ETL jobs and crawler runs, and helps keep your credentials secure.

**Prerequisites**

To use Secrets Manager with AWS Glue, you must grant your [IAM role for AWS Glue](create-an-iam-role.md) permission to retrieve secret values. The AWS managed policy `AWSGlueServiceRole` doesn't include AWS Secrets Manager permissions. For example IAM policies, see [Example: Permission to retrieve secret values](https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access_examples.html#auth-and-access_examples_read) in the *AWS Secrets Manager* *User Guide.*

Depending on your network setup, you might also need to create a VPC endpoint to establish a private connection between your VPC and Secrets Manager. For more information, see [Using an AWS Secrets Manager VPC endpoint](https://docs.aws.amazon.com/secretsmanager/latest/userguide/vpc-endpoint-overview.html).

**To create a secret for AWS Glue**

1. Follow the instructions in [Create and manage secrets](https://docs.aws.amazon.com/secretsmanager/latest/userguide/managing-secrets.html) in the *AWS Secrets Manager User Guide*. The following example JSON shows how to specify your credentials in the **Plaintext** tab when you create a secret for AWS Glue.

   ```
   {
     "username": "EXAMPLE-USERNAME",
     "password": "EXAMPLE-PASSWORD"
   }
   ```

1. Associate your secret with a connection using the AWS Glue Studio interface. For detailed instructions, see [Creating connections for connectors](https://docs.aws.amazon.com/glue/latest/ug/connectors-chapter.html#creating-connections) in the *AWS Glue Studio User Guide.*

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
