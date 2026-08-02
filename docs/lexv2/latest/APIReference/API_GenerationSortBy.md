---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_GenerationSortBy.html
---

# GenerationSortBy
<a name="API_GenerationSortBy"></a>

Specifies the attribute and method by which to sort the generation request information.

## Contents
<a name="API_GenerationSortBy_Contents"></a>

 ** attribute **   <a name="lexv2-Type-GenerationSortBy-attribute"></a>
The attribute by which to sort the generation request information. You can sort by the following attributes.
+  `creationStartTime` – The time at which the generation request was created.
+  `lastUpdatedTime` – The time at which the generation request was last updated.
Type: String
Valid Values: `creationStartTime | lastUpdatedTime`
Required: Yes

 ** order **   <a name="lexv2-Type-GenerationSortBy-order"></a>
The order by which to sort the generation request information.
Type: String
Valid Values: `Ascending | Descending`
Required: Yes

## See Also
<a name="API_GenerationSortBy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/GenerationSortBy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/GenerationSortBy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/GenerationSortBy)
