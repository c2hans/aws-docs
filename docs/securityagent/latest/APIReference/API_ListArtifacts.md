---
source_url: https://docs.aws.amazon.com/securityagent/latest/APIReference/API_ListArtifacts.html
---

# ListArtifacts
<a name="API_ListArtifacts"></a>

Returns a paginated list of artifact summaries for the specified agent space.

## Request Syntax
<a name="API_ListArtifacts_RequestSyntax"></a>

```
POST /ListArtifacts HTTP/1.1
Content-type: application/json

{
   "agentSpaceId": "{{string}}",
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListArtifacts_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListArtifacts_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [agentSpaceId](#API_ListArtifacts_RequestSyntax) **   <a name="securityagent-ListArtifacts-request-agentSpaceId"></a>
The unique identifier of the agent space to list artifacts for.
Type: String
Required: Yes

 ** [maxResults](#API_ListArtifacts_RequestSyntax) **   <a name="securityagent-ListArtifacts-request-maxResults"></a>
The maximum number of results to return in a single call.
Type: Integer
Required: No

 ** [nextToken](#API_ListArtifacts_RequestSyntax) **   <a name="securityagent-ListArtifacts-request-nextToken"></a>
A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request. For subsequent calls, use the nextToken value returned from the previous request.
Type: String
Required: No

## Response Syntax
<a name="API_ListArtifacts_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "artifactSummaries": [
      {
         "artifactId": "string",
         "artifactType": "string",
         "fileName": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListArtifacts_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [artifactSummaries](#API_ListArtifacts_ResponseSyntax) **   <a name="securityagent-ListArtifacts-response-artifactSummaries"></a>
The list of artifact summaries.
Type: Array of [ArtifactSummary](API_ArtifactSummary.md) objects

 ** [nextToken](#API_ListArtifacts_ResponseSyntax) **   <a name="securityagent-ListArtifacts-response-nextToken"></a>
A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request. For subsequent calls, use the nextToken value returned from the previous request.
Type: String

## Errors
<a name="API_ListArtifacts_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
 ** message **
Error description.
HTTP Status Code: 403

 ** InternalServerException **
An unexpected error occurred during the processing of your request.
 ** message **
Error description.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource was not found. Verify that the resource identifier is correct and that the resource exists in the specified agent space or account.
 ** message **
Error description.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
 ** message **
Error description.
 ** quotaCode **
Quota code for throttling limit.
 ** serviceCode **
Service code for throttling limit.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by the service.
 ** fieldList **
A list of specific failures encountered during validation.
 ** message **
A summary of the validation failure.
HTTP Status Code: 400

## See Also
<a name="API_ListArtifacts_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/securityagent-2025-09-06/ListArtifacts)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/securityagent-2025-09-06/ListArtifacts)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityagent-2025-09-06/ListArtifacts)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/securityagent-2025-09-06/ListArtifacts)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityagent-2025-09-06/ListArtifacts)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/securityagent-2025-09-06/ListArtifacts)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/securityagent-2025-09-06/ListArtifacts)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/securityagent-2025-09-06/ListArtifacts)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/securityagent-2025-09-06/ListArtifacts)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityagent-2025-09-06/ListArtifacts)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Agent. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityagent` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
