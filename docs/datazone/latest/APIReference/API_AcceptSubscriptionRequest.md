---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_AcceptSubscriptionRequest.html
---

# AcceptSubscriptionRequest
<a name="API_AcceptSubscriptionRequest"></a>

Accepts a subscription request to a specific asset.

## Request Syntax
<a name="API_AcceptSubscriptionRequest_RequestSyntax"></a>

```
PUT /v2/domains/{{domainIdentifier}}/subscription-requests/{{identifier}}/accept HTTP/1.1
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
   "decisionComment": "{{string}}"
}
```

## URI Request Parameters
<a name="API_AcceptSubscriptionRequest_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domainIdentifier](#API_AcceptSubscriptionRequest_RequestSyntax) **   <a name="datazone-AcceptSubscriptionRequest-request-uri-domainIdentifier"></a>
The Amazon DataZone domain where the specified subscription request is being accepted.
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** [identifier](#API_AcceptSubscriptionRequest_RequestSyntax) **   <a name="datazone-AcceptSubscriptionRequest-request-uri-identifier"></a>
The unique identifier of the subscription request that is to be accepted.
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: Yes

## Request Body
<a name="API_AcceptSubscriptionRequest_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [assetPermissions](#API_AcceptSubscriptionRequest_RequestSyntax) **   <a name="datazone-AcceptSubscriptionRequest-request-assetPermissions"></a>
The asset permissions of the accept subscription request.
Type: Array of [AssetPermission](API_AssetPermission.md) objects
Required: No

 ** [assetScopes](#API_AcceptSubscriptionRequest_RequestSyntax) **   <a name="datazone-AcceptSubscriptionRequest-request-assetScopes"></a>
The asset scopes of the accept subscription request.
Type: Array of [AcceptedAssetScope](API_AcceptedAssetScope.md) objects
Required: No

 ** [decisionComment](#API_AcceptSubscriptionRequest_RequestSyntax) **   <a name="datazone-AcceptSubscriptionRequest-request-decisionComment"></a>
A description that specifies the reason for accepting the specified subscription request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Required: No

## Response Syntax
<a name="API_AcceptSubscriptionRequest_ResponseSyntax"></a>

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
<a name="API_AcceptSubscriptionRequest_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [createdAt](#API_AcceptSubscriptionRequest_ResponseSyntax) **   <a name="datazone-AcceptSubscriptionRequest-response-createdAt"></a>
The timestamp that specifies when the subscription request was accepted.
Type: Timestamp

 ** [createdBy](#API_AcceptSubscriptionRequest_ResponseSyntax) **   <a name="datazone-AcceptSubscriptionRequest-response-createdBy"></a>
Specifies the Amazon DataZone user that accepted the specified subscription request.
Type: String

 ** [decisionComment](#API_AcceptSubscriptionRequest_ResponseSyntax) **   <a name="datazone-AcceptSubscriptionRequest-response-decisionComment"></a>
Specifies the reason for accepting the subscription request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.

 ** [domainId](#API_AcceptSubscriptionRequest_ResponseSyntax) **   <a name="datazone-AcceptSubscriptionRequest-response-domainId"></a>
The unique identifier of the Amazon DataZone domain where the specified subscription request was accepted.
Type: String
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`

 ** [existingSubscriptionId](#API_AcceptSubscriptionRequest_ResponseSyntax) **   <a name="datazone-AcceptSubscriptionRequest-response-existingSubscriptionId"></a>
The ID of the existing subscription.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [id](#API_AcceptSubscriptionRequest_ResponseSyntax) **   <a name="datazone-AcceptSubscriptionRequest-response-id"></a>
The identifier of the subscription request.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [metadataForms](#API_AcceptSubscriptionRequest_ResponseSyntax) **   <a name="datazone-AcceptSubscriptionRequest-response-metadataForms"></a>
The metadata form in the subscription request.
Type: Array of [FormOutput](API_FormOutput.md) objects

 ** [requestReason](#API_AcceptSubscriptionRequest_ResponseSyntax) **   <a name="datazone-AcceptSubscriptionRequest-response-requestReason"></a>
Specifies the reason for requesting a subscription to the asset.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.

 ** [reviewerId](#API_AcceptSubscriptionRequest_ResponseSyntax) **   <a name="datazone-AcceptSubscriptionRequest-response-reviewerId"></a>
Specifes the ID of the Amazon DataZone user who reviewed the subscription request.
Type: String

 ** [status](#API_AcceptSubscriptionRequest_ResponseSyntax) **   <a name="datazone-AcceptSubscriptionRequest-response-status"></a>
Specifies the status of the subscription request.
Type: String
Valid Values: `PENDING | ACCEPTED | REJECTED`

 ** [subscribedListings](#API_AcceptSubscriptionRequest_ResponseSyntax) **   <a name="datazone-AcceptSubscriptionRequest-response-subscribedListings"></a>
Specifies the asset for which the subscription request was created.
Type: Array of [SubscribedListing](API_SubscribedListing.md) objects
Array Members: Fixed number of 1 item.

 ** [subscribedPrincipals](#API_AcceptSubscriptionRequest_ResponseSyntax) **   <a name="datazone-AcceptSubscriptionRequest-response-subscribedPrincipals"></a>
Specifies the Amazon DataZone users who are subscribed to the asset specified in the subscription request.
Type: Array of [SubscribedPrincipal](API_SubscribedPrincipal.md) objects
Array Members: Fixed number of 1 item.

 ** [updatedAt](#API_AcceptSubscriptionRequest_ResponseSyntax) **   <a name="datazone-AcceptSubscriptionRequest-response-updatedAt"></a>
Specifies the timestamp when subscription request was updated.
Type: Timestamp

 ** [updatedBy](#API_AcceptSubscriptionRequest_ResponseSyntax) **   <a name="datazone-AcceptSubscriptionRequest-response-updatedBy"></a>
Specifies the Amazon DataZone user who updated the subscription request.
Type: String

## Errors
<a name="API_AcceptSubscriptionRequest_Errors"></a>

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
<a name="API_AcceptSubscriptionRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datazone-2018-05-10/AcceptSubscriptionRequest)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datazone-2018-05-10/AcceptSubscriptionRequest)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/AcceptSubscriptionRequest)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datazone-2018-05-10/AcceptSubscriptionRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/AcceptSubscriptionRequest)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datazone-2018-05-10/AcceptSubscriptionRequest)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datazone-2018-05-10/AcceptSubscriptionRequest)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datazone-2018-05-10/AcceptSubscriptionRequest)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/datazone-2018-05-10/AcceptSubscriptionRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/AcceptSubscriptionRequest)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DataZone. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datazone` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
