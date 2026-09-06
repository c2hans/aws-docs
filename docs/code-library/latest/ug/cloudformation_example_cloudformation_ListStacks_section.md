---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/cloudformation_example_cloudformation_ListStacks_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `ListStacks` with a CLI
<a name="cloudformation_example_cloudformation_ListStacks_section"></a>

The following code examples show how to use `ListStacks`.

------
#### [ CLI ]

**AWS CLI**
**To list AWS CloudFormation stacks**
The following `list-stacks` command shows a summary of all stacks that have a status of `CREATE_COMPLETE`:

```
aws cloudformation list-stacks --stack-status-filter {{CREATE_COMPLETE}}
```
Output:

```
[
    {
        "StackId": "arn:aws:cloudformation:us-east-1:123456789012:stack/myteststack/466df9e0-0dff-08e3-8e2f-5088487c4896",
        "TemplateDescription": "AWS CloudFormation Sample Template S3_Bucket: Sample template showing how to create a publicly accessible S3 bucket. **WARNING** This template creates an S3 bucket. You will be billed for the AWS resources used if you create a stack from this template.",
        "StackStatusReason": null,
        "CreationTime": "2013-08-26T03:27:10.190Z",
        "StackName": "myteststack",
        "StackStatus": "CREATE_COMPLETE"
    }
]
```
+  For API details, see [ListStacks](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/list-stacks.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: Returns summary information for all stacks.**

```
Get-CFNStackSummary
```
**Example 2: Returns summary information for all stacks that are currently being created.**

```
Get-CFNStackSummary -StackStatusFilter "CREATE_IN_PROGRESS"
```
**Example 3: Returns summary information for all stacks that are currently being created or updated.**

```
Get-CFNStackSummary -StackStatusFilter @("CREATE_IN_PROGRESS", "UPDATE_IN_PROGRESS")
```
+  For API details, see [ListStacks](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: Returns summary information for all stacks.**

```
Get-CFNStackSummary
```
**Example 2: Returns summary information for all stacks that are currently being created.**

```
Get-CFNStackSummary -StackStatusFilter "CREATE_IN_PROGRESS"
```
**Example 3: Returns summary information for all stacks that are currently being created or updated.**

```
Get-CFNStackSummary -StackStatusFilter @("CREATE_IN_PROGRESS", "UPDATE_IN_PROGRESS")
```
+  For API details, see [ListStacks](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------
