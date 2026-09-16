---
source_url: https://docs.aws.amazon.com/athena/latest/APIReference/API_UpdateNotebook.html
---

# UpdateNotebook
<a name="API_UpdateNotebook"></a>

Updates the contents of a Spark notebook.

## Request Syntax
<a name="API_UpdateNotebook_RequestSyntax"></a>

```
{
   "ClientRequestToken": "{{string}}",
   "NotebookId": "{{string}}",
   "Payload": "{{string}}",
   "SessionId": "{{string}}",
   "Type": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateNotebook_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ClientRequestToken](#API_UpdateNotebook_RequestSyntax) **   <a name="athena-UpdateNotebook-request-ClientRequestToken"></a>
A unique case-sensitive string used to ensure the request to create the notebook is idempotent (executes only once).
This token is listed as not required because AWS SDKs (for example the AWS SDK for Java) auto-generate the token for you. If you are not using the AWS SDK or the AWS CLI, you must provide this token or the action will fail.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 36.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: No

 ** [NotebookId](#API_UpdateNotebook_RequestSyntax) **   <a name="athena-UpdateNotebook-request-NotebookId"></a>
The ID of the notebook to update.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 36.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: Yes

 ** [Payload](#API_UpdateNotebook_RequestSyntax) **   <a name="athena-UpdateNotebook-request-Payload"></a>
The updated content for the notebook.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 10485760.
Required: Yes

 ** [SessionId](#API_UpdateNotebook_RequestSyntax) **   <a name="athena-UpdateNotebook-request-SessionId"></a>
The active notebook session ID. Required if the notebook has an active session.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** [Type](#API_UpdateNotebook_RequestSyntax) **   <a name="athena-UpdateNotebook-request-Type"></a>
The notebook content type. Currently, the only valid type is `IPYNB`.
Type: String
Valid Values: `IPYNB`
Required: Yes

## Response Elements
<a name="API_UpdateNotebook_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateNotebook_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
Indicates a platform issue, which may be due to a transient condition or outage.
HTTP Status Code: 500

 ** InvalidRequestException **
Indicates that something is wrong with the input to the request. For example, a required parameter may be missing or out of range.
 ** AthenaErrorCode **
The error code returned when the query execution failed to process, or when the processing request for the named query failed.
HTTP Status Code: 400

 ** TooManyRequestsException **
Indicates that the request was throttled.
 ** Reason **
The reason for the query throttling, for example, when it exceeds the concurrent query limit.
HTTP Status Code: 400

## See Also
<a name="API_UpdateNotebook_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/athena-2017-05-18/UpdateNotebook)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/athena-2017-05-18/UpdateNotebook)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/athena-2017-05-18/UpdateNotebook)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/athena-2017-05-18/UpdateNotebook)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/athena-2017-05-18/UpdateNotebook)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/athena-2017-05-18/UpdateNotebook)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/athena-2017-05-18/UpdateNotebook)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/athena-2017-05-18/UpdateNotebook)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/athena-2017-05-18/UpdateNotebook)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/athena-2017-05-18/UpdateNotebook)
