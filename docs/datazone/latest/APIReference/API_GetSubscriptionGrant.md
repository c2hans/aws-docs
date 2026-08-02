---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_GetSubscriptionGrant.html
---

# GetSubscriptionGrant
<a name="API_GetSubscriptionGrant"></a>

Gets the subscription grant in Amazon DataZone.

## Request Syntax
<a name="API_GetSubscriptionGrant_RequestSyntax"></a>

```
GET /v2/domains/{{domainIdentifier}}/subscription-grants/{{identifier}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetSubscriptionGrant_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domainIdentifier](#API_GetSubscriptionGrant_RequestSyntax) **   <a name="datazone-GetSubscriptionGrant-request-uri-domainIdentifier"></a>
The ID of the Amazon DataZone domain in which the subscription grant exists.
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** [identifier](#API_GetSubscriptionGrant_RequestSyntax) **   <a name="datazone-GetSubscriptionGrant-request-uri-identifier"></a>
The ID of the subscription grant.
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: Yes

## Request Body
<a name="API_GetSubscriptionGrant_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetSubscriptionGrant_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "assets": [
      {
         "assetId": "string",
         "assetRevision": "string",
         "assetScope": {
            "assetId": "string",
            "errorMessage": "string",
            "filterIds": [ "string" ],
            "status": "string"
         },
         "failureCause": {
            "message": "string"
         },
         "failureTimestamp": number,
         "grantedTimestamp": number,
         "permissions": { ... },
         "status": "string",
         "targetName": "string"
      }
   ],
   "createdAt": number,
   "createdBy": "string",
   "domainId": "string",
   "environmentId": "string",
   "grantedEntity": { ... },
   "id": "string",
   "status": "string",
   "subscriptionId": "string",
   "subscriptionTargetId": "string",
   "updatedAt": number,
   "updatedBy": "string"
}
```

## Response Elements
<a name="API_GetSubscriptionGrant_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [assets](#API_GetSubscriptionGrant_ResponseSyntax) **   <a name="datazone-GetSubscriptionGrant-response-assets"></a>
The assets for which the subscription grant is created.
Type: Array of [SubscribedAsset](API_SubscribedAsset.md) objects

 ** [createdAt](#API_GetSubscriptionGrant_ResponseSyntax) **   <a name="datazone-GetSubscriptionGrant-response-createdAt"></a>
The timestamp of when the subscription grant is created.
Type: Timestamp

 ** [createdBy](#API_GetSubscriptionGrant_ResponseSyntax) **   <a name="datazone-GetSubscriptionGrant-response-createdBy"></a>
The Amazon DataZone user who created the subscription grant.
Type: String

 ** [domainId](#API_GetSubscriptionGrant_ResponseSyntax) **   <a name="datazone-GetSubscriptionGrant-response-domainId"></a>
The ID of the Amazon DataZone domain in which the subscription grant exists.
Type: String
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`

 ** [environmentId](#API_GetSubscriptionGrant_ResponseSyntax) **   <a name="datazone-GetSubscriptionGrant-response-environmentId"></a>
The environment ID of the subscription grant.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [grantedEntity](#API_GetSubscriptionGrant_ResponseSyntax) **   <a name="datazone-GetSubscriptionGrant-response-grantedEntity"></a>
The entity to which the subscription is granted.
Type: [GrantedEntity](API_GrantedEntity.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [id](#API_GetSubscriptionGrant_ResponseSyntax) **   <a name="datazone-GetSubscriptionGrant-response-id"></a>
The ID of the subscription grant.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [status](#API_GetSubscriptionGrant_ResponseSyntax) **   <a name="datazone-GetSubscriptionGrant-response-status"></a>
The status of the subscription grant.
Type: String
Valid Values: `PENDING | IN_PROGRESS | GRANT_FAILED | REVOKE_FAILED | GRANT_AND_REVOKE_FAILED | COMPLETED | INACCESSIBLE`

 ** [subscriptionId](#API_GetSubscriptionGrant_ResponseSyntax) **   <a name="datazone-GetSubscriptionGrant-response-subscriptionId"></a>
 *This parameter has been deprecated.*
The identifier of the subscription.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [subscriptionTargetId](#API_GetSubscriptionGrant_ResponseSyntax) **   <a name="datazone-GetSubscriptionGrant-response-subscriptionTargetId"></a>
The subscription target ID associated with the subscription grant.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [updatedAt](#API_GetSubscriptionGrant_ResponseSyntax) **   <a name="datazone-GetSubscriptionGrant-response-updatedAt"></a>
The timestamp of when the subscription grant was upated.
Type: Timestamp

 ** [updatedBy](#API_GetSubscriptionGrant_ResponseSyntax) **   <a name="datazone-GetSubscriptionGrant-response-updatedBy"></a>
The Amazon DataZone user who updated the subscription grant.
Type: String

## Errors
<a name="API_GetSubscriptionGrant_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
The request has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource cannot be found.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** UnauthorizedException **
You do not have permission to perform this action.
HTTP Status Code: 401

 ** ValidationException **
The input fails to satisfy the constraints specified by the AWS service.
HTTP Status Code: 400

## See Also
<a name="API_GetSubscriptionGrant_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datazone-2018-05-10/GetSubscriptionGrant)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datazone-2018-05-10/GetSubscriptionGrant)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/GetSubscriptionGrant)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datazone-2018-05-10/GetSubscriptionGrant)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/GetSubscriptionGrant)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datazone-2018-05-10/GetSubscriptionGrant)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datazone-2018-05-10/GetSubscriptionGrant)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datazone-2018-05-10/GetSubscriptionGrant)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/datazone-2018-05-10/GetSubscriptionGrant)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/GetSubscriptionGrant)
