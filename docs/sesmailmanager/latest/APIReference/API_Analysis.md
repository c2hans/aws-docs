---
source_url: https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_Analysis.html
---

# Analysis
<a name="API_Analysis"></a>

The result of an analysis can be used in conditions to trigger actions. Analyses can inspect the email content and report a certain aspect of the email.

## Contents
<a name="API_Analysis_Contents"></a>

 ** Analyzer **   <a name="sesmailmanager-Type-Analysis-Analyzer"></a>
The Amazon Resource Name (ARN) of an Add On.
Type: String
Pattern: `[a-zA-Z0-9:_/+=,@.#-]+`
Required: Yes

 ** ResultField **   <a name="sesmailmanager-Type-Analysis-ResultField"></a>
The returned value from an Add On.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `(addon\.)?[\sa-zA-Z0-9_]+`
Required: Yes

## See Also
<a name="API_Analysis_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mailmanager-2023-10-17/Analysis)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mailmanager-2023-10-17/Analysis)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mailmanager-2023-10-17/Analysis)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SES Mail Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sesmailmanager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
