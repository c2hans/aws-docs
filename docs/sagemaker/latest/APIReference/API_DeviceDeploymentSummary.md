---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DeviceDeploymentSummary.html
---

# DeviceDeploymentSummary
<a name="API_DeviceDeploymentSummary"></a>

Contains information summarizing device details and deployment status.

## Contents
<a name="API_DeviceDeploymentSummary_Contents"></a>

 ** DeviceArn **   <a name="sagemaker-Type-DeviceDeploymentSummary-DeviceArn"></a>
The ARN of the device.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:[a-z\-]*:[a-z\-]*:\d{12}:[a-z\-]*/?[a-zA-Z_0-9+=,.@\-_/]+`
Required: Yes

 ** DeviceName **   <a name="sagemaker-Type-DeviceDeploymentSummary-DeviceName"></a>
The name of the device.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

 ** EdgeDeploymentPlanArn **   <a name="sagemaker-Type-DeviceDeploymentSummary-EdgeDeploymentPlanArn"></a>
The ARN of the edge deployment plan.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z\-]*:\d{12}:edge-deployment/?[a-zA-Z_0-9+=,.@\-_/]+`
Required: Yes

 ** EdgeDeploymentPlanName **   <a name="sagemaker-Type-DeviceDeploymentSummary-EdgeDeploymentPlanName"></a>
The name of the edge deployment plan.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

 ** StageName **   <a name="sagemaker-Type-DeviceDeploymentSummary-StageName"></a>
The name of the stage in the edge deployment plan.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

 ** DeployedStageName **   <a name="sagemaker-Type-DeviceDeploymentSummary-DeployedStageName"></a>
The name of the deployed stage.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: No

 ** DeploymentStartTime **   <a name="sagemaker-Type-DeviceDeploymentSummary-DeploymentStartTime"></a>
The time when the deployment on the device started.
Type: Timestamp
Required: No

 ** Description **   <a name="sagemaker-Type-DeviceDeploymentSummary-Description"></a>
The description of the device.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 40.
Pattern: `[-a-zA-Z0-9_.,;:! ]*`
Required: No

 ** DeviceDeploymentStatus **   <a name="sagemaker-Type-DeviceDeploymentSummary-DeviceDeploymentStatus"></a>
The deployment status of the device.
Type: String
Valid Values: `READYTODEPLOY | INPROGRESS | DEPLOYED | FAILED | STOPPING | STOPPED`
Required: No

 ** DeviceDeploymentStatusMessage **   <a name="sagemaker-Type-DeviceDeploymentSummary-DeviceDeploymentStatusMessage"></a>
The detailed error message for the deployoment status result.
Type: String
Required: No

 ** DeviceFleetName **   <a name="sagemaker-Type-DeviceDeploymentSummary-DeviceFleetName"></a>
The name of the fleet to which the device belongs to.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: No

## See Also
<a name="API_DeviceDeploymentSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/DeviceDeploymentSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/DeviceDeploymentSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/DeviceDeploymentSummary)
