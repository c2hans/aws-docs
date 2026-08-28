---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_LaunchTemplateInstanceMarketOptionsRequest.html
---

# LaunchTemplateInstanceMarketOptionsRequest
<a name="API_LaunchTemplateInstanceMarketOptionsRequest"></a>

The market (purchasing) option for the instances.

## Contents
<a name="API_LaunchTemplateInstanceMarketOptionsRequest_Contents"></a>

 ** MarketType **
The market type.
Type: String
Valid Values: `spot | capacity-block | interruptible-capacity-reservation | on-demand`
Required: No

 ** SpotOptions **
The options for Spot Instances.
Type: [LaunchTemplateSpotMarketOptionsRequest](API_LaunchTemplateSpotMarketOptionsRequest.md) object
Required: No

## See Also
<a name="API_LaunchTemplateInstanceMarketOptionsRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/LaunchTemplateInstanceMarketOptionsRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/LaunchTemplateInstanceMarketOptionsRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/LaunchTemplateInstanceMarketOptionsRequest)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
