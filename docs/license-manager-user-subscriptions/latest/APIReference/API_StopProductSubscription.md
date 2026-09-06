---
source_url: https://docs.aws.amazon.com/license-manager-user-subscriptions/latest/APIReference/API_StopProductSubscription.html
---

# StopProductSubscription
<a name="API_StopProductSubscription"></a>

Stops a product subscription for a user with the specified identity provider.

## Request Syntax
<a name="API_StopProductSubscription_RequestSyntax"></a>

```
POST /user/StopProductSubscription HTTP/1.1
Content-type: application/json

{
   "Domain": "{{string}}",
   "IdentityProvider": { ... },
   "Product": "{{string}}",
   "ProductUserArn": "{{string}}",
   "Username": "{{string}}"
}
```

## URI Request Parameters
<a name="API_StopProductSubscription_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_StopProductSubscription_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Domain](#API_StopProductSubscription_RequestSyntax) **   <a name="licensemanagerusersubscriptions-StopProductSubscription-request-Domain"></a>
The domain name of the Active Directory that contains the user for whom to stop the product subscription.
Type: String
Required: No

 ** [IdentityProvider](#API_StopProductSubscription_RequestSyntax) **   <a name="licensemanagerusersubscriptions-StopProductSubscription-request-IdentityProvider"></a>
An object that specifies details for the identity provider.
Type: [IdentityProvider](API_IdentityProvider.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** [Product](#API_StopProductSubscription_RequestSyntax) **   <a name="licensemanagerusersubscriptions-StopProductSubscription-request-Product"></a>
The name of the user-based subscription product.
Valid values: `VISUAL_STUDIO_ENTERPRISE` \| `VISUAL_STUDIO_PROFESSIONAL` \| `OFFICE_PROFESSIONAL_PLUS` \| `OFFICE_STANDARD` \| `REMOTE_DESKTOP_SERVICES`
Type: String
Required: No

 ** [ProductUserArn](#API_StopProductSubscription_RequestSyntax) **   <a name="licensemanagerusersubscriptions-StopProductSubscription-request-ProductUserArn"></a>
The Amazon Resource Name (ARN) of the product user.
Type: String
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{1,63}:[a-zA-Z0-9-\.]{1,510}/[a-zA-Z0-9-\.]{1,510}`
Required: No

 ** [Username](#API_StopProductSubscription_RequestSyntax) **   <a name="licensemanagerusersubscriptions-StopProductSubscription-request-Username"></a>
The user name from the identity provider for the user.
Type: String
Required: No

## Response Syntax
<a name="API_StopProductSubscription_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ProductUserSummary": {
      "Domain": "string",
      "IdentityProvider": { ... },
      "Product": "string",
      "ProductUserArn": "string",
      "Status": "string",
      "StatusMessage": "string",
      "SubscriptionEndDate": "string",
      "SubscriptionStartDate": "string",
      "Username": "string"
   }
}
```

## Response Elements
<a name="API_StopProductSubscription_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ProductUserSummary](#API_StopProductSubscription_ResponseSyntax) **   <a name="licensemanagerusersubscriptions-StopProductSubscription-response-ProductUserSummary"></a>
Metadata that describes the start product subscription operation.
Type: [ProductUserSummary](API_ProductUserSummary.md) object

## Errors
<a name="API_StopProductSubscription_Errors"></a>

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
<a name="API_StopProductSubscription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/license-manager-user-subscriptions-2018-05-10/StopProductSubscription)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/license-manager-user-subscriptions-2018-05-10/StopProductSubscription)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/license-manager-user-subscriptions-2018-05-10/StopProductSubscription)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/license-manager-user-subscriptions-2018-05-10/StopProductSubscription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/license-manager-user-subscriptions-2018-05-10/StopProductSubscription)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/license-manager-user-subscriptions-2018-05-10/StopProductSubscription)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/license-manager-user-subscriptions-2018-05-10/StopProductSubscription)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/license-manager-user-subscriptions-2018-05-10/StopProductSubscription)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/license-manager-user-subscriptions-2018-05-10/StopProductSubscription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/license-manager-user-subscriptions-2018-05-10/StopProductSubscription)
