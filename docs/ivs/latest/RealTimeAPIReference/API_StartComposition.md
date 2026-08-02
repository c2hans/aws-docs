---
source_url: https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_StartComposition.html
---

# StartComposition
<a name="API_StartComposition"></a>

Starts a Composition from a stage based on the configuration provided in the request.

A Composition is an ephemeral resource that exists after this operation returns successfully. Composition stops and the resource is deleted:
+ When [StopComposition](API_StopComposition.md) is called.
+ After a 1-minute timeout, when all participants are disconnected from the stage.
+ After a 1-minute timeout, if there are no participants in the stage when StartComposition is called.
+ When broadcasting to the IVS channel fails and all retries are exhausted.
+ When broadcasting is disconnected and all attempts to reconnect are exhausted.

## Request Syntax
<a name="API_StartComposition_RequestSyntax"></a>

```
POST /StartComposition HTTP/1.1
Content-type: application/json

{
   "destinations": [
      {
         "channel": {
            "channelArn": "{{string}}",
            "encoderConfigurationArn": "{{string}}"
         },
         "name": "{{string}}",
         "s3": {
            "encoderConfigurationArns": [ "{{string}}" ],
            "recordingConfiguration": {
               "format": "{{string}}",
               "hlsConfiguration": {
                  "targetSegmentDurationSeconds": {{number}}
               }
            },
            "storageConfigurationArn": "{{string}}",
            "thumbnailConfigurations": [
               {
                  "storage": [ "{{string}}" ],
                  "targetIntervalSeconds": {{number}}
               }
            ]
         }
      }
   ],
   "idempotencyToken": "{{string}}",
   "layout": {
      "grid": {
         "featuredParticipantAttribute": "{{string}}",
         "gridGap": {{number}},
         "omitStoppedVideo": {{boolean}},
         "participantOrderAttribute": "{{string}}",
         "videoAspectRatio": "{{string}}",
         "videoFillMode": "{{string}}"
      },
      "pip": {
         "featuredParticipantAttribute": "{{string}}",
         "gridGap": {{number}},
         "omitStoppedVideo": {{boolean}},
         "participantOrderAttribute": "{{string}}",
         "pipBehavior": "{{string}}",
         "pipHeight": {{number}},
         "pipOffset": {{number}},
         "pipParticipantAttribute": "{{string}}",
         "pipPosition": "{{string}}",
         "pipWidth": {{number}},
         "videoFillMode": "{{string}}"
      }
   },
   "stageArn": "{{string}}",
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_StartComposition_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_StartComposition_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [destinations](#API_StartComposition_RequestSyntax) **   <a name="ivsrealtimeeapireference-StartComposition-request-destinations"></a>
Array of destination configuration.
Type: Array of [DestinationConfiguration](API_DestinationConfiguration.md) objects
Array Members: Minimum number of 1 item. Maximum number of 2 items.
Required: Yes

 ** [idempotencyToken](#API_StartComposition_RequestSyntax) **   <a name="ivsrealtimeeapireference-StartComposition-request-idempotencyToken"></a>
Idempotency token.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9-_]*`
Required: No

 ** [layout](#API_StartComposition_RequestSyntax) **   <a name="ivsrealtimeeapireference-StartComposition-request-layout"></a>
Layout object to configure composition parameters.
Type: [LayoutConfiguration](API_LayoutConfiguration.md) object
Required: No

 ** [stageArn](#API_StartComposition_RequestSyntax) **   <a name="ivsrealtimeeapireference-StartComposition-request-stageArn"></a>
ARN of the stage to be used for compositing.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `arn:aws:ivs:[a-z0-9-]+:[0-9]+:stage/[a-zA-Z0-9-]+`
Required: Yes

 ** [tags](#API_StartComposition_RequestSyntax) **   <a name="ivsrealtimeeapireference-StartComposition-request-tags"></a>
Tags attached to the resource. Array of maps, each of the form `string:string (key:value)`. See [Best practices and strategies](https://docs.aws.amazon.com/tag-editor/latest/userguide/best-practices-and-strats.html) in *Tagging AWS Resources and Tag Editor* for details, including restrictions that apply to tags and "Tag naming limits and requirements"; Amazon IVS has no constraints on tags beyond what is documented there.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## Response Syntax
<a name="API_StartComposition_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "composition": {
      "arn": "string",
      "destinations": [
         {
            "configuration": {
               "channel": {
                  "channelArn": "string",
                  "encoderConfigurationArn": "string"
               },
               "name": "string",
               "s3": {
                  "encoderConfigurationArns": [ "string" ],
                  "recordingConfiguration": {
                     "format": "string",
                     "hlsConfiguration": {
                        "targetSegmentDurationSeconds": number
                     }
                  },
                  "storageConfigurationArn": "string",
                  "thumbnailConfigurations": [
                     {
                        "storage": [ "string" ],
                        "targetIntervalSeconds": number
                     }
                  ]
               }
            },
            "detail": {
               "s3": {
                  "recordingPrefix": "string"
               }
            },
            "endTime": "string",
            "id": "string",
            "startTime": "string",
            "state": "string"
         }
      ],
      "endTime": "string",
      "layout": {
         "grid": {
            "featuredParticipantAttribute": "string",
            "gridGap": number,
            "omitStoppedVideo": boolean,
            "participantOrderAttribute": "string",
            "videoAspectRatio": "string",
            "videoFillMode": "string"
         },
         "pip": {
            "featuredParticipantAttribute": "string",
            "gridGap": number,
            "omitStoppedVideo": boolean,
            "participantOrderAttribute": "string",
            "pipBehavior": "string",
            "pipHeight": number,
            "pipOffset": number,
            "pipParticipantAttribute": "string",
            "pipPosition": "string",
            "pipWidth": number,
            "videoFillMode": "string"
         }
      },
      "stageArn": "string",
      "startTime": "string",
      "state": "string",
      "tags": {
         "string" : "string"
      }
   }
}
```

## Response Elements
<a name="API_StartComposition_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [composition](#API_StartComposition_ResponseSyntax) **   <a name="ivsrealtimeeapireference-StartComposition-response-composition"></a>
The Composition that was created.
Type: [Composition](API_Composition.md) object

## Errors
<a name="API_StartComposition_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **

 ** exceptionMessage **
User does not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **

 ** exceptionMessage **
Updating or deleting a resource can cause an inconsistent state.
HTTP Status Code: 409

 ** InternalServerException **

 ** exceptionMessage **
Unexpected error during processing of request.
HTTP Status Code: 500

 ** PendingVerification **

 ** exceptionMessage **
 Your account is pending verification.
HTTP Status Code: 403

 ** ResourceNotFoundException **

 ** exceptionMessage **
Request references a resource which does not exist.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **

 ** exceptionMessage **
Request would cause a service quota to be exceeded.
HTTP Status Code: 402

 ** ValidationException **

 ** exceptionMessage **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_StartComposition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ivs-realtime-2020-07-14/StartComposition)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ivs-realtime-2020-07-14/StartComposition)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ivs-realtime-2020-07-14/StartComposition)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ivs-realtime-2020-07-14/StartComposition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ivs-realtime-2020-07-14/StartComposition)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ivs-realtime-2020-07-14/StartComposition)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ivs-realtime-2020-07-14/StartComposition)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ivs-realtime-2020-07-14/StartComposition)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ivs-realtime-2020-07-14/StartComposition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ivs-realtime-2020-07-14/StartComposition)
