---
source_url: https://docs.aws.amazon.com/mediapackage/latest/APIReference/API_CreateOriginEndpoint.html
---

# CreateOriginEndpoint
<a name="API_CreateOriginEndpoint"></a>

The endpoint is attached to a channel, and represents the output of the live content. You can associate multiple endpoints to a single channel. Each endpoint gives players and downstream CDNs (such as Amazon CloudFront) access to the content for playback. Content can't be served from a channel until it has an endpoint. You can create only one endpoint with each request.

## Request Syntax
<a name="API_CreateOriginEndpoint_RequestSyntax"></a>

```
POST /channelGroup/{{ChannelGroupName}}/channel/{{ChannelName}}/originEndpoint HTTP/1.1
x-amzn-client-token: {{ClientToken}}
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
   "OriginEndpointName": "{{string}}",
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
            "DrmSystems": [ "{{string}}" ],
            "EncryptionContractConfiguration": {
               "PresetSpeke20Audio": "{{string}}",
               "PresetSpeke20Video": "{{string}}"
            },
            "ResourceId": "{{string}}",
            "RoleArn": "{{string}}",
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
   "Tags": {
      "{{string}}" : "{{string}}"
   },
   "UriSeparator": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateOriginEndpoint_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ChannelGroupName](#API_CreateOriginEndpoint_RequestSyntax) **   <a name="mediapackage-CreateOriginEndpoint-request-uri-ChannelGroupName"></a>
The name that describes the channel group. The name is the primary identifier for the channel group, and must be unique for your account in the AWS Region.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9_-]+`
Required: Yes

 ** [ChannelName](#API_CreateOriginEndpoint_RequestSyntax) **   <a name="mediapackage-CreateOriginEndpoint-request-uri-ChannelName"></a>
The name that describes the channel. The name is the primary identifier for the channel, and must be unique for your account in the AWS Region and channel group.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9_-]+`
Required: Yes

 ** [ClientToken](#API_CreateOriginEndpoint_RequestSyntax) **   <a name="mediapackage-CreateOriginEndpoint-request-ClientToken"></a>
A unique, case-sensitive token that you provide to ensure the idempotency of the request.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[\S]+`

## Request Body
<a name="API_CreateOriginEndpoint_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ContainerType](#API_CreateOriginEndpoint_RequestSyntax) **   <a name="mediapackage-CreateOriginEndpoint-request-ContainerType"></a>
The type of container to attach to this origin endpoint. A container type is a file format that encapsulates one or more media streams, such as audio and video, into a single file. You can't change the container type after you create the endpoint.
Type: String
Valid Values: `TS | CMAF | ISM`
Required: Yes

 ** [DashManifests](#API_CreateOriginEndpoint_RequestSyntax) **   <a name="mediapackage-CreateOriginEndpoint-request-DashManifests"></a>
A DASH manifest configuration.
Type: Array of [CreateDashManifestConfiguration](API_CreateDashManifestConfiguration.md) objects
Required: No

 ** [Description](#API_CreateOriginEndpoint_RequestSyntax) **   <a name="mediapackage-CreateOriginEndpoint-request-Description"></a>
Enter any descriptive text that helps you to identify the origin endpoint.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** [ForceEndpointErrorConfiguration](#API_CreateOriginEndpoint_RequestSyntax) **   <a name="mediapackage-CreateOriginEndpoint-request-ForceEndpointErrorConfiguration"></a>
The failover settings for the endpoint.
Type: [ForceEndpointErrorConfiguration](API_ForceEndpointErrorConfiguration.md) object
Required: No

 ** [HlsManifests](#API_CreateOriginEndpoint_RequestSyntax) **   <a name="mediapackage-CreateOriginEndpoint-request-HlsManifests"></a>
An HTTP live streaming (HLS) manifest configuration.
Type: Array of [CreateHlsManifestConfiguration](API_CreateHlsManifestConfiguration.md) objects
Required: No

 ** [LowLatencyHlsManifests](#API_CreateOriginEndpoint_RequestSyntax) **   <a name="mediapackage-CreateOriginEndpoint-request-LowLatencyHlsManifests"></a>
A low-latency HLS manifest configuration.
Type: Array of [CreateLowLatencyHlsManifestConfiguration](API_CreateLowLatencyHlsManifestConfiguration.md) objects
Required: No

 ** [MssManifests](#API_CreateOriginEndpoint_RequestSyntax) **   <a name="mediapackage-CreateOriginEndpoint-request-MssManifests"></a>
A list of Microsoft Smooth Streaming (MSS) manifest configurations for the origin endpoint. You can configure multiple MSS manifests to provide different streaming experiences or to support different client requirements.
Type: Array of [CreateMssManifestConfiguration](API_CreateMssManifestConfiguration.md) objects
Required: No

 ** [OriginEndpointName](#API_CreateOriginEndpoint_RequestSyntax) **   <a name="mediapackage-CreateOriginEndpoint-request-OriginEndpointName"></a>
The name that describes the origin endpoint. The name is the primary identifier for the origin endpoint, and must be unique for your account in the AWS Region and channel. You can't use spaces in the name. You can't change the name after you create the endpoint.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9_-]+`
Required: Yes

 ** [Segment](#API_CreateOriginEndpoint_RequestSyntax) **   <a name="mediapackage-CreateOriginEndpoint-request-Segment"></a>
The segment configuration, including the segment name, duration, and other configuration values.
Type: [Segment](API_Segment.md) object
Required: No

 ** [StartoverWindowSeconds](#API_CreateOriginEndpoint_RequestSyntax) **   <a name="mediapackage-CreateOriginEndpoint-request-StartoverWindowSeconds"></a>
The size of the window (in seconds) to create a window of the live stream that's available for on-demand viewing. Viewers can start-over or catch-up on content that falls within the window. The maximum startover window is 1,209,600 seconds (14 days).
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 1209600.
Required: No

 ** [Tags](#API_CreateOriginEndpoint_RequestSyntax) **   <a name="mediapackage-CreateOriginEndpoint-request-Tags"></a>
A comma-separated list of tag key:value pairs that you define. For example:
 `"Key1": "Value1",`
 `"Key2": "Value2"`
Type: String to string map
Required: No

 ** [UriSeparator](#API_CreateOriginEndpoint_RequestSyntax) **   <a name="mediapackage-CreateOriginEndpoint-request-UriSeparator"></a>
The separator character to use in generated URIs for this origin endpoint. This setting applies to all manifest types on the endpoint. If you don't specify a value, the default is `UNDERSCORE`.
Type: String
Valid Values: `UNDERSCORE | HYPHEN`
Required: No

## Response Syntax
<a name="API_CreateOriginEndpoint_ResponseSyntax"></a>

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
            "DrmSystems": [ "string" ],
            "EncryptionContractConfiguration": {
               "PresetSpeke20Audio": "string",
               "PresetSpeke20Video": "string"
            },
            "ResourceId": "string",
            "RoleArn": "string",
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
   "Tags": {
      "string" : "string"
   },
   "UriSeparator": "string"
}
```

## Response Elements
<a name="API_CreateOriginEndpoint_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Arn](#API_CreateOriginEndpoint_ResponseSyntax) **   <a name="mediapackage-CreateOriginEndpoint-response-Arn"></a>
The Amazon Resource Name (ARN) associated with the resource.
Type: String

 ** [ChannelGroupName](#API_CreateOriginEndpoint_ResponseSyntax) **   <a name="mediapackage-CreateOriginEndpoint-response-ChannelGroupName"></a>
The name that describes the channel group. The name is the primary identifier for the channel group, and must be unique for your account in the AWS Region.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9_-]+`

 ** [ChannelName](#API_CreateOriginEndpoint_ResponseSyntax) **   <a name="mediapackage-CreateOriginEndpoint-response-ChannelName"></a>
The name that describes the channel. The name is the primary identifier for the channel, and must be unique for your account in the AWS Region and channel group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9_-]+`

 ** [ContainerType](#API_CreateOriginEndpoint_ResponseSyntax) **   <a name="mediapackage-CreateOriginEndpoint-response-ContainerType"></a>
The type of container attached to this origin endpoint.
Type: String
Valid Values: `TS | CMAF | ISM`

 ** [CreatedAt](#API_CreateOriginEndpoint_ResponseSyntax) **   <a name="mediapackage-CreateOriginEndpoint-response-CreatedAt"></a>
The date and time the origin endpoint was created.
Type: Timestamp

 ** [DashManifests](#API_CreateOriginEndpoint_ResponseSyntax) **   <a name="mediapackage-CreateOriginEndpoint-response-DashManifests"></a>
A DASH manifest configuration.
Type: Array of [GetDashManifestConfiguration](API_GetDashManifestConfiguration.md) objects

 ** [Description](#API_CreateOriginEndpoint_ResponseSyntax) **   <a name="mediapackage-CreateOriginEndpoint-response-Description"></a>
The description for your origin endpoint.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.

 ** [ETag](#API_CreateOriginEndpoint_ResponseSyntax) **   <a name="mediapackage-CreateOriginEndpoint-response-ETag"></a>
The current Entity Tag (ETag) associated with this resource. The entity tag can be used to safely make concurrent updates to the resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[\S]+`

 ** [ForceEndpointErrorConfiguration](#API_CreateOriginEndpoint_ResponseSyntax) **   <a name="mediapackage-CreateOriginEndpoint-response-ForceEndpointErrorConfiguration"></a>
The failover settings for the endpoint.
Type: [ForceEndpointErrorConfiguration](API_ForceEndpointErrorConfiguration.md) object

 ** [HlsManifests](#API_CreateOriginEndpoint_ResponseSyntax) **   <a name="mediapackage-CreateOriginEndpoint-response-HlsManifests"></a>
An HTTP live streaming (HLS) manifest configuration.
Type: Array of [GetHlsManifestConfiguration](API_GetHlsManifestConfiguration.md) objects

 ** [LowLatencyHlsManifests](#API_CreateOriginEndpoint_ResponseSyntax) **   <a name="mediapackage-CreateOriginEndpoint-response-LowLatencyHlsManifests"></a>
A low-latency HLS manifest configuration.
Type: Array of [GetLowLatencyHlsManifestConfiguration](API_GetLowLatencyHlsManifestConfiguration.md) objects

 ** [ModifiedAt](#API_CreateOriginEndpoint_ResponseSyntax) **   <a name="mediapackage-CreateOriginEndpoint-response-ModifiedAt"></a>
The date and time the origin endpoint was modified.
Type: Timestamp

 ** [MssManifests](#API_CreateOriginEndpoint_ResponseSyntax) **   <a name="mediapackage-CreateOriginEndpoint-response-MssManifests"></a>
The Microsoft Smooth Streaming (MSS) manifest configurations that were created for this origin endpoint.
Type: Array of [GetMssManifestConfiguration](API_GetMssManifestConfiguration.md) objects

 ** [OriginEndpointName](#API_CreateOriginEndpoint_ResponseSyntax) **   <a name="mediapackage-CreateOriginEndpoint-response-OriginEndpointName"></a>
The name that describes the origin endpoint. The name is the primary identifier for the origin endpoint, and and must be unique for your account in the AWS Region and channel.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9_-]+`

 ** [Segment](#API_CreateOriginEndpoint_ResponseSyntax) **   <a name="mediapackage-CreateOriginEndpoint-response-Segment"></a>
The segment configuration, including the segment name, duration, and other configuration values.
Type: [Segment](API_Segment.md) object

 ** [StartoverWindowSeconds](#API_CreateOriginEndpoint_ResponseSyntax) **   <a name="mediapackage-CreateOriginEndpoint-response-StartoverWindowSeconds"></a>
The size of the window (in seconds) to create a window of the live stream that's available for on-demand viewing. Viewers can start-over or catch-up on content that falls within the window.
Type: Integer

 ** [Tags](#API_CreateOriginEndpoint_ResponseSyntax) **   <a name="mediapackage-CreateOriginEndpoint-response-Tags"></a>
The comma-separated list of tag key:value pairs assigned to the origin endpoint.
Type: String to string map

 ** [UriSeparator](#API_CreateOriginEndpoint_ResponseSyntax) **   <a name="mediapackage-CreateOriginEndpoint-response-UriSeparator"></a>
The separator character used in generated URIs for this origin endpoint.
Type: String
Valid Values: `UNDERSCORE | HYPHEN`

## Errors
<a name="API_CreateOriginEndpoint_Errors"></a>

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
<a name="API_CreateOriginEndpoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mediapackagev2-2022-12-25/CreateOriginEndpoint)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mediapackagev2-2022-12-25/CreateOriginEndpoint)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediapackagev2-2022-12-25/CreateOriginEndpoint)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mediapackagev2-2022-12-25/CreateOriginEndpoint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediapackagev2-2022-12-25/CreateOriginEndpoint)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mediapackagev2-2022-12-25/CreateOriginEndpoint)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mediapackagev2-2022-12-25/CreateOriginEndpoint)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mediapackagev2-2022-12-25/CreateOriginEndpoint)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/mediapackagev2-2022-12-25/CreateOriginEndpoint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediapackagev2-2022-12-25/CreateOriginEndpoint)
