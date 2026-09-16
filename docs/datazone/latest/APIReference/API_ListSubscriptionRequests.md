---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_ListSubscriptionRequests.html
---

# ListSubscriptionRequests
<a name="API_ListSubscriptionRequests"></a>

Lists Amazon DataZone subscription requests.

## Request Syntax
<a name="API_ListSubscriptionRequests_RequestSyntax"></a>

```
GET /v2/domains/{{domainIdentifier}}/subscription-requests?approverProjectId={{approverProjectId}}&maxResults={{maxResults}}&nextToken={{nextToken}}&owningGroupId={{owningGroupId}}&owningIamPrincipalArn={{owningIamPrincipalArn}}&owningProjectId={{owningProjectId}}&owningUserId={{owningUserId}}&sortBy={{sortBy}}&sortOrder={{sortOrder}}&status={{status}}&subscribedListingId={{subscribedListingId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListSubscriptionRequests_RequestParameters"></a>

The request uses the following URI parameters.

 ** [approverProjectId](#API_ListSubscriptionRequests_RequestSyntax) **   <a name="datazone-ListSubscriptionRequests-request-uri-approverProjectId"></a>
The identifier of the subscription request approver's project.
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [domainIdentifier](#API_ListSubscriptionRequests_RequestSyntax) **   <a name="datazone-ListSubscriptionRequests-request-uri-domainIdentifier"></a>
The identifier of the Amazon DataZone domain.
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** [maxResults](#API_ListSubscriptionRequests_RequestSyntax) **   <a name="datazone-ListSubscriptionRequests-request-uri-maxResults"></a>
The maximum number of subscription requests to return in a single call to `ListSubscriptionRequests`. When the number of subscription requests to be listed is greater than the value of `MaxResults`, the response contains a `NextToken` value that you can use in a subsequent call to `ListSubscriptionRequests` to list the next set of subscription requests.
Valid Range: Minimum value of 1. Maximum value of 50.

 ** [nextToken](#API_ListSubscriptionRequests_RequestSyntax) **   <a name="datazone-ListSubscriptionRequests-request-uri-nextToken"></a>
When the number of subscription requests is greater than the default value for the `MaxResults` parameter, or if you explicitly specify a value for `MaxResults` that is less than the number of subscription requests, the response includes a pagination token named `NextToken`. You can specify this `NextToken` value in a subsequent call to `ListSubscriptionRequests` to list the next set of subscription requests.
Length Constraints: Minimum length of 1. Maximum length of 8192.

 ** [owningGroupId](#API_ListSubscriptionRequests_RequestSyntax) **   <a name="datazone-ListSubscriptionRequests-request-uri-owningGroupId"></a>
The ID of the owning group.
Pattern: `([0-9a-f]{10}-|)[A-Fa-f0-9]{8}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{12}`

 ** [owningIamPrincipalArn](#API_ListSubscriptionRequests_RequestSyntax) **   <a name="datazone-ListSubscriptionRequests-request-uri-owningIamPrincipalArn"></a>
The ARN of the owning IAM principal.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `arn:aws[^:]*:iam::\d{12}:(role|user)(/[\w+=,.@-]*)*/[\w+=,.@-]+`

 ** [owningProjectId](#API_ListSubscriptionRequests_RequestSyntax) **   <a name="datazone-ListSubscriptionRequests-request-uri-owningProjectId"></a>
The identifier of the project for the subscription requests.
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [owningUserId](#API_ListSubscriptionRequests_RequestSyntax) **   <a name="datazone-ListSubscriptionRequests-request-uri-owningUserId"></a>
The ID of the owning user.
Pattern: `([0-9a-f]{10}-|)[A-Fa-f0-9]{8}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{12}`

 ** [sortBy](#API_ListSubscriptionRequests_RequestSyntax) **   <a name="datazone-ListSubscriptionRequests-request-uri-sortBy"></a>
 *This parameter has been deprecated.*
Specifies the way to sort the results of this action.
Valid Values: `CREATED_AT | UPDATED_AT`

 ** [sortOrder](#API_ListSubscriptionRequests_RequestSyntax) **   <a name="datazone-ListSubscriptionRequests-request-uri-sortOrder"></a>
Specifies the sort order for the results of this action.
Valid Values: `ASCENDING | DESCENDING`

 ** [status](#API_ListSubscriptionRequests_RequestSyntax) **   <a name="datazone-ListSubscriptionRequests-request-uri-status"></a>
Specifies the status of the subscription requests.
This is not a required parameter, but if not specified, by default, Amazon DataZone returns only `PENDING` subscription requests.
Valid Values: `PENDING | ACCEPTED | REJECTED`

 ** [subscribedListingId](#API_ListSubscriptionRequests_RequestSyntax) **   <a name="datazone-ListSubscriptionRequests-request-uri-subscribedListingId"></a>
The identifier of the subscribed listing.
Pattern: `[a-zA-Z0-9_-]{1,36}`

## Request Body
<a name="API_ListSubscriptionRequests_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListSubscriptionRequests_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "items": [
      {
         "createdAt": number,
         "createdBy": "string",
         "decisionComment": "string",
         "domainId": "string",
         "existingSubscriptionId": "string",
         "id": "string",
         "metadataFormsSummary": [
            {
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
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListSubscriptionRequests_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [items](#API_ListSubscriptionRequests_ResponseSyntax) **   <a name="datazone-ListSubscriptionRequests-response-items"></a>
The results of the `ListSubscriptionRequests` action.
Type: Array of [SubscriptionRequestSummary](API_SubscriptionRequestSummary.md) objects

 ** [nextToken](#API_ListSubscriptionRequests_ResponseSyntax) **   <a name="datazone-ListSubscriptionRequests-response-nextToken"></a>
When the number of subscription requests is greater than the default value for the `MaxResults` parameter, or if you explicitly specify a value for `MaxResults` that is less than the number of subscription requests, the response includes a pagination token named `NextToken`. You can specify this `NextToken` value in a subsequent call to `ListSubscriptionRequests` to list the next set of subscription requests.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 8192.

## Errors
<a name="API_ListSubscriptionRequests_Errors"></a>

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
<a name="API_ListSubscriptionRequests_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datazone-2018-05-10/ListSubscriptionRequests)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datazone-2018-05-10/ListSubscriptionRequests)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/ListSubscriptionRequests)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datazone-2018-05-10/ListSubscriptionRequests)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/ListSubscriptionRequests)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datazone-2018-05-10/ListSubscriptionRequests)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datazone-2018-05-10/ListSubscriptionRequests)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datazone-2018-05-10/ListSubscriptionRequests)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/datazone-2018-05-10/ListSubscriptionRequests)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/ListSubscriptionRequests)
