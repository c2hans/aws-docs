---
source_url: https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-enable-eb-logging.html
---

# `AWSConfigRemediation-EnableElasticBeanstalkEnvironmentLogStreaming`
<a name="automation-aws-enable-eb-logging"></a>

 **Description**

 The `AWSConfigRemediation-EnableElasticBeanstalkEnvironmentLogStreaming` runbook enables logging on the AWS Elastic Beanstalk (Elastic Beanstalk) environment you specify.

 [Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWSConfigRemediation-EnableElasticBeanstalkEnvironmentLogStreaming)

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
+ EnvironmentId

  Type: String

  Description: (Required) The ID of the Elastic Beanstalk environment that you want to enable logging on.

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to use the runbook successfully.
+  `ssm:StartAutomationExecution`
+  `ssm:GetAutomationExecution`
+  `elasticbeanstalk:DescribeConfigurationSettings`
+  `elasticbeanstalk:DescribeEnvironments`
+  `elasticbeanstalk:UpdateEnvironment`

 **Document Steps**
+  `aws:executeAwsApi` - Enables logging on the Elastic Beanstalk environment you specify in the `EnvironmentId` parameter.
+  `aws:waitForAwsResourceProperty` - Waits for the status of the environment to change to `Ready` .
+  `aws:executeScript` - Verifies logging has been enabled on the Elastic Beanstalk environment.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager Automation Runbook Reference. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager-automation-runbooks` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
