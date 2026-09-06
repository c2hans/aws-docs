---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/resource-groups-tagging-api_example_resource-groups-tagging-api_GetTagValues_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `GetTagValues` with a CLI
<a name="resource-groups-tagging-api_example_resource-groups-tagging-api_GetTagValues_section"></a>

The following code examples show how to use `GetTagValues`.

------
#### [ CLI ]

**AWS CLI**
**To get a list of all tag values**
The following `get-tag-values` example displays all of the values used for the specified key for all resources in the

```
aws resourcegroupstaggingapi get-tag-values \
    --key=Environment
```
Output:

```
{
    "TagValues": [
        "Alpha",
        "Gamma",
        "Production"
    ]
}
```
For more information, see [GetTagValues](https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/API_GetTagValues.html) in the *Resource Groups Tagging API Reference*.
+  For API details, see [GetTagValues](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resourcegroupstaggingapi/get-tag-values.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: Returns the value for the specified tag in a region. If the -Region parameter is not specified the cmdlet will attempt to infer the region from the default shell region or EC2 instance metadata.**

```
Get-RGTTagValue -Key "stage" -Region us-west-2
```
**Output:**

```
beta
```
+  For API details, see [GetTagValues](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: Returns the value for the specified tag in a region. If the -Region parameter is not specified the cmdlet will attempt to infer the region from the default shell region or EC2 instance metadata.**

```
Get-RGTTagValue -Key "stage" -Region us-west-2
```
**Output:**

```
beta
```
+  For API details, see [GetTagValues](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------
