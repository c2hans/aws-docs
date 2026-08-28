---
source_url: https://docs.aws.amazon.com/firehose/latest/APIReference/API_PartitionSpec.html
---

# PartitionSpec
<a name="API_PartitionSpec"></a>

Represents how to produce partition data for a table. Partition data is produced by transforming columns in a table. Each column transform is represented by a named `PartitionField`.

Here is an example of the schema in JSON.

 `"partitionSpec": { "identity": [ {"sourceName": "column1"}, {"sourceName": "column2"}, {"sourceName": "column3"} ] }`

Amazon Data Firehose is in preview release and is subject to change.

## Contents
<a name="API_PartitionSpec_Contents"></a>

 ** Identity **   <a name="Firehose-Type-PartitionSpec-Identity"></a>
 List of identity [transforms](https://iceberg.apache.org/spec/#partition-transforms) that performs an identity transformation. The transform takes the source value, and does not modify it. Result type is the source type.
Amazon Data Firehose is in preview release and is subject to change.
Type: Array of [PartitionField](API_PartitionField.md) objects
Required: No

## See Also
<a name="API_PartitionSpec_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/firehose-2015-08-04/PartitionSpec)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/firehose-2015-08-04/PartitionSpec)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/firehose-2015-08-04/PartitionSpec)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Data Firehose. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query firehose` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
