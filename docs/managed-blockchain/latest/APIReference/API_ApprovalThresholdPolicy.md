---
source_url: https://docs.aws.amazon.com/managed-blockchain/latest/APIReference/API_ApprovalThresholdPolicy.html
---

# ApprovalThresholdPolicy
<a name="API_ApprovalThresholdPolicy"></a>

A policy type that defines the voting rules for the network. The rules decide if a proposal is approved. Approval may be based on criteria such as the percentage of `YES` votes and the duration of the proposal. The policy applies to all proposals and is specified when the network is created.

Applies only to Hyperledger Fabric.

## Contents
<a name="API_ApprovalThresholdPolicy_Contents"></a>

 ** ProposalDurationInHours **   <a name="ManagedBlockchain-Type-ApprovalThresholdPolicy-ProposalDurationInHours"></a>
The duration from the time that a proposal is created until it expires. If members cast neither the required number of `YES` votes to approve the proposal nor the number of `NO` votes required to reject it before the duration expires, the proposal is `EXPIRED` and `ProposalActions` aren't carried out.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 168.
Required: No

 ** ThresholdComparator **   <a name="ManagedBlockchain-Type-ApprovalThresholdPolicy-ThresholdComparator"></a>
Determines whether the vote percentage must be greater than the `ThresholdPercentage` or must be greater than or equal to the `ThresholdPercentage` to be approved.
Type: String
Valid Values: `GREATER_THAN | GREATER_THAN_OR_EQUAL_TO`
Required: No

 ** ThresholdPercentage **   <a name="ManagedBlockchain-Type-ApprovalThresholdPolicy-ThresholdPercentage"></a>
The percentage of votes among all members that must be `YES` for a proposal to be approved. For example, a `ThresholdPercentage` value of `50` indicates 50%. The `ThresholdComparator` determines the precise comparison. If a `ThresholdPercentage` value of `50` is specified on a network with 10 members, along with a `ThresholdComparator` value of `GREATER_THAN`, this indicates that 6 `YES` votes are required for the proposal to be approved.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 100.
Required: No

## See Also
<a name="API_ApprovalThresholdPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/managedblockchain-2018-09-24/ApprovalThresholdPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/managedblockchain-2018-09-24/ApprovalThresholdPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/managedblockchain-2018-09-24/ApprovalThresholdPolicy)
