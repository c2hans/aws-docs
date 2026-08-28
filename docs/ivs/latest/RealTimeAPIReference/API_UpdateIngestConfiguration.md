---
source_url: https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_UpdateIngestConfiguration.html
---

# UpdateIngestConfiguration
<a name="API_UpdateIngestConfiguration"></a>

Updates a specified IngestConfiguration. Only the stage ARN attached to the IngestConfiguration can be updated. An IngestConfiguration that is active cannot be updated.

## Request Syntax
<a name="API_UpdateIngestConfiguration_RequestSyntax"></a>

```
POST /UpdateIngestConfiguration HTTP/1.1
Content-type: application/json

{
   "arn": "{{string}}",
   "redundantIngest": {{boolean}},
   "stageArn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateIngestConfiguration_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_UpdateIngestConfiguration_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [arn](#API_UpdateIngestConfiguration_RequestSyntax) **   <a name="ivsrealtimeeapireference-UpdateIngestConfiguration-request-arn"></a>
ARN of the IngestConfiguration, for which the related stage ARN needs to be updated.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `arn:aws:ivs:[a-z0-9-]+:[0-9]+:ingest-configuration/[a-zA-Z0-9-]+`
Required: Yes

 ** [redundantIngest](#API_UpdateIngestConfiguration_RequestSyntax) **   <a name="ivsrealtimeeapireference-UpdateIngestConfiguration-request-redundantIngest"></a>
Indicates whether redundant ingest is enabled for the ingest configuration. Default: `false`.
Type: Boolean
Required: No

 ** [stageArn](#API_UpdateIngestConfiguration_RequestSyntax) **   <a name="ivsrealtimeeapireference-UpdateIngestConfiguration-request-stageArn"></a>
Stage ARN that needs to be updated.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Pattern: `^$|^arn:aws:ivs:[a-z0-9-]+:[0-9]+:stage/[a-zA-Z0-9-]+$`
Required: No

## Response Syntax
<a name="API_UpdateIngestConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ingestConfiguration": {
      "arn": "string",
      "attributes": {
         "string" : "string"
      },
      "ingestProtocol": "string",
      "name": "string",
      "participantId": "string",
      "redundantIngest": boolean,
      "redundantIngestCredentials": [
         {
            "participantId": "string",
            "streamKey": "string"
         }
      ],
      "stageArn": "string",
      "state": "string",
      "streamKey": "string",
      "tags": {
         "string" : "string"
      },
      "userId": "string"
   }
}
```

## Response Elements
<a name="API_UpdateIngestConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ingestConfiguration](#API_UpdateIngestConfiguration_ResponseSyntax) **   <a name="ivsrealtimeeapireference-UpdateIngestConfiguration-response-ingestConfiguration"></a>
The updated IngestConfiguration.
Type: [IngestConfiguration](API_IngestConfiguration.md) object

## Errors
<a name="API_UpdateIngestConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **

 ** exceptionMessage **
User does not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **

 ** exceptionMessage **
Updating or deleting a resource can cause an inconsistent state.
HTTP Status Code: 409

 ** PendingVerification **

 ** exceptionMessage **
 Your account is pending verification.
HTTP Status Code: 403

 ** ResourceNotFoundException **

 ** exceptionMessage **
Request references a resource which does not exist.
HTTP Status Code: 404

 ** ValidationException **

 ** exceptionMessage **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_UpdateIngestConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ivs-realtime-2020-07-14/UpdateIngestConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ivs-realtime-2020-07-14/UpdateIngestConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ivs-realtime-2020-07-14/UpdateIngestConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ivs-realtime-2020-07-14/UpdateIngestConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ivs-realtime-2020-07-14/UpdateIngestConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ivs-realtime-2020-07-14/UpdateIngestConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ivs-realtime-2020-07-14/UpdateIngestConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ivs-realtime-2020-07-14/UpdateIngestConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ivs-realtime-2020-07-14/UpdateIngestConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ivs-realtime-2020-07-14/UpdateIngestConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon IVS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ivs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
