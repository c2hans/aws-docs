---
source_url: https://docs.aws.amazon.com/comprehend-medical/latest/api/API_DescribeRxNormInferenceJob.html
---

# DescribeRxNormInferenceJob
<a name="API_DescribeRxNormInferenceJob"></a>

Gets the properties associated with an InferRxNorm job. Use this operation to get the status of an inference job.

## Request Syntax
<a name="API_DescribeRxNormInferenceJob_RequestSyntax"></a>

```
{
   "JobId": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeRxNormInferenceJob_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [JobId](#API_DescribeRxNormInferenceJob_RequestSyntax) **   <a name="comprehendmedical-DescribeRxNormInferenceJob-request-JobId"></a>
The identifier that Amazon Comprehend Medical generated for the job. The StartRxNormInferenceJob operation returns this identifier in its response.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-%@]*)$`
Required: Yes

## Response Syntax
<a name="API_DescribeRxNormInferenceJob_ResponseSyntax"></a>

```
{
   "ComprehendMedicalAsyncJobProperties": {
      "DataAccessRoleArn": "string",
      "EndTime": number,
      "ExpirationTime": number,
      "InputDataConfig": {
         "S3Bucket": "string",
         "S3Key": "string"
      },
      "JobId": "string",
      "JobName": "string",
      "JobStatus": "string",
      "KMSKey": "string",
      "LanguageCode": "string",
      "ManifestFilePath": "string",
      "Message": "string",
      "ModelVersion": "string",
      "OutputDataConfig": {
         "S3Bucket": "string",
         "S3Key": "string"
      },
      "SubmitTime": number
   }
}
```

## Response Elements
<a name="API_DescribeRxNormInferenceJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ComprehendMedicalAsyncJobProperties](#API_DescribeRxNormInferenceJob_ResponseSyntax) **   <a name="comprehendmedical-DescribeRxNormInferenceJob-response-ComprehendMedicalAsyncJobProperties"></a>
An object that contains the properties associated with a detection job.
Type: [ComprehendMedicalAsyncJobProperties](API_ComprehendMedicalAsyncJobProperties.md) object

## Errors
<a name="API_DescribeRxNormInferenceJob_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
 An internal server error occurred. Retry your request.
HTTP Status Code: 500

 ** InvalidRequestException **
 The request that you made is invalid. Check your request to determine why it's invalid and then retry the request.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The resource identified by the specified Amazon Resource Name (ARN) was not found. Check the ARN and try your request again.
HTTP Status Code: 400

 ** TooManyRequestsException **
 You have made too many requests within a short period of time. Wait for a short time and then try your request again. Contact customer support for more information about a service limit increase.
HTTP Status Code: 400

## See Also
<a name="API_DescribeRxNormInferenceJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/comprehendmedical-2018-10-30/DescribeRxNormInferenceJob)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/comprehendmedical-2018-10-30/DescribeRxNormInferenceJob)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/comprehendmedical-2018-10-30/DescribeRxNormInferenceJob)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/comprehendmedical-2018-10-30/DescribeRxNormInferenceJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/comprehendmedical-2018-10-30/DescribeRxNormInferenceJob)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/comprehendmedical-2018-10-30/DescribeRxNormInferenceJob)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/comprehendmedical-2018-10-30/DescribeRxNormInferenceJob)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/comprehendmedical-2018-10-30/DescribeRxNormInferenceJob)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/comprehendmedical-2018-10-30/DescribeRxNormInferenceJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/comprehendmedical-2018-10-30/DescribeRxNormInferenceJob)
