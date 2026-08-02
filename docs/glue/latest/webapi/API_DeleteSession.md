---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_DeleteSession.html
---

# DeleteSession
<a name="API_DeleteSession"></a>

Deletes the session.

## Request Syntax
<a name="API_DeleteSession_RequestSyntax"></a>

```
{
   "Id": "{{string}}",
   "RequestOrigin": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteSession_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Id](#API_DeleteSession_RequestSyntax) **   <a name="Glue-DeleteSession-request-Id"></a>
The ID of the session to be deleted.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

 ** [RequestOrigin](#API_DeleteSession_RequestSyntax) **   <a name="Glue-DeleteSession-request-RequestOrigin"></a>
The name of the origin of the delete session request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\.\-_A-Za-z0-9]+`
Required: No

## Response Syntax
<a name="API_DeleteSession_ResponseSyntax"></a>

```
{
   "Id": "string"
}
```

## Response Elements
<a name="API_DeleteSession_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Id](#API_DeleteSession_ResponseSyntax) **   <a name="Glue-DeleteSession-response-Id"></a>
Returns the ID of the deleted session.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`

## Errors
<a name="API_DeleteSession_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access to a resource was denied.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** ConcurrentModificationException **
Two processes are trying to modify a resource simultaneously.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** IllegalSessionStateException **
The session is in an invalid state to perform a requested operation.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** InternalServiceException **
An internal service error occurred.
 ** Message **
A message describing the problem.
HTTP Status Code: 500

 ** InvalidInputException **
The input provided was not valid.
 ** FromFederationSource **
Indicates whether or not the exception relates to a federated source.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** OperationTimeoutException **
The operation timed out.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

## See Also
<a name="API_DeleteSession_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/DeleteSession)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/DeleteSession)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/DeleteSession)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/DeleteSession)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/DeleteSession)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/DeleteSession)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/DeleteSession)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/DeleteSession)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/DeleteSession)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/DeleteSession)
