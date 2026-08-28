---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/codedeploy_example_codedeploy_DeleteDeploymentGroup_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `DeleteDeploymentGroup` with a CLI
<a name="codedeploy_example_codedeploy_DeleteDeploymentGroup_section"></a>

The following code examples show how to use `DeleteDeploymentGroup`.

------
#### [ CLI ]

**AWS CLI**
**To delete a deployment group**
The following `delete-deployment-group` example deletes a deployment group that is associated with the specified application.

```
aws deploy delete-deployment-group \
    --application-name {{WordPress_App}} \
    --deployment-group-name {{WordPress_DG}}
```
Output:

```
{
    "hooksNotCleanedUp": []
}
```
+  For API details, see [DeleteDeploymentGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/delete-deployment-group.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example deletes the deployment group with the specified name for the specified application. The command will prompt for confirmation before proceeding. Add the -Force parameter to delete the deployment group without a prompt.**

```
Remove-CDDeploymentGroup -ApplicationName MyNewApplication -DeploymentGroupName MyNewDeploymentGroup
```
+  For API details, see [DeleteDeploymentGroup](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example deletes the deployment group with the specified name for the specified application. The command will prompt for confirmation before proceeding. Add the -Force parameter to delete the deployment group without a prompt.**

```
Remove-CDDeploymentGroup -ApplicationName MyNewApplication -DeploymentGroupName MyNewDeploymentGroup
```
+  For API details, see [DeleteDeploymentGroup](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK Code Examples. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query code-library` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
