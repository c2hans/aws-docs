---
source_url: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_NetworkOriginConfiguration.html
---

# NetworkOriginConfiguration
<a name="API_NetworkOriginConfiguration"></a>

The proposed `InternetConfiguration` or `VpcConfiguration` to apply to the Amazon S3 access point. You can make the access point accessible from the internet, or you can specify that all requests made through that access point must originate from a specific virtual private cloud (VPC). You can specify only one type of network configuration. For more information, see [Creating access points](https://docs.aws.amazon.com/AmazonS3/latest/dev/creating-access-points.html).

## Contents
<a name="API_NetworkOriginConfiguration_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** internetConfiguration **   <a name="accessanalyzer-Type-NetworkOriginConfiguration-internetConfiguration"></a>
The configuration for the Amazon S3 access point or multi-region access point with an `Internet` origin.
Type: [InternetConfiguration](API_InternetConfiguration.md) object
Required: No

 ** vpcConfiguration **   <a name="accessanalyzer-Type-NetworkOriginConfiguration-vpcConfiguration"></a>
The proposed virtual private cloud (VPC) configuration for the Amazon S3 access point. VPC configuration does not apply to multi-region access points. For more information, see [VpcConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_VpcConfiguration.html).
Type: [VpcConfiguration](API_VpcConfiguration.md) object
Required: No

## See Also
<a name="API_NetworkOriginConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/NetworkOriginConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/NetworkOriginConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/NetworkOriginConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IAM Access Analyzer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query access-analyzer` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
