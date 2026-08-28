---
source_url: https://docs.aws.amazon.com/mpa/latest/APIReference/API_ApprovalStrategyResponse.html
---

# ApprovalStrategyResponse
<a name="API_ApprovalStrategyResponse"></a>

Contains details for how an approval team grants approval.

## Contents
<a name="API_ApprovalStrategyResponse_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** MofN **   <a name="mpa-Type-ApprovalStrategyResponse-MofN"></a>
Minimum number of approvals (M) required for a total number of approvers (N).
Type: [MofNApprovalStrategy](API_MofNApprovalStrategy.md) object
Required: No

## See Also
<a name="API_ApprovalStrategyResponse_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mpa-2022-07-26/ApprovalStrategyResponse)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mpa-2022-07-26/ApprovalStrategyResponse)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mpa-2022-07-26/ApprovalStrategyResponse)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Multi-party approval. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mpa` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
