---
source_url: https://docs.aws.amazon.com/datapipeline/latest/APIReference/API_Operator.html
---

# Operator
<a name="API_Operator"></a>

Contains a logical operation for comparing the value of a field with a specified value.

## Contents
<a name="API_Operator_Contents"></a>

 ** type **   <a name="DP-Type-Operator-type"></a>
 The logical operation to be performed: equal (`EQ`), equal reference (`REF_EQ`), less than or equal (`LE`), greater than or equal (`GE`), or between (`BETWEEN`). Equal reference (`REF_EQ`) can be used only with reference fields. The other comparison types can be used only with String fields. The comparison types you can use apply only to certain object fields, as detailed below.
The comparison operators EQ and REF\_EQ act on the following fields:
+ name
+ @sphere
+ parent
+ @componentParent
+ @instanceParent
+ @status
+ @scheduledStartTime
+ @scheduledEndTime
+ @actualStartTime
+ @actualEndTime
 The comparison operators `GE`, `LE`, and `BETWEEN` act on the following fields:
+ @scheduledStartTime
+ @scheduledEndTime
+ @actualStartTime
+ @actualEndTime
Note that fields beginning with the at sign (@) are read-only and set by the web service. When you name fields, you should choose names containing only alpha-numeric values, as symbols may be reserved by AWS Data Pipeline. User-defined fields that you add to a pipeline should prefix their name with the string "my".
Type: String
Valid Values: `EQ | REF_EQ | LE | GE | BETWEEN`
Required: No

 ** values **   <a name="DP-Type-Operator-values"></a>
The value that the actual field value will be compared with.
Type: Array of strings
Required: No

## See Also
<a name="API_Operator_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datapipeline-2012-10-29/Operator)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datapipeline-2012-10-29/Operator)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datapipeline-2012-10-29/Operator)
