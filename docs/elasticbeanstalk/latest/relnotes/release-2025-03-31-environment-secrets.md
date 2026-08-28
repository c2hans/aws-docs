---
source_url: https://docs.aws.amazon.com/elasticbeanstalk/latest/relnotes/release-2025-03-31-environment-secrets.html
---

# Release: Elastic Beanstalk supports retrieving secrets and configuration from AWS Secrets Manager and AWS Systems Manager on March 31, 2025
<a name="release-2025-03-31-environment-secrets"></a>

AWS Elastic Beanstalk adds support for accessing secrets and configuration from AWS Secrets Manager and AWS Systems Manager with environment variables.

**Release date:** March 31, 2025

## Changes
<a name="release-2025-03-31-environment-secrets.changes"></a>

Elastic Beanstalk now offers the ability to reference AWS Systems Manager Parameter Store or AWS Secrets Manager secrets in environment variables.

This new integration eliminates the need for your application to make Systems Manager or Secrets Manager API calls to retrieve sensitive data, since it can access the data natively with environment variables.

This feature is available in all commercial AWS Regions where Elastic Beanstalk is available, including AWS GovCloud (US) Regions.

For more information, see [Using Elastic Beanstalk with Secrets Manager and Systems Manager Parameter Store](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/AWSHowTo.secrets.html) in the *AWS Elastic Beanstalk Developer Guide*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elastic Beanstalk. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elasticbeanstalk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
