---
source_url: https://docs.aws.amazon.com/directconnect/latest/APIReference/API_AssociatedCoreNetwork.html
---

# AssociatedCoreNetwork
<a name="API_AssociatedCoreNetwork"></a>

The AWS Cloud WAN core network that the Direct Connect gateway is associated to. This is only returned when a Direct Connect gateway is associated to a Cloud WAN core network.

## Contents
<a name="API_AssociatedCoreNetwork_Contents"></a>

 ** attachmentId **   <a name="DX-Type-AssociatedCoreNetwork-attachmentId"></a>
the ID of the Direct Connect gateway attachment.
Type: String
Length Constraints: Minimum length of 12. Maximum length of 28.
Pattern: `^attachment-([0-9a-f]{1,17})$`
Required: No

 ** id **   <a name="DX-Type-AssociatedCoreNetwork-id"></a>
The ID of the Cloud WAN core network that the Direct Connect gateway is associated to.
Type: String
Length Constraints: Minimum length of 14. Maximum length of 30.
Pattern: `^core-network-([0-9a-f]{1,17})$`
Required: No

 ** ownerAccount **   <a name="DX-Type-AssociatedCoreNetwork-ownerAccount"></a>
The account owner of the Cloud WAN core network.
Type: String
Required: No

## See Also
<a name="API_AssociatedCoreNetwork_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/directconnect-2012-10-25/AssociatedCoreNetwork)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/directconnect-2012-10-25/AssociatedCoreNetwork)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/directconnect-2012-10-25/AssociatedCoreNetwork)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Direct Connect Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query directconnect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
