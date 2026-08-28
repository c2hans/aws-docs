---
source_url: https://docs.aws.amazon.com/comprehend/latest/APIReference/API_BatchDetectSyntaxItemResult.html
---

# BatchDetectSyntaxItemResult
<a name="API_BatchDetectSyntaxItemResult"></a>

The result of calling the [BatchDetectSyntax](API_BatchDetectSyntax.md) operation. The operation returns one object that is successfully processed by the operation.

## Contents
<a name="API_BatchDetectSyntaxItemResult_Contents"></a>

 ** Index **   <a name="comprehend-Type-BatchDetectSyntaxItemResult-Index"></a>
The zero-based index of the document in the input list.
Type: Integer
Required: No

 ** SyntaxTokens **   <a name="comprehend-Type-BatchDetectSyntaxItemResult-SyntaxTokens"></a>
The syntax tokens for the words in the document, one token for each word.
Type: Array of [SyntaxToken](API_SyntaxToken.md) objects
Required: No

## See Also
<a name="API_BatchDetectSyntaxItemResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/comprehend-2017-11-27/BatchDetectSyntaxItemResult)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/comprehend-2017-11-27/BatchDetectSyntaxItemResult)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/comprehend-2017-11-27/BatchDetectSyntaxItemResult)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Comprehend. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query comprehend` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
