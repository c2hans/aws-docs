---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_SearchTrainingPlanOfferings.html
---

# SearchTrainingPlanOfferings
<a name="API_SearchTrainingPlanOfferings"></a>

Searches for available training plan offerings based on specified criteria.
+ Users search for available plan offerings based on their requirements (e.g., instance type, count, start time, duration).
+ And then, they create a plan that best matches their needs using the ID of the plan offering they want to use.

For more information about how to reserve GPU capacity for your SageMaker training jobs or SageMaker HyperPod clusters using Amazon SageMaker Training Plan , see ` [CreateTrainingPlan](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateTrainingPlan.html) `.

## Request Syntax
<a name="API_SearchTrainingPlanOfferings_RequestSyntax"></a>

```
{
   "DurationHours": {{number}},
   "InstanceCount": {{number}},
   "InstanceType": "{{string}}",
   "TargetResources": [ "{{string}}" ],
   "TrainingPlanArn": "{{string}}",
   "UltraServerCount": {{number}},
   "UltraServerType": "{{string}}"
}
```

## Request Parameters
<a name="API_SearchTrainingPlanOfferings_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [DurationHours](#API_SearchTrainingPlanOfferings_RequestSyntax) **   <a name="sagemaker-SearchTrainingPlanOfferings-request-DurationHours"></a>
The desired duration in hours for the training plan offerings.
Type: Long
Valid Range: Minimum value of 1. Maximum value of 87600.
Required: No

 ** [InstanceCount](#API_SearchTrainingPlanOfferings_RequestSyntax) **   <a name="sagemaker-SearchTrainingPlanOfferings-request-InstanceCount"></a>
The number of instances you want to reserve in the training plan offerings. This allows you to specify the quantity of compute resources needed for your SageMaker training jobs or SageMaker HyperPod clusters, helping you find reserved capacity offerings that match your requirements.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 256.
Required: No

 ** [InstanceType](#API_SearchTrainingPlanOfferings_RequestSyntax) **   <a name="sagemaker-SearchTrainingPlanOfferings-request-InstanceType"></a>
The type of instance you want to search for in the available training plan offerings. This field allows you to filter the search results based on the specific compute resources you require for your SageMaker training jobs or SageMaker HyperPod clusters. When searching for training plan offerings, specifying the instance type helps you find Reserved Instances that match your computational needs.
Type: String
Valid Values: `ml.p4d.24xlarge | ml.p5.48xlarge | ml.p5e.48xlarge | ml.p5en.48xlarge | ml.trn1.32xlarge | ml.trn2.48xlarge | ml.p6-b200.48xlarge | ml.p4de.24xlarge | ml.p6e-gb200.36xlarge | ml.p5.4xlarge | ml.p6-b300.48xlarge`
Required: No

 ** [TargetResources](#API_SearchTrainingPlanOfferings_RequestSyntax) **   <a name="sagemaker-SearchTrainingPlanOfferings-request-TargetResources"></a>
The target resources (e.g., SageMaker Training Jobs, SageMaker HyperPod, SageMaker Endpoints, Studio apps) to search for in the offerings.
Training plans are specific to their target resource.
+ A training plan designed for SageMaker training jobs can only be used to schedule and run training jobs.
+ A training plan for HyperPod clusters can be used exclusively to provide compute resources to a cluster's instance group.
+ A training plan for SageMaker endpoints can be used exclusively to provide compute resources to SageMaker endpoints for model deployment.
+ A training plan for Studio apps can be used to launch JupyterLab and Code Editor apps on reserved training plan capacity.
Type: Array of strings
Array Members: Minimum number of 1 item.
Valid Values: `training-job | hyperpod-cluster | endpoint | studio-apps`
Required: No

 ** [TrainingPlanArn](#API_SearchTrainingPlanOfferings_RequestSyntax) **   <a name="sagemaker-SearchTrainingPlanOfferings-request-TrainingPlanArn"></a>
The Amazon Resource Name (ARN); of an existing training plan to search for extension offerings. When specified, the API returns extension offerings that can be used to extend the specified training plan.
Type: String
Required: No

 ** [UltraServerCount](#API_SearchTrainingPlanOfferings_RequestSyntax) **   <a name="sagemaker-SearchTrainingPlanOfferings-request-UltraServerCount"></a>
The number of UltraServers to search for.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** [UltraServerType](#API_SearchTrainingPlanOfferings_RequestSyntax) **   <a name="sagemaker-SearchTrainingPlanOfferings-request-UltraServerType"></a>
The type of UltraServer to search for, such as ml.u-p6e-gb200x72.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `ml.[a-z0-9\-.]+`
Required: No

## Response Syntax
<a name="API_SearchTrainingPlanOfferings_ResponseSyntax"></a>

```
{
   "TrainingPlanExtensionOfferings": [
      {
         "AvailabilityZone": "string",
         "CurrencyCode": "string",
         "DurationHours": number,
         "TrainingPlanExtensionOfferingId": "string",
         "UpfrontFee": "string"
      }
   ],
   "TrainingPlanOfferings": [
      {
         "CurrencyCode": "string",
         "DurationHours": number,
         "DurationMinutes": number,
         "ReservedCapacityOfferings": [
            {
               "AvailabilityZone": "string",
               "DurationHours": number,
               "DurationMinutes": number,
               "InstanceCount": number,
               "InstanceType": "string",
               "ReservedCapacityType": "string",
               "UltraServerCount": number,
               "UltraServerType": "string"
            }
         ],
         "TargetResources": [ "string" ],
         "TrainingPlanOfferingId": "string",
         "UpfrontFee": "string"
      }
   ]
}
```

## Response Elements
<a name="API_SearchTrainingPlanOfferings_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [TrainingPlanExtensionOfferings](#API_SearchTrainingPlanOfferings_ResponseSyntax) **   <a name="sagemaker-SearchTrainingPlanOfferings-response-TrainingPlanExtensionOfferings"></a>
A list of extension offerings available for the specified training plan. These offerings can be used with the ` [ExtendTrainingPlan](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ExtendTrainingPlan.html) ` API to extend an existing training plan.
Type: Array of [TrainingPlanExtensionOffering](API_TrainingPlanExtensionOffering.md) objects
Array Members: Minimum number of 0 items.

 ** [TrainingPlanOfferings](#API_SearchTrainingPlanOfferings_ResponseSyntax) **   <a name="sagemaker-SearchTrainingPlanOfferings-response-TrainingPlanOfferings"></a>
A list of training plan offerings that match the search criteria.
Type: Array of [TrainingPlanOffering](API_TrainingPlanOffering.md) objects
Array Members: Minimum number of 0 items.

## Errors
<a name="API_SearchTrainingPlanOfferings_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceLimitExceeded **
 You have exceeded an SageMaker resource limit. For example, you might have too many training jobs created.
HTTP Status Code: 400

## See Also
<a name="API_SearchTrainingPlanOfferings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/SearchTrainingPlanOfferings)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/SearchTrainingPlanOfferings)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/SearchTrainingPlanOfferings)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/SearchTrainingPlanOfferings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/SearchTrainingPlanOfferings)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/SearchTrainingPlanOfferings)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/SearchTrainingPlanOfferings)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/SearchTrainingPlanOfferings)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/SearchTrainingPlanOfferings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/SearchTrainingPlanOfferings)
