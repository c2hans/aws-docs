---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateTrainingPlan.html
---

# CreateTrainingPlan
<a name="API_CreateTrainingPlan"></a>

Creates a new training plan in SageMaker to reserve compute capacity.

Amazon SageMaker Training Plan is a capability within SageMaker that allows customers to reserve and manage GPU capacity for large-scale AI model training. It provides a way to secure predictable access to computational resources within specific timelines and budgets, without the need to manage underlying infrastructure.

 **How it works**

Plans can be created for specific resources such as SageMaker Training Jobs or SageMaker HyperPod clusters, automatically provisioning resources, setting up infrastructure, executing workloads, and handling infrastructure failures.

 **Plan creation workflow**
+ Users search for available plan offerings based on their requirements (e.g., instance type, count, start time, duration) using the ` [SearchTrainingPlanOfferings](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_SearchTrainingPlanOfferings.html) ` API operation.
+ They create a plan that best matches their needs using the ID of the plan offering they want to use.
+ After successful upfront payment, the plan's status becomes `Scheduled`.
+ The plan can be used to:
  + Queue training jobs.
  + Allocate to an instance group of a SageMaker HyperPod cluster.
+ When the plan start date arrives, it becomes `Active`. Based on available reserved capacity:
  + Training jobs are launched.
  + Instance groups are provisioned.

 **Plan composition**

A plan can consist of one or more Reserved Capacities, each defined by a specific instance type, quantity, Availability Zone, duration, and start and end times. For more information about Reserved Capacity, see ` [ReservedCapacitySummary](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ReservedCapacitySummary.html) `.

## Request Syntax
<a name="API_CreateTrainingPlan_RequestSyntax"></a>

```
{
   "SpareInstanceCountPerUltraServer": {{number}},
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "TrainingPlanName": "{{string}}",
   "TrainingPlanOfferingId": "{{string}}"
}
```

## Request Parameters
<a name="API_CreateTrainingPlan_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [SpareInstanceCountPerUltraServer](#API_CreateTrainingPlan_RequestSyntax) **   <a name="sagemaker-CreateTrainingPlan-request-SpareInstanceCountPerUltraServer"></a>
Number of spare instances to reserve per UltraServer for enhanced resiliency. Default is 1.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** [Tags](#API_CreateTrainingPlan_RequestSyntax) **   <a name="sagemaker-CreateTrainingPlan-request-Tags"></a>
An array of key-value pairs to apply to this training plan.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

 ** [TrainingPlanName](#API_CreateTrainingPlan_RequestSyntax) **   <a name="sagemaker-CreateTrainingPlan-request-TrainingPlanName"></a>
The name of the training plan to create.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,63}`
Required: Yes

 ** [TrainingPlanOfferingId](#API_CreateTrainingPlan_RequestSyntax) **   <a name="sagemaker-CreateTrainingPlan-request-TrainingPlanOfferingId"></a>
The unique identifier of the training plan offering to use for creating this plan.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-z0-9\-]+`
Required: Yes

## Response Syntax
<a name="API_CreateTrainingPlan_ResponseSyntax"></a>

```
{
   "TrainingPlanArn": "string"
}
```

## Response Elements
<a name="API_CreateTrainingPlan_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [TrainingPlanArn](#API_CreateTrainingPlan_ResponseSyntax) **   <a name="sagemaker-CreateTrainingPlan-response-TrainingPlanArn"></a>
The Amazon Resource Name (ARN); of the created training plan.
Type: String
Length Constraints: Minimum length of 50. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:training-plan/.*`

## Errors
<a name="API_CreateTrainingPlan_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceInUse **
Resource being accessed is in use.
HTTP Status Code: 400

 ** ResourceLimitExceeded **
 You have exceeded an SageMaker resource limit. For example, you might have too many training jobs created.
HTTP Status Code: 400

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_CreateTrainingPlan_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/CreateTrainingPlan)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/CreateTrainingPlan)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/CreateTrainingPlan)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/CreateTrainingPlan)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/CreateTrainingPlan)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/CreateTrainingPlan)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/CreateTrainingPlan)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/CreateTrainingPlan)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/CreateTrainingPlan)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/CreateTrainingPlan)
