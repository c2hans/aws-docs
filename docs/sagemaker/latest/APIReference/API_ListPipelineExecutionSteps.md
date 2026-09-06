---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListPipelineExecutionSteps.html
---

# ListPipelineExecutionSteps
<a name="API_ListPipelineExecutionSteps"></a>

Gets a list of `PipeLineExecutionStep` objects.

## Request Syntax
<a name="API_ListPipelineExecutionSteps_RequestSyntax"></a>

```
{
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "PipelineExecutionArn": "{{string}}",
   "SortOrder": "{{string}}"
}
```

## Request Parameters
<a name="API_ListPipelineExecutionSteps_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MaxResults](#API_ListPipelineExecutionSteps_RequestSyntax) **   <a name="sagemaker-ListPipelineExecutionSteps-request-MaxResults"></a>
The maximum number of pipeline execution steps to return in the response.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_ListPipelineExecutionSteps_RequestSyntax) **   <a name="sagemaker-ListPipelineExecutionSteps-request-NextToken"></a>
If the result of the previous `ListPipelineExecutionSteps` request was truncated, the response includes a `NextToken`. To retrieve the next set of pipeline execution steps, use the token in the next request.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`
Required: No

 ** [PipelineExecutionArn](#API_ListPipelineExecutionSteps_RequestSyntax) **   <a name="sagemaker-ListPipelineExecutionSteps-request-PipelineExecutionArn"></a>
The Amazon Resource Name (ARN) of the pipeline execution.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:pipeline\/.*\/execution\/.*`
Required: No

 ** [SortOrder](#API_ListPipelineExecutionSteps_RequestSyntax) **   <a name="sagemaker-ListPipelineExecutionSteps-request-SortOrder"></a>
The field by which to sort results. The default is `CreatedTime`.
Type: String
Valid Values: `Ascending | Descending`
Required: No

## Response Syntax
<a name="API_ListPipelineExecutionSteps_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "PipelineExecutionSteps": [
      {
         "AttemptCount": number,
         "CacheHitResult": {
            "SourcePipelineExecutionArn": "string"
         },
         "EndTime": number,
         "FailureReason": "string",
         "Metadata": {
            "AutoMLJob": {
               "Arn": "string"
            },
            "BedrockCustomModel": {
               "Arn": "string"
            },
            "BedrockCustomModelDeployment": {
               "Arn": "string"
            },
            "BedrockModelImport": {
               "Arn": "string"
            },
            "BedrockProvisionedModelThroughput": {
               "Arn": "string"
            },
            "Callback": {
               "CallbackToken": "string",
               "OutputParameters": [
                  {
                     "Name": "string",
                     "Value": "string"
                  }
               ],
               "SqsQueueUrl": "string"
            },
            "ClarifyCheck": {
               "BaselineUsedForDriftCheckConstraints": "string",
               "CalculatedBaselineConstraints": "string",
               "CheckJobArn": "string",
               "CheckType": "string",
               "ModelPackageGroupName": "string",
               "RegisterNewBaseline": boolean,
               "SkipCheck": boolean,
               "ViolationReport": "string"
            },
            "Condition": {
               "Outcome": "string"
            },
            "EMR": {
               "ClusterId": "string",
               "LogFilePath": "string",
               "StepId": "string",
               "StepName": "string"
            },
            "Endpoint": {
               "Arn": "string"
            },
            "EndpointConfig": {
               "Arn": "string"
            },
            "Fail": {
               "ErrorMessage": "string"
            },
            "InferenceComponent": {
               "Arn": "string"
            },
            "Job": {
               "Arn": "string"
            },
            "Lambda": {
               "Arn": "string",
               "OutputParameters": [
                  {
                     "Name": "string",
                     "Value": "string"
                  }
               ]
            },
            "Lineage": {
               "ActionArns": {
                  "string" : "string"
               },
               "ArtifactArns": {
                  "string" : "string"
               },
               "Associations": [
                  {
                     "DestinationArn": "string",
                     "SourceArn": "string"
                  }
               ],
               "ContextArns": {
                  "string" : "string"
               }
            },
            "Model": {
               "Arn": "string"
            },
            "ProcessingJob": {
               "Arn": "string"
            },
            "QualityCheck": {
               "BaselineUsedForDriftCheckConstraints": "string",
               "BaselineUsedForDriftCheckStatistics": "string",
               "CalculatedBaselineConstraints": "string",
               "CalculatedBaselineStatistics": "string",
               "CheckJobArn": "string",
               "CheckType": "string",
               "ModelPackageGroupName": "string",
               "RegisterNewBaseline": boolean,
               "SkipCheck": boolean,
               "ViolationReport": "string"
            },
            "RegisterModel": {
               "Arn": "string"
            },
            "TrainingJob": {
               "Arn": "string"
            },
            "TransformJob": {
               "Arn": "string"
            },
            "TuningJob": {
               "Arn": "string"
            }
         },
         "SelectiveExecutionResult": {
            "SourcePipelineExecutionArn": "string"
         },
         "StartTime": number,
         "StepDescription": "string",
         "StepDisplayName": "string",
         "StepName": "string",
         "StepStatus": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListPipelineExecutionSteps_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListPipelineExecutionSteps_ResponseSyntax) **   <a name="sagemaker-ListPipelineExecutionSteps-response-NextToken"></a>
If the result of the previous `ListPipelineExecutionSteps` request was truncated, the response includes a `NextToken`. To retrieve the next set of pipeline execution steps, use the token in the next request.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`

 ** [PipelineExecutionSteps](#API_ListPipelineExecutionSteps_ResponseSyntax) **   <a name="sagemaker-ListPipelineExecutionSteps-response-PipelineExecutionSteps"></a>
A list of `PipeLineExecutionStep` objects. Each `PipeLineExecutionStep` consists of StepName, StartTime, EndTime, StepStatus, and Metadata. Metadata is an object with properties for each job that contains relevant information about the job created by the step.
Type: Array of [PipelineExecutionStep](API_PipelineExecutionStep.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.

## Errors
<a name="API_ListPipelineExecutionSteps_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_ListPipelineExecutionSteps_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/ListPipelineExecutionSteps)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/ListPipelineExecutionSteps)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ListPipelineExecutionSteps)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/ListPipelineExecutionSteps)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ListPipelineExecutionSteps)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/ListPipelineExecutionSteps)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/ListPipelineExecutionSteps)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/ListPipelineExecutionSteps)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/ListPipelineExecutionSteps)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ListPipelineExecutionSteps)
