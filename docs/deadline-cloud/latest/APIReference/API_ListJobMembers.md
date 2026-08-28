---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_ListJobMembers.html
---

# ListJobMembers
<a name="API_ListJobMembers"></a>

Lists members on a job.

## Request Syntax
<a name="API_ListJobMembers_RequestSyntax"></a>

```
GET /2023-10-12/farms/{{farmId}}/queues/{{queueId}}/jobs/{{jobId}}/members?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListJobMembers_RequestParameters"></a>

The request uses the following URI parameters.

 ** [farmId](#API_ListJobMembers_RequestSyntax) **   <a name="deadlinecloud-ListJobMembers-request-uri-farmId"></a>
The farm ID of the job to list.
Pattern: `farm-[0-9a-f]{32}`
Required: Yes

 ** [jobId](#API_ListJobMembers_RequestSyntax) **   <a name="deadlinecloud-ListJobMembers-request-uri-jobId"></a>
The job ID to include on the list.
Pattern: `job-[0-9a-f]{32}`
Required: Yes

 ** [maxResults](#API_ListJobMembers_RequestSyntax) **   <a name="deadlinecloud-ListJobMembers-request-uri-maxResults"></a>
The maximum number of results to return. Use this parameter with `NextToken` to get results as a set of sequential pages.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextToken](#API_ListJobMembers_RequestSyntax) **   <a name="deadlinecloud-ListJobMembers-request-uri-nextToken"></a>
The token for the next set of results, or `null` to start from the beginning.
Length Constraints: Minimum length of 0. Maximum length of 4096.

 ** [queueId](#API_ListJobMembers_RequestSyntax) **   <a name="deadlinecloud-ListJobMembers-request-uri-queueId"></a>
The queue ID to include on the list.
Pattern: `queue-[0-9a-f]{32}`
Required: Yes

## Request Body
<a name="API_ListJobMembers_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListJobMembers_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "members": [
      {
         "farmId": "string",
         "identityStoreId": "string",
         "jobId": "string",
         "membershipLevel": "string",
         "principalId": "string",
         "principalType": "string",
         "queueId": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListJobMembers_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [members](#API_ListJobMembers_ResponseSyntax) **   <a name="deadlinecloud-ListJobMembers-response-members"></a>
The members on the list.
Type: Array of [JobMember](API_JobMember.md) objects

 ** [nextToken](#API_ListJobMembers_ResponseSyntax) **   <a name="deadlinecloud-ListJobMembers-response-nextToken"></a>
If Deadline Cloud returns `nextToken`, then there are more results available. The value of `nextToken` is a unique pagination token for each page. To retrieve the next page, call the operation again using the returned token. Keep all other arguments unchanged. If no results remain, then `nextToken` is set to `null`. Each pagination token expires after 24 hours. If you provide a token that isn't valid, then you receive an HTTP 400 `ValidationException` error.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 4096.

## Errors
<a name="API_ListJobMembers_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have permission to perform the action.
 ** context **
Information about the resources in use when the exception was thrown.
HTTP Status Code: 403

 ** InternalServerErrorException **
Deadline Cloud can't process your request right now. Try again later.
 ** retryAfterSeconds **
The number of seconds a client should wait before retrying the request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The requested resource can't be found.
 ** context **
Information about the resources in use when the exception was thrown.
 ** resourceId **
The identifier of the resource that couldn't be found.
 ** resourceType **
The type of the resource that couldn't be found.
HTTP Status Code: 404

 ** ThrottlingException **
Your request exceeded a request rate quota.
 ** context **
Information about the resources in use when the exception was thrown.
 ** quotaCode **
Identifies the quota that is being throttled.
 ** retryAfterSeconds **
The number of seconds a client should wait before retrying the request.
 ** serviceCode **
Identifies the service that is being throttled.
HTTP Status Code: 429

 ** ValidationException **
The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.
 ** context **
Information about the resources in use when the exception was thrown.
 ** fieldList **
A list of fields that failed validation.
 ** reason **
The reason that the request failed validation.
HTTP Status Code: 400

## See Also
<a name="API_ListJobMembers_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/deadline-2023-10-12/ListJobMembers)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/deadline-2023-10-12/ListJobMembers)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/ListJobMembers)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/deadline-2023-10-12/ListJobMembers)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/ListJobMembers)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/deadline-2023-10-12/ListJobMembers)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/deadline-2023-10-12/ListJobMembers)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/deadline-2023-10-12/ListJobMembers)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/deadline-2023-10-12/ListJobMembers)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/ListJobMembers)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Deadline Cloud. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query deadline-cloud` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
