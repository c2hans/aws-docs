---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/workspaces_example_workspaces_DescribeWorkspacesConnectionStatus_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `DescribeWorkspacesConnectionStatus` with a CLI
<a name="workspaces_example_workspaces_DescribeWorkspacesConnectionStatus_section"></a>

The following code examples show how to use `DescribeWorkspacesConnectionStatus`.

------
#### [ CLI ]

**AWS CLI**
**To describe the connection status of a WorkSpace**
The following `describe-workspaces-connection-status` example describes the connection status of the specified WorkSpace.

```
aws workspaces describe-workspaces-connection-status \
    --workspace-ids {{ws-dk1xzr417}}
```
Output:

```
{
    "WorkspacesConnectionStatus": [
        {
            "WorkspaceId": "ws-dk1xzr417",
            "ConnectionState": "CONNECTED",
            "ConnectionStateCheckTimestamp": 1662526214.744
        }
    ]
}
```
For more information, see [Administer your WorkSpaces](https://docs.aws.amazon.com/workspaces/latest/adminguide/administer-workspaces.html) in the *Amazon WorkSpaces Administration Guide*.
+  For API details, see [DescribeWorkspacesConnectionStatus](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workspaces/describe-workspaces-connection-status.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This sample fetches the connection status for the specified Workspace**

```
Get-WKSWorkspacesConnectionStatus -WorkspaceId ws-w123s234r
```
+  For API details, see [DescribeWorkspacesConnectionStatus](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This sample fetches the connection status for the specified Workspace**

```
Get-WKSWorkspacesConnectionStatus -WorkspaceId ws-w123s234r
```
+  For API details, see [DescribeWorkspacesConnectionStatus](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK Code Examples. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query code-library` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
