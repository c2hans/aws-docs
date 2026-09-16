---
source_url: https://docs.aws.amazon.com/license-manager-user-subscriptions/latest/APIReference/API_CreateLicenseServerEndpoint.html
---

# CreateLicenseServerEndpoint
<a name="API_CreateLicenseServerEndpoint"></a>

Creates a network endpoint for the Remote Desktop Services (RDS) license server.

## Request Syntax
<a name="API_CreateLicenseServerEndpoint_RequestSyntax"></a>

```
POST /license-server/CreateLicenseServerEndpoint HTTP/1.1
Content-type: application/json

{
   "IdentityProviderArn": "{{string}}",
   "LicenseServerSettings": {
      "ServerSettings": { ... },
      "ServerType": "{{string}}"
   },
   "Tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateLicenseServerEndpoint_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateLicenseServerEndpoint_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [IdentityProviderArn](#API_CreateLicenseServerEndpoint_RequestSyntax) **   <a name="licensemanagerusersubscriptions-CreateLicenseServerEndpoint-request-IdentityProviderArn"></a>
The Amazon Resource Name (ARN) that identifies the `IdentityProvider` resource that contains details about a registered identity provider. In the case of Active Directory, that can be a self-managed Active Directory or an AWS Managed Active Directory that contains user identity details.
Type: String
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{1,63}:[a-zA-Z0-9-\.]{1,510}/[a-zA-Z0-9-\.]{1,510}`
Required: Yes

 ** [LicenseServerSettings](#API_CreateLicenseServerEndpoint_RequestSyntax) **   <a name="licensemanagerusersubscriptions-CreateLicenseServerEndpoint-request-LicenseServerSettings"></a>
The `LicenseServerSettings` resource to create for the endpoint. The settings include the type of license server and the AWS Secrets Manager secret that enables administrators to add or remove users associated with the license server.
Type: [LicenseServerSettings](API_LicenseServerSettings.md) object
Required: Yes

 ** [Tags](#API_CreateLicenseServerEndpoint_RequestSyntax) **   <a name="licensemanagerusersubscriptions-CreateLicenseServerEndpoint-request-Tags"></a>
The tags that apply for the license server endpoint.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Required: No

## Response Syntax
<a name="API_CreateLicenseServerEndpoint_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "IdentityProviderArn": "string",
   "LicenseServerEndpointArn": "string"
}
```

## Response Elements
<a name="API_CreateLicenseServerEndpoint_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [IdentityProviderArn](#API_CreateLicenseServerEndpoint_ResponseSyntax) **   <a name="licensemanagerusersubscriptions-CreateLicenseServerEndpoint-response-IdentityProviderArn"></a>
The Amazon Resource Name (ARN) of the identity provider specified in the request.
Type: String
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{1,63}:[a-zA-Z0-9-\.]{1,510}/[a-zA-Z0-9-\.]{1,510}`

 ** [LicenseServerEndpointArn](#API_CreateLicenseServerEndpoint_ResponseSyntax) **   <a name="licensemanagerusersubscriptions-CreateLicenseServerEndpoint-response-LicenseServerEndpointArn"></a>
The ARN of the `LicenseServerEndpoint` resource.
Type: String
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{1,63}:[a-zA-Z0-9-\.]{1,510}/[a-zA-Z0-9-\.]{1,510}`

## Errors
<a name="API_CreateLicenseServerEndpoint_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient access to perform this action.
HTTP Status Code: 400

 ** ConflictException **
The request couldn't be completed because it conflicted with the current state of the resource.
HTTP Status Code: 500

 ** InternalServerException **
An exception occurred with the service.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The resource couldn't be found.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
The request failed because a service quota is exceeded.
HTTP Status Code: 400

 ** ThrottlingException **
The request was denied because of request throttling. Retry the request.
HTTP Status Code: 400

 ** ValidationException **
A parameter is not valid.
HTTP Status Code: 400

## See Also
<a name="API_CreateLicenseServerEndpoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/license-manager-user-subscriptions-2018-05-10/CreateLicenseServerEndpoint)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/license-manager-user-subscriptions-2018-05-10/CreateLicenseServerEndpoint)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/license-manager-user-subscriptions-2018-05-10/CreateLicenseServerEndpoint)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/license-manager-user-subscriptions-2018-05-10/CreateLicenseServerEndpoint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/license-manager-user-subscriptions-2018-05-10/CreateLicenseServerEndpoint)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/license-manager-user-subscriptions-2018-05-10/CreateLicenseServerEndpoint)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/license-manager-user-subscriptions-2018-05-10/CreateLicenseServerEndpoint)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/license-manager-user-subscriptions-2018-05-10/CreateLicenseServerEndpoint)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/license-manager-user-subscriptions-2018-05-10/CreateLicenseServerEndpoint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/license-manager-user-subscriptions-2018-05-10/CreateLicenseServerEndpoint)
