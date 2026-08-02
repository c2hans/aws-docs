---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/sqs_example_sqs_ListDeadLetterSourceQueues_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `ListDeadLetterSourceQueues` with a CLI
<a name="sqs_example_sqs_ListDeadLetterSourceQueues_section"></a>

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
