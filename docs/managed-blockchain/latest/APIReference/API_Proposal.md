---
source_url: https://docs.aws.amazon.com/managed-blockchain/latest/APIReference/API_Proposal.html
---

# Proposal
<a name="API_Proposal"></a>

Properties of a proposal on a Managed Blockchain network.

Applies only to Hyperledger Fabric.

## Contents
<a name="API_Proposal_Contents"></a>

 ** Actions **   <a name="ManagedBlockchain-Type-Proposal-Actions"></a>
The actions to perform on the network if the proposal is `APPROVED`.
Type: [ProposalActions](API_ProposalActions.md) object
Required: No

 ** Arn **   <a name="ManagedBlockchain-Type-Proposal-Arn"></a>
The Amazon Resource Name (ARN) of the proposal. For more information about ARNs and their format, see [Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the * AWS General Reference*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `^arn:.+:.+:.+:.+:.+`
Required: No

 ** CreationDate **   <a name="ManagedBlockchain-Type-Proposal-CreationDate"></a>
 The date and time that the proposal was created.
Type: Timestamp
Required: No

 ** Description **   <a name="ManagedBlockchain-Type-Proposal-Description"></a>
The description of the proposal.
Type: String
Length Constraints: Maximum length of 128.
Required: No

 ** ExpirationDate **   <a name="ManagedBlockchain-Type-Proposal-ExpirationDate"></a>
 The date and time that the proposal expires. This is the `CreationDate` plus the `ProposalDurationInHours` that is specified in the `ProposalThresholdPolicy`. After this date and time, if members haven't cast enough votes to determine the outcome according to the voting policy, the proposal is `EXPIRED` and `Actions` aren't carried out.
Type: Timestamp
Required: No

 ** NetworkId **   <a name="ManagedBlockchain-Type-Proposal-NetworkId"></a>
The unique identifier of the network for which the proposal is made.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Required: No

 ** NoVoteCount **   <a name="ManagedBlockchain-Type-Proposal-NoVoteCount"></a>
 The current total of `NO` votes cast on the proposal by members.
Type: Integer
Required: No

 ** OutstandingVoteCount **   <a name="ManagedBlockchain-Type-Proposal-OutstandingVoteCount"></a>
 The number of votes remaining to be cast on the proposal by members. In other words, the number of members minus the sum of `YES` votes and `NO` votes.
Type: Integer
Required: No

 ** ProposalId **   <a name="ManagedBlockchain-Type-Proposal-ProposalId"></a>
The unique identifier of the proposal.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Required: No

 ** ProposedByMemberId **   <a name="ManagedBlockchain-Type-Proposal-ProposedByMemberId"></a>
The unique identifier of the member that created the proposal.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Required: No

 ** ProposedByMemberName **   <a name="ManagedBlockchain-Type-Proposal-ProposedByMemberName"></a>
The name of the member that created the proposal.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^(?!-|[0-9])(?!.*-$)(?!.*?--)[a-zA-Z0-9-]+$`
Required: No

 ** Status **   <a name="ManagedBlockchain-Type-Proposal-Status"></a>
The status of the proposal. Values are as follows:
+  `IN_PROGRESS` - The proposal is active and open for member voting.
+  `APPROVED` - The proposal was approved with sufficient `YES` votes among members according to the `VotingPolicy` specified for the `Network`. The specified proposal actions are carried out.
+  `REJECTED` - The proposal was rejected with insufficient `YES` votes among members according to the `VotingPolicy` specified for the `Network`. The specified `ProposalActions` aren't carried out.
+  `EXPIRED` - Members didn't cast the number of votes required to determine the proposal outcome before the proposal expired. The specified `ProposalActions` aren't carried out.
+  `ACTION_FAILED` - One or more of the specified `ProposalActions` in a proposal that was approved couldn't be completed because of an error. The `ACTION_FAILED` status occurs even if only one ProposalAction fails and other actions are successful.
Type: String
Valid Values: `IN_PROGRESS | APPROVED | REJECTED | EXPIRED | ACTION_FAILED`
Required: No

 ** Tags **   <a name="ManagedBlockchain-Type-Proposal-Tags"></a>
Tags assigned to the proposal. Each tag consists of a key and optional value.
For more information about tags, see [Tagging Resources](https://docs.aws.amazon.com/managed-blockchain/latest/ethereum-dev/tagging-resources.html) in the *Amazon Managed Blockchain Ethereum Developer Guide*, or [Tagging Resources](https://docs.aws.amazon.com/managed-blockchain/latest/hyperledger-fabric-dev/tagging-resources.html) in the *Amazon Managed Blockchain Hyperledger Fabric Developer Guide*.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** YesVoteCount **   <a name="ManagedBlockchain-Type-Proposal-YesVoteCount"></a>
 The current total of `YES` votes cast on the proposal by members.
Type: Integer
Required: No

## See Also
<a name="API_Proposal_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/managedblockchain-2018-09-24/Proposal)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/managedblockchain-2018-09-24/Proposal)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/managedblockchain-2018-09-24/Proposal)
