---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_PartitionIndexDescriptor.html
---

# PartitionIndexDescriptor
<a name="API_PartitionIndexDescriptor"></a>

A descriptor for a partition index in a table.

## Contents
<a name="API_PartitionIndexDescriptor_Contents"></a>

 ** IndexName **   <a name="Glue-Type-PartitionIndexDescriptor-IndexName"></a>
The name of the partition index.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

 ** IndexStatus **   <a name="Glue-Type-PartitionIndexDescriptor-IndexStatus"></a>
The status of the partition index.
The possible statuses are:
+ CREATING: The index is being created. When an index is in a CREATING state, the index or its table cannot be deleted.
+ ACTIVE: The index creation succeeds.
+ FAILED: The index creation fails.
+ DELETING: The index is deleted from the list of indexes.
Type: String
Valid Values: `CREATING | ACTIVE | DELETING | FAILED`
Required: Yes

 ** Keys **   <a name="Glue-Type-PartitionIndexDescriptor-Keys"></a>
A list of one or more keys, as `KeySchemaElement` structures, for the partition index.
Type: Array of [KeySchemaElement](API_KeySchemaElement.md) objects
Array Members: Minimum number of 1 item.
Required: Yes

 ** BackfillErrors **   <a name="Glue-Type-PartitionIndexDescriptor-BackfillErrors"></a>
A list of errors that can occur when registering partition indexes for an existing table.
Type: Array of [BackfillError](API_BackfillError.md) objects
Required: No

## See Also
<a name="API_PartitionIndexDescriptor_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/PartitionIndexDescriptor)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/PartitionIndexDescriptor)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/PartitionIndexDescriptor)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
