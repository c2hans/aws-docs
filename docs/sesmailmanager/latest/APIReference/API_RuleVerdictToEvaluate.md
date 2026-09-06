---
source_url: https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_RuleVerdictToEvaluate.html
---

# RuleVerdictToEvaluate
<a name="API_RuleVerdictToEvaluate"></a>

The verdict to evaluate in a verdict condition expression.

## Contents
<a name="API_RuleVerdictToEvaluate_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** Analysis **   <a name="sesmailmanager-Type-RuleVerdictToEvaluate-Analysis"></a>
The Add On ARN and its returned value to evaluate in a verdict condition expression.
Type: [Analysis](API_Analysis.md) object
Required: No

 ** Attribute **   <a name="sesmailmanager-Type-RuleVerdictToEvaluate-Attribute"></a>
The email verdict attribute to evaluate in a string verdict expression.
Type: String
Valid Values: `SPF | DKIM`
Required: No

## See Also
<a name="API_RuleVerdictToEvaluate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mailmanager-2023-10-17/RuleVerdictToEvaluate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mailmanager-2023-10-17/RuleVerdictToEvaluate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mailmanager-2023-10-17/RuleVerdictToEvaluate)
