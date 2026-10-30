---
source_url: https://docs.aws.amazon.com/elemental-inference/latest/APIReference/API_DataSourceConfiguration.html
---

# DataSourceConfiguration
<a name="API_DataSourceConfiguration"></a>

Contains the data source configuration for a clipping output. It identifies the fixture whose event data Elemental Inference maps onto the clipping metadata. It is used in the dataSourceConfiguration property of a ClippingConfig.

## Contents
<a name="API_DataSourceConfiguration_Contents"></a>

 ** fixtureId **   <a name="elementalinference-Type-DataSourceConfiguration-fixtureId"></a>
The ID of the fixture whose event data you want Elemental Inference to map onto this clipping output. The fixture should be the sports event in the source media that the feed is processing.
To obtain this ID, use the SearchFixtures operation to find the fixture, then use the fixtureId from the matching FixtureSummary.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

## See Also
<a name="API_DataSourceConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elementalinference-2018-11-14/DataSourceConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elementalinference-2018-11-14/DataSourceConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elementalinference-2018-11-14/DataSourceConfiguration)
