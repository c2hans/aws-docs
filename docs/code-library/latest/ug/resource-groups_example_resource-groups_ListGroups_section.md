---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/resource-groups_example_resource-groups_ListGroups_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `ListGroups` with a CLI
<a name="resource-groups_example_resource-groups_ListGroups_section"></a>

The following code examples show how to use `ListGroups`.

------
#### [ CLI ]

**AWS CLI**
**To list the available resource groups**
The following `list-groups` example displays a list of all of the resource groups.

```
aws resource-groups list-groups
```
Output:

```
{
    "GroupIdentifiers": [
        {
            "GroupName": "tbq-WebServer",
            "GroupArn": "arn:aws:resource-groups:us-west-2:123456789012:group/tbq-WebServer3"
        },
        {
            "GroupName": "cbq-CFNStackQuery",
            "GroupArn": "arn:aws:resource-groups:us-west-2:123456789012:group/cbq-CFNStackQuery"
        }
    ],
    "Groups": [
        {
            "GroupArn": "arn:aws:resource-groups:us-west-2:123456789012:group/tbq-WebServer",
            "Name": "tbq-WebServer"
        },
        {
            "GroupArn": "arn:aws:resource-groups:us-west-2:123456789012:group/cbq-CFNStackQuery",
            "Name": "cbq-CFNStackQuery"
        }
    ]
}
```
+  For API details, see [ListGroups](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resource-groups/list-groups.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
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
+  For API details, see [ListGroups](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

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

------
