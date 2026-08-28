---
source_url: https://docs.aws.amazon.com/cases/latest/APIReference/API_ListCasesForContact.html
---

# ListCasesForContact
<a name="API_connect-cases_ListCasesForContact"></a>

Lists cases for a given contact.

## Request Syntax
<a name="API_connect-cases_ListCasesForContact_RequestSyntax"></a>

```
POST /domains/{{domainId}}/list-cases-for-contact HTTP/1.1
Content-type: application/json

{
   "contactArn": "{{string}}",
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_connect-cases_ListCasesForContact_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domainId](#API_connect-cases_ListCasesForContact_RequestSyntax) **   <a name="connect-connect-cases_ListCasesForContact-request-uri-domainId"></a>
The unique identifier of the Cases domain.
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: Yes

## Request Body
<a name="API_connect-cases_ListCasesForContact_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [contactArn](#API_connect-cases_ListCasesForContact_RequestSyntax) **   <a name="connect-connect-cases_ListCasesForContact-request-contactArn"></a>
A unique identifier of a contact in Connect Customer.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: Yes

 ** [maxResults](#API_connect-cases_ListCasesForContact_RequestSyntax) **   <a name="connect-connect-cases_ListCasesForContact-request-maxResults"></a>
The maximum number of results to return per page.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 10.
Required: No

 ** [nextToken](#API_connect-cases_ListCasesForContact_RequestSyntax) **   <a name="connect-connect-cases_ListCasesForContact-request-nextToken"></a>
The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 9000.
Required: No

## Response Syntax
<a name="API_connect-cases_ListCasesForContact_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "cases": [
      {
         "caseId": "string",
         "templateId": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_connect-cases_ListCasesForContact_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [cases](#API_connect-cases_ListCasesForContact_ResponseSyntax) **   <a name="connect-connect-cases_ListCasesForContact-response-cases"></a>
A list of Case summary information.
Type: Array of [CaseSummary](API_connect-cases_CaseSummary.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.

 ** [nextToken](#API_connect-cases_ListCasesForContact_ResponseSyntax) **   <a name="connect-connect-cases_ListCasesForContact-response-nextToken"></a>
The token for the next set of results. This is null if there are no more results to return.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 9000.

## Errors
<a name="API_connect-cases_ListCasesForContact_Errors"></a>

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
<a name="API_connect-cases_ListCasesForContact_Examples"></a>

### Request and Response example
<a name="API_connect-cases_ListCasesForContact_Example_1"></a>

This example illustrates one usage of ListCasesForContact.

```
{
  "contactArn": "arn:aws:connect:us-west-2:[account_id]:instance/[connect_instance_id]/contact/[contact_id]",
  "maxResults": 10
}
```

```
{
  "cases": [
    {
      "caseId": "[case_id_1]",
      "templateId": "[template_id_1]"
    },
    {
      "caseId": "[case_id_2]",
      "templateId": "[template_id_2]"
      },
      {
      "caseId": "[case_id_3]",
      "templateId": "[template_id_3]"
      }
    ]
  "nextToken": null
}
```

## See Also
<a name="API_connect-cases_ListCasesForContact_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connectcases-2022-10-03/ListCasesForContact)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connectcases-2022-10-03/ListCasesForContact)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connectcases-2022-10-03/ListCasesForContact)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connectcases-2022-10-03/ListCasesForContact)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connectcases-2022-10-03/ListCasesForContact)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connectcases-2022-10-03/ListCasesForContact)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connectcases-2022-10-03/ListCasesForContact)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connectcases-2022-10-03/ListCasesForContact)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connectcases-2022-10-03/ListCasesForContact)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connectcases-2022-10-03/ListCasesForContact)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
