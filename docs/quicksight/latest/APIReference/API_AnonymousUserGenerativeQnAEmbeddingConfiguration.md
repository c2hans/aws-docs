---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_AnonymousUserGenerativeQnAEmbeddingConfiguration.html
---

# AnonymousUserGenerativeQnAEmbeddingConfiguration
<a name="API_AnonymousUserGenerativeQnAEmbeddingConfiguration"></a>

The settings that you want to use for the Generative Q&A experience.

## Contents
<a name="API_AnonymousUserGenerativeQnAEmbeddingConfiguration_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** InitialTopicId **   <a name="QS-Type-AnonymousUserGenerativeQnAEmbeddingConfiguration-InitialTopicId"></a>
The Quick Sight Q topic ID of the new reader experience topic that you want the anonymous user to see first. This ID is included in the output URL. When the URL in response is accessed, Quick Sight renders the Generative Q&A experience with this new reader experience topic pre selected.
The Amazon Resource Name (ARN) of this Q new reader experience topic must be included in the `AuthorizedResourceArns` parameter. Otherwise, the request fails with an `InvalidParameterValueException` error.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[\w\-]+`
Required: Yes

## See Also
<a name="API_AnonymousUserGenerativeQnAEmbeddingConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/AnonymousUserGenerativeQnAEmbeddingConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/AnonymousUserGenerativeQnAEmbeddingConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/AnonymousUserGenerativeQnAEmbeddingConfiguration)
