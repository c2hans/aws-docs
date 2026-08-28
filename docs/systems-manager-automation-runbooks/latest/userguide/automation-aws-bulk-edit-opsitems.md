---
source_url: https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-bulk-edit-opsitems.html
---

# `AWS-BulkEditOpsItems`
<a name="automation-aws-bulk-edit-opsitems"></a>

 **Description**

 The `AWS-BulkEditOpsItems` runbook helps you edit the status, severity, category, or priority of AWS Systems Manager OpsItems. This automation can edit a maximum of 50 OpsItems at a time.

 [Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWS-BulkEditOpsItems)

**Document type**

Automation

**Owner**

Amazon

**Platforms**

Linux, macOS, Windows

**Parameters**
+ AutomationAssumeRole

  Type: String

  Description: (Optional) The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that allows Systems Manager Automation to perform the actions on your behalf. If no role is specified, Systems Manager Automation uses the permissions of the user that starts this runbook.
+ Category

  Type: String

  Valid values:
  + Availability
  + Cost
  + No change
  + Performance
  + Recovery
  + Security

  Default: No change

  Description: (Optional) The new category you want to specify for the edited OpsItems.
+ OpsItemIds

  Type: StringList

  Description: (Required) A comma-separated list of OpsItems IDs you want to edit (for example, oi-XXXXXXXXXXXX,oi-XXXXXXXXXXXX).
+ Priority

  Type: String

  Valid values:
  + No change
  + 1
  + 2
  + 3
  + 4
  + 5

  Default: No change

  Description: (Optional) The importance of the edited OpsItems in relation to other OpsItems in the system.
+ Severity

  Type: String

  Valid values:
  + No change
  + 1
  + 2
  + 3
  + 4

  Default: No change

  Description: (Optional) The severity of the edited OpsItems.
+ WaitTimeBetweenEditsInSecs

  Type: String

  Valid values: 0.0-2.0

  Default: 0.8

   Description: (Optional) The time the automation waits between calling the `UpdateOpsItems` operation.
+ Status

  Type: String

  Valid values:
  + InProgress
  + No change
  + Open
  + Resolved

  Default: No change

  Description: (Optional) The new status of the edited OpsItems.

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to use the runbook successfully.
+  `ssm:GetAutomationExecution`
+  `ssm:StartAutomationExecution`
+  `ssm:UpdateOpsItem`

 **Document Steps**
+  `aws:executeScript` - Edits the OpsItems you specified in the `OpsItemIds` parameter based on the values you specify for the `Category` , `Priority` , `Severity` , and `Status` parameters.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager Automation Runbook Reference. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager-automation-runbooks` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
