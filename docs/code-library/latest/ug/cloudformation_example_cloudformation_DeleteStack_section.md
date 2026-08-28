---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/cloudformation_example_cloudformation_DeleteStack_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `DeleteStack` with a CLI
<a name="cloudformation_example_cloudformation_DeleteStack_section"></a>

The following code examples show how to use `DeleteStack`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in context in the following code examples:
+  [Creating your first infrastructure stack](cloudformation_example_cloudformation_GettingStarted_021_section.md)
+  [Getting started with managed kubernetes clusters](cloudformation_example_eks_GettingStarted_034_section.md)

------
#### [ CLI ]

**AWS CLI**
**To delete a stack**
The following `delete-stack` example deletes the specified stack.

```
aws cloudformation delete-stack \
    --stack-name {{my-stack}}
```
This command produces no output.
+  For API details, see [DeleteStack](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/delete-stack.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: Deletes the specified stack.**

```
Remove-CFNStack -StackName "myStack"
```
+  For API details, see [DeleteStack](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: Deletes the specified stack.**

```
Remove-CFNStack -StackName "myStack"
```
+  For API details, see [DeleteStack](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK Code Examples. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query code-library` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
