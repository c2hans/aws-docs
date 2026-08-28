---
source_url: https://docs.aws.amazon.com/comprehend/latest/APIReference/API_EntityTypesListItem.html
---

# EntityTypesListItem
<a name="API_EntityTypesListItem"></a>

An entity type within a labeled training dataset that Amazon Comprehend uses to train a custom entity recognizer.

## Contents
<a name="API_EntityTypesListItem_Contents"></a>

 ** Type **   <a name="comprehend-Type-EntityTypesListItem-Type"></a>
An entity type within a labeled training dataset that Amazon Comprehend uses to train a custom entity recognizer.
Entity types must not contain the following invalid characters: \\n (line break), \\\\n (escaped line break, \\r (carriage return), \\\\r (escaped carriage return), \\t (tab), \\\\t (escaped tab), and , (comma).
Type: String
Length Constraints: Maximum length of 64.
Pattern: `^(?![^\n\r\t,]*\\n|\\r|\\t)[^\n\r\t,]+$`
Required: Yes

## See Also
<a name="API_EntityTypesListItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/comprehend-2017-11-27/EntityTypesListItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/comprehend-2017-11-27/EntityTypesListItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/comprehend-2017-11-27/EntityTypesListItem)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Comprehend. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query comprehend` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
