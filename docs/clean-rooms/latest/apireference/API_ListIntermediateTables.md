---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_ListIntermediateTables.html
---

# ListIntermediateTables
<a name="API_ListIntermediateTables"></a>

Lists intermediate tables owned by the caller in a membership. We recommend using pagination to ensure that the operation returns quickly and successfully.

## Request Syntax
<a name="API_ListIntermediateTables_RequestSyntax"></a>

```
GET /memberships/{{membershipIdentifier}}/intermediateTables?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListIntermediateTables_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_ListIntermediateTables_RequestSyntax) **   <a name="API-ListIntermediateTables-request-uri-maxResults"></a>
The maximum number of results that are returned for an API request call. The service chooses a default number if you don't set one. The service might return a `nextToken` even if the `maxResults` value has not been met.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [membershipIdentifier](#API_ListIntermediateTables_RequestSyntax) **   <a name="API-ListIntermediateTables-request-uri-membershipIdentifier"></a>
The unique identifier of the membership for which to list intermediate tables.
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** [nextToken](#API_ListIntermediateTables_RequestSyntax) **   <a name="API-ListIntermediateTables-request-uri-nextToken"></a>
The pagination token that's used to fetch the next set of results.
Length Constraints: Minimum length of 0. Maximum length of 10240.

## Request Body
<a name="API_ListIntermediateTables_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListIntermediateTables_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "intermediateTableSummaries": [
      {
         "analysisRuleTypes": [ "string" ],
         "arn": "string",
         "collaborationArn": "string",
         "collaborationId": "string",
         "createTime": number,
         "description": "string",
         "id": "string",
         "membershipArn": "string",
         "membershipId": "string",
         "name": "string",
         "retentionInDays": number,
         "status": "string",
         "updateTime": number
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListIntermediateTables_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [intermediateTableSummaries](#API_ListIntermediateTables_ResponseSyntax) **   <a name="API-ListIntermediateTables-response-intermediateTableSummaries"></a>
The list of intermediate table summaries.
Type: Array of [IntermediateTableSummary](API_IntermediateTableSummary.md) objects

 ** [nextToken](#API_ListIntermediateTables_ResponseSyntax) **   <a name="API-ListIntermediateTables-response-nextToken"></a>
The pagination token that's used to fetch the next set of results.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 10240.

## Errors
<a name="API_ListIntermediateTables_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Caller does not have sufficient access to perform this action.
 ** reason **
A reason code for the exception.
HTTP Status Code: 403

 ** InternalServerException **
Unexpected error during processing of request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
Request references a resource which does not exist.
 ** resourceId **
The Id of the missing resource.
 ** resourceType **
The type of the missing resource.
HTTP Status Code: 404

 ** ThrottlingException **
Request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the specified constraints.
 ** fieldList **
Validation errors for specific input parameters.
 ** reason **
A reason code for the exception.
HTTP Status Code: 400

## See Also
<a name="API_ListIntermediateTables_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cleanrooms-2022-02-17/ListIntermediateTables)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cleanrooms-2022-02-17/ListIntermediateTables)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/ListIntermediateTables)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cleanrooms-2022-02-17/ListIntermediateTables)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/ListIntermediateTables)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cleanrooms-2022-02-17/ListIntermediateTables)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cleanrooms-2022-02-17/ListIntermediateTables)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cleanrooms-2022-02-17/ListIntermediateTables)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cleanrooms-2022-02-17/ListIntermediateTables)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/ListIntermediateTables)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clean-rooms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
