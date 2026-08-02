---
source_url: https://docs.aws.amazon.com/repostprivate/latest/APIReference/API_ChannelData.html
---

# ChannelData
<a name="API_ChannelData"></a>

A structure that contains some information about a channel in a private re:Post.

## Contents
<a name="API_ChannelData_Contents"></a>

 ** channelId **   <a name="repostprivate-Type-ChannelData-channelId"></a>
The unique ID of the private re:Post channel.
Type: String
Length Constraints: Fixed length of 24.
Required: Yes

 ** channelName **   <a name="repostprivate-Type-ChannelData-channelName"></a>
The name for the channel. This must be unique per private re:Post.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

 ** channelStatus **   <a name="repostprivate-Type-ChannelData-channelStatus"></a>
The status pf the channel.
Type: String
Valid Values: `CREATED | CREATING | CREATE_FAILED | DELETED | DELETING | DELETE_FAILED`
Required: Yes

 ** createDateTime **   <a name="repostprivate-Type-ChannelData-createDateTime"></a>
The date when the channel was created.
Type: Timestamp
Required: Yes

 ** groupCount **   <a name="repostprivate-Type-ChannelData-groupCount"></a>
The number of groups that are part of the channel.
Type: Integer
Required: Yes

 ** spaceId **   <a name="repostprivate-Type-ChannelData-spaceId"></a>
The unique ID of the private re:Post.
Type: String
Required: Yes

 ** userCount **   <a name="repostprivate-Type-ChannelData-userCount"></a>
The number of users that are part of the channel.
Type: Integer
Required: Yes

 ** channelDescription **   <a name="repostprivate-Type-ChannelData-channelDescription"></a>
A description for the channel. This is used only to help you identify this channel.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** deleteDateTime **   <a name="repostprivate-Type-ChannelData-deleteDateTime"></a>
The date when the channel was deleted.
Type: Timestamp
Required: No

## See Also
<a name="API_ChannelData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/repostspace-2022-05-13/ChannelData)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/repostspace-2022-05-13/ChannelData)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/repostspace-2022-05-13/ChannelData)
