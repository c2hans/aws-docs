---
source_url: https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_BKS_StringCondition.html
---

# StringCondition
<a name="API_BKS_StringCondition"></a>

This contains the value of the string and can contain one or more operators.

## Contents
<a name="API_BKS_StringCondition_Contents"></a>

 ** Value **   <a name="Backup-Type-BKS_StringCondition-Value"></a>
The value of the string.
Type: String
Required: Yes

 ** Operator **   <a name="Backup-Type-BKS_StringCondition-Operator"></a>
A string that defines what values will be returned.
If this is included, avoid combinations of operators that will return all possible values. For example, including both `EQUALS_TO` and `NOT_EQUALS_TO` with a value of `4` will return all values.
Type: String
Valid Values: `EQUALS_TO | NOT_EQUALS_TO | CONTAINS | DOES_NOT_CONTAIN | BEGINS_WITH | ENDS_WITH | DOES_NOT_BEGIN_WITH | DOES_NOT_END_WITH`
Required: No

## See Also
<a name="API_BKS_StringCondition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/backupsearch-2018-05-10/StringCondition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/backupsearch-2018-05-10/StringCondition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/backupsearch-2018-05-10/StringCondition)
