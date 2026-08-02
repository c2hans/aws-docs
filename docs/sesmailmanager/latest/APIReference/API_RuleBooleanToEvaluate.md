---
source_url: https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_RuleBooleanToEvaluate.html
---

# RuleBooleanToEvaluate
<a name="API_RuleBooleanToEvaluate"></a>

The union type representing the allowed types of operands for a boolean condition.

## Contents
<a name="API_RuleBooleanToEvaluate_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** Analysis **   <a name="sesmailmanager-Type-RuleBooleanToEvaluate-Analysis"></a>
The Add On ARN and its returned value to evaluate in a boolean condition expression.
Type: [Analysis](API_Analysis.md) object
Required: No

 ** Attribute **   <a name="sesmailmanager-Type-RuleBooleanToEvaluate-Attribute"></a>
The boolean type representing the allowed attribute types for an email.
Type: String
Valid Values: `READ_RECEIPT_REQUESTED | TLS | TLS_WRAPPED`
Required: No

 ** IsInAddressList **   <a name="sesmailmanager-Type-RuleBooleanToEvaluate-IsInAddressList"></a>
The structure representing the address lists and address list attribute that will be used in evaluation of boolean expression.
Type: [RuleIsInAddressList](API_RuleIsInAddressList.md) object
Required: No

## See Also
<a name="API_RuleBooleanToEvaluate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mailmanager-2023-10-17/RuleBooleanToEvaluate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mailmanager-2023-10-17/RuleBooleanToEvaluate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mailmanager-2023-10-17/RuleBooleanToEvaluate)
