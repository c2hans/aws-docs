---
source_url: https://docs.aws.amazon.com/mwaa/latest/mwaa-serverless-userguide/security-best-practices.html
---

# Security best practices on Amazon MWAA Serverless
<a name="security-best-practices"></a>

Amazon MWAA Serverless provides a number of security features to consider as you develop and implement your own security policies. The following best practices are general guidelines and don’t represent a complete security solution. Because these best practices might not be appropriate or sufficient for your workflow, treat them as helpful considerations rather than prescriptions.
+ Use least-permissive permission policies. Grant permissions to only the resources or actions that users need to perform tasks.
+ Use AWS CloudTrail to monitor user activity in your account.

## Security best practices in Apache Airflow
<a name="security-best-practices-for-airflow"></a>

To implement security boundaries for your workflows:
+ Store secrets in AWS Secrets Manager. While this will not prevent users who can write workflow definitions from reading secrets, it prevents them from modifying the secrets that your workflow uses.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Workflows for Apache Airflow Serverless. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mwaa` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
