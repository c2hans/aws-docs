---
source_url: https://docs.aws.amazon.com/evs/latest/APIReference/API_EipAssociation.html
---

# EipAssociation
<a name="API_EipAssociation"></a>

An Elastic IP address association with the elastic network interface in the VLAN subnet.

## Contents
<a name="API_EipAssociation_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** allocationId **   <a name="evs-Type-EipAssociation-allocationId"></a>
The Elastic IP address allocation ID.
Type: String
Length Constraints: Minimum length of 9. Maximum length of 26.
Pattern: `eipalloc-[a-zA-Z0-9_-]+`
Required: No

 ** associationId **   <a name="evs-Type-EipAssociation-associationId"></a>
A unique ID for the elastic IP address association with the VLAN subnet.
Type: String
Length Constraints: Minimum length of 9. Maximum length of 26.
Pattern: `eipassoc-[a-zA-Z0-9_-]+`
Required: No

 ** ipAddress **   <a name="evs-Type-EipAssociation-ipAddress"></a>
The Elastic IP address.
Type: String
Pattern: `(\d{1,3}\.){3}\d{1,3}`
Required: No

## See Also
<a name="API_EipAssociation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/evs-2023-07-27/EipAssociation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/evs-2023-07-27/EipAssociation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/evs-2023-07-27/EipAssociation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Elastic VMware Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query evs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
