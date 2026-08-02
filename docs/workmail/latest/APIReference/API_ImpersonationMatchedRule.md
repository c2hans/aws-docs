---
source_url: https://docs.aws.amazon.com/workmail/latest/APIReference/API_ImpersonationMatchedRule.html
---

# ImpersonationMatchedRule
<a name="API_ImpersonationMatchedRule"></a>

**Important**
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the WorkMail console or WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html).

The impersonation rule that matched the input.

## Contents
<a name="API_ImpersonationMatchedRule_Contents"></a>

 ** ImpersonationRuleId **   <a name="workmail-Type-ImpersonationMatchedRule-ImpersonationRuleId"></a>
The ID of the rule that matched the input
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_-]+`
Required: No

 ** Name **   <a name="workmail-Type-ImpersonationMatchedRule-Name"></a>
The name of the rule that matched the input.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[^\x00-\x1F\x7F\x3C\x3E\x5C]+`
Required: No

## See Also
<a name="API_ImpersonationMatchedRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workmail-2017-10-01/ImpersonationMatchedRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workmail-2017-10-01/ImpersonationMatchedRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workmail-2017-10-01/ImpersonationMatchedRule)
