---
source_url: https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_BKS_TimeCondition.html
---

# TimeCondition
<a name="API_BKS_TimeCondition"></a>

A time condition denotes a creation time, last modification time, or other time.

## Contents
<a name="API_BKS_TimeCondition_Contents"></a>

 ** Value **   <a name="Backup-Type-BKS_TimeCondition-Value"></a>
This is the timestamp value of the time condition.
Type: Timestamp
Required: Yes

 ** Operator **   <a name="Backup-Type-BKS_TimeCondition-Operator"></a>
A string that defines what values will be returned.
If this is included, avoid combinations of operators that will return all possible values. For example, including both `EQUALS_TO` and `NOT_EQUALS_TO` with a value of `4` will return all values.
Type: String
Valid Values: `EQUALS_TO | NOT_EQUALS_TO | LESS_THAN_EQUAL_TO | GREATER_THAN_EQUAL_TO`
Required: No

## See Also
<a name="API_BKS_TimeCondition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/backupsearch-2018-05-10/TimeCondition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/backupsearch-2018-05-10/TimeCondition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/backupsearch-2018-05-10/TimeCondition)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Backup. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-backup` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
