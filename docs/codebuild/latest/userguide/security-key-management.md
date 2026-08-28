---
source_url: https://docs.aws.amazon.com/codebuild/latest/userguide/security-key-management.html
---

# Key management
<a name="security-key-management"></a>

You can protect your content from unauthorized use through encryption. Store your encryption keys in AWS Secrets Manager, and then give the CodeBuild service role associated with the build project permission to obtain the encryption keys from your Secrets Manager account. For more information, see [Encrypt build outputs using a customer managed key](setting-up-kms.md), [Create a build project in AWS CodeBuild](create-project.md), [Run AWS CodeBuild builds manually](run-build.md), and [Tutorial: Storing and retrieving a secret](https://docs.aws.amazon.com/secretsmanager/latest/userguide/tutorials_basic.html).

Use the `CODEBUILD_KMS_KEY_ID` environment variable in a build command to obtain the AWS KMS key identifier. For more information, see [Environment variables in build environments](build-env-ref-env-vars.md).

You can use Secrets Manager to protect credentials to a private registry that stores a Docker image used for your runtime environment. For more information, see [Private registry with AWS Secrets Manager sample for CodeBuild](sample-private-registry.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeBuild. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codebuild` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
