---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_CreateSubscriptionGrant.html
---

# CreateSubscriptionGrant
<a name="API_CreateSubscriptionGrant"></a>

Creates a subsscription grant in Amazon DataZone.

## Request Syntax
<a name="API_CreateSubscriptionGrant_RequestSyntax"></a>

```
POST /v2/domains/{{domainIdentifier}}/subscription-grants HTTP/1.1
Content-type: application/json

{
   "assetTargetNames": [
      {
         "assetId": "{{string}}",
         "targetName": "{{string}}"
      }
   ],
   "clientToken": "{{string}}",
   "environmentIdentifier": "{{string}}",
   "grantedEntity": { ... },
   "subscriptionTargetIdentifier": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateSubscriptionGrant_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domainIdentifier](#API_CreateSubscriptionGrant_RequestSyntax) **   <a name="datazone-CreateSubscriptionGrant-request-uri-domainIdentifier"></a>
The ID of the Amazon DataZone domain in which the subscription grant is created.
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

## Request Body
<a name="API_CreateSubscriptionGrant_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [assetTargetNames](#API_CreateSubscriptionGrant_RequestSyntax) **   <a name="datazone-CreateSubscriptionGrant-request-assetTargetNames"></a>
The names of the assets for which the subscription grant is created.
Type: Array of [AssetTargetNameMap](API_AssetTargetNameMap.md) objects
Required: No

 ** [clientToken](#API_CreateSubscriptionGrant_RequestSyntax) **   <a name="datazone-CreateSubscriptionGrant-request-clientToken"></a>
A unique, case-sensitive identifier that is provided to ensure the idempotency of the request.
Type: String
Required: No

 ** [environmentIdentifier](#API_CreateSubscriptionGrant_RequestSyntax) **   <a name="datazone-CreateSubscriptionGrant-request-environmentIdentifier"></a>
The ID of the environment in which the subscription grant is created.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** [grantedEntity](#API_CreateSubscriptionGrant_RequestSyntax) **   <a name="datazone-CreateSubscriptionGrant-request-grantedEntity"></a>
The entity to which the subscription is to be granted.
Type: [GrantedEntityInput](API_GrantedEntityInput.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** [subscriptionTargetIdentifier](#API_CreateSubscriptionGrant_RequestSyntax) **   <a name="datazone-CreateSubscriptionGrant-request-subscriptionTargetIdentifier"></a>
The ID of the subscription target for which the subscription grant is created.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: No

## Response Syntax
<a name="API_CreateSubscriptionGrant_ResponseSyntax"></a>

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
<a name="API_CreateSubscriptionGrant_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [assets](#API_CreateSubscriptionGrant_ResponseSyntax) **   <a name="datazone-CreateSubscriptionGrant-response-assets"></a>
The assets for which the subscription grant is created.
Type: Array of [SubscribedAsset](API_SubscribedAsset.md) objects

 ** [createdAt](#API_CreateSubscriptionGrant_ResponseSyntax) **   <a name="datazone-CreateSubscriptionGrant-response-createdAt"></a>
A timestamp of when the subscription grant is created.
Type: Timestamp

 ** [createdBy](#API_CreateSubscriptionGrant_ResponseSyntax) **   <a name="datazone-CreateSubscriptionGrant-response-createdBy"></a>
The Amazon DataZone user who created the subscription grant.
Type: String

 ** [domainId](#API_CreateSubscriptionGrant_ResponseSyntax) **   <a name="datazone-CreateSubscriptionGrant-response-domainId"></a>
The ID of the Amazon DataZone domain in which the subscription grant is created.
Type: String
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`

 ** [environmentId](#API_CreateSubscriptionGrant_ResponseSyntax) **   <a name="datazone-CreateSubscriptionGrant-response-environmentId"></a>
The environment ID for which subscription grant is created.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [grantedEntity](#API_CreateSubscriptionGrant_ResponseSyntax) **   <a name="datazone-CreateSubscriptionGrant-response-grantedEntity"></a>
The entity to which the subscription is granted.
Type: [GrantedEntity](API_GrantedEntity.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [id](#API_CreateSubscriptionGrant_ResponseSyntax) **   <a name="datazone-CreateSubscriptionGrant-response-id"></a>
The ID of the subscription grant.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [status](#API_CreateSubscriptionGrant_ResponseSyntax) **   <a name="datazone-CreateSubscriptionGrant-response-status"></a>
The status of the subscription grant.
Type: String
Valid Values: `PENDING | IN_PROGRESS | GRANT_FAILED | REVOKE_FAILED | GRANT_AND_REVOKE_FAILED | COMPLETED | INACCESSIBLE`

 ** [subscriptionId](#API_CreateSubscriptionGrant_ResponseSyntax) **   <a name="datazone-CreateSubscriptionGrant-response-subscriptionId"></a>
 *This parameter has been deprecated.*
The identifier of the subscription grant.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [subscriptionTargetId](#API_CreateSubscriptionGrant_ResponseSyntax) **   <a name="datazone-CreateSubscriptionGrant-response-subscriptionTargetId"></a>
The ID of the subscription target for which the subscription grant is created.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [updatedAt](#API_CreateSubscriptionGrant_ResponseSyntax) **   <a name="datazone-CreateSubscriptionGrant-response-updatedAt"></a>
A timestamp of when the subscription grant was updated.
Type: Timestamp

 ** [updatedBy](#API_CreateSubscriptionGrant_ResponseSyntax) **   <a name="datazone-CreateSubscriptionGrant-response-updatedBy"></a>
The Amazon DataZone user who updated the subscription grant.
Type: String

## Errors
<a name="API_CreateSubscriptionGrant_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
There is a conflict while performing this action.
HTTP Status Code: 409

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
<a name="API_CreateSubscriptionGrant_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datazone-2018-05-10/CreateSubscriptionGrant)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datazone-2018-05-10/CreateSubscriptionGrant)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/CreateSubscriptionGrant)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datazone-2018-05-10/CreateSubscriptionGrant)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/CreateSubscriptionGrant)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datazone-2018-05-10/CreateSubscriptionGrant)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datazone-2018-05-10/CreateSubscriptionGrant)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datazone-2018-05-10/CreateSubscriptionGrant)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/datazone-2018-05-10/CreateSubscriptionGrant)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/CreateSubscriptionGrant)
