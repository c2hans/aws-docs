---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_TransitGatewayConnectPeer.html
---

# TransitGatewayConnectPeer
<a name="API_TransitGatewayConnectPeer"></a>

Describes a transit gateway Connect peer.

## Contents
<a name="API_TransitGatewayConnectPeer_Contents"></a>

 ** connectPeerConfiguration **
The Connect peer details.
Type: [TransitGatewayConnectPeerConfiguration](API_TransitGatewayConnectPeerConfiguration.md) object
Required: No

 ** creationTime **
The creation time.
Type: Timestamp
Required: No

 ** state **
The state of the Connect peer.
Type: String
Valid Values: `pending | available | deleting | deleted`
Required: No

 ** TagSet.N **
The tags for the Connect peer.
Type: Array of [Tag](API_Tag.md) objects
Required: No

 ** transitGatewayAttachmentId **
The ID of the Connect attachment.
Type: String
Required: No

 ** transitGatewayConnectPeerId **
The ID of the Connect peer.
Type: String
Required: No

## See Also
<a name="API_TransitGatewayConnectPeer_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/TransitGatewayConnectPeer)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/TransitGatewayConnectPeer)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/TransitGatewayConnectPeer)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
