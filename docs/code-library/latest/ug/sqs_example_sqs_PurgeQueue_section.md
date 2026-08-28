---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/sqs_example_sqs_PurgeQueue_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `PurgeQueue` with a CLI
<a name="sqs_example_sqs_PurgeQueue_section"></a>

The following code examples show how to use `PurgeQueue`.

------
#### [ CLI ]

**AWS CLI**
**To purge a queue**
This example deletes all messages in the specified queue.
Command:

```
aws sqs purge-queue --queue-url {{https://sqs.us-east-1.amazonaws.com/80398EXAMPLE/MyNewQueue}}
```
Output:

```
None.
```
+  For API details, see [PurgeQueue](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sqs/purge-queue.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example deletes all messages from the specified queue.**

```
Clear-SQSQueue -QueueUrl https://sqs.us-east-1.amazonaws.com/80398EXAMPLE/MyQueue
```
+  For API details, see [PurgeQueue](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example deletes all messages from the specified queue.**

```
Clear-SQSQueue -QueueUrl https://sqs.us-east-1.amazonaws.com/80398EXAMPLE/MyQueue
```
+  For API details, see [PurgeQueue](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK Code Examples. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query code-library` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
