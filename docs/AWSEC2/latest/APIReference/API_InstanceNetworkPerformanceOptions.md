---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_InstanceNetworkPerformanceOptions.html
---

# InstanceNetworkPerformanceOptions
<a name="API_InstanceNetworkPerformanceOptions"></a>

With network performance options, you can adjust your bandwidth preferences to meet the needs of the workload that runs on your instance.

## Contents
<a name="API_InstanceNetworkPerformanceOptions_Contents"></a>

 ** bandwidthWeighting **
When you configure network bandwidth weighting, you can boost your baseline bandwidth for either networking or EBS by up to 25%. The total available baseline bandwidth for your instance remains the same. The default option uses the standard bandwidth configuration for your instance type.
Type: String
Valid Values: `default | vpc-1 | ebs-1`
Required: No

## See Also
<a name="API_InstanceNetworkPerformanceOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/InstanceNetworkPerformanceOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/InstanceNetworkPerformanceOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/InstanceNetworkPerformanceOptions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
