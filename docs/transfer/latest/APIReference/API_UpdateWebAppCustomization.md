---
source_url: https://docs.aws.amazon.com/transfer/latest/APIReference/API_UpdateWebAppCustomization.html
---

# UpdateWebAppCustomization
<a name="API_UpdateWebAppCustomization"></a>

Assigns new customization properties to a web app. You can modify the icon file, logo file, and title.

## Request Syntax
<a name="API_UpdateWebAppCustomization_RequestSyntax"></a>

```
{
   "FaviconFile": {{blob}},
   "LogoFile": {{blob}},
   "Title": "{{string}}",
   "WebAppId": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateWebAppCustomization_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [FaviconFile](#API_UpdateWebAppCustomization_RequestSyntax) **   <a name="TransferFamily-UpdateWebAppCustomization-request-FaviconFile"></a>
Specify an icon file data string (in base64 encoding).
Type: Base64-encoded binary data object
Length Constraints: Minimum length of 1. Maximum length of 20960.
Required: No

 ** [LogoFile](#API_UpdateWebAppCustomization_RequestSyntax) **   <a name="TransferFamily-UpdateWebAppCustomization-request-LogoFile"></a>
Specify logo file data string (in base64 encoding).
Type: Base64-encoded binary data object
Length Constraints: Minimum length of 1. Maximum length of 51200.
Required: No

 ** [Title](#API_UpdateWebAppCustomization_RequestSyntax) **   <a name="TransferFamily-UpdateWebAppCustomization-request-Title"></a>
Provide an updated title.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 100.
Required: No

 ** [WebAppId](#API_UpdateWebAppCustomization_RequestSyntax) **   <a name="TransferFamily-UpdateWebAppCustomization-request-WebAppId"></a>
Provide the identifier of the web app that you are updating.
Type: String
Length Constraints: Fixed length of 24.
Pattern: `webapp-[0-9a-f]{17}`
Required: Yes

## Response Syntax
<a name="API_UpdateWebAppCustomization_ResponseSyntax"></a>

```
{
   "WebAppId": "string"
}
```

## Response Elements
<a name="API_UpdateWebAppCustomization_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [WebAppId](#API_UpdateWebAppCustomization_ResponseSyntax) **   <a name="TransferFamily-UpdateWebAppCustomization-response-WebAppId"></a>
Returns the unique identifier for the web app being updated.
Type: String
Length Constraints: Fixed length of 24.
Pattern: `webapp-[0-9a-f]{17}`

## Errors
<a name="API_UpdateWebAppCustomization_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 400

 ** ConflictException **
This exception is thrown when the `UpdateServer` is called for a file transfer protocol-enabled server that has VPC as the endpoint type and the server's `VpcEndpointID` is not in the available state.
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
<a name="API_UpdateWebAppCustomization_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/transfer-2018-11-05/UpdateWebAppCustomization)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/transfer-2018-11-05/UpdateWebAppCustomization)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transfer-2018-11-05/UpdateWebAppCustomization)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/transfer-2018-11-05/UpdateWebAppCustomization)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transfer-2018-11-05/UpdateWebAppCustomization)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/transfer-2018-11-05/UpdateWebAppCustomization)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/transfer-2018-11-05/UpdateWebAppCustomization)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/transfer-2018-11-05/UpdateWebAppCustomization)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/transfer-2018-11-05/UpdateWebAppCustomization)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transfer-2018-11-05/UpdateWebAppCustomization)
