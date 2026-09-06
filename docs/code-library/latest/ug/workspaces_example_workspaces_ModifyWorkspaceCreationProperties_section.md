---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/workspaces_example_workspaces_ModifyWorkspaceCreationProperties_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `ModifyWorkspaceCreationProperties` with a CLI
<a name="workspaces_example_workspaces_ModifyWorkspaceCreationProperties_section"></a>

The following code examples show how to use `ModifyWorkspaceCreationProperties`.

------
#### [ CLI ]

**AWS CLI**
**To modify a WorkSpace creation property of a directory**
The following `modify-workspace-creation-properties` example enables the `EnableInternetAccess` property for the specified directory. This enables automatic assignment of public IP addresses for the WorkSpaces created for the directory.

```
aws workspaces modify-workspace-creation-properties \
    --resource-id {{d-926722edaf}} \
    --workspace-creation-properties {{EnableInternetAccess=true}}
```
This command produces no output.
For more information, see [Update directory details for your WorkSpaces](https://docs.aws.amazon.com/workspaces/latest/adminguide/update-directory-details.html) in the *Amazon WorkSpaces Administration Guide*.
+  For API details, see [ModifyWorkspaceCreationProperties](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workspaces/modify-workspace-creation-properties.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This sample enables Internet Access and Maintenance Mode to true as default values while creating a Workspace**

```
Edit-WKSWorkspaceCreationProperty -Region us-west-2 -ResourceId d-123454a369 -WorkspaceCreationProperties_EnableInternetAccess $true -WorkspaceCreationProperties_EnableMaintenanceMode $true
```
+  For API details, see [ModifyWorkspaceCreationProperties](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This sample enables Internet Access and Maintenance Mode to true as default values while creating a Workspace**

```
Edit-WKSWorkspaceCreationProperty -Region us-west-2 -ResourceId d-123454a369 -WorkspaceCreationProperties_EnableInternetAccess $true -WorkspaceCreationProperties_EnableMaintenanceMode $true
```
+  For API details, see [ModifyWorkspaceCreationProperties](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------
