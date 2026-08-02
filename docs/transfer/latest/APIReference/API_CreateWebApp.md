---
source_url: https://docs.aws.amazon.com/transfer/latest/APIReference/API_CreateWebApp.html
---

# CreateWebApp
<a name="API_CreateWebApp"></a>

Creates a web app based on specified parameters, and returns the ID for the new web app. You can configure the web app to be publicly accessible or hosted within a VPC.

For more information about using VPC endpoints with AWS Transfer Family, see [Create a Transfer Family web app in a VPC](https://docs.aws.amazon.com/transfer/latest/userguide/create-webapp-in-vpc.html).

## Request Syntax
<a name="API_CreateWebApp_RequestSyntax"></a>

```
{
   "AccessEndpoint": "{{string}}",
   "EndpointDetails": { ... },
   "IdentityProviderDetails": { ... },
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "WebAppEndpointPolicy": "{{string}}",
   "WebAppUnits": { ... }
}
```

## Request Parameters
<a name="API_CreateWebApp_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AccessEndpoint](#API_CreateWebApp_RequestSyntax) **   <a name="TransferFamily-CreateWebApp-request-AccessEndpoint"></a>
The `AccessEndpoint` is the URL that you provide to your users for them to interact with the Transfer Family web app. You can specify a custom URL or use the default value.
Before you enter a custom URL for this parameter, follow the steps described in [Update your access endpoint with a custom URL](https://docs.aws.amazon.com/transfer/latest/userguide/webapp-customize.html).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** [EndpointDetails](#API_CreateWebApp_RequestSyntax) **   <a name="TransferFamily-CreateWebApp-request-EndpointDetails"></a>
The endpoint configuration for the web app. You can specify whether the web app endpoint is publicly accessible or hosted within a VPC.
Type: [WebAppEndpointDetails](API_WebAppEndpointDetails.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** [IdentityProviderDetails](#API_CreateWebApp_RequestSyntax) **   <a name="TransferFamily-CreateWebApp-request-IdentityProviderDetails"></a>
You can provide a structure that contains the details for the identity provider to use with your web app.
For more details about this parameter, see [Configure your identity provider for Transfer Family web apps](https://docs.aws.amazon.com/transfer/latest/userguide/webapp-identity-center.html).
Type: [WebAppIdentityProviderDetails](API_WebAppIdentityProviderDetails.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** [Tags](#API_CreateWebApp_RequestSyntax) **   <a name="TransferFamily-CreateWebApp-request-Tags"></a>
Key-value pairs that can be used to group and search for web apps.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Required: No

 ** [WebAppEndpointPolicy](#API_CreateWebApp_RequestSyntax) **   <a name="TransferFamily-CreateWebApp-request-WebAppEndpointPolicy"></a>
 Setting for the type of endpoint policy for the web app. The default value is `STANDARD`.
If you are creating the web app in an AWS GovCloud (US) Region, you can set this parameter to `FIPS`.
Type: String
Valid Values: `FIPS | STANDARD`
Required: No

 ** [WebAppUnits](#API_CreateWebApp_RequestSyntax) **   <a name="TransferFamily-CreateWebApp-request-WebAppUnits"></a>
A union that contains the value for number of concurrent connections or the user sessions on your web app.
Type: [WebAppUnits](API_WebAppUnits.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

## Response Syntax
<a name="API_CreateWebApp_ResponseSyntax"></a>

```
{
   "WebAppId": "string"
}
```

## Response Elements
<a name="API_CreateWebApp_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [WebAppId](#API_CreateWebApp_ResponseSyntax) **   <a name="TransferFamily-CreateWebApp-response-WebAppId"></a>
Returns a unique identifier for the web app.
Type: String
Length Constraints: Fixed length of 24.
Pattern: `webapp-[0-9a-f]{17}`

## Errors
<a name="API_CreateWebApp_Errors"></a>

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
<a name="API_CreateWebApp_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/transfer-2018-11-05/CreateWebApp)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/transfer-2018-11-05/CreateWebApp)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transfer-2018-11-05/CreateWebApp)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/transfer-2018-11-05/CreateWebApp)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transfer-2018-11-05/CreateWebApp)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/transfer-2018-11-05/CreateWebApp)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/transfer-2018-11-05/CreateWebApp)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/transfer-2018-11-05/CreateWebApp)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/transfer-2018-11-05/CreateWebApp)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transfer-2018-11-05/CreateWebApp)
