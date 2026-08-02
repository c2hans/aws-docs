---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeTrainingPlan.html
---

# DescribeTrainingPlan
<a name="API_DescribeTrainingPlan"></a>

Retrieves detailed information about a specific training plan.

## Request Syntax
<a name="API_DescribeTrainingPlan_RequestSyntax"></a>

```
{
   "TrainingPlanName": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeTrainingPlan_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [TrainingPlanName](#API_DescribeTrainingPlan_RequestSyntax) **   <a name="sagemaker-DescribeTrainingPlan-request-TrainingPlanName"></a>
The name of the training plan to describe.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,63}`
Required: Yes

## Response Syntax
<a name="API_DescribeTrainingPlan_ResponseSyntax"></a>

```
{
   "AvailableInstanceCount": number,
   "AvailableSpareInstanceCount": number,
   "CurrencyCode": "string",
   "DurationHours": number,
   "DurationMinutes": number,
   "EndTime": number,
   "InUseInstanceCount": number,
   "ReservedCapacitySummaries": [
      {
         "AvailabilityZone": "string",
         "AvailabilityZoneId": "string",
         "DurationHours": number,
         "DurationMinutes": number,
         "EndTime": number,
         "InstanceType": "string",
         "ReservedCapacityArn": "string",
         "ReservedCapacityType": "string",
         "StartTime": number,
         "Status": "string",
         "TotalInstanceCount": number,
         "UltraServerCount": number,
         "UltraServerType": "string"
      }
   ],
   "StartTime": number,
   "Status": "string",
   "StatusMessage": "string",
   "TargetResources": [ "string" ],
   "TotalInstanceCount": number,
   "TotalUltraServerCount": number,
   "TrainingPlanArn": "string",
   "TrainingPlanName": "string",
   "UnhealthyInstanceCount": number,
   "UpfrontFee": "string"
}
```

## Response Elements
<a name="API_DescribeTrainingPlan_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AvailableInstanceCount](#API_DescribeTrainingPlan_ResponseSyntax) **   <a name="sagemaker-DescribeTrainingPlan-response-AvailableInstanceCount"></a>
The number of instances currently available for use in this training plan.
Type: Integer
Valid Range: Minimum value of 0.

 ** [AvailableSpareInstanceCount](#API_DescribeTrainingPlan_ResponseSyntax) **   <a name="sagemaker-DescribeTrainingPlan-response-AvailableSpareInstanceCount"></a>
The number of available spare instances in the training plan.
Type: Integer
Valid Range: Minimum value of 0.

 ** [CurrencyCode](#API_DescribeTrainingPlan_ResponseSyntax) **   <a name="sagemaker-DescribeTrainingPlan-response-CurrencyCode"></a>
The currency code for the upfront fee (e.g., USD).
Type: String

 ** [DurationHours](#API_DescribeTrainingPlan_ResponseSyntax) **   <a name="sagemaker-DescribeTrainingPlan-response-DurationHours"></a>
The number of whole hours in the total duration for this training plan.
Type: Long
Valid Range: Minimum value of 0. Maximum value of 87600.

 ** [DurationMinutes](#API_DescribeTrainingPlan_ResponseSyntax) **   <a name="sagemaker-DescribeTrainingPlan-response-DurationMinutes"></a>
The additional minutes beyond whole hours in the total duration for this training plan.
Type: Long
Valid Range: Minimum value of 0. Maximum value of 59.

 ** [EndTime](#API_DescribeTrainingPlan_ResponseSyntax) **   <a name="sagemaker-DescribeTrainingPlan-response-EndTime"></a>
The end time of the training plan.
Type: Timestamp

 ** [InUseInstanceCount](#API_DescribeTrainingPlan_ResponseSyntax) **   <a name="sagemaker-DescribeTrainingPlan-response-InUseInstanceCount"></a>
The number of instances currently in use from this training plan.
Type: Integer
Valid Range: Minimum value of 0.

 ** [ReservedCapacitySummaries](#API_DescribeTrainingPlan_ResponseSyntax) **   <a name="sagemaker-DescribeTrainingPlan-response-ReservedCapacitySummaries"></a>
The list of Reserved Capacity providing the underlying compute resources of the plan.
Type: Array of [ReservedCapacitySummary](API_ReservedCapacitySummary.md) objects
Array Members: Minimum number of 0 items. Maximum number of 5 items.

 ** [StartTime](#API_DescribeTrainingPlan_ResponseSyntax) **   <a name="sagemaker-DescribeTrainingPlan-response-StartTime"></a>
The start time of the training plan.
Type: Timestamp

 ** [Status](#API_DescribeTrainingPlan_ResponseSyntax) **   <a name="sagemaker-DescribeTrainingPlan-response-Status"></a>
The current status of the training plan (e.g., Pending, Active, Expired). To see the complete list of status values available for a training plan, refer to the `Status` attribute within the ` [TrainingPlanSummary](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_TrainingPlanSummary.html) ` object.
Type: String
Valid Values: `Pending | Active | Scheduled | Expired | Failed`

 ** [StatusMessage](#API_DescribeTrainingPlan_ResponseSyntax) **   <a name="sagemaker-DescribeTrainingPlan-response-StatusMessage"></a>
A message providing additional information about the current status of the training plan.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.

 ** [TargetResources](#API_DescribeTrainingPlan_ResponseSyntax) **   <a name="sagemaker-DescribeTrainingPlan-response-TargetResources"></a>
The target resources (e.g., SageMaker Training Jobs, SageMaker HyperPod, SageMaker Endpoints, Studio apps) that can use this training plan.
Training plans are specific to their target resource.
+ A training plan designed for SageMaker training jobs can only be used to schedule and run training jobs.
+ A training plan for HyperPod clusters can be used exclusively to provide compute resources to a cluster's instance group.
+ A training plan for SageMaker endpoints can be used exclusively to provide compute resources to SageMaker endpoints for model deployment.
+ A training plan for Studio apps can be used to launch JupyterLab and Code Editor apps on reserved training plan capacity.
Type: Array of strings
Array Members: Minimum number of 1 item.
Valid Values: `training-job | hyperpod-cluster | endpoint | studio-apps`

 ** [TotalInstanceCount](#API_DescribeTrainingPlan_ResponseSyntax) **   <a name="sagemaker-DescribeTrainingPlan-response-TotalInstanceCount"></a>
The total number of instances reserved in this training plan.
Type: Integer
Valid Range: Minimum value of 0.

 ** [TotalUltraServerCount](#API_DescribeTrainingPlan_ResponseSyntax) **   <a name="sagemaker-DescribeTrainingPlan-response-TotalUltraServerCount"></a>
The total number of UltraServers reserved to this training plan.
Type: Integer
Valid Range: Minimum value of 1.

 ** [TrainingPlanArn](#API_DescribeTrainingPlan_ResponseSyntax) **   <a name="sagemaker-DescribeTrainingPlan-response-TrainingPlanArn"></a>
The Amazon Resource Name (ARN); of the training plan.
Type: String
Length Constraints: Minimum length of 50. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:training-plan/.*`

 ** [TrainingPlanName](#API_DescribeTrainingPlan_ResponseSyntax) **   <a name="sagemaker-DescribeTrainingPlan-response-TrainingPlanName"></a>
The name of the training plan.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,63}`

 ** [UnhealthyInstanceCount](#API_DescribeTrainingPlan_ResponseSyntax) **   <a name="sagemaker-DescribeTrainingPlan-response-UnhealthyInstanceCount"></a>
The number of instances in the training plan that are currently in an unhealthy state.
Type: Integer
Valid Range: Minimum value of 0.

 ** [UpfrontFee](#API_DescribeTrainingPlan_ResponseSyntax) **   <a name="sagemaker-DescribeTrainingPlan-response-UpfrontFee"></a>
The upfront fee for the training plan.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.

## Errors
<a name="API_DescribeTrainingPlan_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_DescribeTrainingPlan_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/DescribeTrainingPlan)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/DescribeTrainingPlan)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/DescribeTrainingPlan)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/DescribeTrainingPlan)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/DescribeTrainingPlan)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/DescribeTrainingPlan)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/DescribeTrainingPlan)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/DescribeTrainingPlan)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/DescribeTrainingPlan)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/DescribeTrainingPlan)
