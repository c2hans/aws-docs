---
source_url: https://docs.aws.amazon.com/kendra/latest/APIReference/API_SourceDocument.html
---

# SourceDocument
<a name="API_SourceDocument"></a>

The document ID and its fields/attributes that are used for a query suggestion, if document fields set to use for query suggestions.

## Contents
<a name="API_SourceDocument_Contents"></a>

 ** AdditionalAttributes **   <a name="kendra-Type-SourceDocument-AdditionalAttributes"></a>
The additional fields/attributes to include in the response. You can use additional fields to provide extra information in the response. Additional fields are not used to based suggestions on.
Type: Array of [DocumentAttribute](API_DocumentAttribute.md) objects
Required: No

 ** DocumentId **   <a name="kendra-Type-SourceDocument-DocumentId"></a>
The identifier of the document used for a query suggestion.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** SuggestionAttributes **   <a name="kendra-Type-SourceDocument-SuggestionAttributes"></a>
The document fields/attributes used for a query suggestion.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `[a-zA-Z0-9_][a-zA-Z0-9_-]*`
Required: No

## See Also
<a name="API_SourceDocument_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kendra-2019-02-03/SourceDocument)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kendra-2019-02-03/SourceDocument)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kendra-2019-02-03/SourceDocument)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Kendra. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query kendra` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
