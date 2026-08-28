---
source_url: https://docs.aws.amazon.com/kendra/latest/APIReference/API_TextWithHighlights.html
---

# TextWithHighlights
<a name="API_TextWithHighlights"></a>

Provides text and information about where to highlight the text.

## Contents
<a name="API_TextWithHighlights_Contents"></a>

 ** Highlights **   <a name="kendra-Type-TextWithHighlights-Highlights"></a>
The beginning and end of the text that should be highlighted.
Type: Array of [Highlight](API_Highlight.md) objects
Required: No

 ** Text **   <a name="kendra-Type-TextWithHighlights-Text"></a>
The text to display to the user.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

## See Also
<a name="API_TextWithHighlights_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kendra-2019-02-03/TextWithHighlights)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kendra-2019-02-03/TextWithHighlights)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kendra-2019-02-03/TextWithHighlights)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Kendra. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query kendra` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
