---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_AndStatement.html
---

# AndStatement
<a name="API_AndStatement"></a>

A logical rule statement used to combine other rule statements with AND logic. You provide more than one [Statement](API_Statement.md) within the `AndStatement`.

## Contents
<a name="API_AndStatement_Contents"></a>

 ** Statements **   <a name="WAF-Type-AndStatement-Statements"></a>
The statements to combine with AND logic. You can use any statements that can be nested.
Type: Array of [Statement](API_Statement.md) objects
Required: Yes

## See Also
<a name="API_AndStatement_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wafv2-2019-07-29/AndStatement)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wafv2-2019-07-29/AndStatement)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wafv2-2019-07-29/AndStatement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS WAF. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query waf` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
