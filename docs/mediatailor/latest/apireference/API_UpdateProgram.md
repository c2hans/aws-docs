---
source_url: https://docs.aws.amazon.com/mediatailor/latest/apireference/API_UpdateProgram.html
---

# UpdateProgram
<a name="API_UpdateProgram"></a>

Updates a program within a channel.

## Request Syntax
<a name="API_UpdateProgram_RequestSyntax"></a>

```
PUT /channel/{{ChannelName}}/program/{{ProgramName}} HTTP/1.1
Content-type: application/json

{
   "AdBreaks": [
      {
         "AdBreakMetadata": [
            {
               "Key": "{{string}}",
               "Value": "{{string}}"
            }
         ],
         "MessageType": "{{string}}",
         "OffsetMillis": {{number}},
         "Slate": {
            "SourceLocationName": "{{string}}",
            "VodSourceName": "{{string}}"
         },
         "SpliceInsertMessage": {
            "AvailNum": {{number}},
            "AvailsExpected": {{number}},
            "SpliceEventId": {{number}},
            "UniqueProgramId": {{number}}
         },
         "TimeSignalMessage": {
            "SegmentationDescriptors": [
               {
                  "SegmentationEventId": {{number}},
                  "SegmentationTypeId": {{number}},
                  "SegmentationUpid": "{{string}}",
                  "SegmentationUpidType": {{number}},
                  "SegmentNum": {{number}},
                  "SegmentsExpected": {{number}},
                  "SubSegmentNum": {{number}},
                  "SubSegmentsExpected": {{number}}
               }
            ]
         }
      }
   ],
   "AudienceMedia": [
      {
         "AlternateMedia": [
            {
               "AdBreaks": [
                  {
                     "AdBreakMetadata": [
                        {
                           "Key": "{{string}}",
                           "Value": "{{string}}"
                        }
                     ],
                     "MessageType": "{{string}}",
                     "OffsetMillis": {{number}},
                     "Slate": {
                        "SourceLocationName": "{{string}}",
                        "VodSourceName": "{{string}}"
                     },
                     "SpliceInsertMessage": {
                        "AvailNum": {{number}},
                        "AvailsExpected": {{number}},
                        "SpliceEventId": {{number}},
                        "UniqueProgramId": {{number}}
                     },
                     "TimeSignalMessage": {
                        "SegmentationDescriptors": [
                           {
                              "SegmentationEventId": {{number}},
                              "SegmentationTypeId": {{number}},
                              "SegmentationUpid": "{{string}}",
                              "SegmentationUpidType": {{number}},
                              "SegmentNum": {{number}},
                              "SegmentsExpected": {{number}},
                              "SubSegmentNum": {{number}},
                              "SubSegmentsExpected": {{number}}
                           }
                        ]
                     }
                  }
               ],
               "ClipRange": {
                  "EndOffsetMillis": {{number}},
                  "StartOffsetMillis": {{number}}
               },
               "DurationMillis": {{number}},
               "LiveSourceName": "{{string}}",
               "ScheduledStartTimeMillis": {{number}},
               "SourceLocationName": "{{string}}",
               "VodSourceName": "{{string}}"
            }
         ],
         "Audience": "{{string}}"
      }
   ],
   "ScheduleConfiguration": {
      "ClipRange": {
         "EndOffsetMillis": {{number}},
         "StartOffsetMillis": {{number}}
      },
      "Transition": {
         "DurationMillis": {{number}},
         "ScheduledStartTimeMillis": {{number}}
      }
   }
}
```

## URI Request Parameters
<a name="API_UpdateProgram_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ChannelName](#API_UpdateProgram_RequestSyntax) **   <a name="mediatailor-UpdateProgram-request-uri-ChannelName"></a>
The name of the channel for this Program.
Required: Yes

 ** [ProgramName](#API_UpdateProgram_RequestSyntax) **   <a name="mediatailor-UpdateProgram-request-uri-ProgramName"></a>
The name of the Program.
Required: Yes

## Request Body
<a name="API_UpdateProgram_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [AdBreaks](#API_UpdateProgram_RequestSyntax) **   <a name="mediatailor-UpdateProgram-request-AdBreaks"></a>
The ad break configuration settings.
Type: Array of [AdBreak](API_AdBreak.md) objects
Required: No

 ** [AudienceMedia](#API_UpdateProgram_RequestSyntax) **   <a name="mediatailor-UpdateProgram-request-AudienceMedia"></a>
The list of AudienceMedia defined in program.
Type: Array of [AudienceMedia](API_AudienceMedia.md) objects
Required: No

 ** [ScheduleConfiguration](#API_UpdateProgram_RequestSyntax) **   <a name="mediatailor-UpdateProgram-request-ScheduleConfiguration"></a>
The schedule configuration settings.
Type: [UpdateProgramScheduleConfiguration](API_UpdateProgramScheduleConfiguration.md) object
Required: Yes

## Response Syntax
<a name="API_UpdateProgram_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "AdBreaks": [
      {
         "AdBreakMetadata": [
            {
               "Key": "string",
               "Value": "string"
            }
         ],
         "MessageType": "string",
         "OffsetMillis": number,
         "Slate": {
            "SourceLocationName": "string",
            "VodSourceName": "string"
         },
         "SpliceInsertMessage": {
            "AvailNum": number,
            "AvailsExpected": number,
            "SpliceEventId": number,
            "UniqueProgramId": number
         },
         "TimeSignalMessage": {
            "SegmentationDescriptors": [
               {
                  "SegmentationEventId": number,
                  "SegmentationTypeId": number,
                  "SegmentationUpid": "string",
                  "SegmentationUpidType": number,
                  "SegmentNum": number,
                  "SegmentsExpected": number,
                  "SubSegmentNum": number,
                  "SubSegmentsExpected": number
               }
            ]
         }
      }
   ],
   "Arn": "string",
   "AudienceMedia": [
      {
         "AlternateMedia": [
            {
               "AdBreaks": [
                  {
                     "AdBreakMetadata": [
                        {
                           "Key": "string",
                           "Value": "string"
                        }
                     ],
                     "MessageType": "string",
                     "OffsetMillis": number,
                     "Slate": {
                        "SourceLocationName": "string",
                        "VodSourceName": "string"
                     },
                     "SpliceInsertMessage": {
                        "AvailNum": number,
                        "AvailsExpected": number,
                        "SpliceEventId": number,
                        "UniqueProgramId": number
                     },
                     "TimeSignalMessage": {
                        "SegmentationDescriptors": [
                           {
                              "SegmentationEventId": number,
                              "SegmentationTypeId": number,
                              "SegmentationUpid": "string",
                              "SegmentationUpidType": number,
                              "SegmentNum": number,
                              "SegmentsExpected": number,
                              "SubSegmentNum": number,
                              "SubSegmentsExpected": number
                           }
                        ]
                     }
                  }
               ],
               "ClipRange": {
                  "EndOffsetMillis": number,
                  "StartOffsetMillis": number
               },
               "DurationMillis": number,
               "LiveSourceName": "string",
               "ScheduledStartTimeMillis": number,
               "SourceLocationName": "string",
               "VodSourceName": "string"
            }
         ],
         "Audience": "string"
      }
   ],
   "ChannelName": "string",
   "ClipRange": {
      "EndOffsetMillis": number,
      "StartOffsetMillis": number
   },
   "CreationTime": number,
   "DurationMillis": number,
   "LiveSourceName": "string",
   "ProgramName": "string",
   "ScheduledStartTime": number,
   "SourceLocationName": "string",
   "tags": {
      "string" : "string"
   },
   "VodSourceName": "string"
}
```

## Response Elements
<a name="API_UpdateProgram_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AdBreaks](#API_UpdateProgram_ResponseSyntax) **   <a name="mediatailor-UpdateProgram-response-AdBreaks"></a>
The ad break configuration settings.
Type: Array of [AdBreak](API_AdBreak.md) objects

 ** [Arn](#API_UpdateProgram_ResponseSyntax) **   <a name="mediatailor-UpdateProgram-response-Arn"></a>
The ARN to assign to the program.
Type: String

 ** [AudienceMedia](#API_UpdateProgram_ResponseSyntax) **   <a name="mediatailor-UpdateProgram-response-AudienceMedia"></a>
The list of AudienceMedia defined in program.
Type: Array of [AudienceMedia](API_AudienceMedia.md) objects

 ** [ChannelName](#API_UpdateProgram_ResponseSyntax) **   <a name="mediatailor-UpdateProgram-response-ChannelName"></a>
The name to assign to the channel for this program.
Type: String

 ** [ClipRange](#API_UpdateProgram_ResponseSyntax) **   <a name="mediatailor-UpdateProgram-response-ClipRange"></a>
The clip range configuration settings.
Type: [ClipRange](API_ClipRange.md) object

 ** [CreationTime](#API_UpdateProgram_ResponseSyntax) **   <a name="mediatailor-UpdateProgram-response-CreationTime"></a>
The time the program was created.
Type: Timestamp

 ** [DurationMillis](#API_UpdateProgram_ResponseSyntax) **   <a name="mediatailor-UpdateProgram-response-DurationMillis"></a>
The duration of the live program in milliseconds.
Type: Long

 ** [LiveSourceName](#API_UpdateProgram_ResponseSyntax) **   <a name="mediatailor-UpdateProgram-response-LiveSourceName"></a>
The name of the LiveSource for this Program.
Type: String

 ** [ProgramName](#API_UpdateProgram_ResponseSyntax) **   <a name="mediatailor-UpdateProgram-response-ProgramName"></a>
The name to assign to this program.
Type: String

 ** [ScheduledStartTime](#API_UpdateProgram_ResponseSyntax) **   <a name="mediatailor-UpdateProgram-response-ScheduledStartTime"></a>
The scheduled start time for this Program.
Type: Timestamp

 ** [SourceLocationName](#API_UpdateProgram_ResponseSyntax) **   <a name="mediatailor-UpdateProgram-response-SourceLocationName"></a>
The name to assign to the source location for this program.
Type: String

 ** [tags](#API_UpdateProgram_ResponseSyntax) **   <a name="mediatailor-UpdateProgram-response-tags"></a>
The tags assigned to the program. Tags are key-value pairs that you can associate with Amazon resources to help with organization, access control, and cost tracking. For more information, see [Tagging AWS Elemental MediaTailor Resources](https://docs.aws.amazon.com/mediatailor/latest/ug/tagging.html).
Type: String to string map

 ** [VodSourceName](#API_UpdateProgram_ResponseSyntax) **   <a name="mediatailor-UpdateProgram-response-VodSourceName"></a>
The name that's used to refer to a VOD source.
Type: String

## Errors
<a name="API_UpdateProgram_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_UpdateProgram_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mediatailor-2018-04-23/UpdateProgram)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mediatailor-2018-04-23/UpdateProgram)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediatailor-2018-04-23/UpdateProgram)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mediatailor-2018-04-23/UpdateProgram)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediatailor-2018-04-23/UpdateProgram)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mediatailor-2018-04-23/UpdateProgram)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mediatailor-2018-04-23/UpdateProgram)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mediatailor-2018-04-23/UpdateProgram)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/mediatailor-2018-04-23/UpdateProgram)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediatailor-2018-04-23/UpdateProgram)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaTailor. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediatailor` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
