---
source_url: https://docs.aws.amazon.com/cases/latest/APIReference/API_CaseRuleDetails.html
---

# CaseRuleDetails
<a name="API_connect-cases_CaseRuleDetails"></a>

Represents what rule type should take place, under what conditions. In the Connect Customer admin website, case rules are known as *case field conditions*. For more information about case field conditions, see [Add case field conditions to a case template](https://docs.aws.amazon.com/connect/latest/adminguide/case-field-conditions.html).

## Contents
<a name="API_connect-cases_CaseRuleDetails_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** fieldOptions **   <a name="connect-Type-connect-cases_CaseRuleDetails-fieldOptions"></a>
Which options are available in a child field based on the selected value in a parent field.
Type: [FieldOptionsCaseRule](API_connect-cases_FieldOptionsCaseRule.md) object
Required: No

 ** hidden **   <a name="connect-Type-connect-cases_CaseRuleDetails-hidden"></a>
Whether a field is visible, based on values in other fields.
Type: [HiddenCaseRule](API_connect-cases_HiddenCaseRule.md) object
Required: No

 ** required **   <a name="connect-Type-connect-cases_CaseRuleDetails-required"></a>
Required rule type, used to indicate whether a field is required.
Type: [RequiredCaseRule](API_connect-cases_RequiredCaseRule.md) object
Required: No

## See Also
<a name="API_connect-cases_CaseRuleDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connectcases-2022-10-03/CaseRuleDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connectcases-2022-10-03/CaseRuleDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connectcases-2022-10-03/CaseRuleDetails)
