---
source_url: https://docs.aws.amazon.com/transfer/latest/APIReference/API_DeleteWebApp.html
---

# DeleteWebApp
<a name="API_DeleteWebApp"></a>

Deletes the specified web app.

## Request Syntax
<a name="API_DeleteWebApp_RequestSyntax"></a>

```
{
   "WebAppId": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteWebApp_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [WebAppId](#API_DeleteWebApp_RequestSyntax) **   <a name="TransferFamily-DeleteWebApp-request-WebAppId"></a>
Provide the unique identifier for the web app that you are deleting.
Type: String
Length Constraints: Fixed length of 24.
Pattern: `webapp-[0-9a-f]{17}`
Required: Yes

## Response Elements
<a name="API_DeleteWebApp_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteWebApp_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 400

 ** InternalServiceError **
This exception is thrown when an error occurs in the AWS Transfer Family service.
HTTP Status Code: 500

 ** InvalidRequestException **
This exception is thrown when the client submits a malformed request.
HTTP Status Code: 400

 ** ResourceNotFoundException **
This exception is thrown when a resource is not found by the AWSTransfer Family service.
HTTP Status Code: 400

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 400

## See Also
<a name="API_DeleteWebApp_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/transfer-2018-11-05/DeleteWebApp)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/transfer-2018-11-05/DeleteWebApp)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transfer-2018-11-05/DeleteWebApp)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/transfer-2018-11-05/DeleteWebApp)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transfer-2018-11-05/DeleteWebApp)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/transfer-2018-11-05/DeleteWebApp)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/transfer-2018-11-05/DeleteWebApp)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/transfer-2018-11-05/DeleteWebApp)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/transfer-2018-11-05/DeleteWebApp)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transfer-2018-11-05/DeleteWebApp)
