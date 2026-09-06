---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_NotStatement.html
---

# NotStatement
<a name="API_NotStatement"></a>

A logical rule statement used to negate the results of another rule statement. You provide one [Statement](API_Statement.md) within the `NotStatement`.

## Contents
<a name="API_NotStatement_Contents"></a>

 ** Statement **   <a name="WAF-Type-NotStatement-Statement"></a>
The statement to negate. You can use any statement that can be nested.
Type: [Statement](API_Statement.md) object
Required: Yes

## See Also
<a name="API_NotStatement_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wafv2-2019-07-29/NotStatement)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wafv2-2019-07-29/NotStatement)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wafv2-2019-07-29/NotStatement)
