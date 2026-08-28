---
source_url: https://docs.aws.amazon.com/comprehend/latest/APIReference/API_WarningsListItem.html
---

# WarningsListItem
<a name="API_WarningsListItem"></a>

The system identified one of the following warnings while processing the input document:
+ The document to classify is plain text, but the classifier is a native document model.
+ The document to classify is semi-structured, but the classifier is a plain-text model.

## Contents
<a name="API_WarningsListItem_Contents"></a>

 ** Page **   <a name="comprehend-Type-WarningsListItem-Page"></a>
Page number in the input document.
Type: Integer
Required: No

 ** WarnCode **   <a name="comprehend-Type-WarningsListItem-WarnCode"></a>
The type of warning.
Type: String
Valid Values: `INFERENCING_PLAINTEXT_WITH_NATIVE_TRAINED_MODEL | INFERENCING_NATIVE_DOCUMENT_WITH_PLAINTEXT_TRAINED_MODEL`
Required: No

 ** WarnMessage **   <a name="comprehend-Type-WarningsListItem-WarnMessage"></a>
Text message associated with the warning.
Type: String
Length Constraints: Minimum length of 1.
Required: No

## See Also
<a name="API_WarningsListItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/comprehend-2017-11-27/WarningsListItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/comprehend-2017-11-27/WarningsListItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/comprehend-2017-11-27/WarningsListItem)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Comprehend. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query comprehend` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
