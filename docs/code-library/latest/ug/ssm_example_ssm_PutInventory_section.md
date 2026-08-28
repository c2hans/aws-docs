---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/ssm_example_ssm_PutInventory_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `PutInventory` with a CLI
<a name="ssm_example_ssm_PutInventory_section"></a>

The following code examples show how to use `PutInventory`.

------
#### [ CLI ]

**AWS CLI**
**To assign customer metadata to an instance**
This example assigns rack location information to an instance. There is no output if the command succeeds.
Command (Linux):

```
aws ssm put-inventory --instance-id {{"i-016648b75dd622dab"}} --items '{{[{"TypeName": "Custom:RackInfo","SchemaVersion": "1.0","CaptureTime": "2019-01-22T10:01:01Z","Content":[{"RackLocation": "Bay B/Row C/Rack D/Shelf E"}]}]}}'
```
Command (Windows):

```
aws ssm put-inventory --instance-id {{"i-016648b75dd622dab"}} --items {{"TypeName=Custom:RackInfo,SchemaVersion=1.0,CaptureTime=2019-01-22T10:01:01Z,Content=[{RackLocation='Bay B/Row C/Rack D/Shelf F'}]"}}
```
+  For API details, see [PutInventory](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/put-inventory.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example assigns rack location information to an instance. There is no output if the command succeeds.**

```
$data = New-Object "System.Collections.Generic.Dictionary[System.String,System.String]"
$data.Add("RackLocation", "Bay B/Row C/Rack D/Shelf F")

$items = New-Object "System.Collections.Generic.List[System.Collections.Generic.Dictionary[System.String, System.String]]"
$items.Add($data)

$customInventoryItem = New-Object Amazon.SimpleSystemsManagement.Model.InventoryItem
$customInventoryItem.CaptureTime = "2016-08-22T10:01:01Z"
$customInventoryItem.Content = $items
$customInventoryItem.TypeName = "Custom:TestRackInfo2"
$customInventoryItem.SchemaVersion = "1.0"

$inventoryItems = @($customInventoryItem)

Write-SSMInventory -InstanceId "i-0cb2b964d3e14fd9f" -Item $inventoryItems
```
+  For API details, see [PutInventory](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example assigns rack location information to an instance. There is no output if the command succeeds.**

```
$data = New-Object "System.Collections.Generic.Dictionary[System.String,System.String]"
$data.Add("RackLocation", "Bay B/Row C/Rack D/Shelf F")

$items = New-Object "System.Collections.Generic.List[System.Collections.Generic.Dictionary[System.String, System.String]]"
$items.Add($data)

$customInventoryItem = New-Object Amazon.SimpleSystemsManagement.Model.InventoryItem
$customInventoryItem.CaptureTime = "2016-08-22T10:01:01Z"
$customInventoryItem.Content = $items
$customInventoryItem.TypeName = "Custom:TestRackInfo2"
$customInventoryItem.SchemaVersion = "1.0"

$inventoryItems = @($customInventoryItem)

Write-SSMInventory -InstanceId "i-0cb2b964d3e14fd9f" -Item $inventoryItems
```
+  For API details, see [PutInventory](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK Code Examples. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query code-library` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
