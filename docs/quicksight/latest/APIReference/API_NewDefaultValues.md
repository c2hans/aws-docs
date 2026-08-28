---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_NewDefaultValues.html
---

# NewDefaultValues
<a name="API_NewDefaultValues"></a>

The configuration that overrides the existing default values for a dataset parameter that is inherited from another dataset.

## Contents
<a name="API_NewDefaultValues_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** DateTimeStaticValues **   <a name="QS-Type-NewDefaultValues-DateTimeStaticValues"></a>
A list of static default values for a given date time parameter.
Type: Array of timestamps
Array Members: Minimum number of 1 item. Maximum number of 32 items.
Required: No

 ** DecimalStaticValues **   <a name="QS-Type-NewDefaultValues-DecimalStaticValues"></a>
A list of static default values for a given decimal parameter.
Type: Array of doubles
Array Members: Minimum number of 1 item. Maximum number of 32 items.
Required: No

 ** IntegerStaticValues **   <a name="QS-Type-NewDefaultValues-IntegerStaticValues"></a>
A list of static default values for a given integer parameter.
Type: Array of longs
Array Members: Minimum number of 1 item. Maximum number of 32 items.
Required: No

 ** StringStaticValues **   <a name="QS-Type-NewDefaultValues-StringStaticValues"></a>
A list of static default values for a given string parameter.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 32 items.
Length Constraints: Minimum length of 0. Maximum length of 512.
Required: No

## See Also
<a name="API_NewDefaultValues_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/NewDefaultValues)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/NewDefaultValues)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/NewDefaultValues)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
