---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/ssm_example_ssm_PutComplianceItems_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `PutComplianceItems` with a CLI
<a name="ssm_example_ssm_PutComplianceItems_section"></a>

The following code examples show how to use `PutComplianceItems`.

------
#### [ CLI ]

**AWS CLI**
**To register a compliance type and compliance details to a designated instance**
This example registers the compliance type `Custom:AVCheck` to the specified managed instance. There is no output if the command succeeds.
Command:

```
aws ssm put-compliance-items --resource-id {{"i-1234567890abcdef0"}} --resource-type {{"ManagedInstance"}} --compliance-type {{"Custom:AVCheck"}} --execution-summary {{"ExecutionTime=2019-02-18T16:00:00Z"}} --items {{"Id=Version2.0,Title=ScanHost,Severity=CRITICAL,Status=COMPLIANT"}}
```
+  For API details, see [PutComplianceItems](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/put-compliance-items.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example writes a custom compliance item for the given managed instance**

```
$item = [Amazon.SimpleSystemsManagement.Model.ComplianceItemEntry]::new()
$item.Id = "07Jun2019-3"
$item.Severity="LOW"
$item.Status="COMPLIANT"
$item.Title="Fin-test-1 - custom"
Write-SSMComplianceItem -ResourceId mi-012dcb3ecea45b678 -ComplianceType Custom:VSSCompliant2 -ResourceType ManagedInstance -Item $item -ExecutionSummary_ExecutionTime "07-Jun-2019"
```
+  For API details, see [PutComplianceItems](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example writes a custom compliance item for the given managed instance**

```
$item = [Amazon.SimpleSystemsManagement.Model.ComplianceItemEntry]::new()
$item.Id = "07Jun2019-3"
$item.Severity="LOW"
$item.Status="COMPLIANT"
$item.Title="Fin-test-1 - custom"
Write-SSMComplianceItem -ResourceId mi-012dcb3ecea45b678 -ComplianceType Custom:VSSCompliant2 -ResourceType ManagedInstance -Item $item -ExecutionSummary_ExecutionTime "07-Jun-2019"
```
+  For API details, see [PutComplianceItems](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK Code Examples. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query code-library` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
