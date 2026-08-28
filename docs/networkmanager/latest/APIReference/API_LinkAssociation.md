---
source_url: https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_LinkAssociation.html
---

# LinkAssociation
<a name="API_LinkAssociation"></a>

Describes the association between a device and a link.

## Contents
<a name="API_LinkAssociation_Contents"></a>

 ** DeviceId **   <a name="networkmanager-Type-LinkAssociation-DeviceId"></a>
The device ID for the link association.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 50.
Pattern: `[\s\S]*`
Required: No

 ** GlobalNetworkId **   <a name="networkmanager-Type-LinkAssociation-GlobalNetworkId"></a>
The ID of the global network.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 50.
Pattern: `[\s\S]*`
Required: No

 ** LinkAssociationState **   <a name="networkmanager-Type-LinkAssociation-LinkAssociationState"></a>
The state of the association.
Type: String
Valid Values: `PENDING | AVAILABLE | DELETING | DELETED`
Required: No

 ** LinkId **   <a name="networkmanager-Type-LinkAssociation-LinkId"></a>
The ID of the link.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 50.
Pattern: `[\s\S]*`
Required: No

## See Also
<a name="API_LinkAssociation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/LinkAssociation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/LinkAssociation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/LinkAssociation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Global Networks for Transit Gateways. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query networkmanager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
