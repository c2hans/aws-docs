---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/sqs_example_sqs_RemovePermission_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `RemovePermission` with a CLI
<a name="sqs_example_sqs_RemovePermission_section"></a>

The following code examples show how to use `RemovePermission`.

------
#### [ CLI ]

**AWS CLI**
**To remove a permission**
This example removes the permission with the specified label from the specified queue.
Command:

```
aws sqs remove-permission --queue-url {{https://sqs.us-east-1.amazonaws.com/80398EXAMPLE/MyQueue}} --label {{SendMessagesFromMyQueue}}
```
Output:

```
None.
```
+  For API details, see [RemovePermission](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sqs/remove-permission.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example removes the permission settings with the specified label from the specified queue.**

```
Remove-SQSPermission -Label SendMessagesFromMyQueue -QueueUrl https://sqs.us-east-1.amazonaws.com/80398EXAMPLE/MyQueue
```
+  For API details, see [RemovePermission](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example removes the permission settings with the specified label from the specified queue.**

```
Remove-SQSPermission -Label SendMessagesFromMyQueue -QueueUrl https://sqs.us-east-1.amazonaws.com/80398EXAMPLE/MyQueue
```
+  For API details, see [RemovePermission](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------
