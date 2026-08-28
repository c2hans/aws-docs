---
source_url: https://docs.aws.amazon.com/directconnect/latest/APIReference/API_AssociatedGateway.html
---

# AssociatedGateway
<a name="API_AssociatedGateway"></a>

Information about the associated gateway.

## Contents
<a name="API_AssociatedGateway_Contents"></a>

 ** id **   <a name="DX-Type-AssociatedGateway-id"></a>
The ID of the associated gateway.
Type: String
Required: No

 ** ownerAccount **   <a name="DX-Type-AssociatedGateway-ownerAccount"></a>
The ID of the AWS account that owns the associated virtual private gateway or transit gateway.
Type: String
Required: No

 ** region **   <a name="DX-Type-AssociatedGateway-region"></a>
The Region where the associated gateway is located.
Type: String
Required: No

 ** type **   <a name="DX-Type-AssociatedGateway-type"></a>
The type of associated gateway.
Type: String
Valid Values: `virtualPrivateGateway | transitGateway`
Required: No

## See Also
<a name="API_AssociatedGateway_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/directconnect-2012-10-25/AssociatedGateway)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/directconnect-2012-10-25/AssociatedGateway)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/directconnect-2012-10-25/AssociatedGateway)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Direct Connect Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query directconnect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
