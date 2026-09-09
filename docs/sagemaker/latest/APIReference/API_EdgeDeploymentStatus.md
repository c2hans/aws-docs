---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_EdgeDeploymentStatus.html
---

# EdgeDeploymentStatus
<a name="API_EdgeDeploymentStatus"></a>

Contains information summarizing the deployment stage results.

## Contents
<a name="API_EdgeDeploymentStatus_Contents"></a>

 ** EdgeDeploymentFailedInStage **   <a name="sagemaker-Type-EdgeDeploymentStatus-EdgeDeploymentFailedInStage"></a>
The number of edge devices that failed the deployment in current stage.
Type: Integer
Required: Yes

 ** EdgeDeploymentPendingInStage **   <a name="sagemaker-Type-EdgeDeploymentStatus-EdgeDeploymentPendingInStage"></a>
The number of edge devices yet to pick up the deployment in current stage, or in progress.
Type: Integer
Required: Yes

 ** EdgeDeploymentSuccessInStage **   <a name="sagemaker-Type-EdgeDeploymentStatus-EdgeDeploymentSuccessInStage"></a>
The number of edge devices with the successful deployment in the current stage.
Type: Integer
Required: Yes

 ** StageStatus **   <a name="sagemaker-Type-EdgeDeploymentStatus-StageStatus"></a>
The general status of the current stage.
Type: String
Valid Values: `CREATING | READYTODEPLOY | STARTING | INPROGRESS | DEPLOYED | FAILED | STOPPING | STOPPED`
Required: Yes

 ** EdgeDeploymentStatusMessage **   <a name="sagemaker-Type-EdgeDeploymentStatus-EdgeDeploymentStatusMessage"></a>
A detailed message about deployment status in current stage.
Type: String
Required: No

## See Also
<a name="API_EdgeDeploymentStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/EdgeDeploymentStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/EdgeDeploymentStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/EdgeDeploymentStatus)
