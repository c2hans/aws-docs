---
source_url: https://docs.aws.amazon.com/license-manager-user-subscriptions/latest/APIReference/API_ListProductSubscriptions.html
---

# ListProductSubscriptions
<a name="API_ListProductSubscriptions"></a>

Lists the user-based subscription products available from an identity provider.

## Request Syntax
<a name="API_ListProductSubscriptions_RequestSyntax"></a>

```
POST /user/ListProductSubscriptions HTTP/1.1
Content-type: application/json

{
   "Filters": [
      {
         "Attribute": "{{string}}",
         "Operation": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "IdentityProvider": { ... },
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "Product": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListProductSubscriptions_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListProductSubscriptions_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Filters](#API_ListProductSubscriptions_RequestSyntax) **   <a name="licensemanagerusersubscriptions-ListProductSubscriptions-request-Filters"></a>
You can use the following filters to streamline results:
+ Status
+ Username
+ Domain
Type: Array of [Filter](API_Filter.md) objects
Required: No

 ** [IdentityProvider](#API_ListProductSubscriptions_RequestSyntax) **   <a name="licensemanagerusersubscriptions-ListProductSubscriptions-request-IdentityProvider"></a>
An object that specifies details for the identity provider.
Type: [IdentityProvider](API_IdentityProvider.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** [MaxResults](#API_ListProductSubscriptions_RequestSyntax) **   <a name="licensemanagerusersubscriptions-ListProductSubscriptions-request-MaxResults"></a>
The maximum number of results to return from a single request.
Type: Integer
Required: No

 ** [NextToken](#API_ListProductSubscriptions_RequestSyntax) **   <a name="licensemanagerusersubscriptions-ListProductSubscriptions-request-NextToken"></a>
A token to specify where to start paginating. This is the nextToken from a previously truncated response.
Type: String
Required: No

 ** [Product](#API_ListProductSubscriptions_RequestSyntax) **   <a name="licensemanagerusersubscriptions-ListProductSubscriptions-request-Product"></a>
The name of the user-based subscription product.
Valid values: `VISUAL_STUDIO_ENTERPRISE` \| `VISUAL_STUDIO_PROFESSIONAL` \| `OFFICE_PROFESSIONAL_PLUS` \| `OFFICE_STANDARD` \| `REMOTE_DESKTOP_SERVICES`
Type: String
Required: No

## Response Syntax
<a name="API_ListProductSubscriptions_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "string",
   "ProductUserSummaries": [
      {
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
   ]
}
```

## Response Elements
<a name="API_ListProductSubscriptions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListProductSubscriptions_ResponseSyntax) **   <a name="licensemanagerusersubscriptions-ListProductSubscriptions-response-NextToken"></a>
The next token used for paginated responses. When this field isn't empty, there are additional elements that the service hasn't included in this request. Use this token with the next request to retrieve additional objects.
Type: String

 ** [ProductUserSummaries](#API_ListProductSubscriptions_ResponseSyntax) **   <a name="licensemanagerusersubscriptions-ListProductSubscriptions-response-ProductUserSummaries"></a>
Metadata that describes the list product subscriptions operation.
Type: Array of [ProductUserSummary](API_ProductUserSummary.md) objects

## Errors
<a name="API_ListProductSubscriptions_Errors"></a>

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
<a name="API_ListProductSubscriptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/license-manager-user-subscriptions-2018-05-10/ListProductSubscriptions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/license-manager-user-subscriptions-2018-05-10/ListProductSubscriptions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/license-manager-user-subscriptions-2018-05-10/ListProductSubscriptions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/license-manager-user-subscriptions-2018-05-10/ListProductSubscriptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/license-manager-user-subscriptions-2018-05-10/ListProductSubscriptions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/license-manager-user-subscriptions-2018-05-10/ListProductSubscriptions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/license-manager-user-subscriptions-2018-05-10/ListProductSubscriptions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/license-manager-user-subscriptions-2018-05-10/ListProductSubscriptions)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/license-manager-user-subscriptions-2018-05-10/ListProductSubscriptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/license-manager-user-subscriptions-2018-05-10/ListProductSubscriptions)
