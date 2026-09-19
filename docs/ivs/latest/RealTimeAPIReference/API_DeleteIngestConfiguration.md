---
source_url: https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_DeleteIngestConfiguration.html
---

# DeleteIngestConfiguration
<a name="API_DeleteIngestConfiguration"></a>

Deletes a specified IngestConfiguration, so it can no longer be used to broadcast. An IngestConfiguration cannot be deleted if the publisher is actively streaming to a stage, unless `force` is set to `true`.

## Request Syntax
<a name="API_DeleteIngestConfiguration_RequestSyntax"></a>

```
POST /DeleteIngestConfiguration HTTP/1.1
Content-type: application/json

{
   "arn": "{{string}}",
   "force": {{boolean}}
}
```

## URI Request Parameters
<a name="API_DeleteIngestConfiguration_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_DeleteIngestConfiguration_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [arn](#API_DeleteIngestConfiguration_RequestSyntax) **   <a name="ivsrealtimeeapireference-DeleteIngestConfiguration-request-arn"></a>
ARN of the IngestConfiguration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `arn:aws:ivs:[a-z0-9-]+:[0-9]+:ingest-configuration/[a-zA-Z0-9-]+`
Required: Yes

 ** [force](#API_DeleteIngestConfiguration_RequestSyntax) **   <a name="ivsrealtimeeapireference-DeleteIngestConfiguration-request-force"></a>
Optional field to force deletion of the IngestConfiguration. If this is set to `true` when a participant is actively publishing, the participant is disconnected from the stage, followed by deletion of the IngestConfiguration. Default: `false`.
Type: Boolean
Required: No

## Response Syntax
<a name="API_DeleteIngestConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_DeleteIngestConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteIngestConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
User does not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
Updating or deleting a resource can cause an inconsistent state.
HTTP Status Code: 409

 ** PendingVerification **
Your account is pending verification.
HTTP Status Code: 403

 ** ResourceNotFoundException **
Request references a resource which does not exist.
HTTP Status Code: 404

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_DeleteIngestConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ivs-realtime-2020-07-14/DeleteIngestConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ivs-realtime-2020-07-14/DeleteIngestConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ivs-realtime-2020-07-14/DeleteIngestConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ivs-realtime-2020-07-14/DeleteIngestConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ivs-realtime-2020-07-14/DeleteIngestConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ivs-realtime-2020-07-14/DeleteIngestConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ivs-realtime-2020-07-14/DeleteIngestConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ivs-realtime-2020-07-14/DeleteIngestConfiguration)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ivs-realtime-2020-07-14/DeleteIngestConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ivs-realtime-2020-07-14/DeleteIngestConfiguration)
