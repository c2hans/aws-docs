---
source_url: https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_CreateIngestConfiguration.html
---

# CreateIngestConfiguration
<a name="API_CreateIngestConfiguration"></a>

Creates a new IngestConfiguration resource, used to specify the ingest protocol for a stage.

## Request Syntax
<a name="API_CreateIngestConfiguration_RequestSyntax"></a>

```
POST /CreateIngestConfiguration HTTP/1.1
Content-type: application/json

{
   "attributes": {
      "{{string}}" : "{{string}}"
   },
   "ingestProtocol": "{{string}}",
   "insecureIngest": {{boolean}},
   "name": "{{string}}",
   "redundantIngest": {{boolean}},
   "stageArn": "{{string}}",
   "tags": {
      "{{string}}" : "{{string}}"
   },
   "userId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateIngestConfiguration_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateIngestConfiguration_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [attributes](#API_CreateIngestConfiguration_RequestSyntax) **   <a name="ivsrealtimeeapireference-CreateIngestConfiguration-request-attributes"></a>
Application-provided attributes to store in the IngestConfiguration and attach to a stage. Map keys and values can contain UTF-8 encoded text. The maximum length of this field is 1 KB total. *This field is exposed to all stage participants and should not be used for personally identifying, confidential, or sensitive information.*
Type: String to string map
Required: No

 ** [ingestProtocol](#API_CreateIngestConfiguration_RequestSyntax) **   <a name="ivsrealtimeeapireference-CreateIngestConfiguration-request-ingestProtocol"></a>
Type of ingest protocol that the user employs to broadcast. If this is set to `RTMP`, `insecureIngest` must be set to `true`.
Type: String
Valid Values: `RTMP | RTMPS`
Required: Yes

 ** [insecureIngest](#API_CreateIngestConfiguration_RequestSyntax) **   <a name="ivsrealtimeeapireference-CreateIngestConfiguration-request-insecureIngest"></a>
Whether the stage allows insecure RTMP ingest. This must be set to `true`, if `ingestProtocol` is set to `RTMP`. Default: `false`.
Type: Boolean
Required: No

 ** [name](#API_CreateIngestConfiguration_RequestSyntax) **   <a name="ivsrealtimeeapireference-CreateIngestConfiguration-request-name"></a>
Optional name that can be specified for the IngestConfiguration being created.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Pattern: `[a-zA-Z0-9-_]*`
Required: No

 ** [redundantIngest](#API_CreateIngestConfiguration_RequestSyntax) **   <a name="ivsrealtimeeapireference-CreateIngestConfiguration-request-redundantIngest"></a>
Indicates whether redundant ingest is enabled for the ingest configuration. Default: `false`.
Type: Boolean
Required: No

 ** [stageArn](#API_CreateIngestConfiguration_RequestSyntax) **   <a name="ivsrealtimeeapireference-CreateIngestConfiguration-request-stageArn"></a>
ARN of the stage with which the IngestConfiguration is associated.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Pattern: `^$|^arn:aws:ivs:[a-z0-9-]+:[0-9]+:stage/[a-zA-Z0-9-]+$`
Required: No

 ** [tags](#API_CreateIngestConfiguration_RequestSyntax) **   <a name="ivsrealtimeeapireference-CreateIngestConfiguration-request-tags"></a>
Tags attached to the resource. Array of maps, each of the form `string:string (key:value)`. See [Best practices and strategies](https://docs.aws.amazon.com/tag-editor/latest/userguide/best-practices-and-strats.html) in *Tagging AWS Resources and Tag Editor* for details, including restrictions that apply to tags and "Tag naming limits and requirements"; Amazon IVS has no constraints on tags beyond what is documented there.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** [userId](#API_CreateIngestConfiguration_RequestSyntax) **   <a name="ivsrealtimeeapireference-CreateIngestConfiguration-request-userId"></a>
Customer-assigned name to help identify the participant using the IngestConfiguration; this can be used to link a participant to a user in the customer’s own systems. This can be any UTF-8 encoded text. *This field is exposed to all stage participants and should not be used for personally identifying, confidential, or sensitive information.*
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Required: No

## Response Syntax
<a name="API_CreateIngestConfiguration_ResponseSyntax"></a>

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
<a name="API_CreateIngestConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ingestConfiguration](#API_CreateIngestConfiguration_ResponseSyntax) **   <a name="ivsrealtimeeapireference-CreateIngestConfiguration-response-ingestConfiguration"></a>
The IngestConfiguration that was created.
Type: [IngestConfiguration](API_IngestConfiguration.md) object

## Errors
<a name="API_CreateIngestConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **

 ** exceptionMessage **
User does not have sufficient access to perform this action.
HTTP Status Code: 403

 ** PendingVerification **

 ** exceptionMessage **
 Your account is pending verification.
HTTP Status Code: 403

 ** ServiceQuotaExceededException **

 ** exceptionMessage **
Request would cause a service quota to be exceeded.
HTTP Status Code: 402

 ** ValidationException **

 ** exceptionMessage **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_CreateIngestConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ivs-realtime-2020-07-14/CreateIngestConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ivs-realtime-2020-07-14/CreateIngestConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ivs-realtime-2020-07-14/CreateIngestConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ivs-realtime-2020-07-14/CreateIngestConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ivs-realtime-2020-07-14/CreateIngestConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ivs-realtime-2020-07-14/CreateIngestConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ivs-realtime-2020-07-14/CreateIngestConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ivs-realtime-2020-07-14/CreateIngestConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ivs-realtime-2020-07-14/CreateIngestConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ivs-realtime-2020-07-14/CreateIngestConfiguration)
