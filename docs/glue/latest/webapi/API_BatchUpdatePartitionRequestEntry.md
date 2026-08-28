---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_BatchUpdatePartitionRequestEntry.html
---

# BatchUpdatePartitionRequestEntry
<a name="API_BatchUpdatePartitionRequestEntry"></a>

A structure that contains the values and structure used to update a partition.

## Contents
<a name="API_BatchUpdatePartitionRequestEntry_Contents"></a>

 ** PartitionInput **   <a name="Glue-Type-BatchUpdatePartitionRequestEntry-PartitionInput"></a>
The structure used to update a partition.
Type: [PartitionInput](API_PartitionInput.md) object
Required: Yes

 ** PartitionValueList **   <a name="Glue-Type-BatchUpdatePartitionRequestEntry-PartitionValueList"></a>
A list of values defining the partitions.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: Yes

## See Also
<a name="API_BatchUpdatePartitionRequestEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/BatchUpdatePartitionRequestEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/BatchUpdatePartitionRequestEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/BatchUpdatePartitionRequestEntry)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
