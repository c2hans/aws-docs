---
source_url: https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_ConditionParameter.html
---

# ConditionParameter
<a name="API_ConditionParameter"></a>

Includes information about tags you define to assign tagged resources to a backup plan.

Include the prefix `aws:ResourceTag` in your tags. For example, `"aws:ResourceTag/TagKey1": "Value1"`.

## Contents
<a name="API_ConditionParameter_Contents"></a>

 ** ConditionKey **   <a name="Backup-Type-ConditionParameter-ConditionKey"></a>
The key in a key-value pair. For example, in the tag `Department: Accounting`, `Department` is the key.
Type: String
Required: No

 ** ConditionValue **   <a name="Backup-Type-ConditionParameter-ConditionValue"></a>
The value in a key-value pair. For example, in the tag `Department: Accounting`, `Accounting` is the value.
Type: String
Required: No

## See Also
<a name="API_ConditionParameter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/backup-2018-11-15/ConditionParameter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/backup-2018-11-15/ConditionParameter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/backup-2018-11-15/ConditionParameter)
