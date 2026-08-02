---
source_url: https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_ImageScanningConfiguration.html
---

# ImageScanningConfiguration
<a name="API_ImageScanningConfiguration"></a>

The image scanning configuration for a repository.

## Contents
<a name="API_ImageScanningConfiguration_Contents"></a>

 ** scanOnPush **   <a name="ECR-Type-ImageScanningConfiguration-scanOnPush"></a>
The setting that determines whether images are scanned after being pushed to a repository. If set to `true`, images will be scanned after being pushed. If this parameter is not specified, it will default to `false` and images will not be scanned unless a scan is manually started with the [API\_StartImageScan](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_StartImageScan.html) API.
Type: Boolean
Required: No

## See Also
<a name="API_ImageScanningConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecr-2015-09-21/ImageScanningConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecr-2015-09-21/ImageScanningConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecr-2015-09-21/ImageScanningConfiguration)
