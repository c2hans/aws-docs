---
source_url: https://docs.aws.amazon.com/mediapackage/latest/APIReference/API_OriginEndpointListConfiguration.html
---

# OriginEndpointListConfiguration
<a name="API_OriginEndpointListConfiguration"></a>

The configuration of the origin endpoint.

## Contents
<a name="API_OriginEndpointListConfiguration_Contents"></a>

 ** Arn **   <a name="mediapackage-Type-OriginEndpointListConfiguration-Arn"></a>
The Amazon Resource Name (ARN) associated with the resource.
Type: String
Required: Yes

 ** ChannelGroupName **   <a name="mediapackage-Type-OriginEndpointListConfiguration-ChannelGroupName"></a>
The name that describes the channel group. The name is the primary identifier for the channel group, and must be unique for your account in the AWS Region.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9_-]+`
Required: Yes

 ** ChannelName **   <a name="mediapackage-Type-OriginEndpointListConfiguration-ChannelName"></a>
The name that describes the channel. The name is the primary identifier for the channel, and must be unique for your account in the AWS Region and channel group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9_-]+`
Required: Yes

 ** ContainerType **   <a name="mediapackage-Type-OriginEndpointListConfiguration-ContainerType"></a>
The type of container attached to this origin endpoint. A container type is a file format that encapsulates one or more media streams, such as audio and video, into a single file.
Type: String
Valid Values: `TS | CMAF | ISM`
Required: Yes

 ** OriginEndpointName **   <a name="mediapackage-Type-OriginEndpointListConfiguration-OriginEndpointName"></a>
The name that describes the origin endpoint. The name is the primary identifier for the origin endpoint, and and must be unique for your account in the AWS Region and channel.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9_-]+`
Required: Yes

 ** CreatedAt **   <a name="mediapackage-Type-OriginEndpointListConfiguration-CreatedAt"></a>
The date and time the origin endpoint was created.
Type: Timestamp
Required: No

 ** DashManifests **   <a name="mediapackage-Type-OriginEndpointListConfiguration-DashManifests"></a>
A DASH manifest configuration.
Type: Array of [ListDashManifestConfiguration](API_ListDashManifestConfiguration.md) objects
Required: No

 ** Description **   <a name="mediapackage-Type-OriginEndpointListConfiguration-Description"></a>
Any descriptive information that you want to add to the origin endpoint for future identification purposes.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** ForceEndpointErrorConfiguration **   <a name="mediapackage-Type-OriginEndpointListConfiguration-ForceEndpointErrorConfiguration"></a>
The failover settings for the endpoint.
Type: [ForceEndpointErrorConfiguration](API_ForceEndpointErrorConfiguration.md) object
Required: No

 ** HlsManifests **   <a name="mediapackage-Type-OriginEndpointListConfiguration-HlsManifests"></a>
An HTTP live streaming (HLS) manifest configuration.
Type: Array of [ListHlsManifestConfiguration](API_ListHlsManifestConfiguration.md) objects
Required: No

 ** LowLatencyHlsManifests **   <a name="mediapackage-Type-OriginEndpointListConfiguration-LowLatencyHlsManifests"></a>
A low-latency HLS manifest configuration.
Type: Array of [ListLowLatencyHlsManifestConfiguration](API_ListLowLatencyHlsManifestConfiguration.md) objects
Required: No

 ** ModifiedAt **   <a name="mediapackage-Type-OriginEndpointListConfiguration-ModifiedAt"></a>
The date and time the origin endpoint was modified.
Type: Timestamp
Required: No

 ** MssManifests **   <a name="mediapackage-Type-OriginEndpointListConfiguration-MssManifests"></a>
A list of Microsoft Smooth Streaming (MSS) manifest configurations associated with the origin endpoint. Each configuration represents a different MSS streaming option available from this endpoint.
Type: Array of [ListMssManifestConfiguration](API_ListMssManifestConfiguration.md) objects
Required: No

 ** UriSeparator **   <a name="mediapackage-Type-OriginEndpointListConfiguration-UriSeparator"></a>
The separator character used in generated URIs for this origin endpoint.
Type: String
Valid Values: `UNDERSCORE | HYPHEN`
Required: No

## See Also
<a name="API_OriginEndpointListConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediapackagev2-2022-12-25/OriginEndpointListConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediapackagev2-2022-12-25/OriginEndpointListConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediapackagev2-2022-12-25/OriginEndpointListConfiguration)
