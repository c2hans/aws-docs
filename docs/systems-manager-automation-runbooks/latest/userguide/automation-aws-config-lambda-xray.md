---
source_url: https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-config-lambda-xray.html
---

# `AWSConfigRemediation-ConfigureLambdaFunctionXRayTracing`
<a name="automation-aws-config-lambda-xray"></a>

 **Description**

 The `AWSConfigRemediation-ConfigureLambdaFunctionXRayTracing` runbook enables AWS X-Ray live tracing on the AWS Lambda function you specify in the `FunctionName` parameter.

 [Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWSConfigRemediation-ConfigureLambdaFunctionXRayTracing)

**Document type**

Automation

**Owner**

Amazon

**Platforms**

Linux, macOS, Windows

**Parameters**
+ AutomationAssumeRole

  Type: String

  Description: (Required) The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that allows Systems Manager Automation to perform the actions on your behalf.
+ FunctionName

  Type: String

  Description: (Required) The name or ARN of the Lambda function to enable tracing on.

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to use the runbook successfully.
+  `lambda:UpdateFunctionConfiguration`
+  `ssm:StartAutomationExecution`
+  `ssm:GetAutomationExecution`

 **Document Steps**
+  `aws:executeAwsApi` - Enables X-Ray tracing on the Lambda function you specify in the `FunctionName` parameter.
+  `aws:assertAwsResourceProperty` - Verifies that X-Ray tracing has been enabled on the Lambda function.

 **Outputs**

 UpdateLambdaConfig.UpdateFunctionConfigurationResponse - Response from the `UpdateFunctionConfiguration` API call.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager Automation Runbook Reference. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager-automation-runbooks` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
