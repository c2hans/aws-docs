---
source_url: https://docs.aws.amazon.com/managed-blockchain/latest/APIReference/API_ProposalActions.html
---

# ProposalActions
<a name="API_ProposalActions"></a>

 The actions to carry out if a proposal is `APPROVED`.

Applies only to Hyperledger Fabric.

## Contents
<a name="API_ProposalActions_Contents"></a>

 ** Invitations **   <a name="ManagedBlockchain-Type-ProposalActions-Invitations"></a>
 The actions to perform for an `APPROVED` proposal to invite an AWS account to create a member and join the network.
Type: Array of [InviteAction](API_InviteAction.md) objects
Required: No

 ** Removals **   <a name="ManagedBlockchain-Type-ProposalActions-Removals"></a>
 The actions to perform for an `APPROVED` proposal to remove a member from the network, which deletes the member and all associated member resources from the network.
Type: Array of [RemoveAction](API_RemoveAction.md) objects
Required: No

## See Also
<a name="API_ProposalActions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/managedblockchain-2018-09-24/ProposalActions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/managedblockchain-2018-09-24/ProposalActions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/managedblockchain-2018-09-24/ProposalActions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Blockchain. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managed-blockchain` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
