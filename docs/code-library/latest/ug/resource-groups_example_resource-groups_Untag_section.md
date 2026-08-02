---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/resource-groups_example_resource-groups_Untag_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `Untag` with a CLI
<a name="resource-groups_example_resource-groups_Untag_section"></a>

The following code examples show how to use `Untag`.

------
#### [ CLI ]

**AWS CLI**
**To remove tags from a resource group**
The following `untags` example removes any tag with the specified key from the resource group itself, not its members.

```
aws resource-groups untag \
    --arn {{arn:aws:resource-groups:us-west-2:123456789012:group/tbq-WebServer}} \
    --keys {{QueryType}}
```
Output:

```
{
    "Arn": "arn:aws:resource-groups:us-west-2:123456789012:group/tbq-WebServer",
    "Keys": [
        "QueryType"
    ]
}
```
For more information, see [Manage tags](https://docs.aws.amazon.com/ARG/latest/userguide/tagging-resources.html) in the *AWS Resource Groups User Guide*.
+  For API details, see [Untag](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resource-groups/untag.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
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
+  For API details, see [Untag](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

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

------
