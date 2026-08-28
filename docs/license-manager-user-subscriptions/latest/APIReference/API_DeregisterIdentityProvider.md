---
source_url: https://docs.aws.amazon.com/license-manager-user-subscriptions/latest/APIReference/API_DeregisterIdentityProvider.html
---

# DeregisterIdentityProvider
<a name="API_DeregisterIdentityProvider"></a>

Deregisters the Active Directory identity provider from License Manager user-based subscriptions.

## Request Syntax
<a name="API_DeregisterIdentityProvider_RequestSyntax"></a>

```
POST /identity-provider/DeregisterIdentityProvider HTTP/1.1
Content-type: application/json

{
   "IdentityProvider": { ... },
   "IdentityProviderArn": "{{string}}",
   "Product": "{{string}}"
}
```

## URI Request Parameters
<a name="API_DeregisterIdentityProvider_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_DeregisterIdentityProvider_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [IdentityProvider](#API_DeregisterIdentityProvider_RequestSyntax) **   <a name="licensemanagerusersubscriptions-DeregisterIdentityProvider-request-IdentityProvider"></a>
An object that specifies details for the Active Directory identity provider.
Type: [IdentityProvider](API_IdentityProvider.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** [IdentityProviderArn](#API_DeregisterIdentityProvider_RequestSyntax) **   <a name="licensemanagerusersubscriptions-DeregisterIdentityProvider-request-IdentityProviderArn"></a>
The Amazon Resource Name (ARN) that identifies the identity provider to deregister.
Type: String
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{1,63}:[a-zA-Z0-9-\.]{1,510}/[a-zA-Z0-9-\.]{1,510}`
Required: No

 ** [Product](#API_DeregisterIdentityProvider_RequestSyntax) **   <a name="licensemanagerusersubscriptions-DeregisterIdentityProvider-request-Product"></a>
The name of the user-based subscription product.
Valid values: `VISUAL_STUDIO_ENTERPRISE` \| `VISUAL_STUDIO_PROFESSIONAL` \| `OFFICE_PROFESSIONAL_PLUS` \| `OFFICE_STANDARD` \| `REMOTE_DESKTOP_SERVICES`
Type: String
Required: No

## Response Syntax
<a name="API_DeregisterIdentityProvider_ResponseSyntax"></a>

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
<a name="API_DeregisterIdentityProvider_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [IdentityProviderSummary](#API_DeregisterIdentityProvider_ResponseSyntax) **   <a name="licensemanagerusersubscriptions-DeregisterIdentityProvider-response-IdentityProviderSummary"></a>
Metadata that describes the results of an identity provider operation.
Type: [IdentityProviderSummary](API_IdentityProviderSummary.md) object

## Errors
<a name="API_DeregisterIdentityProvider_Errors"></a>

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
<a name="API_DeregisterIdentityProvider_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/license-manager-user-subscriptions-2018-05-10/DeregisterIdentityProvider)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/license-manager-user-subscriptions-2018-05-10/DeregisterIdentityProvider)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/license-manager-user-subscriptions-2018-05-10/DeregisterIdentityProvider)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/license-manager-user-subscriptions-2018-05-10/DeregisterIdentityProvider)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/license-manager-user-subscriptions-2018-05-10/DeregisterIdentityProvider)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/license-manager-user-subscriptions-2018-05-10/DeregisterIdentityProvider)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/license-manager-user-subscriptions-2018-05-10/DeregisterIdentityProvider)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/license-manager-user-subscriptions-2018-05-10/DeregisterIdentityProvider)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/license-manager-user-subscriptions-2018-05-10/DeregisterIdentityProvider)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/license-manager-user-subscriptions-2018-05-10/DeregisterIdentityProvider)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for License Manager User Subscriptions. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query license-manager-user-subscriptions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
