---
source_url: https://docs.aws.amazon.com/keyspaces/latest/APIReference/API_WarmThroughputSpecificationSummary.html
---

# WarmThroughputSpecificationSummary
<a name="API_WarmThroughputSpecificationSummary"></a>

Contains the current warm throughput settings for a table, including the configured capacity units and the current status of the warm throughput configuration.

## Contents
<a name="API_WarmThroughputSpecificationSummary_Contents"></a>

 ** readUnitsPerSecond **   <a name="keyspaces-Type-WarmThroughputSpecificationSummary-readUnitsPerSecond"></a>
The number of read capacity units per second currently configured for warm throughput.
Type: Long
Required: Yes

 ** status **   <a name="keyspaces-Type-WarmThroughputSpecificationSummary-status"></a>
The current status of the warm throughput configuration. Valid values are `AVAILABLE` when the configuration is active, and `UPDATING` when changes are being applied.
Type: String
Valid Values: `AVAILABLE | UPDATING`
Required: Yes

 ** writeUnitsPerSecond **   <a name="keyspaces-Type-WarmThroughputSpecificationSummary-writeUnitsPerSecond"></a>
The number of write capacity units per second currently configured for warm throughput.
Type: Long
Required: Yes

## See Also
<a name="API_WarmThroughputSpecificationSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/keyspaces-2022-02-10/WarmThroughputSpecificationSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/keyspaces-2022-02-10/WarmThroughputSpecificationSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/keyspaces-2022-02-10/WarmThroughputSpecificationSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Keyspaces (for Apache Cassandra). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query keyspaces` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
