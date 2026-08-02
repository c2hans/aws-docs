---
source_url: https://docs.aws.amazon.com/frauddetector/latest/api/API_CreateBatchPredictionJob.html
---

Amazon Fraud Detector is no longer be open to new customers as of November 7, 2025. For capabilities similar to Amazon Fraud Detector, explore Amazon SageMaker AI, AutoGluon, and AWS WAF.

# CreateBatchPredictionJob
<a name="API_CreateBatchPredictionJob"></a>

Creates a batch prediction job.

## Request Syntax
<a name="API_CreateBatchPredictionJob_RequestSyntax"></a>

```
{
   "detectorName": "{{string}}",
   "detectorVersion": "{{string}}",
   "eventTypeName": "{{string}}",
   "iamRoleArn": "{{string}}",
   "inputPath": "{{string}}",
   "jobId": "{{string}}",
   "outputPath": "{{string}}",
   "tags": [
      {
         "key": "{{string}}",
         "value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_CreateBatchPredictionJob_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [detectorName](#API_CreateBatchPredictionJob_RequestSyntax) **   <a name="FraudDetector-CreateBatchPredictionJob-request-detectorName"></a>
The name of the detector.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[0-9a-z_-]+$`
Required: Yes

 ** [detectorVersion](#API_CreateBatchPredictionJob_RequestSyntax) **   <a name="FraudDetector-CreateBatchPredictionJob-request-detectorVersion"></a>
The detector version.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 5.
Pattern: `^([1-9][0-9]*)$`
Required: No

 ** [eventTypeName](#API_CreateBatchPredictionJob_RequestSyntax) **   <a name="FraudDetector-CreateBatchPredictionJob-request-eventTypeName"></a>
The name of the event type.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[0-9a-z_-]+$`
Required: Yes

 ** [iamRoleArn](#API_CreateBatchPredictionJob_RequestSyntax) **   <a name="FraudDetector-CreateBatchPredictionJob-request-iamRoleArn"></a>
The ARN of the IAM role to use for this job request.
The IAM Role must have read permissions to your input S3 bucket and write permissions to your output S3 bucket. For more information about bucket permissions, see [User policy examples](https://docs.aws.amazon.com/AmazonS3/latest/userguide/example-policies-s3.html) in the *Amazon S3 User Guide*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^arn\:aws[a-z-]{0,15}\:iam\:\:[0-9]{12}\:role\/[^\s]{2,64}$`
Required: Yes

 ** [inputPath](#API_CreateBatchPredictionJob_RequestSyntax) **   <a name="FraudDetector-CreateBatchPredictionJob-request-inputPath"></a>
The Amazon S3 location of your training file.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `^s3:\/\/(.+)$`
Required: Yes

 ** [jobId](#API_CreateBatchPredictionJob_RequestSyntax) **   <a name="FraudDetector-CreateBatchPredictionJob-request-jobId"></a>
The ID of the batch prediction job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[0-9a-z_-]+$`
Required: Yes

 ** [outputPath](#API_CreateBatchPredictionJob_RequestSyntax) **   <a name="FraudDetector-CreateBatchPredictionJob-request-outputPath"></a>
The Amazon S3 location of your output file.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `^s3:\/\/(.+)$`
Required: Yes

 ** [tags](#API_CreateBatchPredictionJob_RequestSyntax) **   <a name="FraudDetector-CreateBatchPredictionJob-request-tags"></a>
A collection of key and value pairs.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Required: No

## Response Elements
<a name="API_CreateBatchPredictionJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_CreateBatchPredictionJob_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
An exception indicating Amazon Fraud Detector does not have the needed permissions. This can occur if you submit a request, such as `PutExternalModel`, that specifies a role that is not in your account.
HTTP Status Code: 400

 ** InternalServerException **
An exception indicating an internal server error.
HTTP Status Code: 500

 ** ResourceNotFoundException **
An exception indicating the specified resource was not found.
HTTP Status Code: 400

 ** ThrottlingException **
An exception indicating a throttling error.
HTTP Status Code: 400

 ** ValidationException **
An exception indicating a specified value is not allowed.
HTTP Status Code: 400

## See Also
<a name="API_CreateBatchPredictionJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/frauddetector-2019-11-15/CreateBatchPredictionJob)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/frauddetector-2019-11-15/CreateBatchPredictionJob)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/frauddetector-2019-11-15/CreateBatchPredictionJob)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/frauddetector-2019-11-15/CreateBatchPredictionJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/frauddetector-2019-11-15/CreateBatchPredictionJob)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/frauddetector-2019-11-15/CreateBatchPredictionJob)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/frauddetector-2019-11-15/CreateBatchPredictionJob)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/frauddetector-2019-11-15/CreateBatchPredictionJob)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/frauddetector-2019-11-15/CreateBatchPredictionJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/frauddetector-2019-11-15/CreateBatchPredictionJob)
