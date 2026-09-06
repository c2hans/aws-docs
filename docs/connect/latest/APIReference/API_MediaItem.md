---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_MediaItem.html
---

# MediaItem
<a name="API_MediaItem"></a>

Contains information about a media asset used in a workspace.

## Contents
<a name="API_MediaItem_Contents"></a>

 ** Source **   <a name="connect-Type-MediaItem-Source"></a>
The source URL or data for the media asset.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 533333.
Pattern: `.*\\S.*`
Required: No

 ** Type **   <a name="connect-Type-MediaItem-Type"></a>
The type of media. Valid values are: `IMAGE_LOGO_FAVICON` and `IMAGE_LOGO_HORIZONTAL`.
Type: String
Valid Values: `IMAGE_LOGO_LIGHT_FAVICON | IMAGE_LOGO_DARK_FAVICON | IMAGE_LOGO_LIGHT_HORIZONTAL | IMAGE_LOGO_DARK_HORIZONTAL`
Required: No

## See Also
<a name="API_MediaItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/MediaItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/MediaItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/MediaItem)
