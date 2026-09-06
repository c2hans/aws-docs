---
source_url: https://docs.aws.amazon.com/cases/latest/APIReference/API_FieldSummary.html
---

# FieldSummary
<a name="API_connect-cases_FieldSummary"></a>

Object for the summarized details of the field.

## Contents
<a name="API_connect-cases_FieldSummary_Contents"></a>

 ** fieldArn **   <a name="connect-Type-connect-cases_FieldSummary-fieldArn"></a>
The Amazon Resource Name (ARN) of the field.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: Yes

 ** fieldId **   <a name="connect-Type-connect-cases_FieldSummary-fieldId"></a>
The unique identifier of a field.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: Yes

 ** name **   <a name="connect-Type-connect-cases_FieldSummary-name"></a>
Name of the field.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `.*[\S]`
Required: Yes

 ** namespace **   <a name="connect-Type-connect-cases_FieldSummary-namespace"></a>
The namespace of a field.
Type: String
Valid Values: `System | Custom`
Required: Yes

 ** type **   <a name="connect-Type-connect-cases_FieldSummary-type"></a>
The type of a field.
Type: String
Valid Values: `Text | Number | Boolean | DateTime | SingleSelect | Url | User`
Required: Yes

 ** attributes **   <a name="connect-Type-connect-cases_FieldSummary-attributes"></a>
Union of field attributes.
Type: [FieldAttributes](API_connect-cases_FieldAttributes.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

## See Also
<a name="API_connect-cases_FieldSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connectcases-2022-10-03/FieldSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connectcases-2022-10-03/FieldSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connectcases-2022-10-03/FieldSummary)
