---
source_url: https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-disable-rds-instance-public-access.html
---

# `AWSConfigRemediation-DisablePublicAccessToRDSInstance`
<a name="automation-aws-disable-rds-instance-public-access"></a>

 **Description**

 The `AWSConfigRemediation-DisablePublicAccessToRDSInstance` runbook disables public accessibility for the Amazon Relational Database Service (Amazon RDS) database (DB) instance that you specify.

 [Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWSConfigRemediation-DisablePublicAccessToRDSInstance)

**Document type**

Automation

**Owner**

Amazon

**Platforms**

Databases

**Parameters**
+ AutomationAssumeRole

  Type: String

  Description: (Required) The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that allows Systems Manager Automation to perform the actions on your behalf.
+ DbiResourceId

  Type: String

  Description: (Required) The resource identifier for the DB instance that you want to disable public accessibility for.

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to use the runbook successfully.
+  `ssm:StartAutomationExecution`
+  `ssm:GetAutomationExecution`
+  `rds:DescribeDBInstances`
+  `rds:ModifyDBInstance`

 **Document Steps**
+  `aws:executeAwsApi` - Gathers the DB instance identifier from the DB instance resource identifier.
+  `aws:assertAwsResourceProperty` - Verifies the DB instances is in an `AVAILABLE` state.
+  `aws:executeAwsApi` - Disables public accessibility on your DB instance.
+  `aws:waitForAwsResourceProperty` - Waits for the DB instance to change to a `MODIFYING` state.
+  `aws:waitForAwsResourceProperty` - Waits for the DB instance to change to an `AVAILABLE` state.
+  `aws:assertAwsResourceProperty` - Confirms public accessibility is disabled on the DB instance.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager Automation Runbook Reference. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager-automation-runbooks` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
