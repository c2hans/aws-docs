---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_FontConfiguration.html
---

# FontConfiguration
<a name="API_FontConfiguration"></a>

Configures the display properties of the given text.

## Contents
<a name="API_FontConfiguration_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** FontColor **   <a name="QS-Type-FontConfiguration-FontColor"></a>
Determines the color of the text.
Type: String
Pattern: `^#[A-F0-9]{6}$`
Required: No

 ** FontDecoration **   <a name="QS-Type-FontConfiguration-FontDecoration"></a>
Determines the appearance of decorative lines on the text.
Type: String
Valid Values: `UNDERLINE | NONE`
Required: No

 ** FontFamily **   <a name="QS-Type-FontConfiguration-FontFamily"></a>
The font family that you want to use.
Type: String
Length Constraints: Maximum length of 256.
Required: No

 ** FontSize **   <a name="QS-Type-FontConfiguration-FontSize"></a>
The option that determines the text display size.
Type: [FontSize](API_FontSize.md) object
Required: No

 ** FontStyle **   <a name="QS-Type-FontConfiguration-FontStyle"></a>
Determines the text display face that is inherited by the given font family.
Type: String
Valid Values: `NORMAL | ITALIC`
Required: No

 ** FontWeight **   <a name="QS-Type-FontConfiguration-FontWeight"></a>
The option that determines the text display weight, or boldness.
Type: [FontWeight](API_FontWeight.md) object
Required: No

## See Also
<a name="API_FontConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/FontConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/FontConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/FontConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
