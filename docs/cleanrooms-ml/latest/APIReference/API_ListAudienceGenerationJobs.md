---
source_url: https://docs.aws.amazon.com/cleanrooms-ml/latest/APIReference/API_ListAudienceGenerationJobs.html
---

# ListAudienceGenerationJobs
<a name="API_ListAudienceGenerationJobs"></a>

Returns a list of audience generation jobs.

## Request Syntax
<a name="API_ListAudienceGenerationJobs_RequestSyntax"></a>

```
GET /audience-generation-job?collaborationId={{collaborationId}}&configuredAudienceModelArn={{configuredAudienceModelArn}}&maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListAudienceGenerationJobs_RequestParameters"></a>

The request uses the following URI parameters.

 ** [collaborationId](#API_ListAudienceGenerationJobs_RequestSyntax) **   <a name="API-ListAudienceGenerationJobs-request-uri-collaborationId"></a>
The identifier of the collaboration that contains the audience generation jobs that you are interested in.
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`

 ** [configuredAudienceModelArn](#API_ListAudienceGenerationJobs_RequestSyntax) **   <a name="API-ListAudienceGenerationJobs-request-uri-configuredAudienceModelArn"></a>
The Amazon Resource Name (ARN) of the configured audience model that was used for the audience generation jobs that you are interested in.
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[-a-z]*:cleanrooms-ml:[-a-z0-9]+:[0-9]{12}:configured-audience-model/[-a-zA-Z0-9_/.]+`

 ** [maxResults](#API_ListAudienceGenerationJobs_RequestSyntax) **   <a name="API-ListAudienceGenerationJobs-request-uri-maxResults"></a>
The maximum size of the results that is returned per call.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextToken](#API_ListAudienceGenerationJobs_RequestSyntax) **   <a name="API-ListAudienceGenerationJobs-request-uri-nextToken"></a>
The token value retrieved from a previous call to access the next page of results.
Length Constraints: Minimum length of 1. Maximum length of 10240.

## Request Body
<a name="API_ListAudienceGenerationJobs_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListAudienceGenerationJobs_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "audienceGenerationJobs": [
      {
         "audienceGenerationJobArn": "string",
         "collaborationId": "string",
         "configuredAudienceModelArn": "string",
         "createTime": "string",
         "description": "string",
         "name": "string",
         "startedBy": "string",
         "status": "string",
         "updateTime": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListAudienceGenerationJobs_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [audienceGenerationJobs](#API_ListAudienceGenerationJobs_ResponseSyntax) **   <a name="API-ListAudienceGenerationJobs-response-audienceGenerationJobs"></a>
The audience generation jobs that match the request.
Type: Array of [AudienceGenerationJobSummary](API_AudienceGenerationJobSummary.md) objects

 ** [nextToken](#API_ListAudienceGenerationJobs_ResponseSyntax) **   <a name="API-ListAudienceGenerationJobs-response-nextToken"></a>
The token value used to access the next page of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 10240.

## Errors
<a name="API_ListAudienceGenerationJobs_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ValidationException **
The request parameters for this request are incorrect.
HTTP Status Code: 400

## See Also
<a name="API_ListAudienceGenerationJobs_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cleanroomsml-2023-09-06/ListAudienceGenerationJobs)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cleanroomsml-2023-09-06/ListAudienceGenerationJobs)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanroomsml-2023-09-06/ListAudienceGenerationJobs)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cleanroomsml-2023-09-06/ListAudienceGenerationJobs)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanroomsml-2023-09-06/ListAudienceGenerationJobs)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cleanroomsml-2023-09-06/ListAudienceGenerationJobs)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cleanroomsml-2023-09-06/ListAudienceGenerationJobs)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cleanroomsml-2023-09-06/ListAudienceGenerationJobs)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cleanroomsml-2023-09-06/ListAudienceGenerationJobs)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanroomsml-2023-09-06/ListAudienceGenerationJobs)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms ML. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cleanrooms-ml` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
