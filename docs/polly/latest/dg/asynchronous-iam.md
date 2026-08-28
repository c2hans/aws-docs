---
source_url: https://docs.aws.amazon.com/polly/latest/dg/asynchronous-iam.html
---

# Setting up the IAM policy for asynchronous synthesis
<a name="asynchronous-iam"></a>

In order to use the asynchronous synthesis functionality, you will need an IAM policy that allows the following:
+ use of new Amazon Polly operations
+ writing to the output S3 bucket
+ publishing to the status SNS topic [optional]

The following policy grants only the necessary permissions required for asynchronous synthesis and can be attached to the IAM user.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Polly. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query polly` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
