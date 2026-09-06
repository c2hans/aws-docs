---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_NestedFilters.html
---

# NestedFilters
<a name="API_NestedFilters"></a>

A list of nested [Filter](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_Filter.html) objects. A resource must satisfy the conditions of all filters to be included in the results returned from the [Search](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_Search.html) API.

For example, to filter on a training job's `InputDataConfig` property with a specific channel name and `S3Uri` prefix, define the following filters:
+  `'{Name:"InputDataConfig.ChannelName", "Operator":"Equals", "Value":"train"}',`
+  `'{Name:"InputDataConfig.DataSource.S3DataSource.S3Uri", "Operator":"Contains", "Value":"mybucket/catdata"}'`

## Contents
<a name="API_NestedFilters_Contents"></a>

 ** Filters **   <a name="sagemaker-Type-NestedFilters-Filters"></a>
A list of filters. Each filter acts on a property. Filters must contain at least one `Filters` value. For example, a `NestedFilters` call might include a filter on the `PropertyName` parameter of the `InputDataConfig` property: `InputDataConfig.DataSource.S3DataSource.S3Uri`.
Type: Array of [Filter](API_Filter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 20 items.
Required: Yes

 ** NestedPropertyName **   <a name="sagemaker-Type-NestedFilters-NestedPropertyName"></a>
The name of the property to use in the nested filters. The value must match a listed property name, such as `InputDataConfig`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `.+`
Required: Yes

## See Also
<a name="API_NestedFilters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/NestedFilters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/NestedFilters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/NestedFilters)
