---
source_url: https://docs.aws.amazon.com/athena/latest/APIReference/API_CreatePresignedNotebookUrl.html
---

# CreatePresignedNotebookUrl
<a name="API_CreatePresignedNotebookUrl"></a>

Gets an authentication token and the URL at which the notebook can be accessed. During programmatic access, `CreatePresignedNotebookUrl` must be called every 10 minutes to refresh the authentication token. For information about granting programmatic access, see [Grant programmatic access](https://docs.aws.amazon.com/athena/latest/ug/setting-up.html#setting-up-grant-programmatic-access).

## Request Syntax
<a name="API_CreatePresignedNotebookUrl_RequestSyntax"></a>

```
{
   "SessionId": "{{string}}"
}
```

## Request Parameters
<a name="API_CreatePresignedNotebookUrl_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [SessionId](#API_CreatePresignedNotebookUrl_RequestSyntax) **   <a name="athena-CreatePresignedNotebookUrl-request-SessionId"></a>
The session ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

## Response Syntax
<a name="API_CreatePresignedNotebookUrl_ResponseSyntax"></a>

```
{
   "AuthToken": "string",
   "AuthTokenExpirationTime": number,
   "NotebookUrl": "string"
}
```

## Response Elements
<a name="API_CreatePresignedNotebookUrl_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AuthToken](#API_CreatePresignedNotebookUrl_ResponseSyntax) **   <a name="athena-CreatePresignedNotebookUrl-response-AuthToken"></a>
The authentication token for the notebook.
Type: String
Length Constraints: Maximum length of 2048.

 ** [AuthTokenExpirationTime](#API_CreatePresignedNotebookUrl_ResponseSyntax) **   <a name="athena-CreatePresignedNotebookUrl-response-AuthTokenExpirationTime"></a>
The UTC epoch time when the authentication token expires.
Type: Long

 ** [NotebookUrl](#API_CreatePresignedNotebookUrl_ResponseSyntax) **   <a name="athena-CreatePresignedNotebookUrl-response-NotebookUrl"></a>
The URL of the notebook. The URL includes the authentication token and notebook file name and points directly to the opened notebook.
Type: String

## Errors
<a name="API_CreatePresignedNotebookUrl_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
Indicates a platform issue, which may be due to a transient condition or outage.
HTTP Status Code: 500

 ** InvalidRequestException **
Indicates that something is wrong with the input to the request. For example, a required parameter may be missing or out of range.
 ** AthenaErrorCode **
The error code returned when the query execution failed to process, or when the processing request for the named query failed.
HTTP Status Code: 400

 ** ResourceNotFoundException **
A resource, such as a workgroup, was not found.
 ** ResourceName **
The name of the Amazon resource.
HTTP Status Code: 400

## See Also
<a name="API_CreatePresignedNotebookUrl_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/athena-2017-05-18/CreatePresignedNotebookUrl)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/athena-2017-05-18/CreatePresignedNotebookUrl)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/athena-2017-05-18/CreatePresignedNotebookUrl)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/athena-2017-05-18/CreatePresignedNotebookUrl)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/athena-2017-05-18/CreatePresignedNotebookUrl)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/athena-2017-05-18/CreatePresignedNotebookUrl)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/athena-2017-05-18/CreatePresignedNotebookUrl)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/athena-2017-05-18/CreatePresignedNotebookUrl)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/athena-2017-05-18/CreatePresignedNotebookUrl)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/athena-2017-05-18/CreatePresignedNotebookUrl)
