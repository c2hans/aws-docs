---
source_url: https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_ConnectPeerSummary.html
---

# ConnectPeerSummary
<a name="API_ConnectPeerSummary"></a>

Summary description of a Connect peer.

## Contents
<a name="API_ConnectPeerSummary_Contents"></a>

 ** ConnectAttachmentId **   <a name="networkmanager-Type-ConnectPeerSummary-ConnectAttachmentId"></a>
The ID of a Connect peer attachment.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 50.
Pattern: `^attachment-([0-9a-f]{8,17})$`
Required: No

 ** ConnectPeerId **   <a name="networkmanager-Type-ConnectPeerSummary-ConnectPeerId"></a>
The ID of a Connect peer.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 50.
Pattern: `^connect-peer-([0-9a-f]{8,17})$`
Required: No

 ** ConnectPeerState **   <a name="networkmanager-Type-ConnectPeerSummary-ConnectPeerState"></a>
The state of a Connect peer.
Type: String
Valid Values: `CREATING | FAILED | AVAILABLE | DELETING`
Required: No

 ** CoreNetworkId **   <a name="networkmanager-Type-ConnectPeerSummary-CoreNetworkId"></a>
The ID of a core network.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 50.
Pattern: `^core-network-([0-9a-f]{8,17})$`
Required: No

 ** CreatedAt **   <a name="networkmanager-Type-ConnectPeerSummary-CreatedAt"></a>
The timestamp when a Connect peer was created.
Type: Timestamp
Required: No

 ** EdgeLocation **   <a name="networkmanager-Type-ConnectPeerSummary-EdgeLocation"></a>
The Region where the edge is located.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[\s\S]*`
Required: No

 ** SubnetArn **   <a name="networkmanager-Type-ConnectPeerSummary-SubnetArn"></a>
The subnet ARN for the Connect peer summary.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.
Pattern: `^arn:[^:]{1,63}:ec2:[^:]{0,63}:[^:]{0,63}:subnet\/subnet-[0-9a-f]{8,17}$|^$`
Required: No

 ** Tags **   <a name="networkmanager-Type-ConnectPeerSummary-Tags"></a>
The list of key-value tags associated with the Connect peer summary.
Type: Array of [Tag](API_Tag.md) objects
Required: No

## See Also
<a name="API_ConnectPeerSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/ConnectPeerSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/ConnectPeerSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/ConnectPeerSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Global Networks for Transit Gateways. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query networkmanager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
