---
source_url: https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_SortAttribute.html
---

# SortAttribute
<a name="API_connect-customer-profiles_SortAttribute"></a>

Defines the characteristics and rules for sorting by a specific attribute.

## Contents
<a name="API_connect-customer-profiles_SortAttribute_Contents"></a>

 ** Name **   <a name="connect-Type-connect-customer-profiles_SortAttribute-Name"></a>
The name of the attribute to sort by.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_.-]+$`
Required: Yes

 ** Order **   <a name="connect-Type-connect-customer-profiles_SortAttribute-Order"></a>
The sort order for the attribute (ascending or descending).
Type: String
Valid Values: `ASC | DESC`
Required: Yes

 ** DataType **   <a name="connect-Type-connect-customer-profiles_SortAttribute-DataType"></a>
The data type of the sort attribute (e.g., string, number, date).
Type: String
Valid Values: `STRING | NUMBER | DATE`
Required: No

 ** Type **   <a name="connect-Type-connect-customer-profiles_SortAttribute-Type"></a>
The type of attribute (e.g., profile, calculated).
Type: String
Valid Values: `PROFILE | CALCULATED`
Required: No

## See Also
<a name="API_connect-customer-profiles_SortAttribute_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/customer-profiles-2020-08-15/SortAttribute)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/customer-profiles-2020-08-15/SortAttribute)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/customer-profiles-2020-08-15/SortAttribute)
