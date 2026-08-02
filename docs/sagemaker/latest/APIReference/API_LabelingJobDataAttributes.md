---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_LabelingJobDataAttributes.html
---

# LabelingJobDataAttributes
<a name="API_LabelingJobDataAttributes"></a>

Attributes of the data specified by the customer. Use these to describe the data to be labeled.

## Contents
<a name="API_LabelingJobDataAttributes_Contents"></a>

 ** ContentClassifiers **   <a name="sagemaker-Type-LabelingJobDataAttributes-ContentClassifiers"></a>
Declares that your content is free of personally identifiable information or adult content. SageMaker may restrict the Amazon Mechanical Turk workers that can view your task based on this information.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 256 items.
Valid Values: `FreeOfPersonallyIdentifiableInformation | FreeOfAdultContent`
Required: No

## See Also
<a name="API_LabelingJobDataAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/LabelingJobDataAttributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/LabelingJobDataAttributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/LabelingJobDataAttributes)
