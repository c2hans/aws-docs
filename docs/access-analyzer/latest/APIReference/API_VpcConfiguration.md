---
source_url: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_VpcConfiguration.html
---

# VpcConfiguration
<a name="API_VpcConfiguration"></a>

The proposed virtual private cloud (VPC) configuration for the Amazon S3 access point. VPC configuration does not apply to multi-region access points. For more information, see [VpcConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_VpcConfiguration.html).

## Contents
<a name="API_VpcConfiguration_Contents"></a>

 ** vpcId **   <a name="accessanalyzer-Type-VpcConfiguration-vpcId"></a>
 If this field is specified, this access point will only allow connections from the specified VPC ID.
Type: String
Pattern: `vpc-([0-9a-f]){8}(([0-9a-f]){9})?`
Required: Yes

## See Also
<a name="API_VpcConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/VpcConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/VpcConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/VpcConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IAM Access Analyzer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query access-analyzer` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
