---
source_url: https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_RuleDmarcExpression.html
---

# RuleDmarcExpression
<a name="API_RuleDmarcExpression"></a>

A DMARC policy expression. The condition matches if the given DMARC policy matches that of the incoming email.

## Contents
<a name="API_RuleDmarcExpression_Contents"></a>

 ** Operator **   <a name="sesmailmanager-Type-RuleDmarcExpression-Operator"></a>
The operator to apply to the DMARC policy of the incoming email.
Type: String
Valid Values: `EQUALS | NOT_EQUALS`
Required: Yes

 ** Values **   <a name="sesmailmanager-Type-RuleDmarcExpression-Values"></a>
The values to use for the given DMARC policy operator. For the operator EQUALS, if multiple values are given, they are evaluated as an OR. That is, if any of the given values match, the condition is deemed to match. For the operator NOT\_EQUALS, if multiple values are given, they are evaluated as an AND. That is, only if the email's DMARC policy is not equal to any of the given values, then the condition is deemed to match.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Valid Values: `NONE | QUARANTINE | REJECT`
Required: Yes

## See Also
<a name="API_RuleDmarcExpression_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mailmanager-2023-10-17/RuleDmarcExpression)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mailmanager-2023-10-17/RuleDmarcExpression)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mailmanager-2023-10-17/RuleDmarcExpression)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SES Mail Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sesmailmanager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
