---
source_url: https://docs.aws.amazon.com/augmented-ai/2019-11-07/APIReference/API_HumanLoopDataAttributes.html
---

# HumanLoopDataAttributes
<a name="API_HumanLoopDataAttributes"></a>

Attributes of the data specified by the customer. Use these to describe the data to be labeled.

## Contents
<a name="API_HumanLoopDataAttributes_Contents"></a>

 ** ContentClassifiers **   <a name="augmentedai-Type-HumanLoopDataAttributes-ContentClassifiers"></a>
Declares that your content is free of personally identifiable information or adult content.
Amazon SageMaker can restrict the Amazon Mechanical Turk workers who can view your task based on this information.
Type: Array of strings
Array Members: Maximum number of 256 items.
Valid Values: `FreeOfPersonallyIdentifiableInformation | FreeOfAdultContent`
Required: Yes

## See Also
<a name="API_HumanLoopDataAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-a2i-runtime-2019-11-07/HumanLoopDataAttributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-a2i-runtime-2019-11-07/HumanLoopDataAttributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-a2i-runtime-2019-11-07/HumanLoopDataAttributes)
