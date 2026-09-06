---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/powershell_5_resource-groups_code_examples.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Resource Groups examples using Tools for PowerShell V5
<a name="powershell_5_resource-groups_code_examples"></a>

The following code examples show you how to perform actions and implement common scenarios by using the AWS Tools for PowerShell V5 with Resource Groups.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Topics**
+ [Actions](#actions)

## Actions
<a name="actions"></a>

### `Add-RGResourceTag`
<a name="resource-groups_Tag_powershell_5_topic"></a>

The following code example shows how to use `Add-RGResourceTag`.

**Tools for PowerShell V5**
**Example 1: This example adds tag key 'Instances' with value 'workboxes' to the given resource group arn**

```
Add-RGResourceTag -Tag @{Instances="workboxes"} -Arn arn:aws:resource-groups:eu-west-1:123456789012:group/workboxes
```
**Output:**

```
Arn                                                            Tags
---                                                            ----
arn:aws:resource-groups:eu-west-1:123456789012:group/workboxes {[Instances, workboxes]}
```
+  For API details, see [Tag](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Find-RGResource`
<a name="resource-groups_SearchResources_powershell_5_topic"></a>

The following code example shows how to use `Find-RGResource`.

**Tools for PowerShell V5**
**Example 1: This example creates a ResourceQuery for Instance resource types with tag filters and finds resources. **

```
$query = [Amazon.ResourceGroups.Model.ResourceQuery]::new()
$query.Type = [Amazon.ResourceGroups.QueryType]::TAG_FILTERS_1_0
$query.Query = ConvertTo-Json -Compress -Depth 4 -InputObject @{
  ResourceTypeFilters = @('AWS::EC2::Instance')
  TagFilters = @(@{
    Key = 'auto'
    Values = @('no')
  })
 }

Find-RGResource -ResourceQuery $query | Select-Object -ExpandProperty ResourceIdentifiers
```
**Output:**

```
ResourceArn                                                     ResourceType
-----------                                                     ------------
arn:aws:ec2:eu-west-1:123456789012:instance/i-0123445b6cb7bd67b AWS::EC2::Instance
```
+  For API details, see [SearchResources](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-RGGroup`
<a name="resource-groups_GetGroup_powershell_5_topic"></a>

The following code example shows how to use `Get-RGGroup`.

**Tools for PowerShell V5**
**Example 1: This example retrieves resource group as per the group name**

```
Get-RGGroup -GroupName auto-no
```
**Output:**

```
Description GroupArn                                                     Name
----------- --------                                                     ----
            arn:aws:resource-groups:eu-west-1:123456789012:group/auto-no auto-no
```
+  For API details, see [GetGroup](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-RGGroupList`
<a name="resource-groups_ListGroups_powershell_5_topic"></a>

The following code example shows how to use `Get-RGGroupList`.

**Tools for PowerShell V5**
**Example 1: This example lists resource group already created.**

```
Get-RGGroupList
```
**Output:**

```
GroupArn                                                                  GroupName
--------                                                                  ---------
arn:aws:resource-groups:eu-west-1:123456789012:group/auto-no              auto-no
arn:aws:resource-groups:eu-west-1:123456789012:group/auto-yes             auto-yes
arn:aws:resource-groups:eu-west-1:123456789012:group/build600             build600
```
+  For API details, see [ListGroups](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-RGGroupQuery`
<a name="resource-groups_GetGroupQuery_powershell_5_topic"></a>

The following code example shows how to use `Get-RGGroupQuery`.

**Tools for PowerShell V5**
**Example 1: This example fetches the resource query for the given resource group**

```
Get-RGGroupQuery -GroupName auto-no | Select-Object -ExpandProperty ResourceQuery
```
**Output:**

```
Query                                                                                        Type
-----                                                                                        ----
{"ResourceTypeFilters":["AWS::EC2::Instance"],"TagFilters":[{"Key":"auto","Values":["no"]}]} TAG_FILTERS_1_0
```
+  For API details, see [GetGroupQuery](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-RGGroupResourceList`
<a name="resource-groups_ListGroupResources_powershell_5_topic"></a>

The following code example shows how to use `Get-RGGroupResourceList`.

**Tools for PowerShell V5**
**Example 1: This example lists group resources on the basis of filtered by resource type**

```
Get-RGGroupResourceList -Filter @{Name="resource-type";Values="AWS::EC2::Instance"} -GroupName auto-yes | Select-Object -ExpandProperty ResourceIdentifiers
```
**Output:**

```
ResourceArn                                                     ResourceType
-----------                                                     ------------
arn:aws:ec2:eu-west-1:123456789012:instance/i-0123bc45b567890e1 AWS::EC2::Instance
arn:aws:ec2:eu-west-1:123456789012:instance/i-0a1caf2345f67d8dc AWS::EC2::Instance
arn:aws:ec2:eu-west-1:123456789012:instance/i-012e3cb4df567e8aa AWS::EC2::Instance
arn:aws:ec2:eu-west-1:123456789012:instance/i-0fd12dd3456789012 AWS::EC2::Instance
```
+  For API details, see [ListGroupResources](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-RGResourceTag`
<a name="resource-groups_GetTags_powershell_5_topic"></a>

The following code example shows how to use `Get-RGResourceTag`.

**Tools for PowerShell V5**
**Example 1: This example lists tags for the given resource group arn**

```
Get-RGResourceTag -Arn arn:aws:resource-groups:eu-west-1:123456789012:group/workboxes
```
**Output:**

```
Key       Value
---       -----
Instances workboxes
```
+  For API details, see [GetTags](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `New-RGGroup`
<a name="resource-groups_CreateGroup_powershell_5_topic"></a>

The following code example shows how to use `New-RGGroup`.

**Tools for PowerShell V5**
**Example 1: This example creates a new tag-based AWS Resource Groups resource group named TestPowerShellGroup. The group includes Amazon EC2 instances in the current region that are tagged with the tag key "Name", and tag value "test2". The command returns the query and type of group, and the results of the operation.**

```
$ResourceQuery = New-Object -TypeName Amazon.ResourceGroups.Model.ResourceQuery
$ResourceQuery.Type = "TAG_FILTERS_1_0"
$ResourceQuery.Query = '{"ResourceTypeFilters":["AWS::EC2::Instance"],"TagFilters":[{"Key":"Name","Values":["test2"]}]}'
$ResourceQuery

New-RGGroup -Name TestPowerShellGroup -ResourceQuery $ResourceQuery -Description "Test resource group."
```
**Output:**

```
Query                                                                                           Type
-----                                                                                           ----
{"ResourceTypeFilters":["AWS::EC2::Instance"],"TagFilters":[{"Key":"Name","Values":["test2"]}]} TAG_FILTERS_1_0

LoggedAt         : 11/20/2018 2:40:59 PM
Group            : Amazon.ResourceGroups.Model.Group
ResourceQuery    : Amazon.ResourceGroups.Model.ResourceQuery
Tags             : {}
ResponseMetadata : Amazon.Runtime.ResponseMetadata
ContentLength    : 338
HttpStatusCode   : OK
```
+  For API details, see [CreateGroup](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Remove-RGGroup`
<a name="resource-groups_DeleteGroup_powershell_5_topic"></a>

The following code example shows how to use `Remove-RGGroup`.

**Tools for PowerShell V5**
**Example 1: This example removes the named resource group**

```
Remove-RGGroup -GroupName non-tag-cfn-elbv2
```
**Output:**

```
Confirm
Are you sure you want to perform this action?
Performing the operation "Remove-RGGroup (DeleteGroup)" on target "non-tag-cfn-elbv2".
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "Y"): Y

Description GroupArn                                                               Name
----------- --------                                                               ----
            arn:aws:resource-groups:eu-west-1:123456789012:group/non-tag-cfn-elbv2 non-tag-cfn-elbv2
```
+  For API details, see [DeleteGroup](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Remove-RGResourceTag`
<a name="resource-groups_Untag_powershell_5_topic"></a>

The following code example shows how to use `Remove-RGResourceTag`.

**Tools for PowerShell V5**
**Example 1: This example removes mentioned tag from the resource group**

```
Remove-RGResourceTag -Arn arn:aws:resource-groups:eu-west-1:123456789012:group/workboxes -Key Instances
```
**Output:**

```
Confirm
Are you sure you want to perform this action?
Performing the operation "Remove-RGResourceTag (Untag)" on target "arn:aws:resource-groups:eu-west-1:933303704102:group/workboxes".
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "Y"): Y

Arn                                                            Keys
---                                                            ----
arn:aws:resource-groups:eu-west-1:123456789012:group/workboxes {Instances}
```
+  For API details, see [Untag](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Update-RGGroup`
<a name="resource-groups_UpdateGroup_powershell_5_topic"></a>

The following code example shows how to use `Update-RGGroup`.

**Tools for PowerShell V5**
**Example 1: This example updates the description of the group**

```
Update-RGGroup -GroupName auto-yes -Description "Instances auto-remove"
```
**Output:**

```
Description             GroupArn                                                      Name
-----------             --------                                                      ----
Instances to be cleaned arn:aws:resource-groups:eu-west-1:123456789012:group/auto-yes auto-yes
```
+  For API details, see [UpdateGroup](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Update-RGGroupQuery`
<a name="resource-groups_UpdateGroupQuery_powershell_5_topic"></a>

The following code example shows how to use `Update-RGGroupQuery`.

**Tools for PowerShell V5**
**Example 1: This example creates a query object and updates the query for the group.**

```
$query = [Amazon.ResourceGroups.Model.ResourceQuery]::new()
$query.Type = [Amazon.ResourceGroups.QueryType]::TAG_FILTERS_1_0
$query.Query = @{
  ResourceTypeFilters = @('AWS::EC2::Instance')
  TagFilters = @(@{
  Key='Environment'
  Values='Build600.11'
  })
} | ConvertTo-Json -Compress -Depth 4

Update-RGGroupQuery -GroupName build600 -ResourceQuery $query
```
**Output:**

```
GroupName ResourceQuery
--------- -------------
build600  Amazon.ResourceGroups.Model.ResourceQuery
```
+  For API details, see [UpdateGroupQuery](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.
