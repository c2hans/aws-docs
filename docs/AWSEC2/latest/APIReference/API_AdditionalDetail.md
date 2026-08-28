---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AdditionalDetail.html
---

# AdditionalDetail
<a name="API_AdditionalDetail"></a>

Describes an additional detail for a path analysis. For more information, see [Reachability Analyzer additional detail codes](https://docs.aws.amazon.com/vpc/latest/reachability/additional-detail-codes.html).

## Contents
<a name="API_AdditionalDetail_Contents"></a>

 ** additionalDetailType **
The additional detail code.
Type: String
Required: No

 ** component **
The path component.
Type: [AnalysisComponent](API_AnalysisComponent.md) object
Required: No

 ** LoadBalancerSet.N **
The load balancers.
Type: Array of [AnalysisComponent](API_AnalysisComponent.md) objects
Required: No

 ** RuleGroupRuleOptionsPairSet.N **
The rule options.
Type: Array of [RuleGroupRuleOptionsPair](API_RuleGroupRuleOptionsPair.md) objects
Required: No

 ** RuleGroupTypePairSet.N **
The rule group type.
Type: Array of [RuleGroupTypePair](API_RuleGroupTypePair.md) objects
Required: No

 ** RuleOptionSet.N **
The rule options.
Type: Array of [RuleOption](API_RuleOption.md) objects
Required: No

 ** serviceName **
The name of the VPC endpoint service.
Type: String
Required: No

 ** vpcEndpointService **
The VPC endpoint service.
Type: [AnalysisComponent](API_AnalysisComponent.md) object
Required: No

## See Also
<a name="API_AdditionalDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/AdditionalDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/AdditionalDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/AdditionalDetail)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
