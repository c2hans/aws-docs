---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AutoMLProblemTypeResolvedAttributes.html
---

# AutoMLProblemTypeResolvedAttributes
<a name="API_AutoMLProblemTypeResolvedAttributes"></a>

Stores resolved attributes specific to the problem type of an AutoML job V2.

## Contents
<a name="API_AutoMLProblemTypeResolvedAttributes_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** TabularResolvedAttributes **   <a name="sagemaker-Type-AutoMLProblemTypeResolvedAttributes-TabularResolvedAttributes"></a>
The resolved attributes for the tabular problem type.
Type: [TabularResolvedAttributes](API_TabularResolvedAttributes.md) object
Required: No

 ** TextGenerationResolvedAttributes **   <a name="sagemaker-Type-AutoMLProblemTypeResolvedAttributes-TextGenerationResolvedAttributes"></a>
The resolved attributes for the text generation problem type.
Type: [TextGenerationResolvedAttributes](API_TextGenerationResolvedAttributes.md) object
Required: No

## See Also
<a name="API_AutoMLProblemTypeResolvedAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/AutoMLProblemTypeResolvedAttributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/AutoMLProblemTypeResolvedAttributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/AutoMLProblemTypeResolvedAttributes)
