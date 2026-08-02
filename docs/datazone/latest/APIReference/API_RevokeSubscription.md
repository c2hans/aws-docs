---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_RevokeSubscription.html
---

# RevokeSubscription
<a name="API_RevokeSubscription"></a>

Revokes a specified subscription in Amazon DataZone.

## Request Syntax
<a name="API_RevokeSubscription_RequestSyntax"></a>

```
PUT /v2/domains/{{domainIdentifier}}/subscriptions/{{identifier}}/revoke HTTP/1.1
Content-type: application/json

{
   "retainPermissions": {{boolean}}
}
```

## URI Request Parameters
<a name="API_RevokeSubscription_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domainIdentifier](#API_RevokeSubscription_RequestSyntax) **   <a name="datazone-RevokeSubscription-request-uri-domainIdentifier"></a>
The identifier of the Amazon DataZone domain where you want to revoke a subscription.
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** [identifier](#API_RevokeSubscription_RequestSyntax) **   <a name="datazone-RevokeSubscription-request-uri-identifier"></a>
The identifier of the revoked subscription.
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: Yes

## Request Body
<a name="API_RevokeSubscription_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [retainPermissions](#API_RevokeSubscription_RequestSyntax) **   <a name="datazone-RevokeSubscription-request-retainPermissions"></a>
Specifies whether permissions are retained when the subscription is revoked.
Type: Boolean
Required: No

## Response Syntax
<a name="API_RevokeSubscription_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "createdAt": number,
   "createdBy": "string",
   "domainId": "string",
   "id": "string",
   "retainPermissions": boolean,
   "status": "string",
   "subscribedListing": {
      "description": "string",
      "id": "string",
      "item": { ... },
      "name": "string",
      "ownerProjectId": "string",
      "ownerProjectName": "string",
      "revision": "string"
   },
   "subscribedPrincipal": { ... },
   "subscriptionRequestId": "string",
   "updatedAt": number,
   "updatedBy": "string"
}
```

## Response Elements
<a name="API_RevokeSubscription_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [createdAt](#API_RevokeSubscription_ResponseSyntax) **   <a name="datazone-RevokeSubscription-response-createdAt"></a>
The timestamp of when the subscription was revoked.
Type: Timestamp

 ** [createdBy](#API_RevokeSubscription_ResponseSyntax) **   <a name="datazone-RevokeSubscription-response-createdBy"></a>
The identifier of the user who revoked the subscription.
Type: String

 ** [domainId](#API_RevokeSubscription_ResponseSyntax) **   <a name="datazone-RevokeSubscription-response-domainId"></a>
The identifier of the Amazon DataZone domain where you want to revoke a subscription.
Type: String
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`

 ** [id](#API_RevokeSubscription_ResponseSyntax) **   <a name="datazone-RevokeSubscription-response-id"></a>
The identifier of the revoked subscription.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [retainPermissions](#API_RevokeSubscription_ResponseSyntax) **   <a name="datazone-RevokeSubscription-response-retainPermissions"></a>
Specifies whether permissions are retained when the subscription is revoked.
Type: Boolean

 ** [status](#API_RevokeSubscription_ResponseSyntax) **   <a name="datazone-RevokeSubscription-response-status"></a>
The status of the revoked subscription.
Type: String
Valid Values: `APPROVED | REVOKED | CANCELLED`

 ** [subscribedListing](#API_RevokeSubscription_ResponseSyntax) **   <a name="datazone-RevokeSubscription-response-subscribedListing"></a>
The subscribed listing of the revoked subscription.
Type: [SubscribedListing](API_SubscribedListing.md) object

 ** [subscribedPrincipal](#API_RevokeSubscription_ResponseSyntax) **   <a name="datazone-RevokeSubscription-response-subscribedPrincipal"></a>
The subscribed principal of the revoked subscription.
Type: [SubscribedPrincipal](API_SubscribedPrincipal.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [subscriptionRequestId](#API_RevokeSubscription_ResponseSyntax) **   <a name="datazone-RevokeSubscription-response-subscriptionRequestId"></a>
The identifier of the subscription request for the revoked subscription.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [updatedAt](#API_RevokeSubscription_ResponseSyntax) **   <a name="datazone-RevokeSubscription-response-updatedAt"></a>
The timestamp of when the subscription was revoked.
Type: Timestamp

 ** [updatedBy](#API_RevokeSubscription_ResponseSyntax) **   <a name="datazone-RevokeSubscription-response-updatedBy"></a>
The Amazon DataZone user who revoked the subscription.
Type: String

## Errors
<a name="API_RevokeSubscription_Errors"></a>

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
<a name="API_RevokeSubscription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datazone-2018-05-10/RevokeSubscription)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datazone-2018-05-10/RevokeSubscription)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/RevokeSubscription)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datazone-2018-05-10/RevokeSubscription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/RevokeSubscription)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datazone-2018-05-10/RevokeSubscription)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datazone-2018-05-10/RevokeSubscription)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datazone-2018-05-10/RevokeSubscription)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/datazone-2018-05-10/RevokeSubscription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/RevokeSubscription)
