---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AutoMLDataSplitConfig.html
---

# AutoMLDataSplitConfig
<a name="API_AutoMLDataSplitConfig"></a>

This structure specifies how to split the data into train and validation datasets.

The validation and training datasets must contain the same headers. For jobs created by calling `CreateAutoMLJob`, the validation dataset must be less than 2 GB in size.

## Contents
<a name="API_AutoMLDataSplitConfig_Contents"></a>

 ** ValidationFraction **   <a name="sagemaker-Type-AutoMLDataSplitConfig-ValidationFraction"></a>
The validation fraction (optional) is a float that specifies the portion of the training dataset to be used for validation. The default value is 0.2, and values must be greater than 0 and less than 1. We recommend setting this value to be less than 0.5.
Type: Float
Valid Range: Minimum value of 0. Maximum value of 1.
Required: No

## See Also
<a name="API_AutoMLDataSplitConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/AutoMLDataSplitConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/AutoMLDataSplitConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/AutoMLDataSplitConfig)
