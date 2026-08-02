---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AutoMLComputeConfig.html
---

# AutoMLComputeConfig
<a name="API_AutoMLComputeConfig"></a>

**Note**
This data type is intended for use exclusively by SageMaker Canvas and cannot be used in other contexts at the moment.

Specifies the compute configuration for an AutoML job V2.

## Contents
<a name="API_AutoMLComputeConfig_Contents"></a>

 ** EmrServerlessComputeConfig **   <a name="sagemaker-Type-AutoMLComputeConfig-EmrServerlessComputeConfig"></a>
The configuration for using [ EMR Serverless](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/emr-serverless.html) to run the AutoML job V2.
To allow your AutoML job V2 to automatically initiate a remote job on EMR Serverless when additional compute resources are needed to process large datasets, you need to provide an `EmrServerlessComputeConfig` object, which includes an `ExecutionRoleARN` attribute, to the `AutoMLComputeConfig` of the AutoML job V2 input request.
By seamlessly transitioning to EMR Serverless when required, the AutoML job can handle datasets that would otherwise exceed the initially provisioned resources, without any manual intervention from you.
EMR Serverless is available for the tabular and time series problem types. We recommend setting up this option for tabular datasets larger than 5 GB and time series datasets larger than 30 GB.
Type: [EmrServerlessComputeConfig](API_EmrServerlessComputeConfig.md) object
Required: No

## See Also
<a name="API_AutoMLComputeConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/AutoMLComputeConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/AutoMLComputeConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/AutoMLComputeConfig)
