---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/ssm_example_ssm_DescribePatchGroups_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `DescribePatchGroups` with a CLI
<a name="ssm_example_ssm_DescribePatchGroups_section"></a>

The following code examples show how to use `DescribePatchGroups`.

------
#### [ CLI ]

**AWS CLI**
**To display patch group registrations**
The following `describe-patch-groups` example lists the patch group registrations.

```
aws ssm describe-patch-groups
```
Output:

```
{
    "Mappings": [
        {
            "PatchGroup": "Production",
            "BaselineIdentity": {
                "BaselineId": "pb-0123456789abcdef0",
                "BaselineName": "ProdPatching",
                "OperatingSystem": "WINDOWS",
                "BaselineDescription": "Patches for Production",
                "DefaultBaseline": false
            }
        },
        {
            "PatchGroup": "Development",
            "BaselineIdentity": {
                "BaselineId": "pb-0713accee01234567",
                "BaselineName": "DevPatching",
                "OperatingSystem": "WINDOWS",
                "BaselineDescription": "Patches for Development",
                "DefaultBaseline": true
            }
        },
        ...
    ]
}
```
For more information, see Create a Patch Group <https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-patch-group-tagging.html>\_\_ and [Add a Patch Group to a Patch Baseline](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-patch-group-patchbaseline.html) in the *AWS Systems Manager User Guide*.
+  For API details, see [DescribePatchGroups](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/describe-patch-groups.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example lists the patch group registrations.**

```
Get-SSMPatchGroup
```
**Output:**

```
BaselineIdentity                                           PatchGroup
----------------                                           ----------
Amazon.SimpleSystemsManagement.Model.PatchBaselineIdentity Production
```
+  For API details, see [DescribePatchGroups](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example lists the patch group registrations.**

```
Get-SSMPatchGroup
```
**Output:**

```
BaselineIdentity                                           PatchGroup
----------------                                           ----------
Amazon.SimpleSystemsManagement.Model.PatchBaselineIdentity Production
```
+  For API details, see [DescribePatchGroups](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------
