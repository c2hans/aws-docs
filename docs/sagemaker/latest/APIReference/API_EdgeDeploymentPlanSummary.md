---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_EdgeDeploymentPlanSummary.html
---

# EdgeDeploymentPlanSummary
<a name="API_EdgeDeploymentPlanSummary"></a>

Contains information summarizing an edge deployment plan.

## Contents
<a name="API_EdgeDeploymentPlanSummary_Contents"></a>

 ** DeviceFleetName **   <a name="sagemaker-Type-EdgeDeploymentPlanSummary-DeviceFleetName"></a>
The name of the device fleet used for the deployment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

 ** EdgeDeploymentFailed **   <a name="sagemaker-Type-EdgeDeploymentPlanSummary-EdgeDeploymentFailed"></a>
The number of edge devices that failed the deployment.
Type: Integer
Required: Yes

 ** EdgeDeploymentPending **   <a name="sagemaker-Type-EdgeDeploymentPlanSummary-EdgeDeploymentPending"></a>
The number of edge devices yet to pick up the deployment, or in progress.
Type: Integer
Required: Yes

 ** EdgeDeploymentPlanArn **   <a name="sagemaker-Type-EdgeDeploymentPlanSummary-EdgeDeploymentPlanArn"></a>
The ARN of the edge deployment plan.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z\-]*:\d{12}:edge-deployment/?[a-zA-Z_0-9+=,.@\-_/]+`
Required: Yes

 ** EdgeDeploymentPlanName **   <a name="sagemaker-Type-EdgeDeploymentPlanSummary-EdgeDeploymentPlanName"></a>
The name of the edge deployment plan.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

 ** EdgeDeploymentSuccess **   <a name="sagemaker-Type-EdgeDeploymentPlanSummary-EdgeDeploymentSuccess"></a>
The number of edge devices with the successful deployment.
Type: Integer
Required: Yes

## See Also
<a name="API_EdgeDeploymentPlanSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/EdgeDeploymentPlanSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/EdgeDeploymentPlanSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/EdgeDeploymentPlanSummary)
