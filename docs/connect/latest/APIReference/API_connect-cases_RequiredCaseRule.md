---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-cases_RequiredCaseRule.html
---

# RequiredCaseRule
<a name="API_connect-cases_RequiredCaseRule"></a>

Required rule type, used to indicate whether a field is required. In the Connect Customer admin website, case rules are known as *case field conditions*. For more information about case field conditions, see [Add case field conditions to a case template](https://docs.aws.amazon.com/connect/latest/adminguide/case-field-conditions.html).

## Contents
<a name="API_connect-cases_RequiredCaseRule_Contents"></a>

 ** conditions **   <a name="connect-Type-connect-cases_RequiredCaseRule-conditions"></a>
List of conditions for the required rule; the first condition to evaluate to true dictates the value of the rule.
Type: Array of [BooleanCondition](API_connect-cases_BooleanCondition.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Required: Yes

 ** defaultValue **   <a name="connect-Type-connect-cases_RequiredCaseRule-defaultValue"></a>
The value of the rule (that is, whether the field is required) should none of the conditions evaluate to true.
Type: Boolean
Required: Yes

## See Also
<a name="API_connect-cases_RequiredCaseRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connectcases-2022-10-03/RequiredCaseRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connectcases-2022-10-03/RequiredCaseRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connectcases-2022-10-03/RequiredCaseRule)
