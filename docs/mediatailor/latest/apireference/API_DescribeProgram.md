---
source_url: https://docs.aws.amazon.com/mediatailor/latest/apireference/API_DescribeProgram.html
---

# DescribeProgram
<a name="API_DescribeProgram"></a>

Describes a program within a channel. For information about programs, see [Working with programs](https://docs.aws.amazon.com/mediatailor/latest/ug/channel-assembly-programs.html) in the *MediaTailor User Guide*.

## Request Syntax
<a name="API_DescribeProgram_RequestSyntax"></a>

```
GET /channel/{{ChannelName}}/program/{{ProgramName}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeProgram_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ChannelName](#API_DescribeProgram_RequestSyntax) **   <a name="mediatailor-DescribeProgram-request-uri-ChannelName"></a>
The name of the channel associated with this Program.
Required: Yes

 ** [ProgramName](#API_DescribeProgram_RequestSyntax) **   <a name="mediatailor-DescribeProgram-request-uri-ProgramName"></a>
The name of the program.
Required: Yes

## Request Body
<a name="API_DescribeProgram_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeProgram_ResponseSyntax"></a>

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
<a name="API_DescribeProgram_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AdBreaks](#API_DescribeProgram_ResponseSyntax) **   <a name="mediatailor-DescribeProgram-response-AdBreaks"></a>
The ad break configuration settings.
Type: Array of [AdBreak](API_AdBreak.md) objects

 ** [Arn](#API_DescribeProgram_ResponseSyntax) **   <a name="mediatailor-DescribeProgram-response-Arn"></a>
The ARN of the program.
Type: String

 ** [AudienceMedia](#API_DescribeProgram_ResponseSyntax) **   <a name="mediatailor-DescribeProgram-response-AudienceMedia"></a>
The list of AudienceMedia defined in program.
Type: Array of [AudienceMedia](API_AudienceMedia.md) objects

 ** [ChannelName](#API_DescribeProgram_ResponseSyntax) **   <a name="mediatailor-DescribeProgram-response-ChannelName"></a>
The name of the channel that the program belongs to.
Type: String

 ** [ClipRange](#API_DescribeProgram_ResponseSyntax) **   <a name="mediatailor-DescribeProgram-response-ClipRange"></a>
The clip range configuration settings.
Type: [ClipRange](API_ClipRange.md) object

 ** [CreationTime](#API_DescribeProgram_ResponseSyntax) **   <a name="mediatailor-DescribeProgram-response-CreationTime"></a>
The timestamp of when the program was created.
Type: Timestamp

 ** [DurationMillis](#API_DescribeProgram_ResponseSyntax) **   <a name="mediatailor-DescribeProgram-response-DurationMillis"></a>
The duration of the live program in milliseconds.
Type: Long

 ** [LiveSourceName](#API_DescribeProgram_ResponseSyntax) **   <a name="mediatailor-DescribeProgram-response-LiveSourceName"></a>
The name of the LiveSource for this Program.
Type: String

 ** [ProgramName](#API_DescribeProgram_ResponseSyntax) **   <a name="mediatailor-DescribeProgram-response-ProgramName"></a>
The name of the program.
Type: String

 ** [ScheduledStartTime](#API_DescribeProgram_ResponseSyntax) **   <a name="mediatailor-DescribeProgram-response-ScheduledStartTime"></a>
The date and time that the program is scheduled to start in ISO 8601 format and Coordinated Universal Time (UTC). For example, the value 2021-03-27T17:48:16.751Z represents March 27, 2021 at 17:48:16.751 UTC.
Type: Timestamp

 ** [SourceLocationName](#API_DescribeProgram_ResponseSyntax) **   <a name="mediatailor-DescribeProgram-response-SourceLocationName"></a>
The source location name.
Type: String

 ** [tags](#API_DescribeProgram_ResponseSyntax) **   <a name="mediatailor-DescribeProgram-response-tags"></a>
The tags assigned to the program. Tags are key-value pairs that you can associate with Amazon resources to help with organization, access control, and cost tracking. For more information, see [Tagging AWS Elemental MediaTailor Resources](https://docs.aws.amazon.com/mediatailor/latest/ug/tagging.html).
Type: String to string map

 ** [VodSourceName](#API_DescribeProgram_ResponseSyntax) **   <a name="mediatailor-DescribeProgram-response-VodSourceName"></a>
The name that's used to refer to a VOD source.
Type: String

## Errors
<a name="API_DescribeProgram_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_DescribeProgram_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mediatailor-2018-04-23/DescribeProgram)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mediatailor-2018-04-23/DescribeProgram)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediatailor-2018-04-23/DescribeProgram)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mediatailor-2018-04-23/DescribeProgram)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediatailor-2018-04-23/DescribeProgram)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mediatailor-2018-04-23/DescribeProgram)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mediatailor-2018-04-23/DescribeProgram)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mediatailor-2018-04-23/DescribeProgram)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/mediatailor-2018-04-23/DescribeProgram)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediatailor-2018-04-23/DescribeProgram)
