---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-cases_HiddenCaseRule.html
---

# HiddenCaseRule
<a name="API_connect-cases_HiddenCaseRule"></a>

A rule that controls field visibility based on conditions. Fields can be shown or hidden dynamically based on values in other fields.

## Contents
<a name="API_connect-cases_HiddenCaseRule_Contents"></a>

 ** conditions **   <a name="connect-Type-connect-cases_HiddenCaseRule-conditions"></a>
A list of conditions that determine field visibility.
Type: Array of [BooleanCondition](API_connect-cases_BooleanCondition.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Required: Yes

 ** defaultValue **   <a name="connect-Type-connect-cases_HiddenCaseRule-defaultValue"></a>
Whether the field is hidden when no conditions match.
Type: Boolean
Required: Yes

## See Also
<a name="API_connect-cases_HiddenCaseRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connectcases-2022-10-03/HiddenCaseRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connectcases-2022-10-03/HiddenCaseRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connectcases-2022-10-03/HiddenCaseRule)
