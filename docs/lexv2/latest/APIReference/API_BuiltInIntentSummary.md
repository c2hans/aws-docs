---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_BuiltInIntentSummary.html
---

# BuiltInIntentSummary
<a name="API_BuiltInIntentSummary"></a>

Provides summary information about a built-in intent for the [ ListBuiltInIntents ](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_ListBuiltInIntents.html) operation.

## Contents
<a name="API_BuiltInIntentSummary_Contents"></a>

 ** description **   <a name="lexv2-Type-BuiltInIntentSummary-description"></a>
The description of the intent.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2000.
Required: No

 ** intentSignature **   <a name="lexv2-Type-BuiltInIntentSummary-intentSignature"></a>
The signature of the built-in intent. Use this to specify the parent intent of a derived intent.
Type: String
Required: No

## See Also
<a name="API_BuiltInIntentSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/BuiltInIntentSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/BuiltInIntentSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/BuiltInIntentSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lex. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lexv2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
