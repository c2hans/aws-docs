---
source_url: https://docs.aws.amazon.com/kendra/latest/APIReference/API_ClickFeedback.html
---

# ClickFeedback
<a name="API_ClickFeedback"></a>

Gathers information about when a particular result was clicked by a user. Your application uses the `SubmitFeedback` API to provide click information.

## Contents
<a name="API_ClickFeedback_Contents"></a>

 ** ClickTime **   <a name="kendra-Type-ClickFeedback-ClickTime"></a>
The Unix timestamp when the result was clicked.
Type: Timestamp
Required: Yes

 ** ResultId **   <a name="kendra-Type-ClickFeedback-ResultId"></a>
The identifier of the search result that was clicked.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 73.
Required: Yes

## See Also
<a name="API_ClickFeedback_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kendra-2019-02-03/ClickFeedback)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kendra-2019-02-03/ClickFeedback)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kendra-2019-02-03/ClickFeedback)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Kendra. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query kendra` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
