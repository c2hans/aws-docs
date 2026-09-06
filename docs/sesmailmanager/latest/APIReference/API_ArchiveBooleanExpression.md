---
source_url: https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_ArchiveBooleanExpression.html
---

# ArchiveBooleanExpression
<a name="API_ArchiveBooleanExpression"></a>

A boolean expression to evaluate email attribute values.

## Contents
<a name="API_ArchiveBooleanExpression_Contents"></a>

 ** Evaluate **   <a name="sesmailmanager-Type-ArchiveBooleanExpression-Evaluate"></a>
The email attribute value to evaluate.
Type: [ArchiveBooleanToEvaluate](API_ArchiveBooleanToEvaluate.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** Operator **   <a name="sesmailmanager-Type-ArchiveBooleanExpression-Operator"></a>
The boolean operator to use for evaluation.
Type: String
Valid Values: `IS_TRUE | IS_FALSE`
Required: Yes

## See Also
<a name="API_ArchiveBooleanExpression_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mailmanager-2023-10-17/ArchiveBooleanExpression)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mailmanager-2023-10-17/ArchiveBooleanExpression)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mailmanager-2023-10-17/ArchiveBooleanExpression)
