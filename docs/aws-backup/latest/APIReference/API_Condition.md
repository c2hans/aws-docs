---
source_url: https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_Condition.html
---

# Condition
<a name="API_Condition"></a>

Contains an array of triplets made up of a condition type (such as `StringEquals`), a key, and a value. Used to filter resources using their tags and assign them to a backup plan. Case sensitive.

## Contents
<a name="API_Condition_Contents"></a>

 ** ConditionKey **   <a name="Backup-Type-Condition-ConditionKey"></a>
The key in a key-value pair. For example, in the tag `Department: Accounting`, `Department` is the key.
Type: String
Required: Yes

 ** ConditionType **   <a name="Backup-Type-Condition-ConditionType"></a>
An operation applied to a key-value pair used to assign resources to your backup plan. Condition only supports `StringEquals`. For more flexible assignment options, including `StringLike` and the ability to exclude resources from your backup plan, use `Conditions` (with an "s" on the end) for your [`BackupSelection`](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_BackupSelection.html).
Type: String
Valid Values: `STRINGEQUALS`
Required: Yes

 ** ConditionValue **   <a name="Backup-Type-Condition-ConditionValue"></a>
The value in a key-value pair. For example, in the tag `Department: Accounting`, `Accounting` is the value.
Type: String
Required: Yes

## See Also
<a name="API_Condition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/backup-2018-11-15/Condition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/backup-2018-11-15/Condition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/backup-2018-11-15/Condition)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Backup. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-backup` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
