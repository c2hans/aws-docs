---
source_url: https://docs.aws.amazon.com/mediapackage/latest/APIReference/API_MultiviewConfiguration.html
---

# MultiviewConfiguration
<a name="API_MultiviewConfiguration"></a>

The multiview configuration for a channel. A multiview channel composites video from several source channels into a single tiled output stream. Players receive one standard HLS or DASH stream instead of several separate streams. This setting is required when `InputType` is `MULTIVIEW`, and can't be set for any other input type.

## Contents
<a name="API_MultiviewConfiguration_Contents"></a>

 ** AvailableLayouts **   <a name="mediapackage-Type-MultiviewConfiguration-AvailableLayouts"></a>
The tile layouts that players can request from this multiview channel's origin endpoints. Only the layouts that you list here are available. Each layout must appear at most once.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 6 items.
Valid Values: `LAYOUT_2EH | LAYOUT_2PL | LAYOUT_3EL | LAYOUT_3PL | LAYOUT_4E | LAYOUT_4PL`
Required: Yes

 ** AvailableSources **   <a name="mediapackage-Type-MultiviewConfiguration-AvailableSources"></a>
The channels that players can use as tiles in this multiview channel's output. Each source channel must be in the same channel group as the multiview channel, and must have an `InputType` of `CMAF`. Only the channels that you list here are available as tiles.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9_-]+`
Required: Yes

## See Also
<a name="API_MultiviewConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediapackagev2-2022-12-25/MultiviewConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediapackagev2-2022-12-25/MultiviewConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediapackagev2-2022-12-25/MultiviewConfiguration)
