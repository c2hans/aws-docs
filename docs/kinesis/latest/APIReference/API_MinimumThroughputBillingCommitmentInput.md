---
source_url: https://docs.aws.amazon.com/kinesis/latest/APIReference/API_MinimumThroughputBillingCommitmentInput.html
---

# MinimumThroughputBillingCommitmentInput
<a name="API_MinimumThroughputBillingCommitmentInput"></a>

Represents the request parameters for configuring minimum throughput billing commitment.

**Note**
Minimum throughput billing commitments provide cost savings on on-demand data streams in exchange for committing to a minimum level of throughput usage.
Commitments have a minimum duration of 24 hours that must be honored before they can be disabled.
If you attempt to disable a commitment before the minimum commitment period ends, the commitment will be scheduled for automatic disable at the earliest allowed end time.
You can cancel a pending disable by enabling the commitment again before the earliest allowed end time.

## Contents
<a name="API_MinimumThroughputBillingCommitmentInput_Contents"></a>

 ** Status **   <a name="Streams-Type-MinimumThroughputBillingCommitmentInput-Status"></a>
The desired status of the minimum throughput billing commitment.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: Yes

## See Also
<a name="API_MinimumThroughputBillingCommitmentInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesis-2013-12-02/MinimumThroughputBillingCommitmentInput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesis-2013-12-02/MinimumThroughputBillingCommitmentInput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesis-2013-12-02/MinimumThroughputBillingCommitmentInput)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Kinesis Streams. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query kinesis` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
