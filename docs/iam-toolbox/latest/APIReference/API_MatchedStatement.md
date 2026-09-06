---
source_url: https://docs.aws.amazon.com/iam-toolbox/latest/APIReference/API_MatchedStatement.html
---

# MatchedStatement
<a name="API_MatchedStatement"></a>

A statement that matched during evaluation.

## Contents
<a name="API_MatchedStatement_Contents"></a>

 ** evaluatedEffect **   <a name="iamtoolbox-Type-MatchedStatement-evaluatedEffect"></a>
The evaluated effect of this statement. Valid values:
+  `ALLOW` - The statement allows the action.
+  `DENY` - The statement denies the action.
Type: String
Valid Values: `ALLOW | DENY`
Required: No

 ** sid **   <a name="iamtoolbox-Type-MatchedStatement-sid"></a>
The statement ID (Sid). If the statement has no Sid, one is generated for reference.
Type: String
Required: No

## See Also
<a name="API_MatchedStatement_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iam-toolbox-2018-05-10/MatchedStatement)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iam-toolbox-2018-05-10/MatchedStatement)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iam-toolbox-2018-05-10/MatchedStatement)
