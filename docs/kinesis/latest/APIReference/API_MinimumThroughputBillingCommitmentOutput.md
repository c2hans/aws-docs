---
source_url: https://docs.aws.amazon.com/kinesis/latest/APIReference/API_MinimumThroughputBillingCommitmentOutput.html
---

# MinimumThroughputBillingCommitmentOutput
<a name="API_MinimumThroughputBillingCommitmentOutput"></a>

Represents the current status of minimum throughput billing commitment for an account.

## Contents
<a name="API_MinimumThroughputBillingCommitmentOutput_Contents"></a>

 ** Status **   <a name="Streams-Type-MinimumThroughputBillingCommitmentOutput-Status"></a>
The current status of the minimum throughput billing commitment.
Type: String
Valid Values: `ENABLED | DISABLED | ENABLED_UNTIL_EARLIEST_ALLOWED_END`
Required: Yes

 ** EarliestAllowedEndAt **   <a name="Streams-Type-MinimumThroughputBillingCommitmentOutput-EarliestAllowedEndAt"></a>
The earliest timestamp when the commitment can be ended.
Type: Timestamp
Required: No

 ** EndedAt **   <a name="Streams-Type-MinimumThroughputBillingCommitmentOutput-EndedAt"></a>
The timestamp when the commitment was ended.
Type: Timestamp
Required: No

 ** StartedAt **   <a name="Streams-Type-MinimumThroughputBillingCommitmentOutput-StartedAt"></a>
The timestamp when the commitment was started.
Type: Timestamp
Required: No

## See Also
<a name="API_MinimumThroughputBillingCommitmentOutput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesis-2013-12-02/MinimumThroughputBillingCommitmentOutput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesis-2013-12-02/MinimumThroughputBillingCommitmentOutput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesis-2013-12-02/MinimumThroughputBillingCommitmentOutput)
