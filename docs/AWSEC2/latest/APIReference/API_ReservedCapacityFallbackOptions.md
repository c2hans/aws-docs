---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ReservedCapacityFallbackOptions.html
---

# ReservedCapacityFallbackOptions
<a name="API_ReservedCapacityFallbackOptions"></a>

Describes the fallback behavior for an EC2 Fleet that uses reserved capacity when the reserved capacity is not enough to meet the target capacity. If you don't specify fallback options, EC2 Fleet does not fall back to any other market type after the specified reservation types are exhausted.

## Contents
<a name="API_ReservedCapacityFallbackOptions_Contents"></a>

 ** MarketTypeSet.N **
The instance purchasing options to fall back to when the reserved capacity is not enough to meet the target capacity. The only supported value is `on-demand`, which launches On-Demand Instances to fulfill the remaining target capacity.
Type: Array of strings
Valid Values: `on-demand`
Required: No

## See Also
<a name="API_ReservedCapacityFallbackOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/ReservedCapacityFallbackOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/ReservedCapacityFallbackOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/ReservedCapacityFallbackOptions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
