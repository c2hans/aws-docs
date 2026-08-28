---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_BatchUpdatePartitionFailureEntry.html
---

# BatchUpdatePartitionFailureEntry
<a name="API_BatchUpdatePartitionFailureEntry"></a>

Contains information about a batch update partition error.

## Contents
<a name="API_BatchUpdatePartitionFailureEntry_Contents"></a>

 ** ErrorDetail **   <a name="Glue-Type-BatchUpdatePartitionFailureEntry-ErrorDetail"></a>
The details about the batch update partition error.
Type: [ErrorDetail](API_ErrorDetail.md) object
Required: No

 ** PartitionValueList **   <a name="Glue-Type-BatchUpdatePartitionFailureEntry-PartitionValueList"></a>
A list of values defining the partitions.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

## See Also
<a name="API_BatchUpdatePartitionFailureEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/BatchUpdatePartitionFailureEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/BatchUpdatePartitionFailureEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/BatchUpdatePartitionFailureEntry)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
