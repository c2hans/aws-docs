---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/codedeploy_example_codedeploy_DeleteDeploymentConfig_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `DeleteDeploymentConfig` with a CLI
<a name="codedeploy_example_codedeploy_DeleteDeploymentConfig_section"></a>

The following code examples show how to use `DeleteDeploymentConfig`.

------
#### [ CLI ]

**AWS CLI**
**To delete a deployment configuration**
The following `delete-deployment-config` example deletes a custom deployment configuration that is associated with the user's AWS account.

```
aws deploy delete-deployment-config --deployment-config-name {{ThreeQuartersHealthy}}
```
This command produces no output.
+  For API details, see [DeleteDeploymentConfig](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/delete-deployment-config.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example deletes the deployment configuration with the specified name. The command will prompt for confirmation before proceeding. Add the -Force parameter to delete the deployment configuration without a prompt.**

```
Remove-CDDeploymentConfig -DeploymentConfigName AtLeastTwoHealthyHosts
```
+  For API details, see [DeleteDeploymentConfig](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example deletes the deployment configuration with the specified name. The command will prompt for confirmation before proceeding. Add the -Force parameter to delete the deployment configuration without a prompt.**

```
Remove-CDDeploymentConfig -DeploymentConfigName AtLeastTwoHealthyHosts
```
+  For API details, see [DeleteDeploymentConfig](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------
