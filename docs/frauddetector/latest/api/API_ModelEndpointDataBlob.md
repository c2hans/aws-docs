---
source_url: https://docs.aws.amazon.com/frauddetector/latest/api/API_ModelEndpointDataBlob.html
---

Amazon Fraud Detector is no longer be open to new customers as of November 7, 2025. For capabilities similar to Amazon Fraud Detector, explore Amazon SageMaker AI, AutoGluon, and AWS WAF.

# ModelEndpointDataBlob
<a name="API_ModelEndpointDataBlob"></a>

A pre-formed Amazon SageMaker model input you can include if your detector version includes an imported Amazon SageMaker model endpoint with pass-through input configuration.

## Contents
<a name="API_ModelEndpointDataBlob_Contents"></a>

 ** byteBuffer **   <a name="FraudDetector-Type-ModelEndpointDataBlob-byteBuffer"></a>
The byte buffer of the Amazon SageMaker model endpoint input data blob.
Type: Base64-encoded binary data object
Required: No

 ** contentType **   <a name="FraudDetector-Type-ModelEndpointDataBlob-contentType"></a>
The content type of the Amazon SageMaker model endpoint input data blob.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

## See Also
<a name="API_ModelEndpointDataBlob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/frauddetector-2019-11-15/ModelEndpointDataBlob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/frauddetector-2019-11-15/ModelEndpointDataBlob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/frauddetector-2019-11-15/ModelEndpointDataBlob)
