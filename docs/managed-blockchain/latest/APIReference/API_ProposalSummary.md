---
source_url: https://docs.aws.amazon.com/managed-blockchain/latest/APIReference/API_ProposalSummary.html
---

# ProposalSummary
<a name="API_ProposalSummary"></a>

Properties of a proposal.

Applies only to Hyperledger Fabric.

## Contents
<a name="API_ProposalSummary_Contents"></a>

 ** Arn **   <a name="ManagedBlockchain-Type-ProposalSummary-Arn"></a>
The Amazon Resource Name (ARN) of the proposal. For more information about ARNs and their format, see [Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the * AWS General Reference*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `^arn:.+:.+:.+:.+:.+`
Required: No

 ** CreationDate **   <a name="ManagedBlockchain-Type-ProposalSummary-CreationDate"></a>
 The date and time that the proposal was created.
Type: Timestamp
Required: No

 ** Description **   <a name="ManagedBlockchain-Type-ProposalSummary-Description"></a>
 The description of the proposal.
Type: String
Length Constraints: Maximum length of 128.
Required: No

 ** ExpirationDate **   <a name="ManagedBlockchain-Type-ProposalSummary-ExpirationDate"></a>
 The date and time that the proposal expires. This is the `CreationDate` plus the `ProposalDurationInHours` that is specified in the `ProposalThresholdPolicy`. After this date and time, if members haven't cast enough votes to determine the outcome according to the voting policy, the proposal is `EXPIRED` and `Actions` aren't carried out.
Type: Timestamp
Required: No

 ** ProposalId **   <a name="ManagedBlockchain-Type-ProposalSummary-ProposalId"></a>
 The unique identifier of the proposal.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Required: No

 ** ProposedByMemberId **   <a name="ManagedBlockchain-Type-ProposalSummary-ProposedByMemberId"></a>
 The unique identifier of the member that created the proposal.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Required: No

 ** ProposedByMemberName **   <a name="ManagedBlockchain-Type-ProposalSummary-ProposedByMemberName"></a>
 The name of the member that created the proposal.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^(?!-|[0-9])(?!.*-$)(?!.*?--)[a-zA-Z0-9-]+$`
Required: No

 ** Status **   <a name="ManagedBlockchain-Type-ProposalSummary-Status"></a>
The status of the proposal. Values are as follows:
+  `IN_PROGRESS` - The proposal is active and open for member voting.
+  `APPROVED` - The proposal was approved with sufficient `YES` votes among members according to the `VotingPolicy` specified for the `Network`. The specified proposal actions are carried out.
+  `REJECTED` - The proposal was rejected with insufficient `YES` votes among members according to the `VotingPolicy` specified for the `Network`. The specified `ProposalActions` aren't carried out.
+  `EXPIRED` - Members didn't cast the number of votes required to determine the proposal outcome before the proposal expired. The specified `ProposalActions` aren't carried out.
+  `ACTION_FAILED` - One or more of the specified `ProposalActions` in a proposal that was approved couldn't be completed because of an error.
Type: String
Valid Values: `IN_PROGRESS | APPROVED | REJECTED | EXPIRED | ACTION_FAILED`
Required: No

## See Also
<a name="API_ProposalSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/managedblockchain-2018-09-24/ProposalSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/managedblockchain-2018-09-24/ProposalSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/managedblockchain-2018-09-24/ProposalSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Blockchain. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managed-blockchain` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
