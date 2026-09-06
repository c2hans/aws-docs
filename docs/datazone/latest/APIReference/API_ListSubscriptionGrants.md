---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_ListSubscriptionGrants.html
---

# ListSubscriptionGrants
<a name="API_ListSubscriptionGrants"></a>

Lists subscription grants.

## Request Syntax
<a name="API_ListSubscriptionGrants_RequestSyntax"></a>

```
GET /v2/domains/{{domainIdentifier}}/subscription-grants?environmentId={{environmentId}}&maxResults={{maxResults}}&nextToken={{nextToken}}&owningGroupId={{owningGroupId}}&owningIamPrincipalArn={{owningIamPrincipalArn}}&owningProjectId={{owningProjectId}}&owningUserId={{owningUserId}}&sortBy={{sortBy}}&sortOrder={{sortOrder}}&subscribedListingId={{subscribedListingId}}&subscriptionId={{subscriptionId}}&subscriptionTargetId={{subscriptionTargetId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListSubscriptionGrants_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domainIdentifier](#API_ListSubscriptionGrants_RequestSyntax) **   <a name="datazone-ListSubscriptionGrants-request-uri-domainIdentifier"></a>
The identifier of the Amazon DataZone domain.
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** [environmentId](#API_ListSubscriptionGrants_RequestSyntax) **   <a name="datazone-ListSubscriptionGrants-request-uri-environmentId"></a>
The identifier of the Amazon DataZone environment.
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [maxResults](#API_ListSubscriptionGrants_RequestSyntax) **   <a name="datazone-ListSubscriptionGrants-request-uri-maxResults"></a>
The maximum number of subscription grants to return in a single call to `ListSubscriptionGrants`. When the number of subscription grants to be listed is greater than the value of `MaxResults`, the response contains a `NextToken` value that you can use in a subsequent call to `ListSubscriptionGrants` to list the next set of subscription grants.
Valid Range: Minimum value of 1. Maximum value of 50.

 ** [nextToken](#API_ListSubscriptionGrants_RequestSyntax) **   <a name="datazone-ListSubscriptionGrants-request-uri-nextToken"></a>
When the number of subscription grants is greater than the default value for the `MaxResults` parameter, or if you explicitly specify a value for `MaxResults` that is less than the number of subscription grants, the response includes a pagination token named `NextToken`. You can specify this `NextToken` value in a subsequent call to `ListSubscriptionGrants` to list the next set of subscription grants.
Length Constraints: Minimum length of 1. Maximum length of 8192.

 ** [owningGroupId](#API_ListSubscriptionGrants_RequestSyntax) **   <a name="datazone-ListSubscriptionGrants-request-uri-owningGroupId"></a>
The ID of the owning group.
Pattern: `([0-9a-f]{10}-|)[A-Fa-f0-9]{8}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{12}`

 ** [owningIamPrincipalArn](#API_ListSubscriptionGrants_RequestSyntax) **   <a name="datazone-ListSubscriptionGrants-request-uri-owningIamPrincipalArn"></a>
The ARN of the owning IAM principal.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `arn:aws[^:]*:iam::\d{12}:(role|user)(/[\w+=,.@-]*)*/[\w+=,.@-]+`

 ** [owningProjectId](#API_ListSubscriptionGrants_RequestSyntax) **   <a name="datazone-ListSubscriptionGrants-request-uri-owningProjectId"></a>
The ID of the owning project of the subscription grants.
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [owningUserId](#API_ListSubscriptionGrants_RequestSyntax) **   <a name="datazone-ListSubscriptionGrants-request-uri-owningUserId"></a>
The ID of the owning user.
Pattern: `([0-9a-f]{10}-|)[A-Fa-f0-9]{8}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{12}`

 ** [sortBy](#API_ListSubscriptionGrants_RequestSyntax) **   <a name="datazone-ListSubscriptionGrants-request-uri-sortBy"></a>
 *This parameter has been deprecated.*
Specifies the way of sorting the results of this action.
Valid Values: `CREATED_AT | UPDATED_AT`

 ** [sortOrder](#API_ListSubscriptionGrants_RequestSyntax) **   <a name="datazone-ListSubscriptionGrants-request-uri-sortOrder"></a>
Specifies the sort order of this action.
Valid Values: `ASCENDING | DESCENDING`

 ** [subscribedListingId](#API_ListSubscriptionGrants_RequestSyntax) **   <a name="datazone-ListSubscriptionGrants-request-uri-subscribedListingId"></a>
The identifier of the subscribed listing.
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [subscriptionId](#API_ListSubscriptionGrants_RequestSyntax) **   <a name="datazone-ListSubscriptionGrants-request-uri-subscriptionId"></a>
The identifier of the subscription.
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [subscriptionTargetId](#API_ListSubscriptionGrants_RequestSyntax) **   <a name="datazone-ListSubscriptionGrants-request-uri-subscriptionTargetId"></a>
The identifier of the subscription target.
Pattern: `[a-zA-Z0-9_-]{1,36}`

## Request Body
<a name="API_ListSubscriptionGrants_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListSubscriptionGrants_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "items": [
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
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListSubscriptionGrants_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [items](#API_ListSubscriptionGrants_ResponseSyntax) **   <a name="datazone-ListSubscriptionGrants-response-items"></a>
The results of the `ListSubscriptionGrants` action.
Type: Array of [SubscriptionGrantSummary](API_SubscriptionGrantSummary.md) objects

 ** [nextToken](#API_ListSubscriptionGrants_ResponseSyntax) **   <a name="datazone-ListSubscriptionGrants-response-nextToken"></a>
When the number of subscription grants is greater than the default value for the `MaxResults` parameter, or if you explicitly specify a value for `MaxResults` that is less than the number of subscription grants, the response includes a pagination token named `NextToken`. You can specify this `NextToken` value in a subsequent call to `ListSubscriptionGrants` to list the next set of subscription grants.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 8192.

## Errors
<a name="API_ListSubscriptionGrants_Errors"></a>

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
<a name="API_ListSubscriptionGrants_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datazone-2018-05-10/ListSubscriptionGrants)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datazone-2018-05-10/ListSubscriptionGrants)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/ListSubscriptionGrants)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datazone-2018-05-10/ListSubscriptionGrants)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/ListSubscriptionGrants)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datazone-2018-05-10/ListSubscriptionGrants)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datazone-2018-05-10/ListSubscriptionGrants)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datazone-2018-05-10/ListSubscriptionGrants)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/datazone-2018-05-10/ListSubscriptionGrants)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/ListSubscriptionGrants)
