---
source_url: https://docs.aws.amazon.com/managed-blockchain/latest/APIReference/API_VoteSummary.html
---

# VoteSummary
<a name="API_VoteSummary"></a>

 Properties of an individual vote that a member cast for a proposal.

Applies only to Hyperledger Fabric.

## Contents
<a name="API_VoteSummary_Contents"></a>

 ** MemberId **   <a name="ManagedBlockchain-Type-VoteSummary-MemberId"></a>
 The unique identifier of the member that cast the vote.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Required: No

 ** MemberName **   <a name="ManagedBlockchain-Type-VoteSummary-MemberName"></a>
 The name of the member that cast the vote.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^(?!-|[0-9])(?!.*-$)(?!.*?--)[a-zA-Z0-9-]+$`
Required: No

 ** Vote **   <a name="ManagedBlockchain-Type-VoteSummary-Vote"></a>
 The vote value, either `YES` or `NO`.
Type: String
Valid Values: `YES | NO`
Required: No

## See Also
<a name="API_VoteSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/managedblockchain-2018-09-24/VoteSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/managedblockchain-2018-09-24/VoteSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/managedblockchain-2018-09-24/VoteSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Blockchain. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managed-blockchain` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
