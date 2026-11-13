---
source_url: https://docs.aws.amazon.com/cases/latest/APIReference/API_FieldsConfiguration.html
---

# FieldsConfiguration
<a name="API_connect-cases_FieldsConfiguration"></a>

Specifies the fields whose values to take from the secondary case when you merge cases.

## Contents
<a name="API_connect-cases_FieldsConfiguration_Contents"></a>

 ** fieldIds **   <a name="connect-Type-connect-cases_FieldsConfiguration-fieldIds"></a>
The fields whose values to take from the source case. Each field must exist on the source case and must be a field that can be merged. Don't list the same field more than once.
Type: Array of [FieldIdentifier](API_connect-cases_FieldIdentifier.md) objects
Required: Yes

 ** sourceCaseId **   <a name="connect-Type-connect-cases_FieldsConfiguration-sourceCaseId"></a>
The unique identifier of the case to take the field values from. This must be the secondary case.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.
Pattern: `[A-Za-z0-9\-._/:#=+-]*`
Required: Yes

## See Also
<a name="API_connect-cases_FieldsConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connectcases-2022-10-03/FieldsConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connectcases-2022-10-03/FieldsConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connectcases-2022-10-03/FieldsConfiguration)
