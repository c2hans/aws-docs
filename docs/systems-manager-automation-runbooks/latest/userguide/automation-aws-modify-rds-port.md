---
source_url: https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-modify-rds-port.html
---

# `AWSConfigRemediation-ModifyRDSInstancePortNumber`
<a name="automation-aws-modify-rds-port"></a>

 **Description**

 The `AWSConfigRemediation-ModifyRDSInstancePortNumber` runbook modifies the port number on which the Amazon Relational Database Service (Amazon RDS) instance accepts connections. Running this automation will restart the database.

 [Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWSConfigRemediation-ModifyRDSInstancePortNumber)

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
+ PortNumber

  Type: String

  Description: (Optional) The port number you want the DB instance to accept connections on.
+ RDSDBInstanceResourceId

  Type: String

  Description: (Required) The resource identifier for the DB instance whose inbound port number you want to modify.

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to use the runbook successfully.
+  `ssm:StartAutomationExecution`
+  `ssm:GetAutomationExecution`
+  `rds:DescribeDBInstances`
+  `rds:ModifyDBInstance`

 **Document Steps**
+  `aws:executeAwsApi` - Gathers the DB instance identifier from the DB instance resource identifier.
+  `aws:assertAwsResourceProperty` - Confirms the DB Instance is in an `AVAILABLE` state.
+  `aws:executeAwsApi` - Modifies the inbound port number on which your DB instance accepts connections.
+  `aws:waitForAwsResourceProperty` - Waits for the DB Instance to be in a `MODIFYING` state.
+  `aws:waitForAwsResourceProperty` - Waits for the DB Instance to be in in an `AVAILABLE` state.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager Automation Runbook Reference. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager-automation-runbooks` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
