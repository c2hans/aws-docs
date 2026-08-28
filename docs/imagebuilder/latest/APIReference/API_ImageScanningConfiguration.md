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
A setting that indicates whether Image Builder keeps a snapshot of the vulnerability scans that Amazon Inspector runs against the build instance when you create a new image.
Type: Boolean
Required: No

## See Also
<a name="API_ImageScanningConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/imagebuilder-2019-12-02/ImageScanningConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/imagebuilder-2019-12-02/ImageScanningConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/ImageScanningConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for EC2 Image Builder. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query imagebuilder` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
