---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/codedeploy_example_codedeploy_ListDeploymentConfigs_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `ListDeploymentConfigs` with a CLI
<a name="codedeploy_example_codedeploy_ListDeploymentConfigs_section"></a>

The following code examples show how to use `ListDeploymentConfigs`.

------
#### [ CLI ]

**AWS CLI**
**To get information about deployment configurations**
The following `list-deployment-configs` example displays information about all deployment configurations that are associated with the user's AWS account.

```
aws deploy list-deployment-configs
```
Output:

```
{
    "deploymentConfigsList": [
        "ThreeQuartersHealthy",
        "CodeDeployDefault.AllAtOnce",
        "CodeDeployDefault.HalfAtATime",
        "CodeDeployDefault.OneAtATime"
    ]
}
```
+  For API details, see [ListDeploymentConfigs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/list-deployment-configs.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example gets a list of available deployment configurations.**

```
Get-CDDeploymentConfigList
```
**Output:**

```
ThreeQuartersHealthy
CodeDeployDefault.OneAtATime
CodeDeployDefault.AllAtOnce
CodeDeployDefault.HalfAtATime
```
+  For API details, see [ListDeploymentConfigs](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example gets a list of available deployment configurations.**

```
Get-CDDeploymentConfigList
```
**Output:**

```
ThreeQuartersHealthy
CodeDeployDefault.OneAtATime
CodeDeployDefault.AllAtOnce
CodeDeployDefault.HalfAtATime
```
+  For API details, see [ListDeploymentConfigs](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------
