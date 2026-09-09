---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_QueryFilters.html
---

# QueryFilters
<a name="API_QueryFilters"></a>

A set of filters to narrow the set of lineage entities connected to the `StartArn`(s) returned by the `QueryLineage` API action.

## Contents
<a name="API_QueryFilters_Contents"></a>

 ** LineageTypes **   <a name="sagemaker-Type-QueryFilters-LineageTypes"></a>
Filter the lineage entities connected to the `StartArn`(s) by the type of the lineage entity.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 4 items.
Valid Values: `TrialComponent | Artifact | Context | Action`
Required: No

 ** Properties **   <a name="sagemaker-Type-QueryFilters-Properties"></a>
Filter the lineage entities connected to the `StartArn`(s) by a set if property key value pairs. If multiple pairs are provided, an entity is included in the results if it matches any of the provided pairs.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 5 items.
Key Length Constraints: Minimum length of 0. Maximum length of 256.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** Types **   <a name="sagemaker-Type-QueryFilters-Types"></a>
Filter the lineage entities connected to the `StartArn` by type. For example: `DataSet`, `Model`, `Endpoint`, or `ModelDeployment`.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 5 items.
Length Constraints: Minimum length of 0. Maximum length of 40.
Required: No

## See Also
<a name="API_QueryFilters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/QueryFilters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/QueryFilters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/QueryFilters)
