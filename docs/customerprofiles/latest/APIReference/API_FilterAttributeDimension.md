---
source_url: https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_FilterAttributeDimension.html
---

# FilterAttributeDimension
<a name="API_connect-customer-profiles_FilterAttributeDimension"></a>

Object that defines how to filter the incoming objects for the calculated attribute.

## Contents
<a name="API_connect-customer-profiles_FilterAttributeDimension_Contents"></a>

 ** DimensionType **   <a name="connect-Type-connect-customer-profiles_FilterAttributeDimension-DimensionType"></a>
The action to filter with.
Type: String
Valid Values: `INCLUSIVE | EXCLUSIVE | CONTAINS | BEGINS_WITH | ENDS_WITH | BEFORE | AFTER | BETWEEN | NOT_BETWEEN | ON | GREATER_THAN | LESS_THAN | GREATER_THAN_OR_EQUAL | LESS_THAN_OR_EQUAL | EQUAL`
Required: Yes

 ** Values **   <a name="connect-Type-connect-customer-profiles_FilterAttributeDimension-Values"></a>
The values to apply the DimensionType on.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

## See Also
<a name="API_connect-customer-profiles_FilterAttributeDimension_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/customer-profiles-2020-08-15/FilterAttributeDimension)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/customer-profiles-2020-08-15/FilterAttributeDimension)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/customer-profiles-2020-08-15/FilterAttributeDimension)
