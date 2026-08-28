---
source_url: https://docs.aws.amazon.com/greengrass/v2/APIReference/API_EffectiveDeployment.html
---

# EffectiveDeployment
<a name="API_EffectiveDeployment"></a>

Contains information about a deployment job that AWS IoT Greengrass sends to a Greengrass core device.

## Contents
<a name="API_EffectiveDeployment_Contents"></a>

 ** coreDeviceExecutionStatus **   <a name="greengrassv2-Type-EffectiveDeployment-coreDeviceExecutionStatus"></a>
The status of the deployment job on the Greengrass core device.
+  `IN_PROGRESS` – The deployment job is running.
+  `QUEUED` – The deployment job is in the job queue and waiting to run.
+  `FAILED` – The deployment failed. For more information, see the `statusDetails` field.
+  `COMPLETED` – The deployment to an AWS IoT thing was completed successfully.
+  `TIMED_OUT` – The deployment didn't complete in the allotted time.
+  `CANCELED` – The deployment was canceled by the user.
+  `REJECTED` – The deployment was rejected. For more information, see the `statusDetails` field.
+  `SUCCEEDED` – The deployment to an AWS IoT thing group was completed successfully.
Type: String
Valid Values: `IN_PROGRESS | QUEUED | FAILED | COMPLETED | TIMED_OUT | CANCELED | REJECTED | SUCCEEDED`
Required: Yes

 ** creationTimestamp **   <a name="greengrassv2-Type-EffectiveDeployment-creationTimestamp"></a>
The time at which the deployment was created, expressed in ISO 8601 format.
Type: Timestamp
Required: Yes

 ** deploymentId **   <a name="greengrassv2-Type-EffectiveDeployment-deploymentId"></a>
The ID of the deployment.
Type: String
Required: Yes

 ** deploymentName **   <a name="greengrassv2-Type-EffectiveDeployment-deploymentName"></a>
The name of the deployment.
Type: String
Required: Yes

 ** modifiedTimestamp **   <a name="greengrassv2-Type-EffectiveDeployment-modifiedTimestamp"></a>
The time at which the deployment job was last modified, expressed in ISO 8601 format.
Type: Timestamp
Required: Yes

 ** targetArn **   <a name="greengrassv2-Type-EffectiveDeployment-targetArn"></a>
The [ARN](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) of the target AWS IoT thing or thing group.
Type: String
Pattern: `arn:[^:]*:iot:[^:]*:[0-9]+:(thing|thinggroup)/.+`
Required: Yes

 ** description **   <a name="greengrassv2-Type-EffectiveDeployment-description"></a>
The description of the deployment job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: No

 ** iotJobArn **   <a name="greengrassv2-Type-EffectiveDeployment-iotJobArn"></a>
The [ARN](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) of the AWS IoT job that applies the deployment to target devices.
Type: String
Pattern: `arn:[^:]*:iot:[^:]+:[0-9]+:job/.+`
Required: No

 ** iotJobId **   <a name="greengrassv2-Type-EffectiveDeployment-iotJobId"></a>
The ID of the AWS IoT job that applies the deployment to target devices.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** reason **   <a name="greengrassv2-Type-EffectiveDeployment-reason"></a>
The reason code for the update, if the job was updated.
Type: String
Required: No

 ** statusDetails **   <a name="greengrassv2-Type-EffectiveDeployment-statusDetails"></a>
The status details that explain why a deployment has an error. This response will be null if the deployment is in a success state.
Type: [EffectiveDeploymentStatusDetails](API_EffectiveDeploymentStatusDetails.md) object
Required: No

## See Also
<a name="API_EffectiveDeployment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/greengrassv2-2020-11-30/EffectiveDeployment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/greengrassv2-2020-11-30/EffectiveDeployment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/greengrassv2-2020-11-30/EffectiveDeployment)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Greengrass. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query greengrass` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
