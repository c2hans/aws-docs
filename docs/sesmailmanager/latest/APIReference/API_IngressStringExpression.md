---
source_url: https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_IngressStringExpression.html
---

# IngressStringExpression
<a name="API_IngressStringExpression"></a>

The structure for a string based condition matching on the incoming mail.

## Contents
<a name="API_IngressStringExpression_Contents"></a>

 ** Evaluate **   <a name="sesmailmanager-Type-IngressStringExpression-Evaluate"></a>
The left hand side argument of a string condition expression.
Type: [IngressStringToEvaluate](API_IngressStringToEvaluate.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** Operator **   <a name="sesmailmanager-Type-IngressStringExpression-Operator"></a>
The matching operator for a string condition expression.
Type: String
Valid Values: `EQUALS | NOT_EQUALS | STARTS_WITH | ENDS_WITH | CONTAINS`
Required: Yes

 ** Values **   <a name="sesmailmanager-Type-IngressStringExpression-Values"></a>
The right hand side argument of a string condition expression.
Type: Array of strings
Required: Yes

## See Also
<a name="API_IngressStringExpression_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mailmanager-2023-10-17/IngressStringExpression)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mailmanager-2023-10-17/IngressStringExpression)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mailmanager-2023-10-17/IngressStringExpression)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SES Mail Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sesmailmanager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
