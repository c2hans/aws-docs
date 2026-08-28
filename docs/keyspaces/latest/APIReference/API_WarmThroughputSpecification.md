---
source_url: https://docs.aws.amazon.com/keyspaces/latest/APIReference/API_WarmThroughputSpecification.html
---

# WarmThroughputSpecification
<a name="API_WarmThroughputSpecification"></a>

Specifies the warm throughput settings for a table. Pre-warming a table by specifying warm throughput pre-provisions read and write capacity units to help avoid capacity exceeded exceptions and reduce latency when your table starts receiving traffic.

For more information about pre-warming in Amazon Keyspaces, see [Pre-warm a table in Amazon Keyspaces](https://docs.aws.amazon.com/keyspaces/latest/devguide/warm-throughput.html) in the *Amazon Keyspaces Developer Guide*.

## Contents
<a name="API_WarmThroughputSpecification_Contents"></a>

 ** readUnitsPerSecond **   <a name="keyspaces-Type-WarmThroughputSpecification-readUnitsPerSecond"></a>
The number of read capacity units per second to pre-warm the table for read capacity throughput. The minimum value is 1.
Type: Long
Valid Range: Minimum value of 1.
Required: No

 ** writeUnitsPerSecond **   <a name="keyspaces-Type-WarmThroughputSpecification-writeUnitsPerSecond"></a>
The number of write capacity units per second to pre-warm the table for write capacity throughput. The minimum value is 1.
Type: Long
Valid Range: Minimum value of 1.
Required: No

## See Also
<a name="API_WarmThroughputSpecification_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/keyspaces-2022-02-10/WarmThroughputSpecification)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/keyspaces-2022-02-10/WarmThroughputSpecification)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/keyspaces-2022-02-10/WarmThroughputSpecification)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Keyspaces (for Apache Cassandra). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query keyspaces` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
