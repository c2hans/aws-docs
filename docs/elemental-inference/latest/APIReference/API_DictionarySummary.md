---
source_url: https://docs.aws.amazon.com/elemental-inference/latest/APIReference/API_DictionarySummary.html
---

# DictionarySummary
<a name="API_DictionarySummary"></a>

Contains summary information about a dictionary. Used in the ListDictionaries response.

## Contents
<a name="API_DictionarySummary_Contents"></a>

 ** arn **   <a name="elementalinference-Type-DictionarySummary-arn"></a>
The ARN of the dictionary.
Type: String
Required: Yes

 ** id **   <a name="elementalinference-Type-DictionarySummary-id"></a>
The ID of the dictionary.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 19.
Pattern: `[a-zA-Z0-9]+`
Required: Yes

 ** language **   <a name="elementalinference-Type-DictionarySummary-language"></a>
The language of the dictionary.
Type: String
Valid Values: `eng | fra | ita | deu | spa | por`
Required: Yes

 ** name **   <a name="elementalinference-Type-DictionarySummary-name"></a>
The name of the dictionary.
Type: String
Pattern: `[a-zA-Z0-9]([a-zA-Z0-9-_]{0,126}[a-zA-Z0-9])?`
Required: Yes

 ** status **   <a name="elementalinference-Type-DictionarySummary-status"></a>
The status of the dictionary.
Type: String
Valid Values: `CREATING | AVAILABLE | REFERENCED | DELETING | DELETED`
Required: Yes

## See Also
<a name="API_DictionarySummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elementalinference-2018-11-14/DictionarySummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elementalinference-2018-11-14/DictionarySummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elementalinference-2018-11-14/DictionarySummary)
