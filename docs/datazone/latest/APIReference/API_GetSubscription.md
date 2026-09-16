---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_GetSubscription.html
---

# GetSubscription
<a name="API_GetSubscription"></a>

Gets a subscription in Amazon DataZone.

## Request Syntax
<a name="API_GetSubscription_RequestSyntax"></a>

```
GET /v2/domains/{{domainIdentifier}}/subscriptions/{{identifier}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetSubscription_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domainIdentifier](#API_GetSubscription_RequestSyntax) **   <a name="datazone-GetSubscription-request-uri-domainIdentifier"></a>
The ID of the Amazon DataZone domain in which the subscription exists.
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** [identifier](#API_GetSubscription_RequestSyntax) **   <a name="datazone-GetSubscription-request-uri-identifier"></a>
The ID of the subscription.
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: Yes

## Request Body
<a name="API_GetSubscription_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetSubscription_ResponseSyntax"></a>

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
<a name="API_GetSubscription_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [createdAt](#API_GetSubscription_ResponseSyntax) **   <a name="datazone-GetSubscription-response-createdAt"></a>
The timestamp of when the subscription was created.
Type: Timestamp

 ** [createdBy](#API_GetSubscription_ResponseSyntax) **   <a name="datazone-GetSubscription-response-createdBy"></a>
The Amazon DataZone user who created the subscription.
Type: String

 ** [domainId](#API_GetSubscription_ResponseSyntax) **   <a name="datazone-GetSubscription-response-domainId"></a>
The ID of the Amazon DataZone domain in which the subscription exists.
Type: String
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`

 ** [id](#API_GetSubscription_ResponseSyntax) **   <a name="datazone-GetSubscription-response-id"></a>
The ID of the subscription.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [retainPermissions](#API_GetSubscription_ResponseSyntax) **   <a name="datazone-GetSubscription-response-retainPermissions"></a>
The retain permissions of the subscription.
Type: Boolean

 ** [status](#API_GetSubscription_ResponseSyntax) **   <a name="datazone-GetSubscription-response-status"></a>
The status of the subscription.
Type: String
Valid Values: `APPROVED | REVOKED | CANCELLED`

 ** [subscribedListing](#API_GetSubscription_ResponseSyntax) **   <a name="datazone-GetSubscription-response-subscribedListing"></a>
The details of the published asset for which the subscription grant is created.
Type: [SubscribedListing](API_SubscribedListing.md) object

 ** [subscribedPrincipal](#API_GetSubscription_ResponseSyntax) **   <a name="datazone-GetSubscription-response-subscribedPrincipal"></a>
The principal that owns the subscription.
Type: [SubscribedPrincipal](API_SubscribedPrincipal.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [subscriptionRequestId](#API_GetSubscription_ResponseSyntax) **   <a name="datazone-GetSubscription-response-subscriptionRequestId"></a>
The ID of the subscription request.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [updatedAt](#API_GetSubscription_ResponseSyntax) **   <a name="datazone-GetSubscription-response-updatedAt"></a>
The timestamp of when the subscription was updated.
Type: Timestamp

 ** [updatedBy](#API_GetSubscription_ResponseSyntax) **   <a name="datazone-GetSubscription-response-updatedBy"></a>
The Amazon DataZone user who updated the subscription.
Type: String

## Errors
<a name="API_GetSubscription_Errors"></a>

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
<a name="API_GetSubscription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datazone-2018-05-10/GetSubscription)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datazone-2018-05-10/GetSubscription)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/GetSubscription)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datazone-2018-05-10/GetSubscription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/GetSubscription)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datazone-2018-05-10/GetSubscription)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datazone-2018-05-10/GetSubscription)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datazone-2018-05-10/GetSubscription)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/datazone-2018-05-10/GetSubscription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/GetSubscription)
