---
source_url: https://docs.aws.amazon.com/keyspaces/latest/APIReference/API_CapacitySpecificationSummary.html
---

# CapacitySpecificationSummary
<a name="API_CapacitySpecificationSummary"></a>

The read/write throughput capacity mode for a table. The options are:
+  `throughputMode:PAY_PER_REQUEST` and
+  `throughputMode:PROVISIONED`.

For more information, see [Read/write capacity modes](https://docs.aws.amazon.com/keyspaces/latest/devguide/ReadWriteCapacityMode.html) in the *Amazon Keyspaces Developer Guide*.

## Contents
<a name="API_CapacitySpecificationSummary_Contents"></a>

 ** throughputMode **   <a name="keyspaces-Type-CapacitySpecificationSummary-throughputMode"></a>
The read/write throughput capacity mode for a table. The options are:
+  `throughputMode:PAY_PER_REQUEST` and
+  `throughputMode:PROVISIONED` - Provisioned capacity mode requires `readCapacityUnits` and `writeCapacityUnits` as input.
The default is `throughput_mode:PAY_PER_REQUEST`.
For more information, see [Read/write capacity modes](https://docs.aws.amazon.com/keyspaces/latest/devguide/ReadWriteCapacityMode.html) in the *Amazon Keyspaces Developer Guide*.
Type: String
Valid Values: `PAY_PER_REQUEST | PROVISIONED`
Required: Yes

 ** lastUpdateToPayPerRequestTimestamp **   <a name="keyspaces-Type-CapacitySpecificationSummary-lastUpdateToPayPerRequestTimestamp"></a>
The timestamp of the last operation that changed the provisioned throughput capacity of a table.
Type: Timestamp
Required: No

 ** readCapacityUnits **   <a name="keyspaces-Type-CapacitySpecificationSummary-readCapacityUnits"></a>
The throughput capacity specified for `read` operations defined in `read capacity units` `(RCUs)`.
Type: Long
Valid Range: Minimum value of 1.
Required: No

 ** writeCapacityUnits **   <a name="keyspaces-Type-CapacitySpecificationSummary-writeCapacityUnits"></a>
The throughput capacity specified for `write` operations defined in `write capacity units` `(WCUs)`.
Type: Long
Valid Range: Minimum value of 1.
Required: No

## See Also
<a name="API_CapacitySpecificationSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/keyspaces-2022-02-10/CapacitySpecificationSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/keyspaces-2022-02-10/CapacitySpecificationSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/keyspaces-2022-02-10/CapacitySpecificationSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Keyspaces (for Apache Cassandra). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query keyspaces` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
