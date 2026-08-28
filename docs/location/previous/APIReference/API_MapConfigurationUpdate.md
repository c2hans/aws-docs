---
source_url: https://docs.aws.amazon.com/location/previous/APIReference/API_MapConfigurationUpdate.html
---

# MapConfigurationUpdate
<a name="API_MapConfigurationUpdate"></a>

Specifies the political view for the style.

## Contents
<a name="API_MapConfigurationUpdate_Contents"></a>

 ** CustomLayers **   <a name="location-Type-MapConfigurationUpdate-CustomLayers"></a>
Specifies the custom layers for the style. Leave unset to not enable any custom layer, or, for styles that support custom layers, you can enable layer(s), such as POI layer for the VectorEsriNavigation style. Default is `unset`.
Not all map resources or styles support custom layers. See Custom Layers for more information.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[-._\w]+`
Required: No

 ** PoliticalView **   <a name="location-Type-MapConfigurationUpdate-PoliticalView"></a>
Specifies the political view for the style. Set to an empty string to not use a political view, or, for styles that support specific political views, you can choose a view, such as `IND` for the Indian view.
Not all map resources or styles support political view styles. See [Political views](https://docs.aws.amazon.com/location/previous/developerguide/map-concepts.html#political-views) for more information.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 3.
Pattern: `[A-Z]{3}$|^`
Required: No

## See Also
<a name="API_MapConfigurationUpdate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/location-2020-11-19/MapConfigurationUpdate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/location-2020-11-19/MapConfigurationUpdate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/location-2020-11-19/MapConfigurationUpdate)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
