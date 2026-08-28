---
source_url: https://docs.aws.amazon.com/gameliftstreams/latest/developerguide/session-credentials.html
---

# Provide AWS credentials to your streaming application
<a name="session-credentials"></a>

By default, applications running on Amazon GameLift Streams do not have access to AWS resources in your account. If your application needs to call AWS APIs — for example, to read from your Amazon S3 buckets, write to your DynamoDB tables, or publish metrics to CloudWatch — you can provide an IAM role when starting a stream session. Amazon GameLift Streams assumes the role on your behalf and makes credentials available to your application. You do not need to change your application code.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GameLift Streams. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query gameliftstreams` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
