---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_GetSubscriptionRequestDetails.html
---

# GetSubscriptionRequestDetails
<a name="API_GetSubscriptionRequestDetails"></a>

Gets the details of the specified subscription request.

## Request Syntax
<a name="API_GetSubscriptionRequestDetails_RequestSyntax"></a>

```
GET /v2/domains/{{domainIdentifier}}/subscription-requests/{{identifier}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetSubscriptionRequestDetails_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domainIdentifier](#API_GetSubscriptionRequestDetails_RequestSyntax) **   <a name="datazone-GetSubscriptionRequestDetails-request-uri-domainIdentifier"></a>
The identifier of the Amazon DataZone domain in which to get the subscription request details.
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** [identifier](#API_GetSubscriptionRequestDetails_RequestSyntax) **   <a name="datazone-GetSubscriptionRequestDetails-request-uri-identifier"></a>
The identifier of the subscription request the details of which to get.
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: Yes

## Request Body
<a name="API_GetSubscriptionRequestDetails_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetSubscriptionRequestDetails_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "createdAt": number,
   "createdBy": "string",
   "decisionComment": "string",
   "domainId": "string",
   "existingSubscriptionId": "string",
   "id": "string",
   "metadataForms": [
      {
         "content": "string",
         "formName": "string",
         "typeName": "string",
         "typeRevision": "string"
      }
   ],
   "requestReason": "string",
   "reviewerId": "string",
   "status": "string",
   "subscribedListings": [
      {
         "description": "string",
         "id": "string",
         "item": { ... },
         "name": "string",
         "ownerProjectId": "string",
         "ownerProjectName": "string",
         "revision": "string"
      }
   ],
   "subscribedPrincipals": [
      { ... }
   ],
   "updatedAt": number,
   "updatedBy": "string"
}
```

## Response Elements
<a name="API_GetSubscriptionRequestDetails_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [createdAt](#API_GetSubscriptionRequestDetails_ResponseSyntax) **   <a name="datazone-GetSubscriptionRequestDetails-response-createdAt"></a>
The timestamp of when the specified subscription request was created.
Type: Timestamp

 ** [createdBy](#API_GetSubscriptionRequestDetails_ResponseSyntax) **   <a name="datazone-GetSubscriptionRequestDetails-response-createdBy"></a>
The Amazon DataZone user who created the subscription request.
Type: String

 ** [decisionComment](#API_GetSubscriptionRequestDetails_ResponseSyntax) **   <a name="datazone-GetSubscriptionRequestDetails-response-decisionComment"></a>
The decision comment of the subscription request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.

 ** [domainId](#API_GetSubscriptionRequestDetails_ResponseSyntax) **   <a name="datazone-GetSubscriptionRequestDetails-response-domainId"></a>
The Amazon DataZone domain of the subscription request.
Type: String
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`

 ** [existingSubscriptionId](#API_GetSubscriptionRequestDetails_ResponseSyntax) **   <a name="datazone-GetSubscriptionRequestDetails-response-existingSubscriptionId"></a>
The ID of the existing subscription.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [id](#API_GetSubscriptionRequestDetails_ResponseSyntax) **   <a name="datazone-GetSubscriptionRequestDetails-response-id"></a>
The identifier of the subscription request.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [metadataForms](#API_GetSubscriptionRequestDetails_ResponseSyntax) **   <a name="datazone-GetSubscriptionRequestDetails-response-metadataForms"></a>
The metadata forms included in the subscription request.
Type: Array of [FormOutput](API_FormOutput.md) objects

 ** [requestReason](#API_GetSubscriptionRequestDetails_ResponseSyntax) **   <a name="datazone-GetSubscriptionRequestDetails-response-requestReason"></a>
The reason for the subscription request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.

 ** [reviewerId](#API_GetSubscriptionRequestDetails_ResponseSyntax) **   <a name="datazone-GetSubscriptionRequestDetails-response-reviewerId"></a>
The identifier of the Amazon DataZone user who reviewed the subscription request.
Type: String

 ** [status](#API_GetSubscriptionRequestDetails_ResponseSyntax) **   <a name="datazone-GetSubscriptionRequestDetails-response-status"></a>
The status of the subscription request.
Type: String
Valid Values: `PENDING | ACCEPTED | REJECTED`

 ** [subscribedListings](#API_GetSubscriptionRequestDetails_ResponseSyntax) **   <a name="datazone-GetSubscriptionRequestDetails-response-subscribedListings"></a>
The subscribed listings in the subscription request.
Type: Array of [SubscribedListing](API_SubscribedListing.md) objects
Array Members: Fixed number of 1 item.

 ** [subscribedPrincipals](#API_GetSubscriptionRequestDetails_ResponseSyntax) **   <a name="datazone-GetSubscriptionRequestDetails-response-subscribedPrincipals"></a>
The subscribed principals in the subscription request.
Type: Array of [SubscribedPrincipal](API_SubscribedPrincipal.md) objects
Array Members: Fixed number of 1 item.

 ** [updatedAt](#API_GetSubscriptionRequestDetails_ResponseSyntax) **   <a name="datazone-GetSubscriptionRequestDetails-response-updatedAt"></a>
The timestamp of when the subscription request was updated.
Type: Timestamp

 ** [updatedBy](#API_GetSubscriptionRequestDetails_ResponseSyntax) **   <a name="datazone-GetSubscriptionRequestDetails-response-updatedBy"></a>
The Amazon DataZone user who updated the subscription request.
Type: String

## Errors
<a name="API_GetSubscriptionRequestDetails_Errors"></a>

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
<a name="API_GetSubscriptionRequestDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datazone-2018-05-10/GetSubscriptionRequestDetails)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datazone-2018-05-10/GetSubscriptionRequestDetails)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/GetSubscriptionRequestDetails)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datazone-2018-05-10/GetSubscriptionRequestDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/GetSubscriptionRequestDetails)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datazone-2018-05-10/GetSubscriptionRequestDetails)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datazone-2018-05-10/GetSubscriptionRequestDetails)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datazone-2018-05-10/GetSubscriptionRequestDetails)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/datazone-2018-05-10/GetSubscriptionRequestDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/GetSubscriptionRequestDetails)
