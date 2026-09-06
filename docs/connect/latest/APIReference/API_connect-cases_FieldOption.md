---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-cases_FieldOption.html
---

# FieldOption
<a name="API_connect-cases_FieldOption"></a>

Object for field Options information.

## Contents
<a name="API_connect-cases_FieldOption_Contents"></a>

 ** active **   <a name="connect-Type-connect-cases_FieldOption-active"></a>
Describes whether the `FieldOption` is active (displayed) or inactive.
Type: Boolean
Required: Yes

 ** name **   <a name="connect-Type-connect-cases_FieldOption-name"></a>
 `FieldOptionName` has max length 100 and disallows trailing spaces.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `.*[\S]`
Required: Yes

 ** value **   <a name="connect-Type-connect-cases_FieldOption-value"></a>
 `FieldOptionValue` has max length 100 and must be alphanumeric with hyphens and underscores.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `.*[\S]`
Required: Yes

## See Also
<a name="API_connect-cases_FieldOption_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connectcases-2022-10-03/FieldOption)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connectcases-2022-10-03/FieldOption)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connectcases-2022-10-03/FieldOption)
