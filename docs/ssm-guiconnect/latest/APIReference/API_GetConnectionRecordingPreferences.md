---
source_url: https://docs.aws.amazon.com/ssm-guiconnect/latest/APIReference/API_GetConnectionRecordingPreferences.html
---

# GetConnectionRecordingPreferences
<a name="API_GetConnectionRecordingPreferences"></a>

Returns the preferences specified for recording RDP connections in the requesting AWS account and AWS Region.

## Request Syntax
<a name="API_GetConnectionRecordingPreferences_RequestSyntax"></a>

```
POST /GetConnectionRecordingPreferences HTTP/1.1
```

## URI Request Parameters
<a name="API_GetConnectionRecordingPreferences_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetConnectionRecordingPreferences_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetConnectionRecordingPreferences_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ClientToken": "string",
   "ConnectionRecordingPreferences": {
      "KMSKeyArn": "string",
      "RecordingDestinations": {
         "S3Buckets": [
            {
               "BucketName": "string",
               "BucketOwner": "string"
            }
         ]
      }
   }
}
```

## Response Elements
<a name="API_GetConnectionRecordingPreferences_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ClientToken](#API_GetConnectionRecordingPreferences_ResponseSyntax) **   <a name="ssmguiconnect-GetConnectionRecordingPreferences-response-ClientToken"></a>
Service-provided idempotency token.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.

 ** [ConnectionRecordingPreferences](#API_GetConnectionRecordingPreferences_ResponseSyntax) **   <a name="ssmguiconnect-GetConnectionRecordingPreferences-response-ConnectionRecordingPreferences"></a>
The set of preferences used for recording RDP connections in the requesting AWS account and AWS Region. This includes details such as which S3 bucket recordings are stored in.
Type: [ConnectionRecordingPreferences](API_ConnectionRecordingPreferences.md) object

## Errors
<a name="API_GetConnectionRecordingPreferences_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
An error occurred due to a conflict.
HTTP Status Code: 409

 ** InternalServerException **
The request processing has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The resource could not be found.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
Your request exceeds a service quota.
HTTP Status Code: 402

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_GetConnectionRecordingPreferences_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-guiconnect-2021-05-01/GetConnectionRecordingPreferences)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-guiconnect-2021-05-01/GetConnectionRecordingPreferences)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-guiconnect-2021-05-01/GetConnectionRecordingPreferences)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-guiconnect-2021-05-01/GetConnectionRecordingPreferences)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-guiconnect-2021-05-01/GetConnectionRecordingPreferences)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-guiconnect-2021-05-01/GetConnectionRecordingPreferences)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-guiconnect-2021-05-01/GetConnectionRecordingPreferences)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-guiconnect-2021-05-01/GetConnectionRecordingPreferences)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ssm-guiconnect-2021-05-01/GetConnectionRecordingPreferences)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-guiconnect-2021-05-01/GetConnectionRecordingPreferences)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager GUI Connect. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ssm-guiconnect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
