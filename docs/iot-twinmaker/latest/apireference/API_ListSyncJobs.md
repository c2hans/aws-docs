---
source_url: https://docs.aws.amazon.com/iot-twinmaker/latest/apireference/API_ListSyncJobs.html
---

# ListSyncJobs
<a name="API_ListSyncJobs"></a>

List all SyncJobs.

## Request Syntax
<a name="API_ListSyncJobs_RequestSyntax"></a>

```
POST /workspaces/{{workspaceId}}/sync-jobs-list HTTP/1.1
Content-type: application/json

{
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListSyncJobs_RequestParameters"></a>

The request uses the following URI parameters.

 ** [workspaceId](#API_ListSyncJobs_RequestSyntax) **   <a name="tm-ListSyncJobs-request-uri-workspaceId"></a>
The ID of the workspace that contains the sync job.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z_0-9][a-zA-Z_\-0-9]*[a-zA-Z0-9]+`
Required: Yes

## Request Body
<a name="API_ListSyncJobs_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [maxResults](#API_ListSyncJobs_RequestSyntax) **   <a name="tm-ListSyncJobs-request-maxResults"></a>
The maximum number of results to return at one time. The default is 50.
Valid Range: Minimum value of 0. Maximum value of 200.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 200.
Required: No

 ** [nextToken](#API_ListSyncJobs_RequestSyntax) **   <a name="tm-ListSyncJobs-request-nextToken"></a>
The string that specifies the next page of results.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 17880.
Pattern: `.*`
Required: No

## Response Syntax
<a name="API_ListSyncJobs_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "syncJobSummaries": [
      {
         "arn": "string",
         "creationDateTime": number,
         "status": {
            "error": {
               "code": "string",
               "message": "string"
            },
            "state": "string"
         },
         "syncSource": "string",
         "updateDateTime": number,
         "workspaceId": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListSyncJobs_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListSyncJobs_ResponseSyntax) **   <a name="tm-ListSyncJobs-response-nextToken"></a>
The string that specifies the next page of results.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 17880.
Pattern: `.*`

 ** [syncJobSummaries](#API_ListSyncJobs_ResponseSyntax) **   <a name="tm-ListSyncJobs-response-syncJobSummaries"></a>
The listed SyncJob summaries.
Type: Array of [SyncJobSummary](API_SyncJobSummary.md) objects

## Errors
<a name="API_ListSyncJobs_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access is denied.
HTTP Status Code: 403

 ** InternalServerException **
An unexpected error has occurred.
HTTP Status Code: 500

 ** ServiceQuotaExceededException **
The service quota was exceeded.
HTTP Status Code: 402

 ** ThrottlingException **
The rate exceeds the limit.
HTTP Status Code: 429

 ** ValidationException **
Failed
HTTP Status Code: 400

## See Also
<a name="API_ListSyncJobs_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iottwinmaker-2021-11-29/ListSyncJobs)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iottwinmaker-2021-11-29/ListSyncJobs)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iottwinmaker-2021-11-29/ListSyncJobs)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iottwinmaker-2021-11-29/ListSyncJobs)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iottwinmaker-2021-11-29/ListSyncJobs)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iottwinmaker-2021-11-29/ListSyncJobs)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iottwinmaker-2021-11-29/ListSyncJobs)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iottwinmaker-2021-11-29/ListSyncJobs)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iottwinmaker-2021-11-29/ListSyncJobs)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iottwinmaker-2021-11-29/ListSyncJobs)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for IoT TwinMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-twinmaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
