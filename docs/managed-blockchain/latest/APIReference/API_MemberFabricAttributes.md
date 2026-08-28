---
source_url: https://docs.aws.amazon.com/managed-blockchain/latest/APIReference/API_MemberFabricAttributes.html
---

# MemberFabricAttributes
<a name="API_MemberFabricAttributes"></a>

Attributes of Hyperledger Fabric for a member in a Managed Blockchain network using the Hyperledger Fabric framework.

## Contents
<a name="API_MemberFabricAttributes_Contents"></a>

 ** AdminUsername **   <a name="ManagedBlockchain-Type-MemberFabricAttributes-AdminUsername"></a>
The user name for the initial administrator user for the member.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 16.
Pattern: `^[a-zA-Z][a-zA-Z0-9]*$`
Required: No

 ** CaEndpoint **   <a name="ManagedBlockchain-Type-MemberFabricAttributes-CaEndpoint"></a>
The endpoint used to access the member's certificate authority.
Type: String
Required: No

## See Also
<a name="API_MemberFabricAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/managedblockchain-2018-09-24/MemberFabricAttributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/managedblockchain-2018-09-24/MemberFabricAttributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/managedblockchain-2018-09-24/MemberFabricAttributes)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Blockchain. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managed-blockchain` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
