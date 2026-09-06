---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/sqs_example_sqs_AddPermission_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `AddPermission` with a CLI
<a name="sqs_example_sqs_AddPermission_section"></a>

The following code examples show how to use `AddPermission`.

------
#### [ CLI ]

**AWS CLI**
**To add a permission to a queue**
This example enables the specified AWS account to send messages to the specified queue.
Command:

```
aws sqs add-permission --queue-url {{https://sqs.us-east-1.amazonaws.com/80398EXAMPLE/MyQueue}} --label {{SendMessagesFromMyQueue}} --aws-account-ids {{12345EXAMPLE}} --actions {{SendMessage}}
```
Output:

```
None.
```
+  For API details, see [AddPermission](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sqs/add-permission.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example allows the specified AWS account to send messages from the specified queue.**

```
Add-SQSPermission -Action SendMessage -AWSAccountId 80398EXAMPLE -Label SendMessagesFromMyQueue -QueueUrl https://sqs.us-east-1.amazonaws.com/80398EXAMPLE/MyQueue
```
+  For API details, see [AddPermission](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example allows the specified AWS account to send messages from the specified queue.**

```
Add-SQSPermission -Action SendMessage -AWSAccountId 80398EXAMPLE -Label SendMessagesFromMyQueue -QueueUrl https://sqs.us-east-1.amazonaws.com/80398EXAMPLE/MyQueue
```
+  For API details, see [AddPermission](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------
