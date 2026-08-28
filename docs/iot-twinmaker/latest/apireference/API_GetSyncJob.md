---
source_url: https://docs.aws.amazon.com/iot-twinmaker/latest/apireference/API_GetSyncJob.html
---

# GetSyncJob
<a name="API_GetSyncJob"></a>

Gets the SyncJob.

## Request Syntax
<a name="API_GetSyncJob_RequestSyntax"></a>

```
GET /sync-jobs/{{syncSource}}?workspace={{workspaceId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetSyncJob_RequestParameters"></a>

The request uses the following URI parameters.

 ** [syncSource](#API_GetSyncJob_RequestSyntax) **   <a name="tm-GetSyncJob-request-uri-syncSource"></a>
The sync source.
Currently the only supported syncSource is `SITEWISE `.
Pattern: `[a-zA-Z_0-9]+`
Required: Yes

 ** [workspaceId](#API_GetSyncJob_RequestSyntax) **   <a name="tm-GetSyncJob-request-uri-workspaceId"></a>
The workspace ID.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z_0-9][a-zA-Z_\-0-9]*[a-zA-Z0-9]+`

## Request Body
<a name="API_GetSyncJob_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetSyncJob_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

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
   "syncRole": "string",
   "syncSource": "string",
   "updateDateTime": number,
   "workspaceId": "string"
}
```

## Response Elements
<a name="API_GetSyncJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_GetSyncJob_ResponseSyntax) **   <a name="tm-GetSyncJob-response-arn"></a>
The sync job ARN.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:((aws)|(aws-cn)|(aws-us-gov)):iottwinmaker:[a-z0-9-]+:[0-9]{12}:[\/a-zA-Z0-9_\-\.:]+`

 ** [creationDateTime](#API_GetSyncJob_ResponseSyntax) **   <a name="tm-GetSyncJob-response-creationDateTime"></a>
The creation date and time.
Type: Timestamp

 ** [status](#API_GetSyncJob_ResponseSyntax) **   <a name="tm-GetSyncJob-response-status"></a>
The SyncJob response status.
Type: [SyncJobStatus](API_SyncJobStatus.md) object

 ** [syncRole](#API_GetSyncJob_ResponseSyntax) **   <a name="tm-GetSyncJob-response-syncRole"></a>
The sync IAM role.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:((aws)|(aws-cn)|(aws-us-gov)):iam::[0-9]{12}:role/.*`

 ** [syncSource](#API_GetSyncJob_ResponseSyntax) **   <a name="tm-GetSyncJob-response-syncSource"></a>
The sync source.
Currently the only supported syncSource is `SITEWISE`.
Type: String
Pattern: `[a-zA-Z_0-9]+`

 ** [updateDateTime](#API_GetSyncJob_ResponseSyntax) **   <a name="tm-GetSyncJob-response-updateDateTime"></a>
The update date and time.
Type: Timestamp

 ** [workspaceId](#API_GetSyncJob_ResponseSyntax) **   <a name="tm-GetSyncJob-response-workspaceId"></a>
The ID of the workspace that contains the sync job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z_0-9][a-zA-Z_\-0-9]*[a-zA-Z0-9]+`

## Errors
<a name="API_GetSyncJob_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access is denied.
HTTP Status Code: 403

 ** InternalServerException **
An unexpected error has occurred.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The resource wasn't found.
HTTP Status Code: 404

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
<a name="API_GetSyncJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iottwinmaker-2021-11-29/GetSyncJob)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iottwinmaker-2021-11-29/GetSyncJob)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iottwinmaker-2021-11-29/GetSyncJob)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iottwinmaker-2021-11-29/GetSyncJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iottwinmaker-2021-11-29/GetSyncJob)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iottwinmaker-2021-11-29/GetSyncJob)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iottwinmaker-2021-11-29/GetSyncJob)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iottwinmaker-2021-11-29/GetSyncJob)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iottwinmaker-2021-11-29/GetSyncJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iottwinmaker-2021-11-29/GetSyncJob)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for IoT TwinMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-twinmaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
