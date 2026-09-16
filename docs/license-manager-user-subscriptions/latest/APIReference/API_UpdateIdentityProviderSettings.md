---
source_url: https://docs.aws.amazon.com/license-manager-user-subscriptions/latest/APIReference/API_UpdateIdentityProviderSettings.html
---

# UpdateIdentityProviderSettings
<a name="API_UpdateIdentityProviderSettings"></a>

Updates additional product configuration settings for the registered identity provider.

## Request Syntax
<a name="API_UpdateIdentityProviderSettings_RequestSyntax"></a>

```
POST /identity-provider/UpdateIdentityProviderSettings HTTP/1.1
Content-type: application/json

{
   "IdentityProvider": { ... },
   "IdentityProviderArn": "{{string}}",
   "Product": "{{string}}",
   "UpdateSettings": {
      "AddSubnets": [ "{{string}}" ],
      "RemoveSubnets": [ "{{string}}" ],
      "SecurityGroupId": "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_UpdateIdentityProviderSettings_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_UpdateIdentityProviderSettings_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [IdentityProvider](#API_UpdateIdentityProviderSettings_RequestSyntax) **   <a name="licensemanagerusersubscriptions-UpdateIdentityProviderSettings-request-IdentityProvider"></a>
Refers to an identity provider.
Type: [IdentityProvider](API_IdentityProvider.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** [IdentityProviderArn](#API_UpdateIdentityProviderSettings_RequestSyntax) **   <a name="licensemanagerusersubscriptions-UpdateIdentityProviderSettings-request-IdentityProviderArn"></a>
The Amazon Resource Name (ARN) of the identity provider to update.
Type: String
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{1,63}:[a-zA-Z0-9-\.]{1,510}/[a-zA-Z0-9-\.]{1,510}`
Required: No

 ** [Product](#API_UpdateIdentityProviderSettings_RequestSyntax) **   <a name="licensemanagerusersubscriptions-UpdateIdentityProviderSettings-request-Product"></a>
The name of the user-based subscription product.
Valid values: `VISUAL_STUDIO_ENTERPRISE` \| `VISUAL_STUDIO_PROFESSIONAL` \| `OFFICE_PROFESSIONAL_PLUS` \| `OFFICE_STANDARD` \| `REMOTE_DESKTOP_SERVICES`
Type: String
Required: No

 ** [UpdateSettings](#API_UpdateIdentityProviderSettings_RequestSyntax) **   <a name="licensemanagerusersubscriptions-UpdateIdentityProviderSettings-request-UpdateSettings"></a>
Updates the registered identity provider’s product related configuration settings. You can update any combination of settings in a single operation such as the:
+ Subnets which you want to add to provision VPC endpoints.
+ Subnets which you want to remove the VPC endpoints from.
+ Security group ID which permits traffic to the VPC endpoints.
Type: [UpdateSettings](API_UpdateSettings.md) object
Required: Yes

## Response Syntax
<a name="API_UpdateIdentityProviderSettings_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "IdentityProviderSummary": {
      "FailureMessage": "string",
      "IdentityProvider": { ... },
      "IdentityProviderArn": "string",
      "OwnerAccountId": "string",
      "Product": "string",
      "Settings": {
         "SecurityGroupId": "string",
         "Subnets": [ "string" ]
      },
      "Status": "string"
   }
}
```

## Response Elements
<a name="API_UpdateIdentityProviderSettings_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [IdentityProviderSummary](#API_UpdateIdentityProviderSettings_ResponseSyntax) **   <a name="licensemanagerusersubscriptions-UpdateIdentityProviderSettings-response-IdentityProviderSummary"></a>
Describes an identity provider.
Type: [IdentityProviderSummary](API_IdentityProviderSummary.md) object

## Errors
<a name="API_UpdateIdentityProviderSettings_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient access to perform this action.
HTTP Status Code: 400

 ** InternalServerException **
An exception occurred with the service.
HTTP Status Code: 500

 ** ThrottlingException **
The request was denied because of request throttling. Retry the request.
HTTP Status Code: 400

 ** ValidationException **
A parameter is not valid.
HTTP Status Code: 400

## See Also
<a name="API_UpdateIdentityProviderSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/license-manager-user-subscriptions-2018-05-10/UpdateIdentityProviderSettings)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/license-manager-user-subscriptions-2018-05-10/UpdateIdentityProviderSettings)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/license-manager-user-subscriptions-2018-05-10/UpdateIdentityProviderSettings)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/license-manager-user-subscriptions-2018-05-10/UpdateIdentityProviderSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/license-manager-user-subscriptions-2018-05-10/UpdateIdentityProviderSettings)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/license-manager-user-subscriptions-2018-05-10/UpdateIdentityProviderSettings)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/license-manager-user-subscriptions-2018-05-10/UpdateIdentityProviderSettings)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/license-manager-user-subscriptions-2018-05-10/UpdateIdentityProviderSettings)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/license-manager-user-subscriptions-2018-05-10/UpdateIdentityProviderSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/license-manager-user-subscriptions-2018-05-10/UpdateIdentityProviderSettings)
