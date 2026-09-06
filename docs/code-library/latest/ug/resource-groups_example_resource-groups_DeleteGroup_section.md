---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/resource-groups_example_resource-groups_DeleteGroup_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `DeleteGroup` with a CLI
<a name="resource-groups_example_resource-groups_DeleteGroup_section"></a>

The following code examples show how to use `DeleteGroup`.

------
#### [ CLI ]

**AWS CLI**
**To update the description for a resource group**
The following `delete-group` example updates the specified resource group.

```
aws resource-groups delete-group \
    --group-name {{tbq-WebServer}}
```
Output:

```
{
    "Group": {
        "GroupArn": "arn:aws:resource-groups:us-west-2:1234567890:group/tbq-WebServer",
        "Name": "tbq-WebServer"
    }
}
```
For more information, see [Delete Groups](https://docs.aws.amazon.com/ARG/latest/userguide/deleting-resource-groups.html) in the *AWS Resource Groups User Guide*.
+  For API details, see [DeleteGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resource-groups/delete-group.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
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
+  For API details, see [DeleteGroup](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

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

------
