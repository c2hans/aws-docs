---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/lambda_example_lambda_GetFunctionConcurrency_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `GetFunctionConcurrency` with a CLI
<a name="lambda_example_lambda_GetFunctionConcurrency_section"></a>

The following code examples show how to use `GetFunctionConcurrency`.

------
#### [ CLI ]

**AWS CLI**
**To view the reserved concurrency setting for a function**
The following `get-function-concurrency` example retrieves the reserved concurrency setting for the specified function.

```
aws lambda get-function-concurrency \
    --function-name {{my-function}}
```
Output:

```
{
    "ReservedConcurrentExecutions": 250
}
```
+  For API details, see [GetFunctionConcurrency](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/get-function-concurrency.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This examples gets the Reserved concurrency for the Lambda Function**

```
Get-LMFunctionConcurrency -FunctionName "MylambdaFunction123" -Select *
```
**Output:**

```
ReservedConcurrentExecutions
----------------------------
100
```
+  For API details, see [GetFunctionConcurrency](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This examples gets the Reserved concurrency for the Lambda Function**

```
Get-LMFunctionConcurrency -FunctionName "MylambdaFunction123" -Select *
```
**Output:**

```
ReservedConcurrentExecutions
----------------------------
100
```
+  For API details, see [GetFunctionConcurrency](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK Code Examples. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query code-library` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
