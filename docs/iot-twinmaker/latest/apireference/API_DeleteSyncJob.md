---
source_url: https://docs.aws.amazon.com/iot-twinmaker/latest/apireference/API_DeleteSyncJob.html
---

# DeleteSyncJob
<a name="API_DeleteSyncJob"></a>

Delete the SyncJob.

## Request Syntax
<a name="API_DeleteSyncJob_RequestSyntax"></a>

```
DELETE /workspaces/{{workspaceId}}/sync-jobs/{{syncSource}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteSyncJob_RequestParameters"></a>

The request uses the following URI parameters.

 ** [syncSource](#API_DeleteSyncJob_RequestSyntax) **   <a name="tm-DeleteSyncJob-request-uri-syncSource"></a>
The sync source.
Currently the only supported syncSource is `SITEWISE `.
Pattern: `[a-zA-Z_0-9]+`
Required: Yes

 ** [workspaceId](#API_DeleteSyncJob_RequestSyntax) **   <a name="tm-DeleteSyncJob-request-uri-workspaceId"></a>
The workspace ID.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z_0-9][a-zA-Z_\-0-9]*[a-zA-Z0-9]+`
Required: Yes

## Request Body
<a name="API_DeleteSyncJob_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteSyncJob_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "state": "string"
}
```

## Response Elements
<a name="API_DeleteSyncJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [state](#API_DeleteSyncJob_ResponseSyntax) **   <a name="tm-DeleteSyncJob-response-state"></a>
The SyncJob response state.
Type: String
Valid Values: `CREATING | INITIALIZING | ACTIVE | DELETING | ERROR`

## Errors
<a name="API_DeleteSyncJob_Errors"></a>

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
<a name="API_DeleteSyncJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iottwinmaker-2021-11-29/DeleteSyncJob)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iottwinmaker-2021-11-29/DeleteSyncJob)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iottwinmaker-2021-11-29/DeleteSyncJob)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iottwinmaker-2021-11-29/DeleteSyncJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iottwinmaker-2021-11-29/DeleteSyncJob)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iottwinmaker-2021-11-29/DeleteSyncJob)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iottwinmaker-2021-11-29/DeleteSyncJob)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iottwinmaker-2021-11-29/DeleteSyncJob)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iottwinmaker-2021-11-29/DeleteSyncJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iottwinmaker-2021-11-29/DeleteSyncJob)
