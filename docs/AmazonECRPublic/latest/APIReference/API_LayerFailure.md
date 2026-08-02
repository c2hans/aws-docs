---
source_url: https://docs.aws.amazon.com/AmazonECRPublic/latest/APIReference/API_LayerFailure.html
---

# LayerFailure
<a name="API_LayerFailure"></a>

An object that represents an Amazon ECR image layer failure.

## Contents
<a name="API_LayerFailure_Contents"></a>

 ** failureCode **   <a name="ecrpublic-Type-LayerFailure-failureCode"></a>
The failure code that's associated with the failure.
Type: String
Valid Values: `InvalidLayerDigest | MissingLayerDigest`
Required: No

 ** failureReason **   <a name="ecrpublic-Type-LayerFailure-failureReason"></a>
The reason for the failure.
Type: String
Required: No

 ** layerDigest **   <a name="ecrpublic-Type-LayerFailure-layerDigest"></a>
The layer digest that's associated with the failure.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.
Required: No

## See Also
<a name="API_LayerFailure_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecr-public-2020-10-30/LayerFailure)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecr-public-2020-10-30/LayerFailure)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecr-public-2020-10-30/LayerFailure)
