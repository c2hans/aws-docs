---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_ConditionalFormattingCustomIconCondition.html
---

# ConditionalFormattingCustomIconCondition
<a name="API_ConditionalFormattingCustomIconCondition"></a>

Determines the custom condition for an icon set.

## Contents
<a name="API_ConditionalFormattingCustomIconCondition_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Expression **   <a name="QS-Type-ConditionalFormattingCustomIconCondition-Expression"></a>
The expression that determines the condition of the icon set.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Required: Yes

 ** IconOptions **   <a name="QS-Type-ConditionalFormattingCustomIconCondition-IconOptions"></a>
Custom icon options for an icon set.
Type: [ConditionalFormattingCustomIconOptions](API_ConditionalFormattingCustomIconOptions.md) object
Required: Yes

 ** Color **   <a name="QS-Type-ConditionalFormattingCustomIconCondition-Color"></a>
Determines the color of the icon.
Type: String
Pattern: `^#[A-F0-9]{6}$`
Required: No

 ** DisplayConfiguration **   <a name="QS-Type-ConditionalFormattingCustomIconCondition-DisplayConfiguration"></a>
Determines the icon display configuration.
Type: [ConditionalFormattingIconDisplayConfiguration](API_ConditionalFormattingIconDisplayConfiguration.md) object
Required: No

## See Also
<a name="API_ConditionalFormattingCustomIconCondition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/ConditionalFormattingCustomIconCondition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/ConditionalFormattingCustomIconCondition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/ConditionalFormattingCustomIconCondition)
