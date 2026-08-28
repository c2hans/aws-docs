---
source_url: https://docs.aws.amazon.com/managed-blockchain/latest/APIReference/API_VotingPolicy.html
---

# VotingPolicy
<a name="API_VotingPolicy"></a>

 The voting rules for the network to decide if a proposal is accepted

Applies only to Hyperledger Fabric.

## Contents
<a name="API_VotingPolicy_Contents"></a>

 ** ApprovalThresholdPolicy **   <a name="ManagedBlockchain-Type-VotingPolicy-ApprovalThresholdPolicy"></a>
Defines the rules for the network for voting on proposals, such as the percentage of `YES` votes required for the proposal to be approved and the duration of the proposal. The policy applies to all proposals and is specified when the network is created.
Type: [ApprovalThresholdPolicy](API_ApprovalThresholdPolicy.md) object
Required: No

## See Also
<a name="API_VotingPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/managedblockchain-2018-09-24/VotingPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/managedblockchain-2018-09-24/VotingPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/managedblockchain-2018-09-24/VotingPolicy)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Blockchain. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managed-blockchain` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
