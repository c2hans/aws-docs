---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/lambda_example_lambda_PutProvisionedConcurrencyConfig_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `PutProvisionedConcurrencyConfig` with a CLI
<a name="lambda_example_lambda_PutProvisionedConcurrencyConfig_section"></a>

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
