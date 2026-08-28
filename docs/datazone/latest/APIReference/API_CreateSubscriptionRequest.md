---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_CreateSubscriptionRequest.html
---

# CreateSubscriptionRequest
<a name="API_CreateSubscriptionRequest"></a>

Creates a subscription request in Amazon DataZone.

## Request Syntax
<a name="API_CreateSubscriptionRequest_RequestSyntax"></a>

```
POST /v2/domains/{{domainIdentifier}}/subscription-requests HTTP/1.1
Content-type: application/json

{
   "assetPermissions": [
      {
         "assetId": "{{string}}",
         "permissions": { ... }
      }
   ],
   "assetScopes": [
      {
         "assetId": "{{string}}",
         "filterIds": [ "{{string}}" ]
      }
   ],
   "clientToken": "{{string}}",
   "metadataForms": [
      {
         "content": "{{string}}",
         "formName": "{{string}}",
         "typeIdentifier": "{{string}}",
         "typeRevision": "{{string}}"
      }
   ],
   "requestReason": "{{string}}",
   "subscribedListings": [
      {
         "identifier": "{{string}}"
      }
   ],
   "subscribedPrincipals": [
      { ... }
   ]
}
```

## URI Request Parameters
<a name="API_CreateSubscriptionRequest_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domainIdentifier](#API_CreateSubscriptionRequest_RequestSyntax) **   <a name="datazone-CreateSubscriptionRequest-request-uri-domainIdentifier"></a>
The ID of the Amazon DataZone domain in which the subscription request is created.
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

## Request Body
<a name="API_CreateSubscriptionRequest_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [assetPermissions](#API_CreateSubscriptionRequest_RequestSyntax) **   <a name="datazone-CreateSubscriptionRequest-request-assetPermissions"></a>
The asset permissions of the subscription request.
Type: Array of [AssetPermission](API_AssetPermission.md) objects
Required: No

 ** [assetScopes](#API_CreateSubscriptionRequest_RequestSyntax) **   <a name="datazone-CreateSubscriptionRequest-request-assetScopes"></a>
The asset scopes of the subscription request.
Type: Array of [AcceptedAssetScope](API_AcceptedAssetScope.md) objects
Required: No

 ** [clientToken](#API_CreateSubscriptionRequest_RequestSyntax) **   <a name="datazone-CreateSubscriptionRequest-request-clientToken"></a>
A unique, case-sensitive identifier that is provided to ensure the idempotency of the request.
Type: String
Required: No

 ** [metadataForms](#API_CreateSubscriptionRequest_RequestSyntax) **   <a name="datazone-CreateSubscriptionRequest-request-metadataForms"></a>
The metadata form included in the subscription request.
Type: Array of [FormInput](API_FormInput.md) objects
Required: No

 ** [requestReason](#API_CreateSubscriptionRequest_RequestSyntax) **   <a name="datazone-CreateSubscriptionRequest-request-requestReason"></a>
The reason for the subscription request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Required: Yes

 ** [subscribedListings](#API_CreateSubscriptionRequest_RequestSyntax) **   <a name="datazone-CreateSubscriptionRequest-request-subscribedListings"></a>
The published asset for which the subscription grant is to be created.
Type: Array of [SubscribedListingInput](API_SubscribedListingInput.md) objects
Array Members: Fixed number of 1 item.
Required: Yes

 ** [subscribedPrincipals](#API_CreateSubscriptionRequest_RequestSyntax) **   <a name="datazone-CreateSubscriptionRequest-request-subscribedPrincipals"></a>
The Amazon DataZone principals for whom the subscription request is created.
Type: Array of [SubscribedPrincipalInput](API_SubscribedPrincipalInput.md) objects
Array Members: Fixed number of 1 item.
Required: Yes

## Response Syntax
<a name="API_CreateSubscriptionRequest_ResponseSyntax"></a>

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
<a name="API_CreateSubscriptionRequest_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [createdAt](#API_CreateSubscriptionRequest_ResponseSyntax) **   <a name="datazone-CreateSubscriptionRequest-response-createdAt"></a>
A timestamp of when the subscription request is created.
Type: Timestamp

 ** [createdBy](#API_CreateSubscriptionRequest_ResponseSyntax) **   <a name="datazone-CreateSubscriptionRequest-response-createdBy"></a>
The Amazon DataZone user who created the subscription request.
Type: String

 ** [decisionComment](#API_CreateSubscriptionRequest_ResponseSyntax) **   <a name="datazone-CreateSubscriptionRequest-response-decisionComment"></a>
The decision comment of the subscription request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.

 ** [domainId](#API_CreateSubscriptionRequest_ResponseSyntax) **   <a name="datazone-CreateSubscriptionRequest-response-domainId"></a>
The ID of the Amazon DataZone domain in whcih the subscription request is created.
Type: String
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`

 ** [existingSubscriptionId](#API_CreateSubscriptionRequest_ResponseSyntax) **   <a name="datazone-CreateSubscriptionRequest-response-existingSubscriptionId"></a>
The ID of the existing subscription.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [id](#API_CreateSubscriptionRequest_ResponseSyntax) **   <a name="datazone-CreateSubscriptionRequest-response-id"></a>
The ID of the subscription request.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [metadataForms](#API_CreateSubscriptionRequest_ResponseSyntax) **   <a name="datazone-CreateSubscriptionRequest-response-metadataForms"></a>
The metadata form included in the subscription request.
Type: Array of [FormOutput](API_FormOutput.md) objects

 ** [requestReason](#API_CreateSubscriptionRequest_ResponseSyntax) **   <a name="datazone-CreateSubscriptionRequest-response-requestReason"></a>
The reason for the subscription request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.

 ** [reviewerId](#API_CreateSubscriptionRequest_ResponseSyntax) **   <a name="datazone-CreateSubscriptionRequest-response-reviewerId"></a>
The ID of the reviewer of the subscription request.
Type: String

 ** [status](#API_CreateSubscriptionRequest_ResponseSyntax) **   <a name="datazone-CreateSubscriptionRequest-response-status"></a>
The status of the subscription request.
Type: String
Valid Values: `PENDING | ACCEPTED | REJECTED`

 ** [subscribedListings](#API_CreateSubscriptionRequest_ResponseSyntax) **   <a name="datazone-CreateSubscriptionRequest-response-subscribedListings"></a>
The published asset for which the subscription grant is to be created.
Type: Array of [SubscribedListing](API_SubscribedListing.md) objects
Array Members: Fixed number of 1 item.

 ** [subscribedPrincipals](#API_CreateSubscriptionRequest_ResponseSyntax) **   <a name="datazone-CreateSubscriptionRequest-response-subscribedPrincipals"></a>
The subscribed principals of the subscription request.
Type: Array of [SubscribedPrincipal](API_SubscribedPrincipal.md) objects
Array Members: Fixed number of 1 item.

 ** [updatedAt](#API_CreateSubscriptionRequest_ResponseSyntax) **   <a name="datazone-CreateSubscriptionRequest-response-updatedAt"></a>
The timestamp of when the subscription request was updated.
Type: Timestamp

 ** [updatedBy](#API_CreateSubscriptionRequest_ResponseSyntax) **   <a name="datazone-CreateSubscriptionRequest-response-updatedBy"></a>
The Amazon DataZone user who updated the subscription request.
Type: String

## Errors
<a name="API_CreateSubscriptionRequest_Errors"></a>

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

 ** ServiceQuotaExceededException **
The request has exceeded the specified service quota.
HTTP Status Code: 402

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
<a name="API_CreateSubscriptionRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datazone-2018-05-10/CreateSubscriptionRequest)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datazone-2018-05-10/CreateSubscriptionRequest)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/CreateSubscriptionRequest)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datazone-2018-05-10/CreateSubscriptionRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/CreateSubscriptionRequest)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datazone-2018-05-10/CreateSubscriptionRequest)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datazone-2018-05-10/CreateSubscriptionRequest)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datazone-2018-05-10/CreateSubscriptionRequest)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/datazone-2018-05-10/CreateSubscriptionRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/CreateSubscriptionRequest)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DataZone. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datazone` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
