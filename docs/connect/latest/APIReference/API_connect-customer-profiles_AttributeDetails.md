---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-customer-profiles_AttributeDetails.html
---

# AttributeDetails
<a name="API_connect-customer-profiles_AttributeDetails"></a>

Mathematical expression and a list of attribute items specified in that expression.

## Contents
<a name="API_connect-customer-profiles_AttributeDetails_Contents"></a>

 ** Attributes **   <a name="connect-Type-connect-customer-profiles_AttributeDetails-Attributes"></a>
A list of attribute items specified in the mathematical expression.
Type: Array of [AttributeItem](API_connect-customer-profiles_AttributeItem.md) objects
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Required: Yes

 ** Expression **   <a name="connect-Type-connect-customer-profiles_AttributeDetails-Expression"></a>
Mathematical expression that is performed on attribute items provided in the attribute list. Each element in the expression should follow the structure of \\"{ObjectTypeName.AttributeName}\\".
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

## See Also
<a name="API_connect-customer-profiles_AttributeDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/customer-profiles-2020-08-15/AttributeDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/customer-profiles-2020-08-15/AttributeDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/customer-profiles-2020-08-15/AttributeDetails)
