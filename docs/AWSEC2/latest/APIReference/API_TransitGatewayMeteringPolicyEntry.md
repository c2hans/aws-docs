---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_TransitGatewayMeteringPolicyEntry.html
---

# TransitGatewayMeteringPolicyEntry
<a name="API_TransitGatewayMeteringPolicyEntry"></a>

Describes an entry in a transit gateway metering policy.

## Contents
<a name="API_TransitGatewayMeteringPolicyEntry_Contents"></a>

 ** meteredAccount **
The AWS account ID to which the metered traffic is attributed.
Type: String
Valid Values: `source-attachment-owner | destination-attachment-owner | transit-gateway-owner`
Required: No

 ** meteringPolicyRule **
The metering policy rule that defines traffic matching criteria.
Type: [TransitGatewayMeteringPolicyRule](API_TransitGatewayMeteringPolicyRule.md) object
Required: No

 ** policyRuleNumber **
The rule number of the metering policy entry.
Type: String
Required: No

 ** state **
The state of the metering policy entry.
Type: String
Valid Values: `available | deleted`
Required: No

 ** updatedAt **
The date and time when the metering policy entry was last updated.
Type: Timestamp
Required: No

 ** updateEffectiveAt **
The date and time when the metering policy entry update becomes effective.
Type: Timestamp
Required: No

## See Also
<a name="API_TransitGatewayMeteringPolicyEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/TransitGatewayMeteringPolicyEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/TransitGatewayMeteringPolicyEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/TransitGatewayMeteringPolicyEntry)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
