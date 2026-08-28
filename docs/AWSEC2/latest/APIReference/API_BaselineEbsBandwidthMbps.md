---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_BaselineEbsBandwidthMbps.html
---

# BaselineEbsBandwidthMbps
<a name="API_BaselineEbsBandwidthMbps"></a>

The minimum and maximum baseline bandwidth to Amazon EBS, in Mbps. For more information, see [Amazon EBS–optimized instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-optimized.html) in the *Amazon EC2 User Guide*.

## Contents
<a name="API_BaselineEbsBandwidthMbps_Contents"></a>

 ** Max ** (request), ** max ** (response)
The maximum baseline bandwidth, in Mbps. If this parameter is not specified, there is no maximum limit.
Type: Integer
Required: No

 ** Min ** (request), ** min ** (response)
The minimum baseline bandwidth, in Mbps. If this parameter is not specified, there is no minimum limit.
Type: Integer
Required: No

## See Also
<a name="API_BaselineEbsBandwidthMbps_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/BaselineEbsBandwidthMbps)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/BaselineEbsBandwidthMbps)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/BaselineEbsBandwidthMbps)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
