---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeTrainingSession.html
---

# DescribeTrainingSession
<a name="API_DescribeTrainingSession"></a>

Retrieves detailed information about a training session, including its current status, model configuration, Low-Rank Adaptation (LoRA) parameters, and timestamps.

The following operations are related to `DescribeTrainingSession`:
+  `CreateTrainingSession`
+  `ListTrainingSessions`
+  `StopTrainingSession`
+  `DeleteTrainingSession`

## Request Syntax
<a name="API_DescribeTrainingSession_RequestSyntax"></a>

```
{
   "TrainingSessionName": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeTrainingSession_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [TrainingSessionName](#API_DescribeTrainingSession_RequestSyntax) **   <a name="sagemaker-DescribeTrainingSession-request-TrainingSessionName"></a>
The name of the training session to describe.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

## Response Syntax
<a name="API_DescribeTrainingSession_ResponseSyntax"></a>

```
{
   "TrainingSessionDetail": {
      "BillableTokenUsage": {
         "PrefillTokenCount": number,
         "SampleTokenCount": number,
         "TrainingTokenCount": number
      },
      "CreationTime": number,
      "EndTime": number,
      "ErrorDetails": "string",
      "LastModifiedTime": number,
      "LastReceivedSequenceNumber": number,
      "LoraConfig": {
         "Alpha": number,
         "Rank": number
      },
      "ModelConfig": {
         "AcceptEula": boolean,
         "BaseModelArn": "string"
      },
      "ModelPackageGroupArn": "string",
      "OutputConfig": {
         "S3Location": {
            "KmsKeyArn": "string",
            "Path": "string"
         }
      },
      "RoleArn": "string",
      "Tags": [
         {
            "Key": "string",
            "Value": "string"
         }
      ],
      "TrainingSessionArn": "string",
      "TrainingSessionName": "string",
      "TrainingSessionStatus": "string",
      "VpcConfig": {
         "SecurityGroupIds": [ "string" ],
         "Subnets": [ "string" ]
      }
   }
}
```

## Response Elements
<a name="API_DescribeTrainingSession_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [TrainingSessionDetail](#API_DescribeTrainingSession_ResponseSyntax) **   <a name="sagemaker-DescribeTrainingSession-response-TrainingSessionDetail"></a>
The detailed information about the training session.
Type: [TrainingSessionDetail](API_TrainingSessionDetail.md) object

## Errors
<a name="API_DescribeTrainingSession_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_DescribeTrainingSession_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/DescribeTrainingSession)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/DescribeTrainingSession)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/DescribeTrainingSession)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/DescribeTrainingSession)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/DescribeTrainingSession)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/DescribeTrainingSession)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/DescribeTrainingSession)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/DescribeTrainingSession)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/DescribeTrainingSession)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/DescribeTrainingSession)
