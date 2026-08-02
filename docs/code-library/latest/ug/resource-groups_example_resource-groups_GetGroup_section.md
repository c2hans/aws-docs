---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/resource-groups_example_resource-groups_GetGroup_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `GetGroup` with a CLI
<a name="resource-groups_example_resource-groups_GetGroup_section"></a>

The following code examples show how to use `GetGroup`.

------
#### [ CLI ]

**AWS CLI**
**To get information about a resource group**
The following `get-group` example displays details about the specified resource group. To get the query attached to the group, use `get-group-query`.

```
aws resource-groups get-group \
    --group-name {{tbq-WebServer}}
```
Output:

```
{
    "Group": {
        "GroupArn": "arn:aws:resource-groups:us-west-2:123456789012:group/tbq-WebServer",
        "Name": "tbq-WebServer",
        "Description": "A tag-based query resource group of WebServers."
    }
}
```
+  For API details, see [GetGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resource-groups/get-group.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
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
+  For API details, see [GetGroup](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

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

------
