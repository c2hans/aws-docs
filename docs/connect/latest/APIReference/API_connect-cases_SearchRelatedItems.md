---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-cases_SearchRelatedItems.html
---

# SearchRelatedItems
<a name="API_connect-cases_SearchRelatedItems"></a>

Searches for related items that are associated with a case.

**Note**
If no filters are provided, this returns all related items associated with a case.

## Request Syntax
<a name="API_connect-cases_SearchRelatedItems_RequestSyntax"></a>

```
POST /domains/{{domainId}}/cases/{{caseId}}/related-items-search HTTP/1.1
Content-type: application/json

{
   "filters": [
      { ... }
   ],
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_connect-cases_SearchRelatedItems_RequestParameters"></a>

The request uses the following URI parameters.

 ** [caseId](#API_connect-cases_SearchRelatedItems_RequestSyntax) **   <a name="connect-connect-cases_SearchRelatedItems-request-uri-caseId"></a>
A unique identifier of the case.
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: Yes

 ** [domainId](#API_connect-cases_SearchRelatedItems_RequestSyntax) **   <a name="connect-connect-cases_SearchRelatedItems-request-uri-domainId"></a>
The unique identifier of the Cases domain.
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: Yes

## Request Body
<a name="API_connect-cases_SearchRelatedItems_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [filters](#API_connect-cases_SearchRelatedItems_RequestSyntax) **   <a name="connect-connect-cases_SearchRelatedItems-request-filters"></a>
The list of types of related items and their parameters to use for filtering.
Type: Array of [RelatedItemTypeFilter](API_connect-cases_RelatedItemTypeFilter.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Required: No

 ** [maxResults](#API_connect-cases_SearchRelatedItems_RequestSyntax) **   <a name="connect-connect-cases_SearchRelatedItems-request-maxResults"></a>
The maximum number of results to return per page.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 25.
Required: No

 ** [nextToken](#API_connect-cases_SearchRelatedItems_RequestSyntax) **   <a name="connect-connect-cases_SearchRelatedItems-request-nextToken"></a>
The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 9000.
Required: No

## Response Syntax
<a name="API_connect-cases_SearchRelatedItems_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "relatedItems": [
      {
         "associationTime": "string",
         "content": { ... },
         "performedBy": { ... },
         "relatedItemId": "string",
         "tags": {
            "string" : "string"
         },
         "type": "string"
      }
   ]
}
```

## Response Elements
<a name="API_connect-cases_SearchRelatedItems_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_connect-cases_SearchRelatedItems_ResponseSyntax) **   <a name="connect-connect-cases_SearchRelatedItems-response-nextToken"></a>
The token for the next set of results. This is null if there are no more results to return.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 9000.

 ** [relatedItems](#API_connect-cases_SearchRelatedItems_ResponseSyntax) **   <a name="connect-connect-cases_SearchRelatedItems-response-relatedItems"></a>
A list of items related to a case.
Type: Array of [SearchRelatedItemsResponseItem](API_connect-cases_SearchRelatedItemsResponseItem.md) objects
Array Members: Minimum number of 0 items. Maximum number of 25 items.

## Errors
<a name="API_connect-cases_SearchRelatedItems_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
We couldn't process your request because of an issue with the server. Try again later.
 ** retryAfterSeconds **
Advice to clients on when the call can be safely retried.
HTTP Status Code: 500

 ** ResourceNotFoundException **
We couldn't find the requested resource. Check that your resources exists and were created in the same AWS Region as your request, and try your request again.
 ** resourceId **
Unique identifier of the resource affected.
 ** resourceType **
Type of the resource affected.
HTTP Status Code: 404

 ** ThrottlingException **
The rate has been exceeded for this API. Please try again after a few minutes.
HTTP Status Code: 429

 ** ValidationException **
The request isn't valid. Check the syntax and try again.
HTTP Status Code: 400

## Examples
<a name="API_connect-cases_SearchRelatedItems_Examples"></a>

### Request and Response example
<a name="API_connect-cases_SearchRelatedItems_Example_1"></a>

This example illustrates one usage of SearchRelatedItems.

```
{
  "maxResults": 25,
  "filters": [
  {
    "contact": {
      "contactArn": "arn:aws:connect:us-west-2:[account_id]:instance/[connect_instance_id]/contact/[contact_id]"
      }
    }
  ]
}
```

```
{
  "nextToken": null,
  "relatedItems": [
    {
    "associationTime": "2022-06-06T18:59:09.865709Z",
    "content": {
      "contact": {
      "channel": "CHAT",
      "connectedToSystemTime": "2022-06-08T18:57:50.558897Z",
      "contactArn": "arn:aws:connect:us-west-2:[account_id]:instance/[connect_instance_id]/contact/[contact_id]"
      }
    },
  "relatedItemId": "[relatedItem_id]",
  "tags": {},
  "type": "Contact"
   }
  ]
}
```

## See Also
<a name="API_connect-cases_SearchRelatedItems_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connectcases-2022-10-03/SearchRelatedItems)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connectcases-2022-10-03/SearchRelatedItems)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connectcases-2022-10-03/SearchRelatedItems)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connectcases-2022-10-03/SearchRelatedItems)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connectcases-2022-10-03/SearchRelatedItems)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connectcases-2022-10-03/SearchRelatedItems)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connectcases-2022-10-03/SearchRelatedItems)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connectcases-2022-10-03/SearchRelatedItems)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connectcases-2022-10-03/SearchRelatedItems)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connectcases-2022-10-03/SearchRelatedItems)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
