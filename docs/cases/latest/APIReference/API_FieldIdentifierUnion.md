---
source_url: https://docs.aws.amazon.com/cases/latest/APIReference/API_FieldIdentifierUnion.html
---

# FieldIdentifierUnion
<a name="API_connect-cases_FieldIdentifierUnion"></a>

Identifies a field by its ID or by its name. Specify only one member. Identifying a field by name is supported only in `BatchUpdateCase`.

## Contents
<a name="API_connect-cases_FieldIdentifierUnion_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** id **   <a name="connect-Type-connect-cases_FieldIdentifierUnion-id"></a>
The unique identifier of the field.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: No

 ** name **   <a name="connect-Type-connect-cases_FieldIdentifierUnion-name"></a>
The name of the field.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `.*[\S]`
Required: No

## See Also
<a name="API_connect-cases_FieldIdentifierUnion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connectcases-2022-10-03/FieldIdentifierUnion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connectcases-2022-10-03/FieldIdentifierUnion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connectcases-2022-10-03/FieldIdentifierUnion)
