---
source_url: https://docs.aws.amazon.com/managed-blockchain/latest/APIReference/API_MemberFabricConfiguration.html
---

# MemberFabricConfiguration
<a name="API_MemberFabricConfiguration"></a>

Configuration properties for Hyperledger Fabric for a member in a Managed Blockchain network that is using the Hyperledger Fabric framework.

## Contents
<a name="API_MemberFabricConfiguration_Contents"></a>

 ** AdminPassword **   <a name="ManagedBlockchain-Type-MemberFabricConfiguration-AdminPassword"></a>
The password for the member's initial administrative user. The `AdminPassword` must be at least 8 characters long and no more than 32 characters. It must contain at least one uppercase letter, one lowercase letter, and one digit. It cannot have a single quotation mark (‘), a double quotation marks (“), a forward slash(/), a backward slash(\\), @, or a space.
Type: String
Length Constraints: Minimum length of 8. Maximum length of 32.
Pattern: `^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?!.*[@'\\"/])[a-zA-Z0-9\S]*$`
Required: Yes

 ** AdminUsername **   <a name="ManagedBlockchain-Type-MemberFabricConfiguration-AdminUsername"></a>
The user name for the member's initial administrative user.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 16.
Pattern: `^[a-zA-Z][a-zA-Z0-9]*$`
Required: Yes

## See Also
<a name="API_MemberFabricConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/managedblockchain-2018-09-24/MemberFabricConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/managedblockchain-2018-09-24/MemberFabricConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/managedblockchain-2018-09-24/MemberFabricConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Blockchain. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managed-blockchain` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
