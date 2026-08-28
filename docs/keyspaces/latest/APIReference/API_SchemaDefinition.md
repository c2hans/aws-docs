---
source_url: https://docs.aws.amazon.com/keyspaces/latest/APIReference/API_SchemaDefinition.html
---

# SchemaDefinition
<a name="API_SchemaDefinition"></a>

Describes the schema of the table.

## Contents
<a name="API_SchemaDefinition_Contents"></a>

 ** allColumns **   <a name="keyspaces-Type-SchemaDefinition-allColumns"></a>
The regular columns of the table.
Type: Array of [ColumnDefinition](API_ColumnDefinition.md) objects
Array Members: Minimum number of 1 item.
Required: Yes

 ** partitionKeys **   <a name="keyspaces-Type-SchemaDefinition-partitionKeys"></a>
The columns that are part of the partition key of the table .
Type: Array of [PartitionKey](API_PartitionKey.md) objects
Array Members: Minimum number of 1 item.
Required: Yes

 ** clusteringKeys **   <a name="keyspaces-Type-SchemaDefinition-clusteringKeys"></a>
The columns that are part of the clustering key of the table.
Type: Array of [ClusteringKey](API_ClusteringKey.md) objects
Required: No

 ** staticColumns **   <a name="keyspaces-Type-SchemaDefinition-staticColumns"></a>
The columns that have been defined as `STATIC`. Static columns store values that are shared by all rows in the same partition.
Type: Array of [StaticColumn](API_StaticColumn.md) objects
Required: No

## See Also
<a name="API_SchemaDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/keyspaces-2022-02-10/SchemaDefinition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/keyspaces-2022-02-10/SchemaDefinition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/keyspaces-2022-02-10/SchemaDefinition)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Keyspaces (for Apache Cassandra). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query keyspaces` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
