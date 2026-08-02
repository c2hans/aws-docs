---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-cases_FieldOptionsCaseRule.html
---

# FieldOptionsCaseRule
<a name="API_connect-cases_FieldOptionsCaseRule"></a>

Rules that control which options are available in a child field based on the selected value in a parent field.

## Contents
<a name="API_connect-cases_FieldOptionsCaseRule_Contents"></a>

 ** parentChildFieldOptionsMappings **   <a name="connect-Type-connect-cases_FieldOptionsCaseRule-parentChildFieldOptionsMappings"></a>
A mapping between a parent field option value and child field option values.
Type: Array of [ParentChildFieldOptionsMapping](API_connect-cases_ParentChildFieldOptionsMapping.md) objects
Array Members: Minimum number of 1 item. Maximum number of 200 items.
Required: Yes

 ** childFieldId **   <a name="connect-Type-connect-cases_FieldOptionsCaseRule-childFieldId"></a>
The identifier of the child field whose options are controlled.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: No

 ** parentFieldId **   <a name="connect-Type-connect-cases_FieldOptionsCaseRule-parentFieldId"></a>
The identifier of the parent field that controls options.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: No

## See Also
<a name="API_connect-cases_FieldOptionsCaseRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connectcases-2022-10-03/FieldOptionsCaseRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connectcases-2022-10-03/FieldOptionsCaseRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connectcases-2022-10-03/FieldOptionsCaseRule)
