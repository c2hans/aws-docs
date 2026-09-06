---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/resource-groups-tagging-api_example_resource-groups-tagging-api_GetTagKeys_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `GetTagKeys` with a CLI
<a name="resource-groups-tagging-api_example_resource-groups-tagging-api_GetTagKeys_section"></a>

The following code examples show how to use `GetTagKeys`.

------
#### [ CLI ]

**AWS CLI**
**To get a list of all tag keys**
The following `get-tag-keys` example retrieves the list of all tag key names used by resources in the account.

```
aws resourcegroupstaggingapi get-tag-keys
```
Output:

```
{
    "TagKeys": [
        "Environment",
        "CostCenter",
        "Department"
    ]
}
```
For more information, see [GetTagKeys](https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/API_GetTagKeys.html) in the *Resource Groups Tagging API Reference*.
+  For API details, see [GetTagKeys](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resourcegroupstaggingapi/get-tag-keys.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: Returns all tag keys in the specified region. If the -Region parameter is not specified the cmdlet will attempt to infer the region from the default shell region or EC2 instance metadata. Note that the tag keys are not returned in any specific order.**

```
Get-RGTTagKey -region us-west-2
```
**Output:**

```
version
stage
```
+  For API details, see [GetTagKeys](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: Returns all tag keys in the specified region. If the -Region parameter is not specified the cmdlet will attempt to infer the region from the default shell region or EC2 instance metadata. Note that the tag keys are not returned in any specific order.**

```
Get-RGTTagKey -region us-west-2
```
**Output:**

```
version
stage
```
+  For API details, see [GetTagKeys](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------
