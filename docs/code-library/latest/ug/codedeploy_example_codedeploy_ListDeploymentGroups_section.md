---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/codedeploy_example_codedeploy_ListDeploymentGroups_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `ListDeploymentGroups` with a CLI
<a name="codedeploy_example_codedeploy_ListDeploymentGroups_section"></a>

The following code examples show how to use `ListDeploymentGroups`.

------
#### [ CLI ]

**AWS CLI**
**To get information about deployment groups**
The following `list-deployment-groups` example displays information about all deployment groups that are associated with the specified application.

```
aws deploy list-deployment-groups --application-name {{WordPress_App}}
```
Output:

```
{
    "applicationName": "WordPress_App",
    "deploymentGroups": [
        "WordPress_DG",
        "WordPress_Beta_DG"
    ]
}
```
+  For API details, see [ListDeploymentGroups](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/list-deployment-groups.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example gets a list of deployment groups for the specified application.**

```
Get-CDDeploymentGroupList -ApplicationName CodeDeployDemoApplication
```
**Output:**

```
ApplicationName              DeploymentGroups                                    NextToken
---------------              ----------------                                    ---------
CodeDeployDemoApplication    {CodeDeployDemoFleet, CodeDeployProductionFleet}
```
+  For API details, see [ListDeploymentGroups](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example gets a list of deployment groups for the specified application.**

```
Get-CDDeploymentGroupList -ApplicationName CodeDeployDemoApplication
```
**Output:**

```
ApplicationName              DeploymentGroups                                    NextToken
---------------              ----------------                                    ---------
CodeDeployDemoApplication    {CodeDeployDemoFleet, CodeDeployProductionFleet}
```
+  For API details, see [ListDeploymentGroups](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK Code Examples. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query code-library` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
