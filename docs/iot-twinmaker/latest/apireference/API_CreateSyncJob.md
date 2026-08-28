---
source_url: https://docs.aws.amazon.com/iot-twinmaker/latest/apireference/API_CreateSyncJob.html
---

# CreateSyncJob
<a name="API_CreateSyncJob"></a>

This action creates a SyncJob.

## Request Syntax
<a name="API_CreateSyncJob_RequestSyntax"></a>

```
POST /workspaces/{{workspaceId}}/sync-jobs/{{syncSource}} HTTP/1.1
Content-type: application/json

{
   "syncRole": "{{string}}",
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateSyncJob_RequestParameters"></a>

The request uses the following URI parameters.

 ** [syncSource](#API_CreateSyncJob_RequestSyntax) **   <a name="tm-CreateSyncJob-request-uri-syncSource"></a>
The sync source.
Currently the only supported syncSoource is `SITEWISE `.
Pattern: `[a-zA-Z_0-9]+`
Required: Yes

 ** [workspaceId](#API_CreateSyncJob_RequestSyntax) **   <a name="tm-CreateSyncJob-request-uri-workspaceId"></a>
The workspace ID.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z_0-9][a-zA-Z_\-0-9]*[a-zA-Z0-9]+`
Required: Yes

## Request Body
<a name="API_CreateSyncJob_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [syncRole](#API_CreateSyncJob_RequestSyntax) **   <a name="tm-CreateSyncJob-request-syncRole"></a>
The SyncJob IAM role. This IAM role is used by the SyncJob to read from the syncSource, and create, update, or delete the corresponding resources.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:((aws)|(aws-cn)|(aws-us-gov)):iam::[0-9]{12}:role/.*`
Required: Yes

 ** [tags](#API_CreateSyncJob_RequestSyntax) **   <a name="tm-CreateSyncJob-request-tags"></a>
The SyncJob tags.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-@]*)`
Value Length Constraints: Minimum length of 1. Maximum length of 256.
Value Pattern: `.*`
Required: No

## Response Syntax
<a name="API_CreateSyncJob_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "arn": "string",
   "creationDateTime": number,
   "state": "string"
}
```

## Response Elements
<a name="API_CreateSyncJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_CreateSyncJob_ResponseSyntax) **   <a name="tm-CreateSyncJob-response-arn"></a>
The SyncJob ARN.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:((aws)|(aws-cn)|(aws-us-gov)):iottwinmaker:[a-z0-9-]+:[0-9]{12}:[\/a-zA-Z0-9_\-\.:]+`

 ** [creationDateTime](#API_CreateSyncJob_ResponseSyntax) **   <a name="tm-CreateSyncJob-response-creationDateTime"></a>
The date and time for the SyncJob creation.
Type: Timestamp

 ** [state](#API_CreateSyncJob_ResponseSyntax) **   <a name="tm-CreateSyncJob-response-state"></a>
The SyncJob response state.
Type: String
Valid Values: `CREATING | INITIALIZING | ACTIVE | DELETING | ERROR`

## Errors
<a name="API_CreateSyncJob_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access is denied.
HTTP Status Code: 403

 ** ConflictException **
A conflict occurred.
HTTP Status Code: 409

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
<a name="API_CreateSyncJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iottwinmaker-2021-11-29/CreateSyncJob)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iottwinmaker-2021-11-29/CreateSyncJob)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iottwinmaker-2021-11-29/CreateSyncJob)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iottwinmaker-2021-11-29/CreateSyncJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iottwinmaker-2021-11-29/CreateSyncJob)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iottwinmaker-2021-11-29/CreateSyncJob)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iottwinmaker-2021-11-29/CreateSyncJob)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iottwinmaker-2021-11-29/CreateSyncJob)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iottwinmaker-2021-11-29/CreateSyncJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iottwinmaker-2021-11-29/CreateSyncJob)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for IoT TwinMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-twinmaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
