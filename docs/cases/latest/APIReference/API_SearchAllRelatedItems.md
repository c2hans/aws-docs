---
source_url: https://docs.aws.amazon.com/cases/latest/APIReference/API_SearchAllRelatedItems.html
---

# SearchAllRelatedItems
<a name="API_connect-cases_SearchAllRelatedItems"></a>

Searches for related items across all cases within a domain. This is a global search operation that returns related items from multiple cases, unlike the case-specific [SearchRelatedItems](https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-cases_SearchRelatedItems.html) API.

 **Use cases**

Following are common uses cases for this API:
+ Find cases with similar issues across the domain. For example, search for all cases containing comments about "product defect" to identify patterns and existing solutions.
+ Locate all cases associated with specific contacts or orders. For example, find all cases linked to a contactArn to understand the complete customer journey.
+ Monitor SLA compliance across cases. For example, search for all cases with "Active" SLA status to prioritize remediation efforts.

 **Important things to know**
+ This API returns case identifiers, not complete case objects. To retrieve full case details, you must make additional calls to the [GetCase](https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-cases_GetCase.html) API for each returned case ID.
+ This API searches across related items content, not case fields. Use the [SearchCases](https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-cases_SearchCases.html) API to search within case field values.

 **Endpoints**: See [Connect Customer endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/connect_region.html).

## Request Syntax
<a name="API_connect-cases_SearchAllRelatedItems_RequestSyntax"></a>

```
POST /domains/{{domainId}}/related-items-search HTTP/1.1
Content-type: application/json

{
   "filters": [
      { ... }
   ],
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "sorts": [
      {
         "sortOrder": "{{string}}",
         "sortProperty": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_connect-cases_SearchAllRelatedItems_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domainId](#API_connect-cases_SearchAllRelatedItems_RequestSyntax) **   <a name="connect-connect-cases_SearchAllRelatedItems-request-uri-domainId"></a>
The unique identifier of the Cases domain.
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: Yes

## Request Body
<a name="API_connect-cases_SearchAllRelatedItems_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [filters](#API_connect-cases_SearchAllRelatedItems_RequestSyntax) **   <a name="connect-connect-cases_SearchAllRelatedItems-request-filters"></a>
The list of types of related items and their parameters to use for filtering. The filters work as an OR condition: caller gets back related items that match any of the specified filter types.
Type: Array of [RelatedItemTypeFilter](API_connect-cases_RelatedItemTypeFilter.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Required: No

 ** [maxResults](#API_connect-cases_SearchAllRelatedItems_RequestSyntax) **   <a name="connect-connect-cases_SearchAllRelatedItems-request-maxResults"></a>
The maximum number of results to return per page.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 25.
Required: No

 ** [nextToken](#API_connect-cases_SearchAllRelatedItems_RequestSyntax) **   <a name="connect-connect-cases_SearchAllRelatedItems-request-nextToken"></a>
The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 9000.
Required: No

 ** [sorts](#API_connect-cases_SearchAllRelatedItems_RequestSyntax) **   <a name="connect-connect-cases_SearchAllRelatedItems-request-sorts"></a>
A structured set of sort terms to specify the order in which related items should be returned. Supports sorting by association time or case ID. The sorts work in the order specified: first sort term takes precedence over subsequent terms.
Type: Array of [SearchAllRelatedItemsSort](API_connect-cases_SearchAllRelatedItemsSort.md) objects
Array Members: Minimum number of 0 items. Maximum number of 2 items.
Required: No

## Response Syntax
<a name="API_connect-cases_SearchAllRelatedItems_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "relatedItems": [
      {
         "associationTime": "string",
         "caseId": "string",
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
<a name="API_connect-cases_SearchAllRelatedItems_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_connect-cases_SearchAllRelatedItems_ResponseSyntax) **   <a name="connect-connect-cases_SearchAllRelatedItems-response-nextToken"></a>
The token for the next set of results. This is null if there are no more results to return.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 9000.

 ** [relatedItems](#API_connect-cases_SearchAllRelatedItems_ResponseSyntax) **   <a name="connect-connect-cases_SearchAllRelatedItems-response-relatedItems"></a>
A list of items related to a case.
Type: Array of [SearchAllRelatedItemsResponseItem](API_connect-cases_SearchAllRelatedItemsResponseItem.md) objects
Array Members: Minimum number of 0 items. Maximum number of 25 items.

## Errors
<a name="API_connect-cases_SearchAllRelatedItems_Errors"></a>

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
<a name="API_connect-cases_SearchAllRelatedItems_Examples"></a>

### Example request to search for all contact-type related items
<a name="API_connect-cases_SearchAllRelatedItems_Example_1"></a>

The following example shows how to search for all contact-type related items across cases in a domain, filtering by a specific contactArn and sorting results by association time in descending order, then by case ID in descending order.

```
{
  "sorts": [
    {
      "sortProperty": "AssociationTime",
      "sortOrder": "Desc"
    },
    {
      "sortProperty": "CaseId",
      "sortOrder": "Desc"
    }
  ],
  "maxResults": 10,
  "filters": [
    {
      "contact": {
        "contactArn": "arn:aws:connect:us-west-2:[account-id]:instance/[instance-id]/contact/[contact-id]"
      }
    }
  ]
}
```

### Example response for a successful search
<a name="API_connect-cases_SearchAllRelatedItems_Example_2"></a>

The following example shows a successful search returning two contact-type related items from different cases, each with their associated case identifiers, contact details, and metadata sorted by most recent association time first.

```
{
  "nextToken": null,
  "relatedItems": [
    {
      "associationTime": "2025-05-16T13:18:37.608074706Z",
      "caseId": "[case-id-1]",
      "content": {
        "contact": {
          "contactArn": "arn:aws:connect:us-west-2:[account-id]:instance/[instance-id]/contact/[contact-id]",
          "channel": "VOICE",
          "connectedToSystemTime": "2025-05-16T13:18:30.000000000Z"
        }
      },
      "performedBy": null,
      "relatedItemId": "[related-item-id-1]",
      "tags": {
        "Company": "AWS",
        "Team": "Connect"
      },
      "type": "Contact"
    },
    {
      "associationTime": "2025-05-16T13:18:19.270469991Z",
      "caseId": "[case-id-2]",
      "content": {
        "contact": {
          "contactArn": "arn:aws:connect:us-west-2:[account-id]:instance/[instance-id]/contact/[contact-id]",
          "channel": "CHAT",
          "connectedToSystemTime": "2025-05-16T13:18:15.000000000Z"
        }
      },
      "performedBy": null,
      "relatedItemId": "[related-item-id-2]",
      "tags": {},
      "type": "Contact"
    }
  ]
}
```

## See Also
<a name="API_connect-cases_SearchAllRelatedItems_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connectcases-2022-10-03/SearchAllRelatedItems)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connectcases-2022-10-03/SearchAllRelatedItems)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connectcases-2022-10-03/SearchAllRelatedItems)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connectcases-2022-10-03/SearchAllRelatedItems)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connectcases-2022-10-03/SearchAllRelatedItems)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connectcases-2022-10-03/SearchAllRelatedItems)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connectcases-2022-10-03/SearchAllRelatedItems)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connectcases-2022-10-03/SearchAllRelatedItems)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connectcases-2022-10-03/SearchAllRelatedItems)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connectcases-2022-10-03/SearchAllRelatedItems)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
