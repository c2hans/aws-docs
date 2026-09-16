---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListInferenceRecommendationsJobSteps.html
---

# ListInferenceRecommendationsJobSteps
<a name="API_ListInferenceRecommendationsJobSteps"></a>

Returns a list of the subtasks for an Inference Recommender job.

The supported subtasks are benchmarks, which evaluate the performance of your model on different instance types.

## Request Syntax
<a name="API_ListInferenceRecommendationsJobSteps_RequestSyntax"></a>

```
{
   "JobName": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "Status": "{{string}}",
   "StepType": "{{string}}"
}
```

## Request Parameters
<a name="API_ListInferenceRecommendationsJobSteps_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [JobName](#API_ListInferenceRecommendationsJobSteps_RequestSyntax) **   <a name="sagemaker-ListInferenceRecommendationsJobSteps-request-JobName"></a>
The name for the Inference Recommender job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,63}`
Required: Yes

 ** [MaxResults](#API_ListInferenceRecommendationsJobSteps_RequestSyntax) **   <a name="sagemaker-ListInferenceRecommendationsJobSteps-request-MaxResults"></a>
The maximum number of results to return.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_ListInferenceRecommendationsJobSteps_RequestSyntax) **   <a name="sagemaker-ListInferenceRecommendationsJobSteps-request-NextToken"></a>
A token that you can specify to return more results from the list. Specify this field if you have a token that was returned from a previous request.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`
Required: No

 ** [Status](#API_ListInferenceRecommendationsJobSteps_RequestSyntax) **   <a name="sagemaker-ListInferenceRecommendationsJobSteps-request-Status"></a>
A filter to return benchmarks of a specified status. If this field is left empty, then all benchmarks are returned.
Type: String
Valid Values: `PENDING | IN_PROGRESS | COMPLETED | FAILED | STOPPING | STOPPED | DELETING | DELETED`
Required: No

 ** [StepType](#API_ListInferenceRecommendationsJobSteps_RequestSyntax) **   <a name="sagemaker-ListInferenceRecommendationsJobSteps-request-StepType"></a>
A filter to return details about the specified type of subtask.
 `BENCHMARK`: Evaluate the performance of your model on different instance types.
Type: String
Valid Values: `BENCHMARK`
Required: No

## Response Syntax
<a name="API_ListInferenceRecommendationsJobSteps_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "Steps": [
      {
         "InferenceBenchmark": {
            "EndpointConfiguration": {
               "EndpointName": "string",
               "InitialInstanceCount": number,
               "InstanceType": "string",
               "ServerlessConfig": {
                  "MaxConcurrency": number,
                  "MemorySizeInMB": number,
                  "ProvisionedConcurrency": number
               },
               "VariantName": "string"
            },
            "EndpointMetrics": {
               "MaxInvocations": number,
               "ModelLatency": number
            },
            "FailureReason": "string",
            "InvocationEndTime": number,
            "InvocationStartTime": number,
            "Metrics": {
               "CostPerHour": number,
               "CostPerInference": number,
               "CpuUtilization": number,
               "MaxInvocations": number,
               "MemoryUtilization": number,
               "ModelLatency": number,
               "ModelSetupTime": number
            },
            "ModelConfiguration": {
               "CompilationJobName": "string",
               "EnvironmentParameters": [
                  {
                     "Key": "string",
                     "Value": "string",
                     "ValueType": "string"
                  }
               ],
               "InferenceSpecificationName": "string"
            }
         },
         "JobName": "string",
         "Status": "string",
         "StepType": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListInferenceRecommendationsJobSteps_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListInferenceRecommendationsJobSteps_ResponseSyntax) **   <a name="sagemaker-ListInferenceRecommendationsJobSteps-response-NextToken"></a>
A token that you can specify in your next request to return more results from the list.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`

 ** [Steps](#API_ListInferenceRecommendationsJobSteps_ResponseSyntax) **   <a name="sagemaker-ListInferenceRecommendationsJobSteps-response-Steps"></a>
A list of all subtask details in Inference Recommender.
Type: Array of [InferenceRecommendationsJobStep](API_InferenceRecommendationsJobStep.md) objects

## Errors
<a name="API_ListInferenceRecommendationsJobSteps_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_ListInferenceRecommendationsJobSteps_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/ListInferenceRecommendationsJobSteps)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/ListInferenceRecommendationsJobSteps)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ListInferenceRecommendationsJobSteps)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/ListInferenceRecommendationsJobSteps)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ListInferenceRecommendationsJobSteps)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/ListInferenceRecommendationsJobSteps)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/ListInferenceRecommendationsJobSteps)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/ListInferenceRecommendationsJobSteps)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/ListInferenceRecommendationsJobSteps)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ListInferenceRecommendationsJobSteps)
