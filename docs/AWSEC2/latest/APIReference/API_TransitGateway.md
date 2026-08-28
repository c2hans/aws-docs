---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_TransitGateway.html
---

# TransitGateway
<a name="API_TransitGateway"></a>

Describes a transit gateway.

## Contents
<a name="API_TransitGateway_Contents"></a>

 ** creationTime **
The creation time.
Type: Timestamp
Required: No

 ** description **
The description of the transit gateway.
Type: String
Required: No

 ** options **
The transit gateway options.
Type: [TransitGatewayOptions](API_TransitGatewayOptions.md) object
Required: No

 ** ownerId **
The ID of the AWS account that owns the transit gateway.
Type: String
Required: No

 ** state **
The state of the transit gateway.
Type: String
Valid Values: `pending | available | modifying | deleting | deleted`
Required: No

 ** TagSet.N **
The tags for the transit gateway.
Type: Array of [Tag](API_Tag.md) objects
Required: No

 ** transitGatewayArn **
The Amazon Resource Name (ARN) of the transit gateway.
Type: String
Required: No

 ** transitGatewayId **
The ID of the transit gateway.
Type: String
Required: No

## See Also
<a name="API_TransitGateway_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/TransitGateway)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/TransitGateway)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/TransitGateway)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
