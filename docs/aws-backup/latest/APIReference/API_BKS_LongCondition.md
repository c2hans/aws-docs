---
source_url: https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_BKS_LongCondition.html
---

# LongCondition
<a name="API_BKS_LongCondition"></a>

The long condition contains a `Value` and can optionally contain an `Operator`.

## Contents
<a name="API_BKS_LongCondition_Contents"></a>

 ** Value **   <a name="Backup-Type-BKS_LongCondition-Value"></a>
The value of an item included in one of the search item filters.
Type: Long
Required: Yes

 ** Operator **   <a name="Backup-Type-BKS_LongCondition-Operator"></a>
A string that defines what values will be returned.
If this is included, avoid combinations of operators that will return all possible values. For example, including both `EQUALS_TO` and `NOT_EQUALS_TO` with a value of `4` will return all values.
Type: String
Valid Values: `EQUALS_TO | NOT_EQUALS_TO | LESS_THAN_EQUAL_TO | GREATER_THAN_EQUAL_TO`
Required: No

## See Also
<a name="API_BKS_LongCondition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/backupsearch-2018-05-10/LongCondition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/backupsearch-2018-05-10/LongCondition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/backupsearch-2018-05-10/LongCondition)
