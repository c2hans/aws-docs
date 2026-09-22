---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_ImageScanningConfiguration.html
---

# ImageScanningConfiguration
<a name="API_ImageScanningConfiguration"></a>

Contains settings for Image Builder image resource and container image scans.

## Contents
<a name="API_ImageScanningConfiguration_Contents"></a>

 ** ecrConfiguration **   <a name="imagebuilder-Type-ImageScanningConfiguration-ecrConfiguration"></a>
Contains Amazon ECR settings for vulnerability scans.
Type: [EcrConfiguration](API_EcrConfiguration.md) object
Required: No

 ** imageScanningEnabled **   <a name="imagebuilder-Type-ImageScanningConfiguration-imageScanningEnabled"></a>
Specifies whether Amazon Inspector scans for vulnerabilities when you create a new image, and whether Image Builder saves the findings. Amazon Inspector must be enabled in the account. Image tests must also be enabled. For AMI output, Amazon Inspector scans the test instance. For container output, Amazon Inspector scans the container image that Image Builder pushes to the Amazon ECR repository from your `ecrConfiguration` settings.
Type: Boolean
Required: No

## See Also
<a name="API_ImageScanningConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/imagebuilder-2019-12-02/ImageScanningConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/imagebuilder-2019-12-02/ImageScanningConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/ImageScanningConfiguration)
