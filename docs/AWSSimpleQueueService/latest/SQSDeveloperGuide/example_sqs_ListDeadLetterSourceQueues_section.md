---
source_url: https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/example_sqs_ListDeadLetterSourceQueues_section.html
---

# Use `ListDeadLetterSourceQueues` with a CLI
<a name="example_sqs_ListDeadLetterSourceQueues_section"></a>

The following code examples show how to use `ListDeadLetterSourceQueues`.

------
#### [ CLI ]

**AWS CLI**
**To list dead letter source queues**
This example lists the queues that are associated with the specified dead letter source queue.
Command:

```
aws sqs list-dead-letter-source-queues --queue-url {{https://sqs.us-east-1.amazonaws.com/80398EXAMPLE/MyDeadLetterQueue}}
```
Output:

```
{
  "queueUrls": [
    "https://queue.amazonaws.com/80398EXAMPLE/MyQueue",
    "https://queue.amazonaws.com/80398EXAMPLE/MyOtherQueue"
  ]
}
```
+  For API details, see [ListDeadLetterSourceQueues](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sqs/list-dead-letter-source-queues.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example lists the URLs of any queues that rely on the specified queue as their dead letter queue.**

```
Get-SQSDeadLetterSourceQueue -QueueUrl https://sqs.us-east-1.amazonaws.com/80398EXAMPLE/MyDeadLetterQueue
```
**Output:**

```
https://sqs.us-east-1.amazonaws.com/80398EXAMPLE/MyQueue
https://sqs.us-east-1.amazonaws.com/80398EXAMPLE/MyOtherQueue
```
+  For API details, see [ListDeadLetterSourceQueues](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example lists the URLs of any queues that rely on the specified queue as their dead letter queue.**

```
Get-SQSDeadLetterSourceQueue -QueueUrl https://sqs.us-east-1.amazonaws.com/80398EXAMPLE/MyDeadLetterQueue
```
**Output:**

```
https://sqs.us-east-1.amazonaws.com/80398EXAMPLE/MyQueue
https://sqs.us-east-1.amazonaws.com/80398EXAMPLE/MyOtherQueue
```
+  For API details, see [ListDeadLetterSourceQueues](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------

For a complete list of AWS SDK developer guides and code examples, see [Using Amazon SQS with an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Queue Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSSimpleQueueService` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
