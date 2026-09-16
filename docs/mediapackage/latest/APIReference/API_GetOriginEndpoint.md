---
source_url: https://docs.aws.amazon.com/mediapackage/latest/APIReference/API_GetOriginEndpoint.html
---

# GetOriginEndpoint
<a name="API_GetOriginEndpoint"></a>

Retrieves the specified origin endpoint that's configured in AWS Elemental MediaPackage to obtain its playback URL and to view the packaging settings that it's currently using.

## Request Syntax
<a name="API_GetOriginEndpoint_RequestSyntax"></a>

```
GET /channelGroup/{{ChannelGroupName}}/channel/{{ChannelName}}/originEndpoint/{{OriginEndpointName}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetOriginEndpoint_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ChannelGroupName](#API_GetOriginEndpoint_RequestSyntax) **   <a name="mediapackage-GetOriginEndpoint-request-uri-ChannelGroupName"></a>
The name that describes the channel group. The name is the primary identifier for the channel group, and must be unique for your account in the AWS Region.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9_-]+`
Required: Yes

 ** [ChannelName](#API_GetOriginEndpoint_RequestSyntax) **   <a name="mediapackage-GetOriginEndpoint-request-uri-ChannelName"></a>
The name that describes the channel. The name is the primary identifier for the channel, and must be unique for your account in the AWS Region and channel group.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9_-]+`
Required: Yes

 ** [OriginEndpointName](#API_GetOriginEndpoint_RequestSyntax) **   <a name="mediapackage-GetOriginEndpoint-request-uri-OriginEndpointName"></a>
The name that describes the origin endpoint. The name is the primary identifier for the origin endpoint, and and must be unique for your account in the AWS Region and channel.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9_-]+`
Required: Yes

## Request Body
<a name="API_GetOriginEndpoint_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetOriginEndpoint_ResponseSyntax"></a>

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
   "ResetAt": number,
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
<a name="API_GetOriginEndpoint_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Arn](#API_GetOriginEndpoint_ResponseSyntax) **   <a name="mediapackage-GetOriginEndpoint-response-Arn"></a>
The Amazon Resource Name (ARN) associated with the resource.
Type: String

 ** [ChannelGroupName](#API_GetOriginEndpoint_ResponseSyntax) **   <a name="mediapackage-GetOriginEndpoint-response-ChannelGroupName"></a>
The name that describes the channel group. The name is the primary identifier for the channel group, and must be unique for your account in the AWS Region.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9_-]+`

 ** [ChannelName](#API_GetOriginEndpoint_ResponseSyntax) **   <a name="mediapackage-GetOriginEndpoint-response-ChannelName"></a>
The name that describes the channel. The name is the primary identifier for the channel, and must be unique for your account in the AWS Region and channel group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9_-]+`

 ** [ContainerType](#API_GetOriginEndpoint_ResponseSyntax) **   <a name="mediapackage-GetOriginEndpoint-response-ContainerType"></a>
The type of container attached to this origin endpoint.
Type: String
Valid Values: `TS | CMAF | ISM`

 ** [CreatedAt](#API_GetOriginEndpoint_ResponseSyntax) **   <a name="mediapackage-GetOriginEndpoint-response-CreatedAt"></a>
The date and time the origin endpoint was created.
Type: Timestamp

 ** [DashManifests](#API_GetOriginEndpoint_ResponseSyntax) **   <a name="mediapackage-GetOriginEndpoint-response-DashManifests"></a>
A DASH manifest configuration.
Type: Array of [GetDashManifestConfiguration](API_GetDashManifestConfiguration.md) objects

 ** [Description](#API_GetOriginEndpoint_ResponseSyntax) **   <a name="mediapackage-GetOriginEndpoint-response-Description"></a>
The description for your origin endpoint.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.

 ** [ETag](#API_GetOriginEndpoint_ResponseSyntax) **   <a name="mediapackage-GetOriginEndpoint-response-ETag"></a>
The current Entity Tag (ETag) associated with this resource. The entity tag can be used to safely make concurrent updates to the resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[\S]+`

 ** [ForceEndpointErrorConfiguration](#API_GetOriginEndpoint_ResponseSyntax) **   <a name="mediapackage-GetOriginEndpoint-response-ForceEndpointErrorConfiguration"></a>
The failover settings for the endpoint.
Type: [ForceEndpointErrorConfiguration](API_ForceEndpointErrorConfiguration.md) object

 ** [HlsManifests](#API_GetOriginEndpoint_ResponseSyntax) **   <a name="mediapackage-GetOriginEndpoint-response-HlsManifests"></a>
An HTTP live streaming (HLS) manifest configuration.
Type: Array of [GetHlsManifestConfiguration](API_GetHlsManifestConfiguration.md) objects

 ** [LowLatencyHlsManifests](#API_GetOriginEndpoint_ResponseSyntax) **   <a name="mediapackage-GetOriginEndpoint-response-LowLatencyHlsManifests"></a>
A low-latency HLS manifest configuration.
Type: Array of [GetLowLatencyHlsManifestConfiguration](API_GetLowLatencyHlsManifestConfiguration.md) objects

 ** [ModifiedAt](#API_GetOriginEndpoint_ResponseSyntax) **   <a name="mediapackage-GetOriginEndpoint-response-ModifiedAt"></a>
The date and time the origin endpoint was modified.
Type: Timestamp

 ** [MssManifests](#API_GetOriginEndpoint_ResponseSyntax) **   <a name="mediapackage-GetOriginEndpoint-response-MssManifests"></a>
The Microsoft Smooth Streaming (MSS) manifest configurations associated with this origin endpoint.
Type: Array of [GetMssManifestConfiguration](API_GetMssManifestConfiguration.md) objects

 ** [OriginEndpointName](#API_GetOriginEndpoint_ResponseSyntax) **   <a name="mediapackage-GetOriginEndpoint-response-OriginEndpointName"></a>
The name that describes the origin endpoint. The name is the primary identifier for the origin endpoint, and and must be unique for your account in the AWS Region and channel.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9_-]+`

 ** [ResetAt](#API_GetOriginEndpoint_ResponseSyntax) **   <a name="mediapackage-GetOriginEndpoint-response-ResetAt"></a>
The time that the origin endpoint was last reset.
Type: Timestamp

 ** [Segment](#API_GetOriginEndpoint_ResponseSyntax) **   <a name="mediapackage-GetOriginEndpoint-response-Segment"></a>
The segment configuration, including the segment name, duration, and other configuration values.
Type: [Segment](API_Segment.md) object

 ** [StartoverWindowSeconds](#API_GetOriginEndpoint_ResponseSyntax) **   <a name="mediapackage-GetOriginEndpoint-response-StartoverWindowSeconds"></a>
The size of the window (in seconds) to create a window of the live stream that's available for on-demand viewing. Viewers can start-over or catch-up on content that falls within the window.
Type: Integer

 ** [Tags](#API_GetOriginEndpoint_ResponseSyntax) **   <a name="mediapackage-GetOriginEndpoint-response-Tags"></a>
The comma-separated list of tag key:value pairs assigned to the origin endpoint.
Type: String to string map

 ** [UriSeparator](#API_GetOriginEndpoint_ResponseSyntax) **   <a name="mediapackage-GetOriginEndpoint-response-UriSeparator"></a>
The separator character used in generated URIs for this origin endpoint.
Type: String
Valid Values: `UNDERSCORE | HYPHEN`

## Errors
<a name="API_GetOriginEndpoint_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access is denied because either you don't have permissions to perform the requested operation or MediaPackage is getting throttling errors with CDN authorization. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions. For more information, see Access Management in the IAM User Guide. Or, if you're using CDN authorization, you will receive this exception if MediaPackage receives a throttling error from Secrets Manager.
HTTP Status Code: 403

 ** InternalServerException **
Indicates that an error from the service occurred while trying to process a request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource doesn't exist.
 ** ResourceTypeNotFound **
The specified resource type wasn't found.
HTTP Status Code: 404

 ** ThrottlingException **
The request throughput limit was exceeded.
HTTP Status Code: 429

 ** ValidationException **
The input failed to meet the constraints specified by the AWS service.
 ** ValidationExceptionType **
The type of ValidationException.
HTTP Status Code: 400

## See Also
<a name="API_GetOriginEndpoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mediapackagev2-2022-12-25/GetOriginEndpoint)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mediapackagev2-2022-12-25/GetOriginEndpoint)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediapackagev2-2022-12-25/GetOriginEndpoint)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mediapackagev2-2022-12-25/GetOriginEndpoint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediapackagev2-2022-12-25/GetOriginEndpoint)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mediapackagev2-2022-12-25/GetOriginEndpoint)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mediapackagev2-2022-12-25/GetOriginEndpoint)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mediapackagev2-2022-12-25/GetOriginEndpoint)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/mediapackagev2-2022-12-25/GetOriginEndpoint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediapackagev2-2022-12-25/GetOriginEndpoint)
