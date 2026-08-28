---
source_url: https://docs.aws.amazon.com/comprehend/latest/APIReference/API_BatchDetectDominantLanguageItemResult.html
---

# BatchDetectDominantLanguageItemResult
<a name="API_BatchDetectDominantLanguageItemResult"></a>

The result of calling the [BatchDetectDominantLanguage](API_BatchDetectDominantLanguage.md) operation. The operation returns one object for each document that is successfully processed by the operation.

## Contents
<a name="API_BatchDetectDominantLanguageItemResult_Contents"></a>

 ** Index **   <a name="comprehend-Type-BatchDetectDominantLanguageItemResult-Index"></a>
The zero-based index of the document in the input list.
Type: Integer
Required: No

 ** Languages **   <a name="comprehend-Type-BatchDetectDominantLanguageItemResult-Languages"></a>
One or more [DominantLanguage](API_DominantLanguage.md) objects describing the dominant languages in the document.
Type: Array of [DominantLanguage](API_DominantLanguage.md) objects
Required: No

## See Also
<a name="API_BatchDetectDominantLanguageItemResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/comprehend-2017-11-27/BatchDetectDominantLanguageItemResult)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/comprehend-2017-11-27/BatchDetectDominantLanguageItemResult)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/comprehend-2017-11-27/BatchDetectDominantLanguageItemResult)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Comprehend. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query comprehend` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
