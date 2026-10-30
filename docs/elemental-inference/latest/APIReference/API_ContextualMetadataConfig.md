---
source_url: https://docs.aws.amazon.com/elemental-inference/latest/APIReference/API_ContextualMetadataConfig.html
---

# ContextualMetadataConfig
<a name="API_ContextualMetadataConfig"></a>

The output configuration settings for the contextual metadata feature. Use this structure when the feed output generates metadata that describes the media content.

## Contents
<a name="API_ContextualMetadataConfig_Contents"></a>

 ** extendedAnalysis **   <a name="elementalinference-Type-ContextualMetadataConfig-extendedAnalysis"></a>
Specifies whether Elemental Inference generates extended analysis of the media content for this output. Extended analysis identifies the people, environments, brands, and on-screen text in the media content. This setting is independent of `summaryGeneration`.
Valid values:
+ ENABLED (default) – Elemental Inference populates the people, environments, brands, and on-screen text fields.
+ DISABLED – Elemental Inference doesn't populate the people, environments, brands, and on-screen text fields.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

 ** summaryGeneration **   <a name="elementalinference-Type-ContextualMetadataConfig-summaryGeneration"></a>
Specifies whether Elemental Inference generates a descriptive summary of the media content for this output, along with the objects and actions that it detects. This setting is independent of `extendedAnalysis`.
Valid values:
+ ENABLED (default) – Elemental Inference populates the summary, objects, and actions fields, along with the IAB taxonomy and GARM suitability classifications.
+ DISABLED – Elemental Inference doesn't populate the summary, objects, and actions fields.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

## See Also
<a name="API_ContextualMetadataConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elementalinference-2018-11-14/ContextualMetadataConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elementalinference-2018-11-14/ContextualMetadataConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elementalinference-2018-11-14/ContextualMetadataConfig)
