---
source_url: https://docs.aws.amazon.com/translate/latest/APIReference/API_Term.html
---

# Term
<a name="API_Term"></a>

The term being translated by the custom terminology.

## Contents
<a name="API_Term_Contents"></a>

 ** SourceText **   <a name="translate-Type-Term-SourceText"></a>
The source text of the term being translated by the custom terminology.
Type: String
Length Constraints: Maximum length of 10000.
Pattern: `[\P{M}\p{M}]{0,10000}`
Required: No

 ** TargetText **   <a name="translate-Type-Term-TargetText"></a>
The target text of the term being translated by the custom terminology.
Type: String
Length Constraints: Maximum length of 10000.
Pattern: `[\P{M}\p{M}]{0,10000}`
Required: No

## See Also
<a name="API_Term_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/translate-2017-07-01/Term)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/translate-2017-07-01/Term)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/translate-2017-07-01/Term)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Translate. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query translate` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
