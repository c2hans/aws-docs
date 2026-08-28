---
source_url: https://docs.aws.amazon.com/lexv2/latest/dg/conversation-logs-s3.html
---

# Accessing audio logs in Amazon S3
<a name="conversation-logs-s3"></a>

Amazon Lex V2 stores audio logs for your conversations in an S3 bucket.

You can use the Amazon S3 console or API to access audio logs. You can see the S3 object key prefix of the audio files in the Amazon Lex V2 console, or in the `conversationLogSettings` field in the `DescribeBotAlias` operation response.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lex. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lexv2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
