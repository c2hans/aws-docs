---
source_url: https://docs.aws.amazon.com/keyspaces/latest/APIReference/API_ReplicaSpecificationSummary.html
---

# ReplicaSpecificationSummary
<a name="API_ReplicaSpecificationSummary"></a>

The Region-specific settings of a multi-Region table in the specified AWS Region.

If the multi-Region table is using provisioned capacity and has optional auto scaling policies configured, note that the Region specific summary returns both read and write capacity settings. But only Region specific read capacity settings can be configured for a multi-Region table. In a multi-Region table, your write capacity units will be synced across all AWS Regions to ensure that there is enough capacity to replicate write events across Regions.

## Contents
<a name="API_ReplicaSpecificationSummary_Contents"></a>

 ** capacitySpecification **   <a name="keyspaces-Type-ReplicaSpecificationSummary-capacitySpecification"></a>
The read/write throughput capacity mode for a table. The options are:
+  `throughputMode:PAY_PER_REQUEST` and
+  `throughputMode:PROVISIONED`.
For more information, see [Read/write capacity modes](https://docs.aws.amazon.com/keyspaces/latest/devguide/ReadWriteCapacityMode.html) in the *Amazon Keyspaces Developer Guide*.
Type: [CapacitySpecificationSummary](API_CapacitySpecificationSummary.md) object
Required: No

 ** region **   <a name="keyspaces-Type-ReplicaSpecificationSummary-region"></a>
The AWS Region.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 25.
Required: No

 ** status **   <a name="keyspaces-Type-ReplicaSpecificationSummary-status"></a>
The status of the multi-Region table in the specified AWS Region.
Type: String
Valid Values: `ACTIVE | CREATING | UPDATING | DELETING | DELETED | RESTORING | INACCESSIBLE_ENCRYPTION_CREDENTIALS`
Required: No

 ** warmThroughputSpecification **   <a name="keyspaces-Type-ReplicaSpecificationSummary-warmThroughputSpecification"></a>
The warm throughput settings for this replica, including the current status and configured read and write capacity units.
Type: [WarmThroughputSpecificationSummary](API_WarmThroughputSpecificationSummary.md) object
Required: No

## See Also
<a name="API_ReplicaSpecificationSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/keyspaces-2022-02-10/ReplicaSpecificationSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/keyspaces-2022-02-10/ReplicaSpecificationSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/keyspaces-2022-02-10/ReplicaSpecificationSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Keyspaces (for Apache Cassandra). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query keyspaces` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
