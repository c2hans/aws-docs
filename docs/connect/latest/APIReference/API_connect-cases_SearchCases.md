---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-cases_SearchCases.html
---

# SearchCases
<a name="API_connect-cases_SearchCases"></a>

Searches for cases within their associated Cases domain. Search results are returned as a paginated list of abridged case documents.

**Note**
For `customer_id` you must provide the full customer profile ARN in this format: ` arn:aws:profile:your AWS Region:your AWS account ID:domains/profiles domain name/profiles/profile ID`.

## Request Syntax
<a name="API_connect-cases_SearchCases_RequestSyntax"></a>

```
POST /domains/{{domainId}}/cases-search HTTP/1.1
Content-type: application/json

{
   "fields": [
      {
         "id": "{{string}}"
      }
   ],
   "filter": { ... },
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "searchTerm": "{{string}}",
   "sorts": [
      {
         "fieldId": "{{string}}",
         "sortOrder": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_connect-cases_SearchCases_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domainId](#API_connect-cases_SearchCases_RequestSyntax) **   <a name="connect-connect-cases_SearchCases-request-uri-domainId"></a>
The unique identifier of the Cases domain.
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: Yes

## Request Body
<a name="API_connect-cases_SearchCases_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [fields](#API_connect-cases_SearchCases_RequestSyntax) **   <a name="connect-connect-cases_SearchCases-request-fields"></a>
The list of field identifiers to be returned as part of the response.
Type: Array of [FieldIdentifier](API_connect-cases_FieldIdentifier.md) objects
Array Members: Minimum number of 0 items. Maximum number of 25 items.
Required: No

 ** [filter](#API_connect-cases_SearchCases_RequestSyntax) **   <a name="connect-connect-cases_SearchCases-request-filter"></a>
A list of filter objects.
Type: [CaseFilter](API_connect-cases_CaseFilter.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** [maxResults](#API_connect-cases_SearchCases_RequestSyntax) **   <a name="connect-connect-cases_SearchCases-request-maxResults"></a>
The maximum number of cases to return. When no value is provided, 25 is the default.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [nextToken](#API_connect-cases_SearchCases_RequestSyntax) **   <a name="connect-connect-cases_SearchCases-request-nextToken"></a>
The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 9000.
Required: No

 ** [searchTerm](#API_connect-cases_SearchCases_RequestSyntax) **   <a name="connect-connect-cases_SearchCases-request-searchTerm"></a>
A word or phrase used to perform a quick search.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Required: No

 ** [sorts](#API_connect-cases_SearchCases_RequestSyntax) **   <a name="connect-connect-cases_SearchCases-request-sorts"></a>
A list of sorts where each sort specifies a field and their sort order to be applied to the results.
Type: Array of [Sort](API_connect-cases_Sort.md) objects
Array Members: Minimum number of 0 items. Maximum number of 2 items.
Required: No

## Response Syntax
<a name="API_connect-cases_SearchCases_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "cases": [
      {
         "caseId": "string",
         "fields": [
            {
               "id": "string",
               "value": { ... }
            }
         ],
         "tags": {
            "string" : "string"
         },
         "templateId": "string"
      }
   ],
   "nextToken": "string",
   "totalCount": number
}
```

## Response Elements
<a name="API_connect-cases_SearchCases_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [cases](#API_connect-cases_SearchCases_ResponseSyntax) **   <a name="connect-connect-cases_SearchCases-response-cases"></a>
A list of case documents where each case contains the properties `CaseId` and `Fields` where each field is a complex union structure.
Type: Array of [SearchCasesResponseItem](API_connect-cases_SearchCasesResponseItem.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.

 ** [nextToken](#API_connect-cases_SearchCases_ResponseSyntax) **   <a name="connect-connect-cases_SearchCases-response-nextToken"></a>
The token for the next set of results. This is null if there are no more results to return.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 9000.

 ** [totalCount](#API_connect-cases_SearchCases_ResponseSyntax) **   <a name="connect-connect-cases_SearchCases-response-totalCount"></a>
The total number of cases that matched the search criteria.
Type: Long
Valid Range: Minimum value of 0.

## Errors
<a name="API_connect-cases_SearchCases_Errors"></a>

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
<a name="API_connect-cases_SearchCases_Examples"></a>

### Request example
<a name="API_connect-cases_SearchCases_Example_1"></a>

This example illustrates one usage of SearchCases.

```
{
   "filter":{
      "andAll":[
         {
            "field":{
               "equalTo":{
                  "id":"title",
                  "value":{
                     "stringValue":"Forward Web Engineer"
                  }
               }
            }
         },
         {
            "not":{
               "field":{
                  "greaterThan":{
                     "id":"customer_age",
                     "value":{
                        "doubleValue":38
                     }
                  }
               }
            }
         }
      ]
   },
   "fields":[
      {
         "id":"title"
      }
   ],
   "maxResults":10,
   "nextToken":null,
   "sorts":[
      {
         "fieldId":"created_datetime",
         "sortOrder":"Asc"
      }
   ]
}
```

### Response example
<a name="API_connect-cases_SearchCases_Example_2"></a>

This example illustrates one usage of SearchCases.

```
{
   "cases":[
      {
         "caseId":"[case_id_1]",
         "fields":[
            {
               "id":"title",
               "value":{
                  "stringValue":"Forward Web Engineer-1"
               }
            }
         ],
         "tags":{

         },
         "templateId":"[template_id]"
      },
      {
         "caseId":"[case_id_2]",
         "fields":[
            {
               "id":"title",
               "value":{
                  "stringValue":"Forward Web Engineer-2"
               }
            }
         ],
         "tags":{

         },
         "templateId":"[template_id]"
      },
      {
         "caseId":"[case_id_3]",
         "fields":[
            {
               "id":"title",
               "value":{
                  "stringValue":"Forward Web Engineer-3"
               }
            }
         ],
         "tags":{

         },
         "templateId":"[template_id]"
      }
   ],
   "nextToken":"[nextToken]"
}
```

## See Also
<a name="API_connect-cases_SearchCases_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connectcases-2022-10-03/SearchCases)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connectcases-2022-10-03/SearchCases)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connectcases-2022-10-03/SearchCases)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connectcases-2022-10-03/SearchCases)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connectcases-2022-10-03/SearchCases)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connectcases-2022-10-03/SearchCases)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connectcases-2022-10-03/SearchCases)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connectcases-2022-10-03/SearchCases)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connectcases-2022-10-03/SearchCases)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connectcases-2022-10-03/SearchCases)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
