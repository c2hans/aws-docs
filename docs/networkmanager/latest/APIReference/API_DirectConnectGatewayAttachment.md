---
source_url: https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_DirectConnectGatewayAttachment.html
---

# DirectConnectGatewayAttachment
<a name="API_DirectConnectGatewayAttachment"></a>

Describes a Direct Connect gateway attachment.

## Contents
<a name="API_DirectConnectGatewayAttachment_Contents"></a>

 ** Attachment **   <a name="networkmanager-Type-DirectConnectGatewayAttachment-Attachment"></a>
Describes a core network attachment.
Type: [Attachment](API_Attachment.md) object
Required: No

 ** DirectConnectGatewayArn **   <a name="networkmanager-Type-DirectConnectGatewayAttachment-DirectConnectGatewayArn"></a>
The Direct Connect gateway attachment ARN.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.
Pattern: `^arn:[^:]{1,63}:directconnect::[^:]{0,63}:dx-gateway\/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$`
Required: No

## See Also
<a name="API_DirectConnectGatewayAttachment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/DirectConnectGatewayAttachment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/DirectConnectGatewayAttachment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/DirectConnectGatewayAttachment)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Global Networks for Transit Gateways. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query networkmanager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
