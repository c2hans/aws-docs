---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/lambda_example_lambda_ListProvisionedConcurrencyConfigs_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `ListProvisionedConcurrencyConfigs` with a CLI
<a name="lambda_example_lambda_ListProvisionedConcurrencyConfigs_section"></a>

The following code examples show how to use `ListProvisionedConcurrencyConfigs`.

------
#### [ CLI ]

**AWS CLI**
**To get a list of provisioned concurrency configurations**
The following `list-provisioned-concurrency-configs` example lists the provisioned concurrency configurations for the specified function.

```
aws lambda list-provisioned-concurrency-configs \
    --function-name {{my-function}}
```
Output:

```
{
    "ProvisionedConcurrencyConfigs": [
        {
            "FunctionArn": "arn:aws:lambda:us-east-2:123456789012:function:my-function:GREEN",
            "RequestedProvisionedConcurrentExecutions": 100,
            "AvailableProvisionedConcurrentExecutions": 100,
            "AllocatedProvisionedConcurrentExecutions": 100,
            "Status": "READY",
            "LastModified": "2019-12-31T20:29:00+0000"
        },
        {
            "FunctionArn": "arn:aws:lambda:us-east-2:123456789012:function:my-function:BLUE",
            "RequestedProvisionedConcurrentExecutions": 100,
            "AvailableProvisionedConcurrentExecutions": 100,
            "AllocatedProvisionedConcurrentExecutions": 100,
            "Status": "READY",
            "LastModified": "2019-12-31T20:28:49+0000"
        }
    ]
}
```
+  For API details, see [ListProvisionedConcurrencyConfigs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/list-provisioned-concurrency-configs.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example retrieves the list of provisioned concurrency configurations for a Lambda function.**

```
Get-LMProvisionedConcurrencyConfigList -FunctionName "MylambdaFunction123"
```
+  For API details, see [ListProvisionedConcurrencyConfigs](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example retrieves the list of provisioned concurrency configurations for a Lambda function.**

```
Get-LMProvisionedConcurrencyConfigList -FunctionName "MylambdaFunction123"
```
+  For API details, see [ListProvisionedConcurrencyConfigs](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK Code Examples. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query code-library` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
