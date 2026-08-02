---
source_url: https://docs.aws.amazon.com/transfer/latest/APIReference/API_UpdateWebApp.html
---

# UpdateWebApp
<a name="API_UpdateWebApp"></a>

Assigns new properties to a web app. You can modify the access point, identity provider details, endpoint configuration, and the web app units.

For more information about using VPC endpoints with AWS Transfer Family, see [Create a Transfer Family web app in a VPC](https://docs.aws.amazon.com/transfer/latest/userguide/create-webapp-in-vpc.html).

## Request Syntax
<a name="API_UpdateWebApp_RequestSyntax"></a>

```
{
   "AccessEndpoint": "{{string}}",
   "EndpointDetails": { ... },
   "IdentityProviderDetails": { ... },
   "WebAppId": "{{string}}",
   "WebAppUnits": { ... }
}
```

## Request Parameters
<a name="API_UpdateWebApp_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AccessEndpoint](#API_UpdateWebApp_RequestSyntax) **   <a name="TransferFamily-UpdateWebApp-request-AccessEndpoint"></a>
The `AccessEndpoint` is the URL that you provide to your users for them to interact with the Transfer Family web app. You can specify a custom URL or use the default value.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** [EndpointDetails](#API_UpdateWebApp_RequestSyntax) **   <a name="TransferFamily-UpdateWebApp-request-EndpointDetails"></a>
The updated endpoint configuration for the web app. You can modify the endpoint type and VPC configuration settings.
Type: [UpdateWebAppEndpointDetails](API_UpdateWebAppEndpointDetails.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** [IdentityProviderDetails](#API_UpdateWebApp_RequestSyntax) **   <a name="TransferFamily-UpdateWebApp-request-IdentityProviderDetails"></a>
Provide updated identity provider values in a `WebAppIdentityProviderDetails` object.
Type: [UpdateWebAppIdentityProviderDetails](API_UpdateWebAppIdentityProviderDetails.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** [WebAppId](#API_UpdateWebApp_RequestSyntax) **   <a name="TransferFamily-UpdateWebApp-request-WebAppId"></a>
Provide the identifier of the web app that you are updating.
Type: String
Length Constraints: Fixed length of 24.
Pattern: `webapp-[0-9a-f]{17}`
Required: Yes

 ** [WebAppUnits](#API_UpdateWebApp_RequestSyntax) **   <a name="TransferFamily-UpdateWebApp-request-WebAppUnits"></a>
A union that contains the value for number of concurrent connections or the user sessions on your web app.
Type: [WebAppUnits](API_WebAppUnits.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

## Response Syntax
<a name="API_UpdateWebApp_ResponseSyntax"></a>

```
{
   "WebAppId": "string"
}
```

## Response Elements
<a name="API_UpdateWebApp_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [WebAppId](#API_UpdateWebApp_ResponseSyntax) **   <a name="TransferFamily-UpdateWebApp-response-WebAppId"></a>
Returns the unique identifier for the web app being updated.
Type: String
Length Constraints: Fixed length of 24.
Pattern: `webapp-[0-9a-f]{17}`

## Errors
<a name="API_UpdateWebApp_Errors"></a>

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
<a name="API_UpdateWebApp_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/transfer-2018-11-05/UpdateWebApp)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/transfer-2018-11-05/UpdateWebApp)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transfer-2018-11-05/UpdateWebApp)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/transfer-2018-11-05/UpdateWebApp)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transfer-2018-11-05/UpdateWebApp)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/transfer-2018-11-05/UpdateWebApp)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/transfer-2018-11-05/UpdateWebApp)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/transfer-2018-11-05/UpdateWebApp)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/transfer-2018-11-05/UpdateWebApp)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transfer-2018-11-05/UpdateWebApp)
