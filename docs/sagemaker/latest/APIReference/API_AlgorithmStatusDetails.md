---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AlgorithmStatusDetails.html
---

# AlgorithmStatusDetails
<a name="API_AlgorithmStatusDetails"></a>

Specifies the validation and image scan statuses of the algorithm.

## Contents
<a name="API_AlgorithmStatusDetails_Contents"></a>

 ** ImageScanStatuses **   <a name="sagemaker-Type-AlgorithmStatusDetails-ImageScanStatuses"></a>
The status of the scan of the algorithm's Docker image container.
Type: Array of [AlgorithmStatusItem](API_AlgorithmStatusItem.md) objects
Required: No

 ** ValidationStatuses **   <a name="sagemaker-Type-AlgorithmStatusDetails-ValidationStatuses"></a>
The status of algorithm validation.
Type: Array of [AlgorithmStatusItem](API_AlgorithmStatusItem.md) objects
Required: No

## See Also
<a name="API_AlgorithmStatusDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/AlgorithmStatusDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/AlgorithmStatusDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/AlgorithmStatusDetails)
