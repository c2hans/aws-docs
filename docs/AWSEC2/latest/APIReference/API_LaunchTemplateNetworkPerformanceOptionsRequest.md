---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_LaunchTemplateNetworkPerformanceOptionsRequest.html
---

# LaunchTemplateNetworkPerformanceOptionsRequest
<a name="API_LaunchTemplateNetworkPerformanceOptionsRequest"></a>

When you configure network performance options in your launch template, your instance is geared for performance improvements based on the workload that it runs as soon as it's available.

## Contents
<a name="API_LaunchTemplateNetworkPerformanceOptionsRequest_Contents"></a>

 ** BandwidthWeighting **
Specify the bandwidth weighting option to boost the associated type of baseline bandwidth, as follows:
default
This option uses the standard bandwidth configuration for your instance type.
vpc-1
This option boosts your networking baseline bandwidth and reduces your EBS baseline bandwidth.
ebs-1
This option boosts your EBS baseline bandwidth and reduces your networking baseline bandwidth.
Type: String
Valid Values: `default | vpc-1 | ebs-1`
Required: No

## See Also
<a name="API_LaunchTemplateNetworkPerformanceOptionsRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/LaunchTemplateNetworkPerformanceOptionsRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/LaunchTemplateNetworkPerformanceOptionsRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/LaunchTemplateNetworkPerformanceOptionsRequest)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
