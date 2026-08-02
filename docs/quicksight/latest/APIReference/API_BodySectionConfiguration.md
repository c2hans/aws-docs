---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_BodySectionConfiguration.html
---

# BodySectionConfiguration
<a name="API_BodySectionConfiguration"></a>

The configuration of a body section.

## Contents
<a name="API_BodySectionConfiguration_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Content **   <a name="QS-Type-BodySectionConfiguration-Content"></a>
The configuration of content in a body section.
Type: [BodySectionContent](API_BodySectionContent.md) object
Required: Yes

 ** SectionId **   <a name="QS-Type-BodySectionConfiguration-SectionId"></a>
The unique identifier of a body section.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\w\-]+`
Required: Yes

 ** PageBreakConfiguration **   <a name="QS-Type-BodySectionConfiguration-PageBreakConfiguration"></a>
The configuration of a page break for a section.
Type: [SectionPageBreakConfiguration](API_SectionPageBreakConfiguration.md) object
Required: No

 ** RepeatConfiguration **   <a name="QS-Type-BodySectionConfiguration-RepeatConfiguration"></a>
Describes the configurations that are required to declare a section as repeating.
Type: [BodySectionRepeatConfiguration](API_BodySectionRepeatConfiguration.md) object
Required: No

 ** Style **   <a name="QS-Type-BodySectionConfiguration-Style"></a>
The style options of a body section.
Type: [SectionStyle](API_SectionStyle.md) object
Required: No

## See Also
<a name="API_BodySectionConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/BodySectionConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/BodySectionConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/BodySectionConfiguration)
