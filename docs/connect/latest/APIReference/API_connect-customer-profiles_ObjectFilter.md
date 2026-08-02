---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-customer-profiles_ObjectFilter.html
---

# ObjectFilter
<a name="API_connect-customer-profiles_ObjectFilter"></a>

The filter applied to `ListProfileObjects` response to include profile objects with the specified index values.

## Contents
<a name="API_connect-customer-profiles_ObjectFilter_Contents"></a>

 ** KeyName **   <a name="connect-Type-connect-customer-profiles_ObjectFilter-KeyName"></a>
A searchable identifier of a profile object. The predefined keys you can use to search for `_asset` include: `_assetId`, `_assetName`, and `_serialNumber`. The predefined keys you can use to search for `_case` include: `_caseId`. The predefined keys you can use to search for `_order` include: `_orderId`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`
Required: Yes

 ** Values **   <a name="connect-Type-connect-customer-profiles_ObjectFilter-Values"></a>
A list of key values.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

## See Also
<a name="API_connect-customer-profiles_ObjectFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/customer-profiles-2020-08-15/ObjectFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/customer-profiles-2020-08-15/ObjectFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/customer-profiles-2020-08-15/ObjectFilter)
