---
source_url: https://docs.aws.amazon.com/codecommit/latest/APIReference/API_ApprovalStateChangedEventMetadata.html
---

# ApprovalStateChangedEventMetadata
<a name="API_ApprovalStateChangedEventMetadata"></a>

Returns information about a change in the approval state for a pull request.

## Contents
<a name="API_ApprovalStateChangedEventMetadata_Contents"></a>

 ** approvalStatus **   <a name="CodeCommit-Type-ApprovalStateChangedEventMetadata-approvalStatus"></a>
The approval status for the pull request.
Type: String
Valid Values: `APPROVE | REVOKE`
Required: No

 ** revisionId **   <a name="CodeCommit-Type-ApprovalStateChangedEventMetadata-revisionId"></a>
The revision ID of the pull request when the approval state changed.
Type: String
Required: No

## See Also
<a name="API_ApprovalStateChangedEventMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codecommit-2015-04-13/ApprovalStateChangedEventMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codecommit-2015-04-13/ApprovalStateChangedEventMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codecommit-2015-04-13/ApprovalStateChangedEventMetadata)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeCommit. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codecommit` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
