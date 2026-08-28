---
source_url: https://docs.aws.amazon.com/batch/latest/userguide/specifying-sensitive-data.html
---

# Specify sensitive data
<a name="specifying-sensitive-data"></a>

With AWS Batch, you can inject sensitive data into your jobs by storing your sensitive data in either AWS Secrets Manager secrets or AWS Systems Manager Parameter Store parameters, and then reference them in your job definition.

Secrets can be exposed to a job in the following ways:
+ To inject sensitive data into your containers as environment variables, use the `secrets` job definition parameter.
+ To reference sensitive information in the log configuration of a job, use the `secretOptions` job definition parameter.

**Topics**
+ [Specify sensitive data with Secrets Manager](specifying-sensitive-data-secrets.md)
+ [Specify sensitive data with Systems Manager Parameter Store](specifying-sensitive-data-parameters.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Batch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query batch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
