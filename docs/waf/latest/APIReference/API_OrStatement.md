---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_OrStatement.html
---

# OrStatement
<a name="API_OrStatement"></a>

A logical rule statement used to combine other rule statements with OR logic. You provide more than one [Statement](API_Statement.md) within the `OrStatement`.

## Contents
<a name="API_OrStatement_Contents"></a>

 ** Statements **   <a name="WAF-Type-OrStatement-Statements"></a>
The statements to combine with OR logic. You can use any statements that can be nested.
Type: Array of [Statement](API_Statement.md) objects
Required: Yes

## See Also
<a name="API_OrStatement_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wafv2-2019-07-29/OrStatement)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wafv2-2019-07-29/OrStatement)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wafv2-2019-07-29/OrStatement)
