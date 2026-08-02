---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_WorkflowUpdate.html
---

# WorkflowUpdate
<a name="API_WorkflowUpdate"></a>

Used to update information about the investigation into the finding.

## Contents
<a name="API_WorkflowUpdate_Contents"></a>

 ** Status **   <a name="securityhub-Type-WorkflowUpdate-Status"></a>
The status of the investigation into the finding. The workflow status is specific to an individual finding. It does not affect the generation of new findings. For example, setting the workflow status to `SUPPRESSED` or `RESOLVED` does not prevent a new finding for the same issue.
The allowed values are the following.
+  `NEW` - The initial state of a finding, before it is reviewed.

  Security Hub CSPM also resets `WorkFlowStatus` from `NOTIFIED` or `RESOLVED` to `NEW` in the following cases:
  + The record state changes from `ARCHIVED` to `ACTIVE`.
  + The compliance status changes from `PASSED` to either `WARNING`, `FAILED`, or `NOT_AVAILABLE`.
+  `NOTIFIED` - Indicates that you notified the resource owner about the security issue. Used when the initial reviewer is not the resource owner, and needs intervention from the resource owner.
+  `RESOLVED` - The finding was reviewed and remediated and is now considered resolved.
+  `SUPPRESSED` - Indicates that you reviewed the finding and don't believe that any action is needed. The finding is no longer updated.
Type: String
Valid Values: `NEW | NOTIFIED | RESOLVED | SUPPRESSED`
Required: No

## See Also
<a name="API_WorkflowUpdate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/WorkflowUpdate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/WorkflowUpdate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/WorkflowUpdate)
