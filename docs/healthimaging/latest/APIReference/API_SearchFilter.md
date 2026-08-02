---
source_url: https://docs.aws.amazon.com/healthimaging/latest/APIReference/API_SearchFilter.html
---

# SearchFilter
<a name="API_SearchFilter"></a>

The search filter.

## Contents
<a name="API_SearchFilter_Contents"></a>

 ** operator **   <a name="healthimaging-Type-SearchFilter-operator"></a>
The search filter operator for `imageSetDateTime`.
Type: String
Valid Values: `EQUAL | BETWEEN`
Required: Yes

 ** values **   <a name="healthimaging-Type-SearchFilter-values"></a>
The search filter values.
Type: Array of [SearchByAttributeValue](API_SearchByAttributeValue.md) objects
Array Members: Minimum number of 1 item. Maximum number of 2 items.
Required: Yes

## See Also
<a name="API_SearchFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/medical-imaging-2023-07-19/SearchFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/medical-imaging-2023-07-19/SearchFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/medical-imaging-2023-07-19/SearchFilter)
