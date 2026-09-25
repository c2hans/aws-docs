---
source_url: https://docs.aws.amazon.com/mediapackage/latest/APIReference/API_UpdateOriginEndpoint.html
---

# UpdateOriginEndpoint
<a name="API_UpdateOriginEndpoint"></a>

Update the specified origin endpoint. Edit the packaging preferences on an endpoint to optimize the viewing experience. You can't edit the name of the endpoint.

Any edits you make that impact the video output may not be reflected for a few minutes.

## Request Syntax
<a name="API_UpdateOriginEndpoint_RequestSyntax"></a>

```
PUT /channelGroup/{{ChannelGroupName}}/channel/{{ChannelName}}/originEndpoint/{{OriginEndpointName}} HTTP/1.1
x-amzn-update-if-match: {{ETag}}
Content-type: application/json

{
   "ContainerType": "{{string}}",
   "DashManifests": [
      {
         "AudioTimelinePattern": "{{string}}",
         "AvailabilityStartTimeConfiguration": { ... },
         "BaseUrls": [
            {
               "DvbPriority": {{number}},
               "DvbWeight": {{number}},
               "ServiceLocation": "{{string}}",
               "Url": "{{string}}"
            }
         ],
         "Compactness": "{{string}}",
         "DrmSignaling": "{{string}}",
         "DvbSettings": {
            "ErrorMetrics": [
               {
                  "Probability": {{number}},
                  "ReportingUrl": "{{string}}"
               }
            ],
            "FontDownload": {
               "FontFamily": "{{string}}",
               "MimeType": "{{string}}",
               "Url": "{{string}}"
            }
         },
         "FilterConfiguration": {
            "ClipStartTime": {{number}},
            "DrmSettings": "{{string}}",
            "End": {{number}},
            "ManifestFilter": "{{string}}",
            "Start": {{number}},
            "TimeDelaySeconds": {{number}}
         },
         "ManifestName": "{{string}}",
         "ManifestWindowSeconds": {{number}},
         "MinBufferTimeSeconds": {{number}},
         "MinUpdatePeriodSeconds": {{number}},
         "PeriodTriggers": [ "{{string}}" ],
         "Profiles": [ "{{string}}" ],
         "ProgramInformation": {
            "Copyright": "{{string}}",
            "LanguageCode": "{{string}}",
            "MoreInformationUrl": "{{string}}",
            "Source": "{{string}}",
            "Title": "{{string}}"
         },
         "ScteDash": {
            "AdMarkerDash": "{{string}}",
            "ScteInManifests": "{{string}}"
         },
         "SegmentTemplateFormat": "{{string}}",
         "SubtitleConfiguration": {
            "TtmlConfiguration": {
               "TtmlProfile": "{{string}}"
            }
         },
         "SuggestedPresentationDelaySeconds": {{number}},
         "UriPathType": "{{string}}",
         "UtcTiming": {
            "TimingMode": "{{string}}",
            "TimingSource": "{{string}}"
         }
      }
   ],
   "Description": "{{string}}",
   "ForceEndpointErrorConfiguration": {
      "EndpointErrorConditions": [ "{{string}}" ]
   },
   "HlsManifests": [
      {
         "ChildManifestName": "{{string}}",
         "FilterConfiguration": {
            "ClipStartTime": {{number}},
            "DrmSettings": "{{string}}",
            "End": {{number}},
            "ManifestFilter": "{{string}}",
            "Start": {{number}},
            "TimeDelaySeconds": {{number}}
         },
         "ManifestName": "{{string}}",
         "ManifestWindowSeconds": {{number}},
         "ProgramDateTimeIntervalSeconds": {{number}},
         "ScteHls": {
            "AdMarkerHls": "{{string}}",
            "ScteInManifests": "{{string}}"
         },
         "StartTag": {
            "Precise": {{boolean}},
            "TimeOffset": {{number}}
         },
         "UriPathType": "{{string}}",
         "UrlEncodeChildManifest": {{boolean}}
      }
   ],
   "LowLatencyHlsManifests": [
      {
         "ChildManifestName": "{{string}}",
         "FilterConfiguration": {
            "ClipStartTime": {{number}},
            "DrmSettings": "{{string}}",
            "End": {{number}},
            "ManifestFilter": "{{string}}",
            "Start": {{number}},
            "TimeDelaySeconds": {{number}}
         },
         "ManifestName": "{{string}}",
         "ManifestWindowSeconds": {{number}},
         "ProgramDateTimeIntervalSeconds": {{number}},
         "ScteHls": {
            "AdMarkerHls": "{{string}}",
            "ScteInManifests": "{{string}}"
         },
         "StartTag": {
            "Precise": {{boolean}},
            "TimeOffset": {{number}}
         },
         "UriPathType": "{{string}}",
         "UrlEncodeChildManifest": {{boolean}}
      }
   ],
   "MssManifests": [
      {
         "FilterConfiguration": {
            "ClipStartTime": {{number}},
            "DrmSettings": "{{string}}",
            "End": {{number}},
            "ManifestFilter": "{{string}}",
            "Start": {{number}},
            "TimeDelaySeconds": {{number}}
         },
         "ManifestLayout": "{{string}}",
         "ManifestName": "{{string}}",
         "ManifestWindowSeconds": {{number}}
      }
   ],
   "Segment": {
      "Encryption": {
         "CmafExcludeSegmentDrmMetadata": {{boolean}},
         "ConstantInitializationVector": "{{string}}",
         "EncryptionMethod": {
            "CmafEncryptionMethod": "{{string}}",
            "IsmEncryptionMethod": "{{string}}",
            "TsEncryptionMethod": "{{string}}"
         },
         "KeyRotationIntervalSeconds": {{number}},
         "SpekeKeyProvider": {
            "CertificateArn": "{{string}}",
            "ContentKeyPeriodConfiguration": {
               "ContentKeyPeriodTiming": "{{string}}"
            },
            "DrmSystems": [ "{{string}}" ],
            "EncryptionContractConfiguration": {
               "PresetSpeke20Audio": "{{string}}",
               "PresetSpeke20Video": "{{string}}"
            },
            "ResourceId": "{{string}}",
            "RoleArn": "{{string}}",
            "SpekeVersion": "{{string}}",
            "Url": "{{string}}"
         }
      },
      "IncludeIframeOnlyStreams": {{boolean}},
      "OutputTimestampMode": "{{string}}",
      "Scte": {
         "CustomAdTypes": [ "{{string}}" ],
         "ScteFilter": [ "{{string}}" ],
         "ScteInSegments": "{{string}}"
      },
      "SegmentDurationSeconds": {{number}},
      "SegmentName": "{{string}}",
      "TsIncludeDvbSubtitles": {{boolean}},
      "TsUseAudioRenditionGroup": {{boolean}}
   },
   "StartoverWindowSeconds": {{number}},
   "StreamNameOutputMode": "{{string}}",
   "UriSeparator": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateOriginEndpoint_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ChannelGroupName](#API_UpdateOriginEndpoint_RequestSyntax) **   <a name="mediapackage-UpdateOriginEndpoint-request-uri-ChannelGroupName"></a>
The name that describes the channel group. The name is the primary identifier for the channel group, and must be unique for your account in the AWS Region.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9_-]+`
Required: Yes

 ** [ChannelName](#API_UpdateOriginEndpoint_RequestSyntax) **   <a name="mediapackage-UpdateOriginEndpoint-request-uri-ChannelName"></a>
The name that describes the channel. The name is the primary identifier for the channel, and must be unique for your account in the AWS Region and channel group.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9_-]+`
Required: Yes

 ** [ETag](#API_UpdateOriginEndpoint_RequestSyntax) **   <a name="mediapackage-UpdateOriginEndpoint-request-ETag"></a>
The expected current Entity Tag (ETag) for the resource. If the specified ETag does not match the resource's current entity tag, the update request will be rejected.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[\S]+`

 ** [OriginEndpointName](#API_UpdateOriginEndpoint_RequestSyntax) **   <a name="mediapackage-UpdateOriginEndpoint-request-uri-OriginEndpointName"></a>
The name that describes the origin endpoint. The name is the primary identifier for the origin endpoint, and and must be unique for your account in the AWS Region and channel.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9_-]+`
Required: Yes

## Request Body
<a name="API_UpdateOriginEndpoint_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ContainerType](#API_UpdateOriginEndpoint_RequestSyntax) **   <a name="mediapackage-UpdateOriginEndpoint-request-ContainerType"></a>
The type of container attached to this origin endpoint. A container type is a file format that encapsulates one or more media streams, such as audio and video, into a single file.
Type: String
Valid Values: `TS | CMAF | ISM`
Required: Yes

 ** [DashManifests](#API_UpdateOriginEndpoint_RequestSyntax) **   <a name="mediapackage-UpdateOriginEndpoint-request-DashManifests"></a>
A DASH manifest configuration.
Type: Array of [CreateDashManifestConfiguration](API_CreateDashManifestConfiguration.md) objects
Required: No

 ** [Description](#API_UpdateOriginEndpoint_RequestSyntax) **   <a name="mediapackage-UpdateOriginEndpoint-request-Description"></a>
Any descriptive information that you want to add to the origin endpoint for future identification purposes.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** [ForceEndpointErrorConfiguration](#API_UpdateOriginEndpoint_RequestSyntax) **   <a name="mediapackage-UpdateOriginEndpoint-request-ForceEndpointErrorConfiguration"></a>
The failover settings for the endpoint.
Type: [ForceEndpointErrorConfiguration](API_ForceEndpointErrorConfiguration.md) object
Required: No

 ** [HlsManifests](#API_UpdateOriginEndpoint_RequestSyntax) **   <a name="mediapackage-UpdateOriginEndpoint-request-HlsManifests"></a>
An HTTP live streaming (HLS) manifest configuration.
Type: Array of [CreateHlsManifestConfiguration](API_CreateHlsManifestConfiguration.md) objects
Required: No

 ** [LowLatencyHlsManifests](#API_UpdateOriginEndpoint_RequestSyntax) **   <a name="mediapackage-UpdateOriginEndpoint-request-LowLatencyHlsManifests"></a>
A low-latency HLS manifest configuration.
Type: Array of [CreateLowLatencyHlsManifestConfiguration](API_CreateLowLatencyHlsManifestConfiguration.md) objects
Required: No

 ** [MssManifests](#API_UpdateOriginEndpoint_RequestSyntax) **   <a name="mediapackage-UpdateOriginEndpoint-request-MssManifests"></a>
A list of Microsoft Smooth Streaming (MSS) manifest configurations to update for the origin endpoint. This replaces the existing MSS manifest configurations.
Type: Array of [CreateMssManifestConfiguration](API_CreateMssManifestConfiguration.md) objects
Required: No

 ** [Segment](#API_UpdateOriginEndpoint_RequestSyntax) **   <a name="mediapackage-UpdateOriginEndpoint-request-Segment"></a>
The segment configuration, including the segment name, duration, and other configuration values.
Type: [Segment](API_Segment.md) object
Required: No

 ** [StartoverWindowSeconds](#API_UpdateOriginEndpoint_RequestSyntax) **   <a name="mediapackage-UpdateOriginEndpoint-request-StartoverWindowSeconds"></a>
The size of the window (in seconds) to create a window of the live stream that's available for on-demand viewing. Viewers can start-over or catch-up on content that falls within the window. The maximum startover window is 1,209,600 seconds (14 days).
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 1209600.
Required: No

 ** [StreamNameOutputMode](#API_UpdateOriginEndpoint_RequestSyntax) **   <a name="mediapackage-UpdateOriginEndpoint-request-StreamNameOutputMode"></a>
The output mode for stream names in egress manifests. If you provide a value, it must match the current value. You can't change the stream name output mode after you create the endpoint.
Type: String
Valid Values: `INDEX | PASSTHROUGH_NAME`
Required: No

 ** [UriSeparator](#API_UpdateOriginEndpoint_RequestSyntax) **   <a name="mediapackage-UpdateOriginEndpoint-request-UriSeparator"></a>
The separator character to use in generated URIs for this origin endpoint. This setting applies to all manifest types on the endpoint. If you don't specify a value in the update request, the current value is preserved.
Type: String
Valid Values: `UNDERSCORE | HYPHEN`
Required: No

## Response Syntax
<a name="API_UpdateOriginEndpoint_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Arn": "string",
   "ChannelGroupName": "string",
   "ChannelName": "string",
   "ContainerType": "string",
   "CreatedAt": number,
   "DashManifests": [
      {
         "AudioTimelinePattern": "string",
         "AvailabilityStartTimeConfiguration": { ... },
         "BaseUrls": [
            {
               "DvbPriority": number,
               "DvbWeight": number,
               "ServiceLocation": "string",
               "Url": "string"
            }
         ],
         "Compactness": "string",
         "DrmSignaling": "string",
         "DvbSettings": {
            "ErrorMetrics": [
               {
                  "Probability": number,
                  "ReportingUrl": "string"
               }
            ],
            "FontDownload": {
               "FontFamily": "string",
               "MimeType": "string",
               "Url": "string"
            }
         },
         "FilterConfiguration": {
            "ClipStartTime": number,
            "DrmSettings": "string",
            "End": number,
            "ManifestFilter": "string",
            "Start": number,
            "TimeDelaySeconds": number
         },
         "ManifestName": "string",
         "ManifestWindowSeconds": number,
         "MinBufferTimeSeconds": number,
         "MinUpdatePeriodSeconds": number,
         "PeriodTriggers": [ "string" ],
         "Profiles": [ "string" ],
         "ProgramInformation": {
            "Copyright": "string",
            "LanguageCode": "string",
            "MoreInformationUrl": "string",
            "Source": "string",
            "Title": "string"
         },
         "ScteDash": {
            "AdMarkerDash": "string",
            "ScteInManifests": "string"
         },
         "SegmentTemplateFormat": "string",
         "SubtitleConfiguration": {
            "TtmlConfiguration": {
               "TtmlProfile": "string"
            }
         },
         "SuggestedPresentationDelaySeconds": number,
         "UriPathType": "string",
         "Url": "string",
         "UtcTiming": {
            "TimingMode": "string",
            "TimingSource": "string"
         }
      }
   ],
   "Description": "string",
   "ETag": "string",
   "ForceEndpointErrorConfiguration": {
      "EndpointErrorConditions": [ "string" ]
   },
   "HlsManifests": [
      {
         "ChildManifestName": "string",
         "FilterConfiguration": {
            "ClipStartTime": number,
            "DrmSettings": "string",
            "End": number,
            "ManifestFilter": "string",
            "Start": number,
            "TimeDelaySeconds": number
         },
         "ManifestName": "string",
         "ManifestWindowSeconds": number,
         "ProgramDateTimeIntervalSeconds": number,
         "ScteHls": {
            "AdMarkerHls": "string",
            "ScteInManifests": "string"
         },
         "StartTag": {
            "Precise": boolean,
            "TimeOffset": number
         },
         "UriPathType": "string",
         "Url": "string",
         "UrlEncodeChildManifest": boolean
      }
   ],
   "LowLatencyHlsManifests": [
      {
         "ChildManifestName": "string",
         "FilterConfiguration": {
            "ClipStartTime": number,
            "DrmSettings": "string",
            "End": number,
            "ManifestFilter": "string",
            "Start": number,
            "TimeDelaySeconds": number
         },
         "ManifestName": "string",
         "ManifestWindowSeconds": number,
         "ProgramDateTimeIntervalSeconds": number,
         "ScteHls": {
            "AdMarkerHls": "string",
            "ScteInManifests": "string"
         },
         "StartTag": {
            "Precise": boolean,
            "TimeOffset": number
         },
         "UriPathType": "string",
         "Url": "string",
         "UrlEncodeChildManifest": boolean
      }
   ],
   "ModifiedAt": number,
   "MssManifests": [
      {
         "FilterConfiguration": {
            "ClipStartTime": number,
            "DrmSettings": "string",
            "End": number,
            "ManifestFilter": "string",
            "Start": number,
            "TimeDelaySeconds": number
         },
         "ManifestLayout": "string",
         "ManifestName": "string",
         "ManifestWindowSeconds": number,
         "Url": "string"
      }
   ],
   "OriginEndpointName": "string",
   "Segment": {
      "Encryption": {
         "CmafExcludeSegmentDrmMetadata": boolean,
         "ConstantInitializationVector": "string",
         "EncryptionMethod": {
            "CmafEncryptionMethod": "string",
            "IsmEncryptionMethod": "string",
            "TsEncryptionMethod": "string"
         },
         "KeyRotationIntervalSeconds": number,
         "SpekeKeyProvider": {
            "CertificateArn": "string",
            "ContentKeyPeriodConfiguration": {
               "ContentKeyPeriodTiming": "string"
            },
            "DrmSystems": [ "string" ],
            "EncryptionContractConfiguration": {
               "PresetSpeke20Audio": "string",
               "PresetSpeke20Video": "string"
            },
            "ResourceId": "string",
            "RoleArn": "string",
            "SpekeVersion": "string",
            "Url": "string"
         }
      },
      "IncludeIframeOnlyStreams": boolean,
      "OutputTimestampMode": "string",
      "Scte": {
         "CustomAdTypes": [ "string" ],
         "ScteFilter": [ "string" ],
         "ScteInSegments": "string"
      },
      "SegmentDurationSeconds": number,
      "SegmentName": "string",
      "TsIncludeDvbSubtitles": boolean,
      "TsUseAudioRenditionGroup": boolean
   },
   "StartoverWindowSeconds": number,
   "StreamNameOutputMode": "string",
   "tags": {
      "string" : "string"
   },
   "UriSeparator": "string"
}
```

## Response Elements
<a name="API_UpdateOriginEndpoint_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Arn](#API_UpdateOriginEndpoint_ResponseSyntax) **   <a name="mediapackage-UpdateOriginEndpoint-response-Arn"></a>
The ARN associated with the resource.
Type: String

 ** [ChannelGroupName](#API_UpdateOriginEndpoint_ResponseSyntax) **   <a name="mediapackage-UpdateOriginEndpoint-response-ChannelGroupName"></a>
The name that describes the channel group. The name is the primary identifier for the channel group, and must be unique for your account in the AWS Region.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9_-]+`

 ** [ChannelName](#API_UpdateOriginEndpoint_ResponseSyntax) **   <a name="mediapackage-UpdateOriginEndpoint-response-ChannelName"></a>
The name that describes the channel. The name is the primary identifier for the channel, and must be unique for your account in the AWS Region and channel group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9_-]+`

 ** [ContainerType](#API_UpdateOriginEndpoint_ResponseSyntax) **   <a name="mediapackage-UpdateOriginEndpoint-response-ContainerType"></a>
The type of container attached to this origin endpoint.
Type: String
Valid Values: `TS | CMAF | ISM`

 ** [CreatedAt](#API_UpdateOriginEndpoint_ResponseSyntax) **   <a name="mediapackage-UpdateOriginEndpoint-response-CreatedAt"></a>
The date and time the origin endpoint was created.
Type: Timestamp

 ** [DashManifests](#API_UpdateOriginEndpoint_ResponseSyntax) **   <a name="mediapackage-UpdateOriginEndpoint-response-DashManifests"></a>
A DASH manifest configuration.
Type: Array of [GetDashManifestConfiguration](API_GetDashManifestConfiguration.md) objects

 ** [Description](#API_UpdateOriginEndpoint_ResponseSyntax) **   <a name="mediapackage-UpdateOriginEndpoint-response-Description"></a>
The description of the origin endpoint.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.

 ** [ETag](#API_UpdateOriginEndpoint_ResponseSyntax) **   <a name="mediapackage-UpdateOriginEndpoint-response-ETag"></a>
The current Entity Tag (ETag) associated with this resource. The entity tag can be used to safely make concurrent updates to the resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[\S]+`

 ** [ForceEndpointErrorConfiguration](#API_UpdateOriginEndpoint_ResponseSyntax) **   <a name="mediapackage-UpdateOriginEndpoint-response-ForceEndpointErrorConfiguration"></a>
The failover settings for the endpoint.
Type: [ForceEndpointErrorConfiguration](API_ForceEndpointErrorConfiguration.md) object

 ** [HlsManifests](#API_UpdateOriginEndpoint_ResponseSyntax) **   <a name="mediapackage-UpdateOriginEndpoint-response-HlsManifests"></a>
An HTTP live streaming (HLS) manifest configuration.
Type: Array of [GetHlsManifestConfiguration](API_GetHlsManifestConfiguration.md) objects

 ** [LowLatencyHlsManifests](#API_UpdateOriginEndpoint_ResponseSyntax) **   <a name="mediapackage-UpdateOriginEndpoint-response-LowLatencyHlsManifests"></a>
A low-latency HLS manifest configuration.
Type: Array of [GetLowLatencyHlsManifestConfiguration](API_GetLowLatencyHlsManifestConfiguration.md) objects

 ** [ModifiedAt](#API_UpdateOriginEndpoint_ResponseSyntax) **   <a name="mediapackage-UpdateOriginEndpoint-response-ModifiedAt"></a>
The date and time the origin endpoint was modified.
Type: Timestamp

 ** [MssManifests](#API_UpdateOriginEndpoint_ResponseSyntax) **   <a name="mediapackage-UpdateOriginEndpoint-response-MssManifests"></a>
The updated Microsoft Smooth Streaming (MSS) manifest configurations for this origin endpoint.
Type: Array of [GetMssManifestConfiguration](API_GetMssManifestConfiguration.md) objects

 ** [OriginEndpointName](#API_UpdateOriginEndpoint_ResponseSyntax) **   <a name="mediapackage-UpdateOriginEndpoint-response-OriginEndpointName"></a>
The name that describes the origin endpoint. The name is the primary identifier for the origin endpoint, and and must be unique for your account in the AWS Region and channel.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9_-]+`

 ** [Segment](#API_UpdateOriginEndpoint_ResponseSyntax) **   <a name="mediapackage-UpdateOriginEndpoint-response-Segment"></a>
The segment configuration, including the segment name, duration, and other configuration values.
Type: [Segment](API_Segment.md) object

 ** [StartoverWindowSeconds](#API_UpdateOriginEndpoint_ResponseSyntax) **   <a name="mediapackage-UpdateOriginEndpoint-response-StartoverWindowSeconds"></a>
The size of the window (in seconds) to create a window of the live stream that's available for on-demand viewing. Viewers can start-over or catch-up on content that falls within the window.
Type: Integer

 ** [StreamNameOutputMode](#API_UpdateOriginEndpoint_ResponseSyntax) **   <a name="mediapackage-UpdateOriginEndpoint-response-StreamNameOutputMode"></a>
The output mode for stream names in egress manifests for this origin endpoint.
Type: String
Valid Values: `INDEX | PASSTHROUGH_NAME`

 ** [tags](#API_UpdateOriginEndpoint_ResponseSyntax) **   <a name="mediapackage-UpdateOriginEndpoint-response-tags"></a>
The comma-separated list of tag key:value pairs assigned to the origin endpoint.
Type: String to string map

 ** [UriSeparator](#API_UpdateOriginEndpoint_ResponseSyntax) **   <a name="mediapackage-UpdateOriginEndpoint-response-UriSeparator"></a>
The separator character used in generated URIs for this origin endpoint.
Type: String
Valid Values: `UNDERSCORE | HYPHEN`

## Errors
<a name="API_UpdateOriginEndpoint_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access is denied because either you don't have permissions to perform the requested operation or MediaPackage is getting throttling errors with CDN authorization. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions. For more information, see Access Management in the IAM User Guide. Or, if you're using CDN authorization, you will receive this exception if MediaPackage receives a throttling error from Secrets Manager.
HTTP Status Code: 403

 ** ConflictException **
Updating or deleting this resource can cause an inconsistent state.
 ** ConflictExceptionType **
The type of ConflictException.
HTTP Status Code: 409

 ** InternalServerException **
Indicates that an error from the service occurred while trying to process a request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource doesn't exist.
 ** ResourceTypeNotFound **
The specified resource type wasn't found.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
The request would cause a service quota to be exceeded.
HTTP Status Code: 402

 ** ThrottlingException **
The request throughput limit was exceeded.
HTTP Status Code: 429

 ** ValidationException **
The input failed to meet the constraints specified by the AWS service.
 ** ValidationExceptionType **
The type of ValidationException.
HTTP Status Code: 400

## See Also
<a name="API_UpdateOriginEndpoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mediapackagev2-2022-12-25/UpdateOriginEndpoint)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mediapackagev2-2022-12-25/UpdateOriginEndpoint)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediapackagev2-2022-12-25/UpdateOriginEndpoint)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mediapackagev2-2022-12-25/UpdateOriginEndpoint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediapackagev2-2022-12-25/UpdateOriginEndpoint)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mediapackagev2-2022-12-25/UpdateOriginEndpoint)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mediapackagev2-2022-12-25/UpdateOriginEndpoint)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mediapackagev2-2022-12-25/UpdateOriginEndpoint)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/mediapackagev2-2022-12-25/UpdateOriginEndpoint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediapackagev2-2022-12-25/UpdateOriginEndpoint)
