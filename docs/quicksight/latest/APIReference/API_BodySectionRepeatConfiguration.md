---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_BodySectionRepeatConfiguration.html
---

# BodySectionRepeatConfiguration
<a name="API_BodySectionRepeatConfiguration"></a>

Describes the configurations that are required to declare a section as repeating.

## Contents
<a name="API_BodySectionRepeatConfiguration_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** DimensionConfigurations **   <a name="QS-Type-BodySectionRepeatConfiguration-DimensionConfigurations"></a>
List of `BodySectionRepeatDimensionConfiguration` values that describe the dataset column and constraints for the column used to repeat the contents of a section.
Type: Array of [BodySectionRepeatDimensionConfiguration](API_BodySectionRepeatDimensionConfiguration.md) objects
Array Members: Maximum number of 3 items.
Required: No

 ** NonRepeatingVisuals **   <a name="QS-Type-BodySectionRepeatConfiguration-NonRepeatingVisuals"></a>
List of visuals to exclude from repetition in repeating sections. The visuals will render identically, and ignore the repeating configurations in all repeating instances.
Type: Array of strings
Array Members: Maximum number of 20 items.
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\w\-]+`
Required: No

 ** PageBreakConfiguration **   <a name="QS-Type-BodySectionRepeatConfiguration-PageBreakConfiguration"></a>
Page break configuration to apply for each repeating instance.
Type: [BodySectionRepeatPageBreakConfiguration](API_BodySectionRepeatPageBreakConfiguration.md) object
Required: No

## See Also
<a name="API_BodySectionRepeatConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/BodySectionRepeatConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/BodySectionRepeatConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/BodySectionRepeatConfiguration)
