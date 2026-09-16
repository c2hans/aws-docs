---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeLabelingJob.html
---

# DescribeLabelingJob
<a name="API_DescribeLabelingJob"></a>

Gets information about a labeling job.

## Request Syntax
<a name="API_DescribeLabelingJob_RequestSyntax"></a>

```
{
   "LabelingJobName": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeLabelingJob_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [LabelingJobName](#API_DescribeLabelingJob_RequestSyntax) **   <a name="sagemaker-DescribeLabelingJob-request-LabelingJobName"></a>
The name of the labeling job to return information for.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

## Response Syntax
<a name="API_DescribeLabelingJob_ResponseSyntax"></a>

```
{
   "FailureReason": "string",
   "HumanTaskConfig": {
      "AnnotationConsolidationConfig": {
         "AnnotationConsolidationLambdaArn": "string"
      },
      "MaxConcurrentTaskCount": number,
      "NumberOfHumanWorkersPerDataObject": number,
      "PreHumanTaskLambdaArn": "string",
      "PublicWorkforceTaskPrice": {
         "AmountInUsd": {
            "Cents": number,
            "Dollars": number,
            "TenthFractionsOfACent": number
         }
      },
      "TaskAvailabilityLifetimeInSeconds": number,
      "TaskDescription": "string",
      "TaskKeywords": [ "string" ],
      "TaskTimeLimitInSeconds": number,
      "TaskTitle": "string",
      "UiConfig": {
         "HumanTaskUiArn": "string",
         "UiTemplateS3Uri": "string"
      },
      "WorkteamArn": "string"
   },
   "InputConfig": {
      "DataAttributes": {
         "ContentClassifiers": [ "string" ]
      },
      "DataSource": {
         "S3DataSource": {
            "ManifestS3Uri": "string"
         },
         "SnsDataSource": {
            "SnsTopicArn": "string"
         }
      }
   },
   "JobReferenceCode": "string",
   "LabelAttributeName": "string",
   "LabelCategoryConfigS3Uri": "string",
   "LabelCounters": {
      "FailedNonRetryableError": number,
      "HumanLabeled": number,
      "MachineLabeled": number,
      "TotalLabeled": number,
      "Unlabeled": number
   },
   "LabelingJobAlgorithmsConfig": {
      "InitialActiveLearningModelArn": "string",
      "LabelingJobAlgorithmSpecificationArn": "string",
      "LabelingJobResourceConfig": {
         "VolumeKmsKeyId": "string",
         "VpcConfig": {
            "SecurityGroupIds": [ "string" ],
            "Subnets": [ "string" ]
         }
      }
   },
   "LabelingJobArn": "string",
   "LabelingJobName": "string",
   "LabelingJobOutput": {
      "FinalActiveLearningModelArn": "string",
      "OutputDatasetS3Uri": "string"
   },
   "LabelingJobStatus": "string",
   "OutputConfig": {
      "KmsKeyId": "string",
      "S3OutputPath": "string",
      "SnsTopicArn": "string"
   },
   "RoleArn": "string",
   "StoppingConditions": {
      "MaxHumanLabeledObjectCount": number,
      "MaxPercentageOfInputDatasetLabeled": number
   },
   "Tags": [
      {
         "Key": "string",
         "Value": "string"
      }
   ]
}
```

## Response Elements
<a name="API_DescribeLabelingJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [FailureReason](#API_DescribeLabelingJob_ResponseSyntax) **   <a name="sagemaker-DescribeLabelingJob-response-FailureReason"></a>
If the job failed, the reason that it failed.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.

 ** [HumanTaskConfig](#API_DescribeLabelingJob_ResponseSyntax) **   <a name="sagemaker-DescribeLabelingJob-response-HumanTaskConfig"></a>
Configuration information required for human workers to complete a labeling task.
Type: [HumanTaskConfig](API_HumanTaskConfig.md) object

 ** [InputConfig](#API_DescribeLabelingJob_ResponseSyntax) **   <a name="sagemaker-DescribeLabelingJob-response-InputConfig"></a>
Input configuration information for the labeling job, such as the Amazon S3 location of the data objects and the location of the manifest file that describes the data objects.
Type: [LabelingJobInputConfig](API_LabelingJobInputConfig.md) object

 ** [JobReferenceCode](#API_DescribeLabelingJob_ResponseSyntax) **   <a name="sagemaker-DescribeLabelingJob-response-JobReferenceCode"></a>
A unique identifier for work done as part of a labeling job.
Type: String
Length Constraints: Minimum length of 1.
Pattern: `.+`

 ** [LabelAttributeName](#API_DescribeLabelingJob_ResponseSyntax) **   <a name="sagemaker-DescribeLabelingJob-response-LabelAttributeName"></a>
The attribute used as the label in the output manifest file.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 127.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,126}`

 ** [LabelCategoryConfigS3Uri](#API_DescribeLabelingJob_ResponseSyntax) **   <a name="sagemaker-DescribeLabelingJob-response-LabelCategoryConfigS3Uri"></a>
The S3 location of the JSON file that defines the categories used to label data objects. Please note the following label-category limits:
+ Semantic segmentation labeling jobs using automated labeling: 20 labels
+ Box bounding labeling jobs (all): 10 labels
The file is a JSON structure in the following format:
 `{`
 ` "document-version": "2018-11-28"`
 ` "labels": [`
 ` {`
 ` "label": "label 1"`
 ` },`
 ` {`
 ` "label": "label 2"`
 ` },`
 ` ...`
 ` {`
 ` "label": "label n"`
 ` }`
 ` ]`
 `}`
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `(https|s3)://([^/]+)/?(.*)`

 ** [LabelCounters](#API_DescribeLabelingJob_ResponseSyntax) **   <a name="sagemaker-DescribeLabelingJob-response-LabelCounters"></a>
Provides a breakdown of the number of data objects labeled by humans, the number of objects labeled by machine, the number of objects than couldn't be labeled, and the total number of objects labeled.
Type: [LabelCounters](API_LabelCounters.md) object

 ** [LabelingJobAlgorithmsConfig](#API_DescribeLabelingJob_ResponseSyntax) **   <a name="sagemaker-DescribeLabelingJob-response-LabelingJobAlgorithmsConfig"></a>
Configuration information for automated data labeling.
Type: [LabelingJobAlgorithmsConfig](API_LabelingJobAlgorithmsConfig.md) object

 ** [LabelingJobArn](#API_DescribeLabelingJob_ResponseSyntax) **   <a name="sagemaker-DescribeLabelingJob-response-LabelingJobArn"></a>
The Amazon Resource Name (ARN) of the labeling job.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:labeling-job/.*`

 ** [LabelingJobName](#API_DescribeLabelingJob_ResponseSyntax) **   <a name="sagemaker-DescribeLabelingJob-response-LabelingJobName"></a>
The name assigned to the labeling job when it was created.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`

 ** [LabelingJobOutput](#API_DescribeLabelingJob_ResponseSyntax) **   <a name="sagemaker-DescribeLabelingJob-response-LabelingJobOutput"></a>
The location of the output produced by the labeling job.
Type: [LabelingJobOutput](API_LabelingJobOutput.md) object

 ** [LabelingJobStatus](#API_DescribeLabelingJob_ResponseSyntax) **   <a name="sagemaker-DescribeLabelingJob-response-LabelingJobStatus"></a>
The processing status of the labeling job.
Type: String
Valid Values: `Initializing | InProgress | Completed | Failed | Stopping | Stopped`

 ** [OutputConfig](#API_DescribeLabelingJob_ResponseSyntax) **   <a name="sagemaker-DescribeLabelingJob-response-OutputConfig"></a>
The location of the job's output data and the AWS Key Management Service key ID for the key used to encrypt the output data, if any.
Type: [LabelingJobOutputConfig](API_LabelingJobOutputConfig.md) object

 ** [RoleArn](#API_DescribeLabelingJob_ResponseSyntax) **   <a name="sagemaker-DescribeLabelingJob-response-RoleArn"></a>
The Amazon Resource Name (ARN) that SageMaker assumes to perform tasks on your behalf during data labeling.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`

 ** [StoppingConditions](#API_DescribeLabelingJob_ResponseSyntax) **   <a name="sagemaker-DescribeLabelingJob-response-StoppingConditions"></a>
A set of conditions for stopping a labeling job. If any of the conditions are met, the job is automatically stopped.
Type: [LabelingJobStoppingConditions](API_LabelingJobStoppingConditions.md) object

 ** [Tags](#API_DescribeLabelingJob_ResponseSyntax) **   <a name="sagemaker-DescribeLabelingJob-response-Tags"></a>
An array of key-value pairs. You can use tags to categorize your AWS resources in different ways, for example, by purpose, owner, or environment. For more information, see [Tagging AWS Resources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html).
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.

## Errors
<a name="API_DescribeLabelingJob_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_DescribeLabelingJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/DescribeLabelingJob)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/DescribeLabelingJob)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/DescribeLabelingJob)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/DescribeLabelingJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/DescribeLabelingJob)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/DescribeLabelingJob)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/DescribeLabelingJob)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/DescribeLabelingJob)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/DescribeLabelingJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/DescribeLabelingJob)
