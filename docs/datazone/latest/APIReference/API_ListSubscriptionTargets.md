---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_ListSubscriptionTargets.html
---

# ListSubscriptionTargets
<a name="API_ListSubscriptionTargets"></a>

Lists subscription targets in Amazon DataZone.

## Request Syntax
<a name="API_ListSubscriptionTargets_RequestSyntax"></a>

```
GET /v2/domains/{{domainIdentifier}}/environments/{{environmentIdentifier}}/subscription-targets?maxResults={{maxResults}}&nextToken={{nextToken}}&sortBy={{sortBy}}&sortOrder={{sortOrder}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListSubscriptionTargets_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domainIdentifier](#API_ListSubscriptionTargets_RequestSyntax) **   <a name="datazone-ListSubscriptionTargets-request-uri-domainIdentifier"></a>
The identifier of the Amazon DataZone domain where you want to list subscription targets.
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** [environmentIdentifier](#API_ListSubscriptionTargets_RequestSyntax) **   <a name="datazone-ListSubscriptionTargets-request-uri-environmentIdentifier"></a>
The identifier of the environment where you want to list subscription targets.
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** [maxResults](#API_ListSubscriptionTargets_RequestSyntax) **   <a name="datazone-ListSubscriptionTargets-request-uri-maxResults"></a>
The maximum number of subscription targets to return in a single call to `ListSubscriptionTargets`. When the number of subscription targets to be listed is greater than the value of `MaxResults`, the response contains a `NextToken` value that you can use in a subsequent call to `ListSubscriptionTargets` to list the next set of subscription targets.
Valid Range: Minimum value of 1. Maximum value of 50.

 ** [nextToken](#API_ListSubscriptionTargets_RequestSyntax) **   <a name="datazone-ListSubscriptionTargets-request-uri-nextToken"></a>
When the number of subscription targets is greater than the default value for the `MaxResults` parameter, or if you explicitly specify a value for `MaxResults` that is less than the number of subscription targets, the response includes a pagination token named `NextToken`. You can specify this `NextToken` value in a subsequent call to `ListSubscriptionTargets` to list the next set of subscription targets.
Length Constraints: Minimum length of 1. Maximum length of 8192.

 ** [sortBy](#API_ListSubscriptionTargets_RequestSyntax) **   <a name="datazone-ListSubscriptionTargets-request-uri-sortBy"></a>
Specifies the way in which the results of this action are to be sorted.
Valid Values: `CREATED_AT | UPDATED_AT`

 ** [sortOrder](#API_ListSubscriptionTargets_RequestSyntax) **   <a name="datazone-ListSubscriptionTargets-request-uri-sortOrder"></a>
Specifies the sort order for the results of this action.
Valid Values: `ASCENDING | DESCENDING`

## Request Body
<a name="API_ListSubscriptionTargets_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListSubscriptionTargets_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "items": [
      {
         "applicableAssetTypes": [ "string" ],
         "authorizedPrincipals": [ "string" ],
         "createdAt": number,
         "createdBy": "string",
         "domainId": "string",
         "environmentId": "string",
         "id": "string",
         "manageAccessRole": "string",
         "name": "string",
         "projectId": "string",
         "provider": "string",
         "subscriptionGrantCreationMode": "string",
         "subscriptionTargetConfig": [
            {
               "content": "string",
               "formName": "string"
            }
         ],
         "type": "string",
         "updatedAt": number,
         "updatedBy": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListSubscriptionTargets_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [items](#API_ListSubscriptionTargets_ResponseSyntax) **   <a name="datazone-ListSubscriptionTargets-response-items"></a>
The results of the `ListSubscriptionTargets` action.
Type: Array of [SubscriptionTargetSummary](API_SubscriptionTargetSummary.md) objects

 ** [nextToken](#API_ListSubscriptionTargets_ResponseSyntax) **   <a name="datazone-ListSubscriptionTargets-response-nextToken"></a>
When the number of subscription targets is greater than the default value for the `MaxResults` parameter, or if you explicitly specify a value for `MaxResults` that is less than the number of subscription targets, the response includes a pagination token named `NextToken`. You can specify this `NextToken` value in a subsequent call to `ListSubscriptionTargets` to list the next set of subscription targets.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 8192.

## Errors
<a name="API_ListSubscriptionTargets_Errors"></a>

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
<a name="API_ListSubscriptionTargets_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datazone-2018-05-10/ListSubscriptionTargets)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datazone-2018-05-10/ListSubscriptionTargets)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/ListSubscriptionTargets)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datazone-2018-05-10/ListSubscriptionTargets)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/ListSubscriptionTargets)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datazone-2018-05-10/ListSubscriptionTargets)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datazone-2018-05-10/ListSubscriptionTargets)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datazone-2018-05-10/ListSubscriptionTargets)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/datazone-2018-05-10/ListSubscriptionTargets)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/ListSubscriptionTargets)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DataZone. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datazone` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
