---
source_url: https://docs.aws.amazon.com/streams/latest/dev/tutorial-stock-data-lambda.html
---

# Tutorial: Use AWS Lambda with Amazon Kinesis Data Streams
<a name="tutorial-stock-data-lambda"></a>

In this tutorial, you create a Lambda function to consume events from a Kinesis data stream. In this example scenario, a custom application writes records to a Kinesis data stream. AWS Lambda then polls this data stream and, when it detects new data records, invokes your Lambda function. AWS Lambda then executes the Lambda function by assuming the execution role that you specified when you created the Lambda function.

For the detailed step by step instructions, see [Tutorial: Using AWS Lambda with Amazon Kinesis](https://docs.aws.amazon.com/lambda/latest/dg/with-kinesis-example.html).

**Note**
This tutorial assumes that you have some knowledge of basic Lambda operations and the AWS Lambda console. If you haven't already, follow the instructions in [Getting Started with AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/getting-started.html) to create your first Lambda function.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Kinesis Streams. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query streams` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
