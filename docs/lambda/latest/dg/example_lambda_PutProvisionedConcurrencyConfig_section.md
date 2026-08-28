---
source_url: https://docs.aws.amazon.com/lambda/latest/dg/example_lambda_PutProvisionedConcurrencyConfig_section.html
---

# Use `PutProvisionedConcurrencyConfig` with a CLI
<a name="example_lambda_PutProvisionedConcurrencyConfig_section"></a>

The following code examples show how to use `PutProvisionedConcurrencyConfig`.

------
#### [ CLI ]

**AWS CLI**
**To allocate provisioned concurrency**
The following `put-provisioned-concurrency-config` example allocates 100 provisioned concurrency for the `BLUE` alias of the specified function.

```
aws lambda put-provisioned-concurrency-config \
    --function-name {{my-function}} \
    --qualifier {{BLUE}} \
    --provisioned-concurrent-executions {{100}}
```
Output:

```
{
    "Requested ProvisionedConcurrentExecutions": 100,
    "Allocated ProvisionedConcurrentExecutions": 0,
    "Status": "IN_PROGRESS",
    "LastModified": "2019-11-21T19:32:12+0000"
}
```
+  For API details, see [PutProvisionedConcurrencyConfig](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/put-provisioned-concurrency-config.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example adds a provisioned concurrency configuration to a Function's Alias**

```
Write-LMProvisionedConcurrencyConfig -FunctionName "MylambdaFunction123" -ProvisionedConcurrentExecution 20 -Qualifier "NewAlias1"
```
+  For API details, see [PutProvisionedConcurrencyConfig](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example adds a provisioned concurrency configuration to a Function's Alias**

```
Write-LMProvisionedConcurrencyConfig -FunctionName "MylambdaFunction123" -ProvisionedConcurrentExecution 20 -Qualifier "NewAlias1"
```
+  For API details, see [PutProvisionedConcurrencyConfig](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------

For a complete list of AWS SDK developer guides and code examples, see [Using Lambda with an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Lambda. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lambda` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
