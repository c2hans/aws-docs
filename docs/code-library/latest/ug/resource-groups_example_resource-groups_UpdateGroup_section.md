---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/resource-groups_example_resource-groups_UpdateGroup_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `UpdateGroup` with a CLI
<a name="resource-groups_example_resource-groups_UpdateGroup_section"></a>

The following code examples show how to use `UpdateGroup`.

------
#### [ CLI ]

**AWS CLI**
**To update the description for a resource group**
The following `update-group` example updates the description for the specified resource group.

```
aws resource-groups update-group \
    --group-name {{tbq-WebServer}} \
    --description {{"Resource group for all web server resources."}}
```
Output:

```
{
    "Group": {
        "GroupArn": "arn:aws:resource-groups:us-west-2:123456789012:group/tbq-WebServer",
        "Name": "tbq-WebServer"
        "Description": "Resource group for all web server resources."
    }
}
```
For more information, see [Update Groups](https://docs.aws.amazon.com/ARG/latest/userguide/updating-resource-groups.html) in the *AWS Resource Groups User Guide*.
+  For API details, see [UpdateGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resource-groups/update-group.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
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
+  For API details, see [UpdateGroup](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

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

------
