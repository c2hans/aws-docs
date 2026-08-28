---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_TransitGatewayMeteringPolicy.html
---

# TransitGatewayMeteringPolicy
<a name="API_TransitGatewayMeteringPolicy"></a>

Describes a transit gateway metering policy.

## Contents
<a name="API_TransitGatewayMeteringPolicy_Contents"></a>

 ** MiddleboxAttachmentIdSet.N **
The IDs of the middlebox attachments associated with the metering policy.
Type: Array of strings
Required: No

 ** state **
The state of the transit gateway metering policy.
Type: String
Valid Values: `available | deleted | pending | modifying | deleting`
Required: No

 ** TagSet.N **
The tags assigned to the transit gateway metering policy.
Type: Array of [Tag](API_Tag.md) objects
Required: No

 ** transitGatewayId **
The ID of the transit gateway associated with the metering policy.
Type: String
Required: No

 ** transitGatewayMeteringPolicyId **
The ID of the transit gateway metering policy.
Type: String
Required: No

 ** updateEffectiveAt **
The date and time when the metering policy update becomes effective.
Type: Timestamp
Required: No

## See Also
<a name="API_TransitGatewayMeteringPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/TransitGatewayMeteringPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/TransitGatewayMeteringPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/TransitGatewayMeteringPolicy)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
