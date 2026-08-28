---
source_url: https://docs.aws.amazon.com/translate/latest/APIReference/API_AppliedTerminology.html
---

# AppliedTerminology
<a name="API_AppliedTerminology"></a>

The custom terminology applied to the input text by Amazon Translate for the translated text response. This is optional in the response and will only be present if you specified terminology input in the request. Currently, only one terminology can be applied per TranslateText request.

## Contents
<a name="API_AppliedTerminology_Contents"></a>

 ** Name **   <a name="translate-Type-AppliedTerminology-Name"></a>
The name of the custom terminology applied to the input text by Amazon Translate for the translated text response.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^([A-Za-z0-9-]_?)+$`
Required: No

 ** Terms **   <a name="translate-Type-AppliedTerminology-Terms"></a>
The specific terms of the custom terminology applied to the input text by Amazon Translate for the translated text response. A maximum of 250 terms will be returned, and the specific terms applied will be the first 250 terms in the source text.
Type: Array of [Term](API_Term.md) objects
Required: No

## See Also
<a name="API_AppliedTerminology_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/translate-2017-07-01/AppliedTerminology)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/translate-2017-07-01/AppliedTerminology)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/translate-2017-07-01/AppliedTerminology)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Translate. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query translate` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
