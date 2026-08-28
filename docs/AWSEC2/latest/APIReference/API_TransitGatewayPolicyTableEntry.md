---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_TransitGatewayPolicyTableEntry.html
---

# TransitGatewayPolicyTableEntry
<a name="API_TransitGatewayPolicyTableEntry"></a>

Describes a transit gateway policy table entry

## Contents
<a name="API_TransitGatewayPolicyTableEntry_Contents"></a>

 ** policyRule **
The policy rule associated with the transit gateway policy table.
Type: [TransitGatewayPolicyRule](API_TransitGatewayPolicyRule.md) object
Required: No

 ** policyRuleNumber **
The rule number for the transit gateway policy table entry.
Type: String
Required: No

 ** state **
The state of the transit gateway policy table entry.
Type: String
Valid Values: `active | deleted`
Required: No

 ** targetRouteTableId **
The ID of the target route table.
Type: String
Required: No

## See Also
<a name="API_TransitGatewayPolicyTableEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/TransitGatewayPolicyTableEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/TransitGatewayPolicyTableEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/TransitGatewayPolicyTableEntry)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
