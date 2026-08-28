---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-customer-profiles_ListWorkflows.html
---

# ListWorkflows
<a name="API_connect-customer-profiles_ListWorkflows"></a>

Query to list all workflows.

## Request Syntax
<a name="API_connect-customer-profiles_ListWorkflows_RequestSyntax"></a>

```
POST /domains/{{DomainName}}/workflows?max-results={{MaxResults}}&next-token={{NextToken}} HTTP/1.1
Content-type: application/json

{
   "QueryEndDate": {{number}},
   "QueryStartDate": {{number}},
   "Status": "{{string}}",
   "WorkflowType": "{{string}}"
}
```

## URI Request Parameters
<a name="API_connect-customer-profiles_ListWorkflows_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DomainName](#API_connect-customer-profiles_ListWorkflows_RequestSyntax) **   <a name="connect-connect-customer-profiles_ListWorkflows-request-uri-DomainName"></a>
The unique name of the domain.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`
Required: Yes

 ** [MaxResults](#API_connect-customer-profiles_ListWorkflows_RequestSyntax) **   <a name="connect-connect-customer-profiles_ListWorkflows-request-uri-MaxResults"></a>
The maximum number of results to return per page.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [NextToken](#API_connect-customer-profiles_ListWorkflows_RequestSyntax) **   <a name="connect-connect-customer-profiles_ListWorkflows-request-uri-NextToken"></a>
The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
Length Constraints: Minimum length of 1. Maximum length of 1024.

## Request Body
<a name="API_connect-customer-profiles_ListWorkflows_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [QueryEndDate](#API_connect-customer-profiles_ListWorkflows_RequestSyntax) **   <a name="connect-connect-customer-profiles_ListWorkflows-request-QueryEndDate"></a>
Retrieve workflows ended after timestamp.
Type: Timestamp
Required: No

 ** [QueryStartDate](#API_connect-customer-profiles_ListWorkflows_RequestSyntax) **   <a name="connect-connect-customer-profiles_ListWorkflows-request-QueryStartDate"></a>
Retrieve workflows started after timestamp.
Type: Timestamp
Required: No

 ** [Status](#API_connect-customer-profiles_ListWorkflows_RequestSyntax) **   <a name="connect-connect-customer-profiles_ListWorkflows-request-Status"></a>
Status of workflow execution.
Type: String
Valid Values: `NOT_STARTED | IN_PROGRESS | COMPLETE | FAILED | SPLIT | RETRY | CANCELLED`
Required: No

 ** [WorkflowType](#API_connect-customer-profiles_ListWorkflows_RequestSyntax) **   <a name="connect-connect-customer-profiles_ListWorkflows-request-WorkflowType"></a>
The type of workflow. The only supported value is APPFLOW\_INTEGRATION.
Type: String
Valid Values: `APPFLOW_INTEGRATION`
Required: No

## Response Syntax
<a name="API_connect-customer-profiles_ListWorkflows_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Items": [
      {
         "CreatedAt": number,
         "LastUpdatedAt": number,
         "Status": "string",
         "StatusDescription": "string",
         "WorkflowId": "string",
         "WorkflowType": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_connect-customer-profiles_ListWorkflows_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Items](#API_connect-customer-profiles_ListWorkflows_ResponseSyntax) **   <a name="connect-connect-customer-profiles_ListWorkflows-response-Items"></a>
List containing workflow details.
Type: Array of [ListWorkflowsItem](API_connect-customer-profiles_ListWorkflowsItem.md) objects

 ** [NextToken](#API_connect-customer-profiles_ListWorkflows_ResponseSyntax) **   <a name="connect-connect-customer-profiles_ListWorkflows-response-NextToken"></a>
If there are additional results, this is the token for the next set of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.

## Errors
<a name="API_connect-customer-profiles_ListWorkflows_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** BadRequestException **
The input you provided is invalid.
HTTP Status Code: 400

 ** InternalServerException **
An internal service error occurred.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The requested resource does not exist, or access was denied.
HTTP Status Code: 404

 ** ThrottlingException **
You exceeded the maximum number of requests.
HTTP Status Code: 429

## See Also
<a name="API_connect-customer-profiles_ListWorkflows_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/customer-profiles-2020-08-15/ListWorkflows)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/customer-profiles-2020-08-15/ListWorkflows)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/customer-profiles-2020-08-15/ListWorkflows)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/customer-profiles-2020-08-15/ListWorkflows)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/customer-profiles-2020-08-15/ListWorkflows)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/customer-profiles-2020-08-15/ListWorkflows)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/customer-profiles-2020-08-15/ListWorkflows)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/customer-profiles-2020-08-15/ListWorkflows)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/customer-profiles-2020-08-15/ListWorkflows)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/customer-profiles-2020-08-15/ListWorkflows)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
