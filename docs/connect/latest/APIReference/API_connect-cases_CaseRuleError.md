---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-cases_CaseRuleError.html
---

# CaseRuleError
<a name="API_connect-cases_CaseRuleError"></a>

Error for batch describe case rules API failure. In the Connect Customer admin website, case rules are known as *case field conditions*. For more information about case field conditions, see [Add case field conditions to a case template](https://docs.aws.amazon.com/connect/latest/adminguide/case-field-conditions.html).

## Contents
<a name="API_connect-cases_CaseRuleError_Contents"></a>

 ** errorCode **   <a name="connect-Type-connect-cases_CaseRuleError-errorCode"></a>
Error code from getting a case rule.
Type: String
Required: Yes

 ** id **   <a name="connect-Type-connect-cases_CaseRuleError-id"></a>
The case rule identifier that caused the error.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: Yes

 ** message **   <a name="connect-Type-connect-cases_CaseRuleError-message"></a>
Error message from getting a case rule.
Type: String
Required: No

## See Also
<a name="API_connect-cases_CaseRuleError_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connectcases-2022-10-03/CaseRuleError)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connectcases-2022-10-03/CaseRuleError)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connectcases-2022-10-03/CaseRuleError)
