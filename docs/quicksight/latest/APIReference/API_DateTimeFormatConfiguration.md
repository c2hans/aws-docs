---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DateTimeFormatConfiguration.html
---

# DateTimeFormatConfiguration
<a name="API_DateTimeFormatConfiguration"></a>

Formatting configuration for `DateTime` fields.

## Contents
<a name="API_DateTimeFormatConfiguration_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** DateTimeFormat **   <a name="QS-Type-DateTimeFormatConfiguration-DateTimeFormat"></a>
Determines the `DateTime` format.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** NullValueFormatConfiguration **   <a name="QS-Type-DateTimeFormatConfiguration-NullValueFormatConfiguration"></a>
The options that determine the null value format configuration.
Type: [NullValueFormatConfiguration](API_NullValueFormatConfiguration.md) object
Required: No

 ** NumericFormatConfiguration **   <a name="QS-Type-DateTimeFormatConfiguration-NumericFormatConfiguration"></a>
The formatting configuration for numeric `DateTime` fields.
Type: [NumericFormatConfiguration](API_NumericFormatConfiguration.md) object
Required: No

## See Also
<a name="API_DateTimeFormatConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/DateTimeFormatConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/DateTimeFormatConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/DateTimeFormatConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
