---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_VisualMessageConfiguration.html
---

# VisualMessageConfiguration
<a name="API_VisualMessageConfiguration"></a>

The configuration for a customizable message displayed on a visual. Supports parameter substitution in text fields.

## Contents
<a name="API_VisualMessageConfiguration_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Description **   <a name="QS-Type-VisualMessageConfiguration-Description"></a>
The description text of the message that is displayed on the visual.
Type: String
Length Constraints: Maximum length of 120.
Pattern: `\A[\p{L}\p{M}\p{N}\s.,/\\:_()\[\]<>$!?'"#@%+&|^\-]*\z`
Required: No

 ** DescriptionVisibility **   <a name="QS-Type-VisualMessageConfiguration-DescriptionVisibility"></a>
Specifies whether the description of the message is displayed.
Type: String
Valid Values: `HIDDEN | VISIBLE`
Required: No

 ** Enabled **   <a name="QS-Type-VisualMessageConfiguration-Enabled"></a>
Specifies whether the custom message is displayed on the visual. When set to `true`, the custom message appears in place of the default message. When set to `false` or omitted, the default message is displayed.
Type: Boolean
Required: No

 ** LinkText **   <a name="QS-Type-VisualMessageConfiguration-LinkText"></a>
The display text of the hyperlink that is shown in the message.
Type: String
Length Constraints: Maximum length of 120.
Pattern: `\A[\p{L}\p{M}\p{N}\s.,/\\:_()\[\]<>$!?'"#@%+&|^\-]*\z`
Required: No

 ** LinkUrl **   <a name="QS-Type-VisualMessageConfiguration-LinkUrl"></a>
The destination URL of the hyperlink that is shown in the message. Only valid `http`, `https`, and `mailto` URLs are supported.
Type: String
Length Constraints: Maximum length of 120.
Pattern: `(?i)\A(?:(?:https?://|mailto:)\S*<<\$.+?>>\S*|https?://[a-z\d.-]+\.[a-z]{2,63}(?::\d+)?(?:[/?#][^\s]*)?|mailto:[^\s@]+@[a-z\d.-]+\.[a-z]{2,63})\z`
Required: No

 ** LinkVisibility **   <a name="QS-Type-VisualMessageConfiguration-LinkVisibility"></a>
Specifies whether the hyperlink in the message is displayed.
Type: String
Valid Values: `HIDDEN | VISIBLE`
Required: No

 ** Title **   <a name="QS-Type-VisualMessageConfiguration-Title"></a>
The title text of the message that is displayed on the visual.
Type: String
Length Constraints: Maximum length of 120.
Pattern: `\A[\p{L}\p{M}\p{N}\s.,/\\:_()\[\]<>$!?'"#@%+&|^\-]*\z`
Required: No

 ** TitleVisibility **   <a name="QS-Type-VisualMessageConfiguration-TitleVisibility"></a>
Specifies whether the title of the message is displayed.
Type: String
Valid Values: `HIDDEN | VISIBLE`
Required: No

## See Also
<a name="API_VisualMessageConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/VisualMessageConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/VisualMessageConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/VisualMessageConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
