---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/codedeploy_example_codedeploy_GetDeploymentConfig_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `GetDeploymentConfig` with a CLI
<a name="codedeploy_example_codedeploy_GetDeploymentConfig_section"></a>

The following code examples show how to use `GetDeploymentConfig`.

------
#### [ CLI ]

**AWS CLI**
**To get information about a deployment configuration**
The following `get-deployment-config` example displays information about a deployment configuration that is associated with the user's AWS account.

```
aws deploy get-deployment-config --deployment-config-name {{ThreeQuartersHealthy}}
```
Output:

```
{
    "deploymentConfigInfo": {
        "deploymentConfigId": "a1b2c3d4-5678-90ab-cdef-11111EXAMPLE",
        "minimumHealthyHosts": {
            "type": "FLEET_PERCENT",
            "value": 75
        },
        "createTime": 1411081164.379,
        "deploymentConfigName": "ThreeQuartersHealthy"
    }
}
```
+  For API details, see [GetDeploymentConfig](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/get-deployment-config.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example gets summary information about the specified deployment configuration.**

```
Get-CDDeploymentConfig -DeploymentConfigName ThreeQuartersHealthy
```
**Output:**

```
CreateTime              DeploymentConfigId                      DeploymentConfigName    MinimumHealthyHosts
----------              ------------------                      --------------------    -------------------
10/3/2014 4:32:30 PM    518a3950-d034-46a1-9d2c-3c949EXAMPLE    ThreeQuartersHealthy    Amazon.CodeDeploy.Model.MinimumHealthyHosts
```
**Example 2: This example gets information about the definition of the specified deployment configuration.**

```
Write-Output ((Get-CDDeploymentConfig -DeploymentConfigName ThreeQuartersHealthy).MinimumHealthyHosts)
```
**Output:**

```
Type             Value
----             -----
FLEET_PERCENT    75
```
+  For API details, see [GetDeploymentConfig](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example gets summary information about the specified deployment configuration.**

```
Get-CDDeploymentConfig -DeploymentConfigName ThreeQuartersHealthy
```
**Output:**

```
CreateTime              DeploymentConfigId                      DeploymentConfigName    MinimumHealthyHosts
----------              ------------------                      --------------------    -------------------
10/3/2014 4:32:30 PM    518a3950-d034-46a1-9d2c-3c949EXAMPLE    ThreeQuartersHealthy    Amazon.CodeDeploy.Model.MinimumHealthyHosts
```
**Example 2: This example gets information about the definition of the specified deployment configuration.**

```
Write-Output ((Get-CDDeploymentConfig -DeploymentConfigName ThreeQuartersHealthy).MinimumHealthyHosts)
```
**Output:**

```
Type             Value
----             -----
FLEET_PERCENT    75
```
+  For API details, see [GetDeploymentConfig](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------
