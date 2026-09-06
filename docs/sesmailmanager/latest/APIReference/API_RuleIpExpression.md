---
source_url: https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_RuleIpExpression.html
---

# RuleIpExpression
<a name="API_RuleIpExpression"></a>

An IP address expression matching certain IP addresses within a given range of IP addresses.

## Contents
<a name="API_RuleIpExpression_Contents"></a>

 ** Evaluate **   <a name="sesmailmanager-Type-RuleIpExpression-Evaluate"></a>
The IP address to evaluate in this condition.
Type: [RuleIpToEvaluate](API_RuleIpToEvaluate.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** Operator **   <a name="sesmailmanager-Type-RuleIpExpression-Operator"></a>
The operator to evaluate the IP address.
Type: String
Valid Values: `CIDR_MATCHES | NOT_CIDR_MATCHES`
Required: Yes

 ** Values **   <a name="sesmailmanager-Type-RuleIpExpression-Values"></a>
The IP CIDR blocks in format "x.y.z.w/n" (eg 10.0.0.0/8) to match with the email's IP address. For the operator CIDR\_MATCHES, if multiple values are given, they are evaluated as an OR. That is, if the IP address is contained within any of the given CIDR ranges, the condition is deemed to match. For NOT\_CIDR\_MATCHES, if multiple CIDR ranges are given, the condition is deemed to match if the IP address is not contained in any of the given CIDR ranges.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 43.
Pattern: `(([0-9]|.|:|/)*)`
Required: Yes

## See Also
<a name="API_RuleIpExpression_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mailmanager-2023-10-17/RuleIpExpression)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mailmanager-2023-10-17/RuleIpExpression)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mailmanager-2023-10-17/RuleIpExpression)
