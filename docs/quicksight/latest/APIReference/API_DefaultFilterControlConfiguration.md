---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DefaultFilterControlConfiguration.html
---

# DefaultFilterControlConfiguration
<a name="API_DefaultFilterControlConfiguration"></a>

The default configuration for all dependent controls of the filter.

## Contents
<a name="API_DefaultFilterControlConfiguration_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ControlOptions **   <a name="QS-Type-DefaultFilterControlConfiguration-ControlOptions"></a>
The control option for the `DefaultFilterControlConfiguration`.
Type: [DefaultFilterControlOptions](API_DefaultFilterControlOptions.md) object
Required: Yes

 ** ControlTitleFormatText **   <a name="QS-Type-DefaultFilterControlConfiguration-ControlTitleFormatText"></a>
The title text format configuration for the default filter control.
Type: [ControlTitleFormatText](API_ControlTitleFormatText.md) object
Required: No

 ** Title **   <a name="QS-Type-DefaultFilterControlConfiguration-Title"></a>
The title of the `DefaultFilterControlConfiguration`. This title is shared by all controls that are tied to this filter.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Required: No

## See Also
<a name="API_DefaultFilterControlConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/DefaultFilterControlConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/DefaultFilterControlConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/DefaultFilterControlConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
