---
source_url: https://docs.aws.amazon.com/mediapackage/latest/APIReference/API_ChannelListConfiguration.html
---

# ChannelListConfiguration
<a name="API_ChannelListConfiguration"></a>

The configuration of the channel.

## Contents
<a name="API_ChannelListConfiguration_Contents"></a>

 ** Arn **   <a name="mediapackage-Type-ChannelListConfiguration-Arn"></a>
The Amazon Resource Name (ARN) associated with the resource.
Type: String
Required: Yes

 ** ChannelGroupName **   <a name="mediapackage-Type-ChannelListConfiguration-ChannelGroupName"></a>
The name that describes the channel group. The name is the primary identifier for the channel group, and must be unique for your account in the AWS Region.
Type: String
Required: Yes

 ** ChannelName **   <a name="mediapackage-Type-ChannelListConfiguration-ChannelName"></a>
The name that describes the channel. The name is the primary identifier for the channel, and must be unique for your account in the AWS Region and channel group.
Type: String
Required: Yes

 ** CreatedAt **   <a name="mediapackage-Type-ChannelListConfiguration-CreatedAt"></a>
The date and time the channel was created.
Type: Timestamp
Required: Yes

 ** ModifiedAt **   <a name="mediapackage-Type-ChannelListConfiguration-ModifiedAt"></a>
The date and time the channel was modified.
Type: Timestamp
Required: Yes

 ** Description **   <a name="mediapackage-Type-ChannelListConfiguration-Description"></a>
Any descriptive information that you want to add to the channel for future identification purposes.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** InputType **   <a name="mediapackage-Type-ChannelListConfiguration-InputType"></a>
The input type will be an immutable field which will be used to define whether the channel will allow CMAF ingest or HLS ingest. If unprovided, it will default to HLS to preserve current behavior.
The allowed values are:
+  `HLS` - The HLS streaming specification (which defines M3U8 manifests and TS segments).
+  `CMAF` - The DASH-IF CMAF Ingest specification (which defines CMAF segments with optional DASH manifests).
Type: String
Valid Values: `HLS | CMAF`
Required: No

 ** OutputLockingMode **   <a name="mediapackage-Type-ChannelListConfiguration-OutputLockingMode"></a>
The output locking mode configured for the channel.
The allowed values are:
+  `EPOCH_LOCKED` - The channel uses epoch-locked behavior with deterministic sequence numbering and fixed segment boundaries aligned to epoch time.
+  `NON_EPOCH_LOCKED` - The channel uses non-epoch-locked behavior with duration-based segment combining and monotonically increasing sequence numbers starting from 0.
Type: String
Valid Values: `EPOCH_LOCKED | NON_EPOCH_LOCKED`
Required: No

## See Also
<a name="API_ChannelListConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediapackagev2-2022-12-25/ChannelListConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediapackagev2-2022-12-25/ChannelListConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediapackagev2-2022-12-25/ChannelListConfiguration)
