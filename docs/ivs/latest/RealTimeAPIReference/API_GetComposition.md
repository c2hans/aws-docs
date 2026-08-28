---
source_url: https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_GetComposition.html
---

# GetComposition
<a name="API_GetComposition"></a>

Get information about the specified Composition resource.

## Request Syntax
<a name="API_GetComposition_RequestSyntax"></a>

```
POST /GetComposition HTTP/1.1
Content-type: application/json

{
   "arn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_GetComposition_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetComposition_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [arn](#API_GetComposition_RequestSyntax) **   <a name="ivsrealtimeeapireference-GetComposition-request-arn"></a>
ARN of the Composition resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `arn:aws:ivs:[a-z0-9-]+:[0-9]+:composition/[a-zA-Z0-9-]+`
Required: Yes

## Response Syntax
<a name="API_GetComposition_ResponseSyntax"></a>

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
<a name="API_GetComposition_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [composition](#API_GetComposition_ResponseSyntax) **   <a name="ivsrealtimeeapireference-GetComposition-response-composition"></a>
The Composition that was returned.
Type: [Composition](API_Composition.md) object

## Errors
<a name="API_GetComposition_Errors"></a>

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
<a name="API_GetComposition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ivs-realtime-2020-07-14/GetComposition)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ivs-realtime-2020-07-14/GetComposition)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ivs-realtime-2020-07-14/GetComposition)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ivs-realtime-2020-07-14/GetComposition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ivs-realtime-2020-07-14/GetComposition)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ivs-realtime-2020-07-14/GetComposition)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ivs-realtime-2020-07-14/GetComposition)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ivs-realtime-2020-07-14/GetComposition)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ivs-realtime-2020-07-14/GetComposition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ivs-realtime-2020-07-14/GetComposition)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon IVS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ivs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
