---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_CancelSubscription.html
---

# CancelSubscription
<a name="API_CancelSubscription"></a>

Cancels the subscription to the specified asset.

## Request Syntax
<a name="API_CancelSubscription_RequestSyntax"></a>

```
PUT /v2/domains/{{domainIdentifier}}/subscriptions/{{identifier}}/cancel HTTP/1.1
```

## URI Request Parameters
<a name="API_CancelSubscription_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domainIdentifier](#API_CancelSubscription_RequestSyntax) **   <a name="datazone-CancelSubscription-request-uri-domainIdentifier"></a>
The unique identifier of the Amazon DataZone domain where the subscription request is being cancelled.
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** [identifier](#API_CancelSubscription_RequestSyntax) **   <a name="datazone-CancelSubscription-request-uri-identifier"></a>
The unique identifier of the subscription that is being cancelled.
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: Yes

## Request Body
<a name="API_CancelSubscription_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_CancelSubscription_ResponseSyntax"></a>

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
<a name="API_CancelSubscription_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [createdAt](#API_CancelSubscription_ResponseSyntax) **   <a name="datazone-CancelSubscription-response-createdAt"></a>
The timestamp that specifies when the request to cancel the subscription was created.
Type: Timestamp

 ** [createdBy](#API_CancelSubscription_ResponseSyntax) **   <a name="datazone-CancelSubscription-response-createdBy"></a>
Specifies the Amazon DataZone user who is cancelling the subscription.
Type: String

 ** [domainId](#API_CancelSubscription_ResponseSyntax) **   <a name="datazone-CancelSubscription-response-domainId"></a>
The unique identifier of the Amazon DataZone domain where the subscription is being cancelled.
Type: String
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`

 ** [id](#API_CancelSubscription_ResponseSyntax) **   <a name="datazone-CancelSubscription-response-id"></a>
The identifier of the subscription.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [retainPermissions](#API_CancelSubscription_ResponseSyntax) **   <a name="datazone-CancelSubscription-response-retainPermissions"></a>
Specifies whether the permissions to the asset are retained after the subscription is cancelled.
Type: Boolean

 ** [status](#API_CancelSubscription_ResponseSyntax) **   <a name="datazone-CancelSubscription-response-status"></a>
The status of the request to cancel the subscription.
Type: String
Valid Values: `APPROVED | REVOKED | CANCELLED`

 ** [subscribedListing](#API_CancelSubscription_ResponseSyntax) **   <a name="datazone-CancelSubscription-response-subscribedListing"></a>
The asset to which a subscription is being cancelled.
Type: [SubscribedListing](API_SubscribedListing.md) object

 ** [subscribedPrincipal](#API_CancelSubscription_ResponseSyntax) **   <a name="datazone-CancelSubscription-response-subscribedPrincipal"></a>
The Amazon DataZone user who is made a subscriber to the specified asset by the subscription that is being cancelled.
Type: [SubscribedPrincipal](API_SubscribedPrincipal.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [subscriptionRequestId](#API_CancelSubscription_ResponseSyntax) **   <a name="datazone-CancelSubscription-response-subscriptionRequestId"></a>
The unique ID of the subscripton request for the subscription that is being cancelled.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [updatedAt](#API_CancelSubscription_ResponseSyntax) **   <a name="datazone-CancelSubscription-response-updatedAt"></a>
The timestamp that specifies when the subscription was cancelled.
Type: Timestamp

 ** [updatedBy](#API_CancelSubscription_ResponseSyntax) **   <a name="datazone-CancelSubscription-response-updatedBy"></a>
The Amazon DataZone user that cancelled the subscription.
Type: String

## Errors
<a name="API_CancelSubscription_Errors"></a>

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
<a name="API_CancelSubscription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datazone-2018-05-10/CancelSubscription)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datazone-2018-05-10/CancelSubscription)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/CancelSubscription)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datazone-2018-05-10/CancelSubscription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/CancelSubscription)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datazone-2018-05-10/CancelSubscription)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datazone-2018-05-10/CancelSubscription)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datazone-2018-05-10/CancelSubscription)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/datazone-2018-05-10/CancelSubscription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/CancelSubscription)
