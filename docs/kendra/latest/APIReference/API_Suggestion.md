---
source_url: https://docs.aws.amazon.com/kendra/latest/APIReference/API_Suggestion.html
---

# Suggestion
<a name="API_Suggestion"></a>

A single query suggestion.

## Contents
<a name="API_Suggestion_Contents"></a>

 ** Id **   <a name="kendra-Type-Suggestion-Id"></a>
The UUID (universally unique identifier) of a single query suggestion.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 73.
Required: No

 ** SourceDocuments **   <a name="kendra-Type-Suggestion-SourceDocuments"></a>
The list of document IDs and their fields/attributes that are used for a single query suggestion, if document fields set to use for query suggestions.
Type: Array of [SourceDocument](API_SourceDocument.md) objects
Required: No

 ** Value **   <a name="kendra-Type-Suggestion-Value"></a>
The value for the UUID (universally unique identifier) of a single query suggestion.
The value is the text string of a suggestion.
Type: [SuggestionValue](API_SuggestionValue.md) object
Required: No

## See Also
<a name="API_Suggestion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kendra-2019-02-03/Suggestion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kendra-2019-02-03/Suggestion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kendra-2019-02-03/Suggestion)
