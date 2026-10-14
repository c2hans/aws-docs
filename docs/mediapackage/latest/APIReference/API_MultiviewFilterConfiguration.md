---
source_url: https://docs.aws.amazon.com/mediapackage/latest/APIReference/API_MultiviewFilterConfiguration.html
---

# MultiviewFilterConfiguration
<a name="API_MultiviewFilterConfiguration"></a>

The multiview combination for a pinned manifest. MediaPackage serves the manifest with this layout and these sources, so players request it without an `aws.multiview` query parameter.

If a request for a pinned manifest also includes an `aws.multiview` query parameter, MediaPackage rejects the request, even when that parameter requests the same combination.

## Contents
<a name="API_MultiviewFilterConfiguration_Contents"></a>

 ** Layout **   <a name="mediapackage-Type-MultiviewFilterConfiguration-Layout"></a>
The layout that MediaPackage uses to composite the tiles into a single output. This layout must be one of the `AvailableLayouts` of the channel that this origin endpoint is on.
Type: String
Valid Values: `LAYOUT_2EH | LAYOUT_2PL | LAYOUT_3EL | LAYOUT_3PL | LAYOUT_4E | LAYOUT_4PL`
Required: Yes

 ** Sources **   <a name="mediapackage-Type-MultiviewFilterConfiguration-Sources"></a>
The source channels to composite, in tile order. Each channel must be one of the `AvailableSources` of the channel that this origin endpoint is on, and the number of channels must equal the number of tiles in `Layout`.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9_-]+`
Required: Yes

## See Also
<a name="API_MultiviewFilterConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediapackagev2-2022-12-25/MultiviewFilterConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediapackagev2-2022-12-25/MultiviewFilterConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediapackagev2-2022-12-25/MultiviewFilterConfiguration)
