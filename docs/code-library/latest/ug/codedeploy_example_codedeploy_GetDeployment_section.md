---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/codedeploy_example_codedeploy_GetDeployment_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `GetDeployment` with a CLI
<a name="codedeploy_example_codedeploy_GetDeployment_section"></a>

The following code examples show how to use `GetDeployment`.

------
#### [ CLI ]

**AWS CLI**
**To get information about a deployment**
The following `get-deployment` example displays information about a deployment that is associated with the user's AWS account.

```
aws deploy get-deployment --deployment-id {{d-A1B2C3123}}
```
Output:

```
{
    "deploymentInfo": {
        "applicationName": "WordPress_App",
        "status": "Succeeded",
        "deploymentOverview": {
            "Failed": 0,
            "InProgress": 0,
            "Skipped": 0,
            "Succeeded": 1,
            "Pending": 0
        },
        "deploymentConfigName": "CodeDeployDefault.OneAtATime",
        "creator": "user",
        "description": "My WordPress app deployment",
        "revision": {
            "revisionType": "S3",
            "s3Location":  {
            "bundleType": "zip",
            "eTag": "\"dd56cfdEXAMPLE8e768f9d77fEXAMPLE\"",
            "bucket": "CodeDeployDemoBucket",
            "key": "WordPressApp.zip"
            }
        },
        "deploymentId": "d-A1B2C3123",
        "deploymentGroupName": "WordPress_DG",
        "createTime": 1409764576.589,
        "completeTime": 1409764596.101,
        "ignoreApplicationStopFailures": false
    }
}
```
+  For API details, see [GetDeployment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/get-deployment.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example gets summary information about the specified deployment.**

```
Get-CDDeployment -DeploymentId d-QZMRGSTEX
```
**Output:**

```
ApplicationName               : CodeDeployDemoApplication
CompleteTime                  : 7/23/2015 11:26:04 PM
CreateTime                    : 7/23/2015 11:24:43 PM
Creator                       : user
DeploymentConfigName          : CodeDeployDefault.OneAtATime
DeploymentGroupName           : CodeDeployDemoFleet
DeploymentId                  : d-QZMRGSTEX
DeploymentOverview            : Amazon.CodeDeploy.Model.DeploymentOverview
Description                   :
ErrorInformation              :
IgnoreApplicationStopFailures : False
Revision                      : Amazon.CodeDeploy.Model.RevisionLocation
StartTime                     : 1/1/0001 12:00:00 AM
Status                        : Succeeded
```
**Example 2: This example gets information about the status of instances that are participating in the specified deployment.**

```
(Get-CDDeployment -DeploymentId d-QZMRGSTEX).DeploymentOverview
```
**Output:**

```
Failed     : 0
InProgress : 0
Pending    : 0
Skipped    : 0
Succeeded  : 3
```
**Example 3: This example gets information about the application revision for the specified deployment.**

```
(Get-CDDeployment -DeploymentId d-QZMRGSTEX).Revision.S3Location
```
**Output:**

```
Bucket     : amzn-s3-demo-bucket
BundleType : zip
ETag       : cfbb81b304ee5e27efc21adaed3EXAMPLE
Key        : clzfqEX
Version    :
```
+  For API details, see [GetDeployment](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example gets summary information about the specified deployment.**

```
Get-CDDeployment -DeploymentId d-QZMRGSTEX
```
**Output:**

```
ApplicationName               : CodeDeployDemoApplication
CompleteTime                  : 7/23/2015 11:26:04 PM
CreateTime                    : 7/23/2015 11:24:43 PM
Creator                       : user
DeploymentConfigName          : CodeDeployDefault.OneAtATime
DeploymentGroupName           : CodeDeployDemoFleet
DeploymentId                  : d-QZMRGSTEX
DeploymentOverview            : Amazon.CodeDeploy.Model.DeploymentOverview
Description                   :
ErrorInformation              :
IgnoreApplicationStopFailures : False
Revision                      : Amazon.CodeDeploy.Model.RevisionLocation
StartTime                     : 1/1/0001 12:00:00 AM
Status                        : Succeeded
```
**Example 2: This example gets information about the status of instances that are participating in the specified deployment.**

```
(Get-CDDeployment -DeploymentId d-QZMRGSTEX).DeploymentOverview
```
**Output:**

```
Failed     : 0
InProgress : 0
Pending    : 0
Skipped    : 0
Succeeded  : 3
```
**Example 3: This example gets information about the application revision for the specified deployment.**

```
(Get-CDDeployment -DeploymentId d-QZMRGSTEX).Revision.S3Location
```
**Output:**

```
Bucket     : amzn-s3-demo-bucket
BundleType : zip
ETag       : cfbb81b304ee5e27efc21adaed3EXAMPLE
Key        : clzfqEX
Version    :
```
+  For API details, see [GetDeployment](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------
