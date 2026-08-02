---
source_url: https://docs.aws.amazon.com/ivs/latest/ChatAPIReference/API_DeleteLoggingConfiguration.html
---

# DeleteLoggingConfiguration
<a name="API_DeleteLoggingConfiguration"></a>

Deletes the specified logging configuration.

## Request Syntax
<a name="API_DeleteLoggingConfiguration_RequestSyntax"></a>

```
POST /DeleteLoggingConfiguration HTTP/1.1
Content-type: application/json

{
   "identifier": "{{string}}"
}
```

## URI Request Parameters
<a name="API_DeleteLoggingConfiguration_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_DeleteLoggingConfiguration_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [identifier](#API_DeleteLoggingConfiguration_RequestSyntax) **   <a name="ivs-DeleteLoggingConfiguration-request-identifier"></a>
Identifier of the logging configuration to be deleted.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `arn:aws:ivschat:[a-z0-9-]+:[0-9]+:logging-configuration/[a-zA-Z0-9-]+`
Required: Yes

## Response Syntax
<a name="API_DeleteLoggingConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 204
```

## Response Elements
<a name="API_DeleteLoggingConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 204 response with an empty HTTP body.

## Errors
<a name="API_DeleteLoggingConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **

HTTP Status Code: 403

 ** ConflictException **

HTTP Status Code: 409

 ** PendingVerification **

HTTP Status Code: 403

 ** ResourceNotFoundException **

HTTP Status Code: 404

 ** ValidationException **

HTTP Status Code: 400

## See Also
<a name="API_DeleteLoggingConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ivschat-2020-07-14/DeleteLoggingConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ivschat-2020-07-14/DeleteLoggingConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ivschat-2020-07-14/DeleteLoggingConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ivschat-2020-07-14/DeleteLoggingConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ivschat-2020-07-14/DeleteLoggingConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ivschat-2020-07-14/DeleteLoggingConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ivschat-2020-07-14/DeleteLoggingConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ivschat-2020-07-14/DeleteLoggingConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ivschat-2020-07-14/DeleteLoggingConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ivschat-2020-07-14/DeleteLoggingConfiguration)
