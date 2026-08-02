---
source_url: https://docs.aws.amazon.com/comprehend-medical/latest/api/API_StartRxNormInferenceJob.html
---

# StartRxNormInferenceJob
<a name="API_StartRxNormInferenceJob"></a>

Starts an asynchronous job to detect medication entities and link them to the RxNorm ontology. Use the `DescribeRxNormInferenceJob` operation to track the status of a job.

## Request Syntax
<a name="API_StartRxNormInferenceJob_RequestSyntax"></a>

```
{
   "ClientRequestToken": "{{string}}",
   "DataAccessRoleArn": "{{string}}",
   "InputDataConfig": {
      "S3Bucket": "{{string}}",
      "S3Key": "{{string}}"
   },
   "JobName": "{{string}}",
   "KMSKey": "{{string}}",
   "LanguageCode": "{{string}}",
   "OutputDataConfig": {
      "S3Bucket": "{{string}}",
      "S3Key": "{{string}}"
   }
}
```

## Request Parameters
<a name="API_StartRxNormInferenceJob_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ClientRequestToken](#API_StartRxNormInferenceJob_RequestSyntax) **   <a name="comprehendmedical-StartRxNormInferenceJob-request-ClientRequestToken"></a>
A unique identifier for the request. If you don't set the client request token, Comprehend Medical; generates one.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9-]+$`
Required: No

 ** [DataAccessRoleArn](#API_StartRxNormInferenceJob_RequestSyntax) **   <a name="comprehendmedical-StartRxNormInferenceJob-request-DataAccessRoleArn"></a>
The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that grants Comprehend Medical; read access to your input data. For more information, see [ Role-Based Permissions Required for Asynchronous Operations](https://docs.aws.amazon.com/comprehend/latest/dg/access-control-managing-permissions-med.html#auth-role-permissions-med).
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws(-[^:]+)?:iam::[0-9]{12}:role/.+`
Required: Yes

 ** [InputDataConfig](#API_StartRxNormInferenceJob_RequestSyntax) **   <a name="comprehendmedical-StartRxNormInferenceJob-request-InputDataConfig"></a>
Specifies the format and location of the input data for the job.
Type: [InputDataConfig](API_InputDataConfig.md) object
Required: Yes

 ** [JobName](#API_StartRxNormInferenceJob_RequestSyntax) **   <a name="comprehendmedical-StartRxNormInferenceJob-request-JobName"></a>
The identifier of the job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-%@]*)$`
Required: No

 ** [KMSKey](#API_StartRxNormInferenceJob_RequestSyntax) **   <a name="comprehendmedical-StartRxNormInferenceJob-request-KMSKey"></a>
An AWS Key Management Service key to encrypt your output files. If you do not specify a key, the files are written in plain text.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `.*`
Required: No

 ** [LanguageCode](#API_StartRxNormInferenceJob_RequestSyntax) **   <a name="comprehendmedical-StartRxNormInferenceJob-request-LanguageCode"></a>
The language of the input documents. All documents must be in the same language.
Type: String
Valid Values: `en`
Required: Yes

 ** [OutputDataConfig](#API_StartRxNormInferenceJob_RequestSyntax) **   <a name="comprehendmedical-StartRxNormInferenceJob-request-OutputDataConfig"></a>
Specifies where to send the output files.
Type: [OutputDataConfig](API_OutputDataConfig.md) object
Required: Yes

## Response Syntax
<a name="API_StartRxNormInferenceJob_ResponseSyntax"></a>

```
{
   "JobId": "string"
}
```

## Response Elements
<a name="API_StartRxNormInferenceJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [JobId](#API_StartRxNormInferenceJob_ResponseSyntax) **   <a name="comprehendmedical-StartRxNormInferenceJob-response-JobId"></a>
The identifier of the job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-%@]*)$`

## Errors
<a name="API_StartRxNormInferenceJob_Errors"></a>

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
<a name="API_StartRxNormInferenceJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/comprehendmedical-2018-10-30/StartRxNormInferenceJob)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/comprehendmedical-2018-10-30/StartRxNormInferenceJob)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/comprehendmedical-2018-10-30/StartRxNormInferenceJob)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/comprehendmedical-2018-10-30/StartRxNormInferenceJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/comprehendmedical-2018-10-30/StartRxNormInferenceJob)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/comprehendmedical-2018-10-30/StartRxNormInferenceJob)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/comprehendmedical-2018-10-30/StartRxNormInferenceJob)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/comprehendmedical-2018-10-30/StartRxNormInferenceJob)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/comprehendmedical-2018-10-30/StartRxNormInferenceJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/comprehendmedical-2018-10-30/StartRxNormInferenceJob)
