---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/codedeploy_example_codedeploy_ListDeployments_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `ListDeployments` with a CLI
<a name="codedeploy_example_codedeploy_ListDeployments_section"></a>

The following code examples show how to use `ListDeployments`.

------
#### [ CLI ]

**AWS CLI**
**To get information about deployments**
The following `list-deployments` example displays information about all deployments that are associated with the specified application and deployment group.

```
aws deploy list-deployments \
    --application-name {{WordPress_App}} \
    --create-time-range {{start=2014-08-19T00:00:00,end=2014-08-20T00:00:00}} \
    --deployment-group-name {{WordPress_DG}} \
    --include-only-statuses {{Failed}}
```
Output:

```
{
    "deployments": [
        "d-EXAMPLE11",
        "d-EXAMPLE22",
        "d-EXAMPLE33"
    ]
}
```
+  For API details, see [ListDeployments](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/list-deployments.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example gets a list of deployment IDs for the specified application and deployment group.**

```
Get-CDDeploymentList -ApplicationName CodeDeployDemoApplication -DeploymentGroupName CodeDeployDemoFleet
```
**Output:**

```
d-QZMRGSTEX
d-RR0T5KTEX
```
+  For API details, see [ListDeployments](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example gets a list of deployment IDs for the specified application and deployment group.**

```
Get-CDDeploymentList -ApplicationName CodeDeployDemoApplication -DeploymentGroupName CodeDeployDemoFleet
```
**Output:**

```
d-QZMRGSTEX
d-RR0T5KTEX
```
+  For API details, see [ListDeployments](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK Code Examples. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query code-library` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
