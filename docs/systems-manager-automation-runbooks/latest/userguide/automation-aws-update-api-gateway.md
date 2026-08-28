---
source_url: https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-update-api-gateway.html
---

# `AWSConfigRemediation-UpdateAPIGatewayMethodCaching`
<a name="automation-aws-update-api-gateway"></a>

 **Description**

 The `AWSConfigRemediation-UpdateAPIGatewayMethodCaching` runbook updates the cache method setting for an Amazon API Gateway stage resource.

 [Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWSConfigRemediation-UpdateAPIGatewayMethodCaching)

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
+ CachingAuthorizedMethods

  Type: StringList

   Description: (Required) The methods authorized to have caching enabled. The list must be some combination of `DELETE` , `GET` , `HEAD` , `OPTIONS` , `PATCH` , `POST` , and `PUT` . Caching is enabled for selected methods and disabled for non-selected methods. Caching is enabled for all methods if `ANY` is selected and is disabled for all methods if `NONE` is selected.
+ StageArn

  Type: String

   Description: (Required) The API Gateway stage ARN for the `REST` API.

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to use the runbook successfully.
+  `ssm:StartAutomationExecution`
+  `ssm:GetAutomationExecution`
+  `apigateway:PATCH`
+  `apigateway:GET`

 **Document Steps**
+  `aws:executeScript` - Accepts the stage resource ID as input, updates the cache method setting for an API Gateway stage using the `UpdateStage` API action, and verifies the update.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager Automation Runbook Reference. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager-automation-runbooks` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
