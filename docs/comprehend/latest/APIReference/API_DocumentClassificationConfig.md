---
source_url: https://docs.aws.amazon.com/comprehend/latest/APIReference/API_DocumentClassificationConfig.html
---

# DocumentClassificationConfig
<a name="API_DocumentClassificationConfig"></a>

Configuration required for a document classification model.

## Contents
<a name="API_DocumentClassificationConfig_Contents"></a>

 ** Mode **   <a name="comprehend-Type-DocumentClassificationConfig-Mode"></a>
Classification mode indicates whether the documents are `MULTI_CLASS` or `MULTI_LABEL`.
Type: String
Valid Values: `MULTI_CLASS | MULTI_LABEL`
Required: Yes

 ** Labels **   <a name="comprehend-Type-DocumentClassificationConfig-Labels"></a>
One or more labels to associate with the custom classifier.
Type: Array of strings
Array Members: Maximum number of 1000 items.
Length Constraints: Maximum length of 5000.
Pattern: `^\P{C}*$`
Required: No

## See Also
<a name="API_DocumentClassificationConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/comprehend-2017-11-27/DocumentClassificationConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/comprehend-2017-11-27/DocumentClassificationConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/comprehend-2017-11-27/DocumentClassificationConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Comprehend. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query comprehend` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
