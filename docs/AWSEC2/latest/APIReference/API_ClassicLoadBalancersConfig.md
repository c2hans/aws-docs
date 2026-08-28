---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ClassicLoadBalancersConfig.html
---

# ClassicLoadBalancersConfig
<a name="API_ClassicLoadBalancersConfig"></a>

Describes the Classic Load Balancers to attach to a Spot Fleet. Spot Fleet registers the running Spot Instances with these Classic Load Balancers.

## Contents
<a name="API_ClassicLoadBalancersConfig_Contents"></a>

 ** ClassicLoadBalancers.N **
One or more Classic Load Balancers.
Type: Array of [ClassicLoadBalancer](API_ClassicLoadBalancer.md) objects
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Required: No

## See Also
<a name="API_ClassicLoadBalancersConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/ClassicLoadBalancersConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/ClassicLoadBalancersConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/ClassicLoadBalancersConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
