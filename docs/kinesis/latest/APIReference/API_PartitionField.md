---
source_url: https://docs.aws.amazon.com/kinesis/latest/APIReference/API_PartitionField.html
---

# PartitionField
<a name="API_PartitionField"></a>

Specifies a single partition field.

## Contents
<a name="API_PartitionField_Contents"></a>

 ** SourceName **   <a name="Streams-Type-PartitionField-SourceName"></a>
The name of the source column used for partitioning. This column must be of the `timestamptz` type.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9\.\_]+`
Required: Yes

 ** Transform **   <a name="Streams-Type-PartitionField-Transform"></a>
The partition transform to apply. The only valid value is `TIME_HOUR`.
Type: String
Valid Values: `TIME_HOUR`
Required: Yes

## See Also
<a name="API_PartitionField_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesis-2013-12-02/PartitionField)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesis-2013-12-02/PartitionField)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesis-2013-12-02/PartitionField)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Kinesis Streams. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query kinesis` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
