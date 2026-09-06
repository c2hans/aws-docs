---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/codedeploy_example_codedeploy_CreateDeployment_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `CreateDeployment` with a CLI
<a name="codedeploy_example_codedeploy_CreateDeployment_section"></a>

The following code examples show how to use `CreateDeployment`.

------
#### [ CLI ]

**AWS CLI**
**Example 1: To create a CodeDeploy deployment using the EC2/On-premises compute platform**
The following `create-deployment` example creates a deployment and associates it with the user's AWS account.

```
aws deploy create-deployment \
    --application-name {{WordPress_App}} \
    --deployment-config-name {{CodeDeployDefault.OneAtATime}} \
    --deployment-group-name {{WordPress_DG}} \
    --description {{"My demo deployment"}} \
    --s3-location {{bucket=amzn-s3-demo-bucket,bundleType=zip,eTag=dd56cfdEXAMPLE8e768f9d77fEXAMPLE,key=WordPressApp.zip}}
```
Output:

```
{
    "deploymentId": "d-A1B2C3111"
}
```
**Example 2: To create a CodeDeploy deployment using the Amazon ECS compute platform**
The following `create-deployment` example uses the following two files to deploy an Amazon ECS service.
Contents of `create-deployment.json` file:

```
{
    "applicationName": "ecs-deployment",
    "deploymentGroupName": "ecs-deployment-dg",
    "revision": {
        "revisionType": "S3",
        "s3Location": {
            "bucket": "ecs-deployment-bucket",
            "key": "appspec.yaml",
            "bundleType": "YAML"
        }
    }
}
```
That file, in turn, retrieves the following file `appspec.yaml` from an S3 bucket called `ecs-deployment-bucket`.

```
version: 0.0
Resources:
  - TargetService:
      Type: AWS::ECS::Service
      Properties:
        TaskDefinition: "arn:aws:ecs:region:123456789012:task-definition/ecs-task-def:2"
        LoadBalancerInfo:
          ContainerName: "sample-app"
          ContainerPort: 80
        PlatformVersion: "LATEST"
```
Command:

```
aws deploy create-deployment \
    --cli-input-json {{file://create-deployment.json}} \
    --region {{us-east-1}}
```
Output:

```
{
    "deploymentId": "d-1234ABCDE"
}
```
For more information, see [CreateDeployment](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_CreateDeployment.html) in the *AWS CodeDeploy API Reference*.
+  For API details, see [CreateDeployment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/create-deployment.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example creates a new deployment for the specified application and deployment group with the specified deployment configuration and application revision.**

```
New-CDDeployment -ApplicationName MyNewApplication -S3Location_Bucket amzn-s3-demo-bucket -S3Location_BundleType zip -DeploymentConfigName CodeDeployDefault.OneAtATime -DeploymentGroupName MyNewDeploymentGroup -IgnoreApplicationStopFailures $True -S3Location_Key aws-codedeploy_linux-master.zip -RevisionType S3
```
**Output:**

```
d-ZHROG7UEX
```
**Example 2: This example shows how to specify groups of EC2 instance tags that an instance must be identified by in order for it to be included in the replacement environment for a blue/green deployment.**

```
New-CDDeployment -ApplicationName MyNewApplication -S3Location_Bucket amzn-s3-demo-bucket -S3Location_BundleType zip -DeploymentConfigName CodeDeployDefault.OneAtATime -DeploymentGroupName MyNewDeploymentGroup -IgnoreApplicationStopFailures $True -S3Location_Key aws-codedeploy_linux-master.zip -RevisionType S3 -Ec2TagSetList @(@{Key="key1";Type="KEY_ONLY"},@{Key="Key2";Type="KEY_AND_VALUE";Value="Value2"}),@(@{Key="Key3";Type="VALUE_ONLY";Value="Value3"})
```
**Output:**

```
d-ZHROG7UEX
```
+  For API details, see [CreateDeployment](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example creates a new deployment for the specified application and deployment group with the specified deployment configuration and application revision.**

```
New-CDDeployment -ApplicationName MyNewApplication -S3Location_Bucket amzn-s3-demo-bucket -S3Location_BundleType zip -DeploymentConfigName CodeDeployDefault.OneAtATime -DeploymentGroupName MyNewDeploymentGroup -IgnoreApplicationStopFailures $True -S3Location_Key aws-codedeploy_linux-master.zip -RevisionType S3
```
**Output:**

```
d-ZHROG7UEX
```
**Example 2: This example shows how to specify groups of EC2 instance tags that an instance must be identified by in order for it to be included in the replacement environment for a blue/green deployment.**

```
New-CDDeployment -ApplicationName MyNewApplication -S3Location_Bucket amzn-s3-demo-bucket -S3Location_BundleType zip -DeploymentConfigName CodeDeployDefault.OneAtATime -DeploymentGroupName MyNewDeploymentGroup -IgnoreApplicationStopFailures $True -S3Location_Key aws-codedeploy_linux-master.zip -RevisionType S3 -Ec2TagSetList @(@{Key="key1";Type="KEY_ONLY"},@{Key="Key2";Type="KEY_AND_VALUE";Value="Value2"}),@(@{Key="Key3";Type="VALUE_ONLY";Value="Value3"})
```
**Output:**

```
d-ZHROG7UEX
```
+  For API details, see [CreateDeployment](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------
