---
source_url: https://docs.aws.amazon.com/solutions/latest/video-on-demand-on-aws/error-handling.html
---

# Error handling
<a name="error-handling"></a>

The ingest, processing, and publishing workflow AWS Lambda functions, and Amazon CloudWatch Events are configured to invoke an *error handler* Lambda function that updates the Amazon DynamoDB table with error message details, and sends an Amazon Simple Notification Service (Amazon SNS) notification to a subscribed email address.

 **Video on demand solution error handling overview**

![video on demand error handling](http://docs.aws.amazon.com/solutions/latest/video-on-demand-on-aws/images/video-on-demand-error-handling.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Video on Demand on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
