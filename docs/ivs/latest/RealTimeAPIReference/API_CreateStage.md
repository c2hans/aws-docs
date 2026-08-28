---
source_url: https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_CreateStage.html
---

# CreateStage
<a name="API_CreateStage"></a>

Creates a new stage (and optionally participant tokens).

## Request Syntax
<a name="API_CreateStage_RequestSyntax"></a>

```
POST /CreateStage HTTP/1.1
Content-type: application/json

{
   "autoParticipantRecordingConfiguration": {
      "hlsConfiguration": {
         "targetSegmentDurationSeconds": {{number}}
      },
      "mediaTypes": [ "{{string}}" ],
      "recordingReconnectWindowSeconds": {{number}},
      "recordParticipantReplicas": {{boolean}},
      "storageConfigurationArn": "{{string}}",
      "thumbnailConfiguration": {
         "recordingMode": "{{string}}",
         "storage": [ "{{string}}" ],
         "targetIntervalSeconds": {{number}}
      }
   },
   "name": "{{string}}",
   "participantTokenConfigurations": [
      {
         "attributes": {
            "{{string}}" : "{{string}}"
         },
         "capabilities": [ "{{string}}" ],
         "duration": {{number}},
         "userId": "{{string}}"
      }
   ],
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateStage_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateStage_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [autoParticipantRecordingConfiguration](#API_CreateStage_RequestSyntax) **   <a name="ivsrealtimeeapireference-CreateStage-request-autoParticipantRecordingConfiguration"></a>
Configuration object for individual participant recording, to attach to the new stage.
Type: [AutoParticipantRecordingConfiguration](API_AutoParticipantRecordingConfiguration.md) object
Required: No

 ** [name](#API_CreateStage_RequestSyntax) **   <a name="ivsrealtimeeapireference-CreateStage-request-name"></a>
Optional name that can be specified for the stage being created.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Pattern: `[a-zA-Z0-9-_]*`
Required: No

 ** [participantTokenConfigurations](#API_CreateStage_RequestSyntax) **   <a name="ivsrealtimeeapireference-CreateStage-request-participantTokenConfigurations"></a>
Array of participant token configuration objects to attach to the new stage.
Type: Array of [ParticipantTokenConfiguration](API_ParticipantTokenConfiguration.md) objects
Array Members: Minimum number of 0 items. Maximum number of 12 items.
Required: No

 ** [tags](#API_CreateStage_RequestSyntax) **   <a name="ivsrealtimeeapireference-CreateStage-request-tags"></a>
Tags attached to the resource. Array of maps, each of the form `string:string (key:value)`. See [Best practices and strategies](https://docs.aws.amazon.com/tag-editor/latest/userguide/best-practices-and-strats.html) in *Tagging AWS Resources and Tag Editor* for details, including restrictions that apply to tags and "Tag naming limits and requirements"; Amazon IVS has no constraints on tags beyond what is documented there.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## Response Syntax
<a name="API_CreateStage_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "participantTokens": [
      {
         "attributes": {
            "string" : "string"
         },
         "capabilities": [ "string" ],
         "duration": number,
         "expirationTime": "string",
         "participantId": "string",
         "token": "string",
         "userId": "string"
      }
   ],
   "stage": {
      "activeSessionId": "string",
      "arn": "string",
      "autoParticipantRecordingConfiguration": {
         "hlsConfiguration": {
            "targetSegmentDurationSeconds": number
         },
         "mediaTypes": [ "string" ],
         "recordingReconnectWindowSeconds": number,
         "recordParticipantReplicas": boolean,
         "storageConfigurationArn": "string",
         "thumbnailConfiguration": {
            "recordingMode": "string",
            "storage": [ "string" ],
            "targetIntervalSeconds": number
         }
      },
      "endpoints": {
         "events": "string",
         "rtmp": "string",
         "rtmps": "string",
         "whip": "string"
      },
      "name": "string",
      "tags": {
         "string" : "string"
      }
   }
}
```

## Response Elements
<a name="API_CreateStage_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [participantTokens](#API_CreateStage_ResponseSyntax) **   <a name="ivsrealtimeeapireference-CreateStage-response-participantTokens"></a>
Participant tokens attached to the stage. These correspond to the `participants` in the request.
Type: Array of [ParticipantToken](API_ParticipantToken.md) objects

 ** [stage](#API_CreateStage_ResponseSyntax) **   <a name="ivsrealtimeeapireference-CreateStage-response-stage"></a>
The stage that was created.
Type: [Stage](API_Stage.md) object

## Errors
<a name="API_CreateStage_Errors"></a>

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
<a name="API_CreateStage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ivs-realtime-2020-07-14/CreateStage)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ivs-realtime-2020-07-14/CreateStage)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ivs-realtime-2020-07-14/CreateStage)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ivs-realtime-2020-07-14/CreateStage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ivs-realtime-2020-07-14/CreateStage)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ivs-realtime-2020-07-14/CreateStage)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ivs-realtime-2020-07-14/CreateStage)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ivs-realtime-2020-07-14/CreateStage)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ivs-realtime-2020-07-14/CreateStage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ivs-realtime-2020-07-14/CreateStage)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon IVS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ivs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
