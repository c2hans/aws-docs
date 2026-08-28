---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_TransitGatewayPrefixListReference.html
---

# TransitGatewayPrefixListReference
<a name="API_TransitGatewayPrefixListReference"></a>

Describes a prefix list reference.

## Contents
<a name="API_TransitGatewayPrefixListReference_Contents"></a>

 ** blackhole **
Indicates whether traffic that matches this route is dropped.
Type: Boolean
Required: No

 ** prefixListId **
The ID of the prefix list.
Type: String
Required: No

 ** prefixListOwnerId **
The ID of the prefix list owner.
Type: String
Required: No

 ** state **
The state of the prefix list reference.
Type: String
Valid Values: `pending | available | modifying | deleting`
Required: No

 ** transitGatewayAttachment **
Information about the transit gateway attachment.
Type: [TransitGatewayPrefixListAttachment](API_TransitGatewayPrefixListAttachment.md) object
Required: No

 ** transitGatewayRouteTableId **
The ID of the transit gateway route table.
Type: String
Required: No

## See Also
<a name="API_TransitGatewayPrefixListReference_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/TransitGatewayPrefixListReference)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/TransitGatewayPrefixListReference)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/TransitGatewayPrefixListReference)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
