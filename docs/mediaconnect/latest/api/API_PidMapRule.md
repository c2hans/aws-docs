---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_PidMapRule.html
---

# PidMapRule
<a name="API_PidMapRule"></a>

A rule that selects elementary streams and specifies the action to apply to them. For more information, see [Rules](https://docs.aws.amazon.com/mediaconnect/latest/ug/pid-remapping-writing-rules.html) in the * AWS Elemental MediaConnect User Guide*.

## Contents
<a name="API_PidMapRule_Contents"></a>

 ** action **   <a name="mediaconnect-Type-PidMapRule-action"></a>
The action to apply to the elementary streams that match this rule. For more information, see [Rule actions](https://docs.aws.amazon.com/mediaconnect/latest/ug/pid-remapping-writing-rules.html#pid-remapping-actions) in the * AWS Elemental MediaConnect User Guide*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** matchExpression **   <a name="mediaconnect-Type-PidMapRule-matchExpression"></a>
An expression that selects the elementary streams that this rule applies to. For more information, see [Rule match expressions](https://docs.aws.amazon.com/mediaconnect/latest/ug/pid-remapping-writing-rules.html#pid-remapping-match-expressions) in the * AWS Elemental MediaConnect User Guide*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

## See Also
<a name="API_PidMapRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/PidMapRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/PidMapRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/PidMapRule)
