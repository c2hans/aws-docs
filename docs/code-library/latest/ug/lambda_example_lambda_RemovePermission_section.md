---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/lambda_example_lambda_RemovePermission_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `RemovePermission` with a CLI
<a name="lambda_example_lambda_RemovePermission_section"></a>

The following code examples show how to use `RemovePermission`.

------
#### [ CLI ]

**AWS CLI**
**To remove permissions from an existing Lambda function**
The following `remove-permission` example removes permission to invoke a function named `my-function`.

```
aws lambda remove-permission \
    --function-name {{my-function}} \
    --statement-id {{sns}}
```
This command produces no output.
For more information, see [Using Resource-based Policies for AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/access-control-resource-based.html) in the *AWS Lambda Developer Guide*.
+  For API details, see [RemovePermission](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/remove-permission.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example removes the function policy for the specified StatementId of a Lambda Function.**

```
$policy =  Get-LMPolicy -FunctionName "MylambdaFunction123" -Select Policy | ConvertFrom-Json| Select-Object -ExpandProperty Statement
Remove-LMPermission -FunctionName "MylambdaFunction123" -StatementId $policy[0].Sid
```
+  For API details, see [RemovePermission](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example removes the function policy for the specified StatementId of a Lambda Function.**

```
$policy =  Get-LMPolicy -FunctionName "MylambdaFunction123" -Select Policy | ConvertFrom-Json| Select-Object -ExpandProperty Statement
Remove-LMPermission -FunctionName "MylambdaFunction123" -StatementId $policy[0].Sid
```
+  For API details, see [RemovePermission](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK Code Examples. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query code-library` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
