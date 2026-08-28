---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/sqs_example_sqs_ChangeMessageVisibilityBatch_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `ChangeMessageVisibilityBatch` with a CLI
<a name="sqs_example_sqs_ChangeMessageVisibilityBatch_section"></a>

The following code examples show how to use `ChangeMessageVisibilityBatch`.

------
#### [ CLI ]

**AWS CLI**
**To change multiple messages' timeout visibilities as a batch**
This example changes the 2 specified messages' timeout visibilities to 10 hours (10 hours \* 60 minutes \* 60 seconds).
Command:

```
aws sqs change-message-visibility-batch --queue-url {{https://sqs.us-east-1.amazonaws.com/80398EXAMPLE/MyQueue}} --entries {{file://change-message-visibility-batch.json}}
```
Input file (change-message-visibility-batch.json):

```
[
  {
    "Id": "FirstMessage",
        "ReceiptHandle": "AQEBhz2q...Jf3kaw==",
        "VisibilityTimeout": 36000
  },
  {
    "Id": "SecondMessage",
        "ReceiptHandle": "AQEBkTUH...HifSnw==",
        "VisibilityTimeout": 36000
  }
]
```
Output:

```
{
  "Successful": [
    {
      "Id": "SecondMessage"
    },
    {
      "Id": "FirstMessage"
    }
  ]
}
```
+  For API details, see [ChangeMessageVisibilityBatch](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sqs/change-message-visibility-batch.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example changes the visibility timeout for 2 messages with the specified receipt handles in the specified queue. The first message's visibility timeout is changed to 10 hours (10 hours \* 60 minutes \* 60 seconds = 36000 seconds). The second message's visibility timeout is changed to 5 hours (5 hours \* 60 minutes \* 60 seconds = 18000 seconds).**

```
$changeVisibilityRequest1 = New-Object Amazon.SQS.Model.ChangeMessageVisibilityBatchRequestEntry
$changeVisibilityRequest1.Id = "Request1"
$changeVisibilityRequest1.ReceiptHandle = "AQEBd329...v6gl8Q=="
$changeVisibilityRequest1.VisibilityTimeout = 36000

$changeVisibilityRequest2 = New-Object Amazon.SQS.Model.ChangeMessageVisibilityBatchRequestEntry
$changeVisibilityRequest2.Id = "Request2"
$changeVisibilityRequest2.ReceiptHandle = "AQEBgGDh...J/Iqww=="
$changeVisibilityRequest2.VisibilityTimeout = 18000

Edit-SQSMessageVisibilityBatch -QueueUrl https://sqs.us-east-1.amazonaws.com/80398EXAMPLE/MyQueue -Entry $changeVisibilityRequest1, $changeVisibilityRequest2
```
**Output:**

```
Failed    Successful
------    ----------
{}        {Request2, Request1}
```
+  For API details, see [ChangeMessageVisibilityBatch](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example changes the visibility timeout for 2 messages with the specified receipt handles in the specified queue. The first message's visibility timeout is changed to 10 hours (10 hours \* 60 minutes \* 60 seconds = 36000 seconds). The second message's visibility timeout is changed to 5 hours (5 hours \* 60 minutes \* 60 seconds = 18000 seconds).**

```
$changeVisibilityRequest1 = New-Object Amazon.SQS.Model.ChangeMessageVisibilityBatchRequestEntry
$changeVisibilityRequest1.Id = "Request1"
$changeVisibilityRequest1.ReceiptHandle = "AQEBd329...v6gl8Q=="
$changeVisibilityRequest1.VisibilityTimeout = 36000

$changeVisibilityRequest2 = New-Object Amazon.SQS.Model.ChangeMessageVisibilityBatchRequestEntry
$changeVisibilityRequest2.Id = "Request2"
$changeVisibilityRequest2.ReceiptHandle = "AQEBgGDh...J/Iqww=="
$changeVisibilityRequest2.VisibilityTimeout = 18000

Edit-SQSMessageVisibilityBatch -QueueUrl https://sqs.us-east-1.amazonaws.com/80398EXAMPLE/MyQueue -Entry $changeVisibilityRequest1, $changeVisibilityRequest2
```
**Output:**

```
Failed    Successful
------    ----------
{}        {Request2, Request1}
```
+  For API details, see [ChangeMessageVisibilityBatch](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK Code Examples. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query code-library` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
