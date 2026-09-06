---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_SectionBasedLayoutConfiguration.html
---

# SectionBasedLayoutConfiguration
<a name="API_SectionBasedLayoutConfiguration"></a>

The configuration for a section-based layout.

## Contents
<a name="API_SectionBasedLayoutConfiguration_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** BodySections **   <a name="QS-Type-SectionBasedLayoutConfiguration-BodySections"></a>
A list of body section configurations.
Type: Array of [BodySectionConfiguration](API_BodySectionConfiguration.md) objects
Array Members: Maximum number of 28 items.
Required: Yes

 ** CanvasSizeOptions **   <a name="QS-Type-SectionBasedLayoutConfiguration-CanvasSizeOptions"></a>
The options for the canvas of a section-based layout.
Type: [SectionBasedLayoutCanvasSizeOptions](API_SectionBasedLayoutCanvasSizeOptions.md) object
Required: Yes

 ** FooterSections **   <a name="QS-Type-SectionBasedLayoutConfiguration-FooterSections"></a>
A list of footer section configurations.
Type: Array of [HeaderFooterSectionConfiguration](API_HeaderFooterSectionConfiguration.md) objects
Array Members: Maximum number of 1 item.
Required: Yes

 ** HeaderSections **   <a name="QS-Type-SectionBasedLayoutConfiguration-HeaderSections"></a>
A list of header section configurations.
Type: Array of [HeaderFooterSectionConfiguration](API_HeaderFooterSectionConfiguration.md) objects
Array Members: Maximum number of 1 item.
Required: Yes

## See Also
<a name="API_SectionBasedLayoutConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/SectionBasedLayoutConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/SectionBasedLayoutConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/SectionBasedLayoutConfiguration)
