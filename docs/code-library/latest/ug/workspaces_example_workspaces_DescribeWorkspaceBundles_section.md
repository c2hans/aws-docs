---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/workspaces_example_workspaces_DescribeWorkspaceBundles_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `DescribeWorkspaceBundles` with a CLI
<a name="workspaces_example_workspaces_DescribeWorkspaceBundles_section"></a>

The following code examples show how to use `DescribeWorkspaceBundles`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in context in the following code example:
+  [Creating and managing personal virtual desktops](workspaces_example_workspaces_GettingStarted_035_section.md)

------
#### [ CLI ]

**AWS CLI**
**To list the bundles provided by Amazon**
The following `describe-workspace-bundles` example lists the names and IDs of the bundles provided by Amazon, in table format and sorted by name.

```
aws workspaces describe-workspace-bundles \
    --owner {{AMAZON}} \
    --query {{"Bundles[*].[Name, BundleId]"}}
```
Output:

```
[
    [
        "Standard with Amazon Linux 2",
        "wsb-clj85qzj1"
    ],
    [
        "Performance with Windows 10 (Server 2016 based)",
        "wsb-gm4d5tx2v"
    ],
    [
        "PowerPro with Windows 7",
        "wsb-1pzkp0bx4"
    ],
    [
        "Power with Amazon Linux 2",
        "wsb-2bs6k5lgn"
    ],
    [
        "Graphics with Windows 10 (Server 2019 based)",
        "wsb-03gyjnfyy"
    ],
    ...
]
```
For more information, see [WorkSpaces bundles and images](https://docs.aws.amazon.com/workspaces/latest/adminguide/amazon-workspaces-bundles.html) in the *Amazon WorkSpaces Administration Guide*.
+  For API details, see [DescribeWorkspaceBundles](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workspaces/describe-workspace-bundles.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This sample fetches details of all the Workspace bundles in the current region**

```
Get-WKSWorkspaceBundle
```
**Output:**

```
BundleId        : wsb-sfhdgv342
ComputeType     : Amazon.WorkSpaces.Model.ComputeType
Description     : This bundle is custom
ImageId         : wsi-235aeqges
LastUpdatedTime : 12/26/2019 06:44:07
Name            : CustomBundleTest
Owner           : 233816212345
RootStorage     : Amazon.WorkSpaces.Model.RootStorage
UserStorage     : Amazon.WorkSpaces.Model.UserStorage
```
+  For API details, see [DescribeWorkspaceBundles](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This sample fetches details of all the Workspace bundles in the current region**

```
Get-WKSWorkspaceBundle
```
**Output:**

```
BundleId        : wsb-sfhdgv342
ComputeType     : Amazon.WorkSpaces.Model.ComputeType
Description     : This bundle is custom
ImageId         : wsi-235aeqges
LastUpdatedTime : 12/26/2019 06:44:07
Name            : CustomBundleTest
Owner           : 233816212345
RootStorage     : Amazon.WorkSpaces.Model.RootStorage
UserStorage     : Amazon.WorkSpaces.Model.UserStorage
```
+  For API details, see [DescribeWorkspaceBundles](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------
