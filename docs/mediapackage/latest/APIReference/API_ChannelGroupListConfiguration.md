---
source_url: https://docs.aws.amazon.com/mediapackage/latest/APIReference/API_ChannelGroupListConfiguration.html
---

# ChannelGroupListConfiguration
<a name="API_ChannelGroupListConfiguration"></a>

The configuration of the channel group.

## Contents
<a name="API_ChannelGroupListConfiguration_Contents"></a>

 ** Arn **   <a name="mediapackage-Type-ChannelGroupListConfiguration-Arn"></a>
The Amazon Resource Name (ARN) associated with the resource.
Type: String
Required: Yes

 ** ChannelGroupName **   <a name="mediapackage-Type-ChannelGroupListConfiguration-ChannelGroupName"></a>
The name that describes the channel group. The name is the primary identifier for the channel group, and must be unique for your account in the AWS Region.
Type: String
Required: Yes

 ** CreatedAt **   <a name="mediapackage-Type-ChannelGroupListConfiguration-CreatedAt"></a>
The date and time the channel group was created.
Type: Timestamp
Required: Yes

 ** ModifiedAt **   <a name="mediapackage-Type-ChannelGroupListConfiguration-ModifiedAt"></a>
The date and time the channel group was modified.
Type: Timestamp
Required: Yes

 ** Description **   <a name="mediapackage-Type-ChannelGroupListConfiguration-Description"></a>
Any descriptive information that you want to add to the channel group for future identification purposes.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

## See Also
<a name="API_ChannelGroupListConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediapackagev2-2022-12-25/ChannelGroupListConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediapackagev2-2022-12-25/ChannelGroupListConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediapackagev2-2022-12-25/ChannelGroupListConfiguration)
