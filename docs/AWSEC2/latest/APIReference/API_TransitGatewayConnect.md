---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_TransitGatewayConnect.html
---

# TransitGatewayConnect
<a name="API_TransitGatewayConnect"></a>

Describes a transit gateway Connect attachment.

## Contents
<a name="API_TransitGatewayConnect_Contents"></a>

 ** creationTime **
The creation time.
Type: Timestamp
Required: No

 ** options **
The Connect attachment options.
Type: [TransitGatewayConnectOptions](API_TransitGatewayConnectOptions.md) object
Required: No

 ** state **
The state of the attachment.
Type: String
Valid Values: `initiating | initiatingRequest | pendingAcceptance | rollingBack | pending | available | modifying | deleting | deleted | failed | rejected | rejecting | failing`
Required: No

 ** TagSet.N **
The tags for the attachment.
Type: Array of [Tag](API_Tag.md) objects
Required: No

 ** transitGatewayAttachmentId **
The ID of the Connect attachment.
Type: String
Required: No

 ** transitGatewayId **
The ID of the transit gateway.
Type: String
Required: No

 ** transportTransitGatewayAttachmentId **
The ID of the attachment from which the Connect attachment was created.
Type: String
Required: No

## See Also
<a name="API_TransitGatewayConnect_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/TransitGatewayConnect)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/TransitGatewayConnect)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/TransitGatewayConnect)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
