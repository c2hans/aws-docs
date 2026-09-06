---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_ImageScanFindingAggregation.html
---

# ImageScanFindingAggregation
<a name="API_ImageScanFindingAggregation"></a>

This returns exactly one type of aggregation, based on the filter that Image Builder applies in its API action.

## Contents
<a name="API_ImageScanFindingAggregation_Contents"></a>

 ** accountAggregation **   <a name="imagebuilder-Type-ImageScanFindingAggregation-accountAggregation"></a>
Returns an object that contains severity counts based on an account ID.
Type: [AccountAggregation](API_AccountAggregation.md) object
Required: No

 ** imageAggregation **   <a name="imagebuilder-Type-ImageScanFindingAggregation-imageAggregation"></a>
Returns an object that contains severity counts based on the Amazon Resource Name (ARN) for a specific image.
Type: [ImageAggregation](API_ImageAggregation.md) object
Required: No

 ** imagePipelineAggregation **   <a name="imagebuilder-Type-ImageScanFindingAggregation-imagePipelineAggregation"></a>
Returns an object that contains severity counts based on an image pipeline ARN.
Type: [ImagePipelineAggregation](API_ImagePipelineAggregation.md) object
Required: No

 ** vulnerabilityIdAggregation **   <a name="imagebuilder-Type-ImageScanFindingAggregation-vulnerabilityIdAggregation"></a>
Returns an object that contains severity counts based on vulnerability ID.
Type: [VulnerabilityIdAggregation](API_VulnerabilityIdAggregation.md) object
Required: No

## See Also
<a name="API_ImageScanFindingAggregation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/imagebuilder-2019-12-02/ImageScanFindingAggregation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/imagebuilder-2019-12-02/ImageScanFindingAggregation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/ImageScanFindingAggregation)
