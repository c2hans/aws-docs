---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/codedeploy_example_codedeploy_StopDeployment_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `StopDeployment` with a CLI
<a name="codedeploy_example_codedeploy_StopDeployment_section"></a>

The following code examples show how to use `StopDeployment`.

------
#### [ CLI ]

**AWS CLI**
**To attempt to stop a deployment**
The following `stop-deployment` example attempts to stop an in-progress deployment that is associated with the user's AWS account.
aws deploy stop-deployment --deployment-id d-A1B2C3111
Output:

```
{
    "status": "Succeeded",
    "statusMessage": "No more commands will be scheduled for execution in the deployment instances"
}
```
+  For API details, see [StopDeployment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/stop-deployment.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example attempts to stop the deployment with the specified deployment ID.**

```
Stop-CDDeployment -DeploymentId d-LJQNREYEX
```
**Output:**

```
Status     StatusMessage
------     -------------
Pending    Stopping Pending. Stopping to schedule commands in the deployment instances
```
+  For API details, see [StopDeployment](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example attempts to stop the deployment with the specified deployment ID.**

```
Stop-CDDeployment -DeploymentId d-LJQNREYEX
```
**Output:**

```
Status     StatusMessage
------     -------------
Pending    Stopping Pending. Stopping to schedule commands in the deployment instances
```
+  For API details, see [StopDeployment](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------
