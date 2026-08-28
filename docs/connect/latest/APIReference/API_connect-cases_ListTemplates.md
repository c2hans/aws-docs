---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-cases_ListTemplates.html
---

# ListTemplates
<a name="API_connect-cases_ListTemplates"></a>

Lists all of the templates in a Cases domain. Each list item is a condensed summary object of the template.

 Other template APIs are:
+  [CreateTemplate](https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-cases_CreateTemplate.html)
+  [DeleteTemplate](https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-cases_DeleteTemplate.html)
+  [GetTemplate](https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-cases_GetTemplate.html)
+  [UpdateTemplate](https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-cases_UpdateTemplate.html)

## Request Syntax
<a name="API_connect-cases_ListTemplates_RequestSyntax"></a>

```
POST /domains/{{domainId}}/templates-list?maxResults={{maxResults}}&nextToken={{nextToken}}&status={{status}} HTTP/1.1
```

## URI Request Parameters
<a name="API_connect-cases_ListTemplates_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domainId](#API_connect-cases_ListTemplates_RequestSyntax) **   <a name="connect-connect-cases_ListTemplates-request-uri-domainId"></a>
The unique identifier of the Cases domain.
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: Yes

 ** [maxResults](#API_connect-cases_ListTemplates_RequestSyntax) **   <a name="connect-connect-cases_ListTemplates-request-uri-maxResults"></a>
The maximum number of results to return per page.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextToken](#API_connect-cases_ListTemplates_RequestSyntax) **   <a name="connect-connect-cases_ListTemplates-request-uri-nextToken"></a>
The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
Length Constraints: Minimum length of 0. Maximum length of 9000.

 ** [status](#API_connect-cases_ListTemplates_RequestSyntax) **   <a name="connect-connect-cases_ListTemplates-request-uri-status"></a>
A list of status values to filter on.
Array Members: Minimum number of 1 item. Maximum number of 2 items.
Valid Values: `Active | Inactive`

## Request Body
<a name="API_connect-cases_ListTemplates_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_connect-cases_ListTemplates_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "templates": [
      {
         "name": "string",
         "status": "string",
         "tagPropagationConfigurations": [
            {
               "resourceType": "string",
               "tagMap": {
                  "string" : "string"
               }
            }
         ],
         "templateArn": "string",
         "templateId": "string"
      }
   ]
}
```

## Response Elements
<a name="API_connect-cases_ListTemplates_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_connect-cases_ListTemplates_ResponseSyntax) **   <a name="connect-connect-cases_ListTemplates-response-nextToken"></a>
The token for the next set of results. This is null if there are no more results to return.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 9000.

 ** [templates](#API_connect-cases_ListTemplates_ResponseSyntax) **   <a name="connect-connect-cases_ListTemplates-response-templates"></a>
List of template summary objects.
Type: Array of [TemplateSummary](API_connect-cases_TemplateSummary.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.

## Errors
<a name="API_connect-cases_ListTemplates_Errors"></a>

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
<a name="API_connect-cases_ListTemplates_Examples"></a>

### Request and Response example
<a name="API_connect-cases_ListTemplates_Example_1"></a>

This example illustrates one usage of ListTemplates.

```
{ }
```

```
{
  "templates":[
  {
    "name":"Test",
    "templateArn":"arn:aws:cases:us-west-2:[account_id]:domain/[domain_id]/template/[template_id]",
    "templateId":"[template_id]",
    "status": "Active",
    "tagPropagationConfigurations": [
      {
        "resourceType": "Cases",
        "tagMap": {
          "Department" : "Support"
        }
      }
    ]
  }
  ],
  "nextToken":"[nextToken]"
}
```

## See Also
<a name="API_connect-cases_ListTemplates_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connectcases-2022-10-03/ListTemplates)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connectcases-2022-10-03/ListTemplates)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connectcases-2022-10-03/ListTemplates)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connectcases-2022-10-03/ListTemplates)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connectcases-2022-10-03/ListTemplates)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connectcases-2022-10-03/ListTemplates)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connectcases-2022-10-03/ListTemplates)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connectcases-2022-10-03/ListTemplates)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connectcases-2022-10-03/ListTemplates)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connectcases-2022-10-03/ListTemplates)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
