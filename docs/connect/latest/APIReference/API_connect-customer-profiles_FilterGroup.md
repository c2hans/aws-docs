---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-customer-profiles_FilterGroup.html
---

# FilterGroup
<a name="API_connect-customer-profiles_FilterGroup"></a>

Object that holds the dimensions to filter on.

## Contents
<a name="API_connect-customer-profiles_FilterGroup_Contents"></a>

 ** Dimensions **   <a name="connect-Type-connect-customer-profiles_FilterGroup-Dimensions"></a>
Object that holds the attributes to filter on.
Type: Array of [FilterDimension](API_connect-customer-profiles_FilterDimension.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: Yes

 ** Type **   <a name="connect-Type-connect-customer-profiles_FilterGroup-Type"></a>
The type of logical relationship between the dimensions of the Filter group.
Type: String
Valid Values: `ALL | ANY | NONE`
Required: Yes

## See Also
<a name="API_connect-customer-profiles_FilterGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/customer-profiles-2020-08-15/FilterGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/customer-profiles-2020-08-15/FilterGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/customer-profiles-2020-08-15/FilterGroup)
