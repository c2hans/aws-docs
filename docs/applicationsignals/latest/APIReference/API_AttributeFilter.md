---
source_url: https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_AttributeFilter.html
---

# AttributeFilter
<a name="API_AttributeFilter"></a>

A structure that defines a filter for narrowing down results based on specific attribute values. This can be used to filter services by platform, environment, or other service characteristics.

## Contents
<a name="API_AttributeFilter_Contents"></a>

 ** AttributeFilterName **   <a name="applicationsignals-Type-AttributeFilter-AttributeFilterName"></a>
The name of the attribute to filter by, such as `Platform`, `Environment`, or `BusinessUnit`.
Type: String
Pattern: `[A-Za-z0-9 :/-]+`
Required: Yes

 ** AttributeFilterValues **   <a name="applicationsignals-Type-AttributeFilter-AttributeFilterValues"></a>
An array of values to match for the specified attribute. Services that have any of these values for the attribute will be included in the results.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 20 items.
Pattern: `[A-Za-z0-9 :/-]+`
Required: Yes

## See Also
<a name="API_AttributeFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/application-signals-2024-04-15/AttributeFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/application-signals-2024-04-15/AttributeFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/application-signals-2024-04-15/AttributeFilter)
