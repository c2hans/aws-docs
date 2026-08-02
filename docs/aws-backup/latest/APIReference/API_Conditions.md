---
source_url: https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_Conditions.html
---

# Conditions
<a name="API_Conditions"></a>

Contains information about which resources to include or exclude from a backup plan using their tags. Conditions are case sensitive.

## Contents
<a name="API_Conditions_Contents"></a>

 ** StringEquals **   <a name="Backup-Type-Conditions-StringEquals"></a>
Filters the values of your tagged resources for only those resources that you tagged with the same value. Also called "exact matching."
Type: Array of [ConditionParameter](API_ConditionParameter.md) objects
Required: No

 ** StringLike **   <a name="Backup-Type-Conditions-StringLike"></a>
Filters the values of your tagged resources for matching tag values with the use of a wildcard character (\*) anywhere in the string. For example, "prod\*" or "\*rod\*" matches the tag value "production".
Type: Array of [ConditionParameter](API_ConditionParameter.md) objects
Required: No

 ** StringNotEquals **   <a name="Backup-Type-Conditions-StringNotEquals"></a>
Filters the values of your tagged resources for only those resources that you tagged that do not have the same value. Also called "negated matching."
Type: Array of [ConditionParameter](API_ConditionParameter.md) objects
Required: No

 ** StringNotLike **   <a name="Backup-Type-Conditions-StringNotLike"></a>
Filters the values of your tagged resources for non-matching tag values with the use of a wildcard character (\*) anywhere in the string.
Type: Array of [ConditionParameter](API_ConditionParameter.md) objects
Required: No

## See Also
<a name="API_Conditions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/backup-2018-11-15/Conditions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/backup-2018-11-15/Conditions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/backup-2018-11-15/Conditions)
