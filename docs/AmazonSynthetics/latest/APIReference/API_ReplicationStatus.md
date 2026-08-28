---
source_url: https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_ReplicationStatus.html
---

# ReplicationStatus
<a name="API_ReplicationStatus"></a>

A structure that contains information about the replication status of a canary replica.

## Contents
<a name="API_ReplicationStatus_Contents"></a>

 ** State **   <a name="synthetics-Type-ReplicationStatus-State"></a>
The replication state of the replica. Valid values are `InProgress`, `InSync`, and `Inconsistent`.
Type: String
Valid Values: `InProgress | InSync | Inconsistent`
Required: No

 ** StateReason **   <a name="synthetics-Type-ReplicationStatus-StateReason"></a>
A description that provides more detail about the current replication state.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** StateReasonCode **   <a name="synthetics-Type-ReplicationStatus-StateReasonCode"></a>
A code that provides more detail about the current replication state.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

## See Also
<a name="API_ReplicationStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/synthetics-2017-10-11/ReplicationStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/synthetics-2017-10-11/ReplicationStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/synthetics-2017-10-11/ReplicationStatus)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch Synthetics. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonSynthetics` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
