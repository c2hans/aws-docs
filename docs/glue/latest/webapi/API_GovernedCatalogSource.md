---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_GovernedCatalogSource.html
---

# GovernedCatalogSource
<a name="API_GovernedCatalogSource"></a>

Specifies the data store in the governed AWS Glue Data Catalog.

## Contents
<a name="API_GovernedCatalogSource_Contents"></a>

 ** Database **   <a name="Glue-Type-GovernedCatalogSource-Database"></a>
The database to read from.
Type: String
Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: Yes

 ** Name **   <a name="Glue-Type-GovernedCatalogSource-Name"></a>
The name of the data store.
Type: String
Pattern: `([^\r\n])*`
Required: Yes

 ** Table **   <a name="Glue-Type-GovernedCatalogSource-Table"></a>
The database table to read from.
Type: String
Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: Yes

 ** AdditionalOptions **   <a name="Glue-Type-GovernedCatalogSource-AdditionalOptions"></a>
Specifies additional connection options.
Type: [S3SourceAdditionalOptions](API_S3SourceAdditionalOptions.md) object
Required: No

 ** PartitionPredicate **   <a name="Glue-Type-GovernedCatalogSource-PartitionPredicate"></a>
Partitions satisfying this predicate are deleted. Files within the retention period in these partitions are not deleted. Set to `""` – empty by default.
Type: String
Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: No

## See Also
<a name="API_GovernedCatalogSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/GovernedCatalogSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/GovernedCatalogSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/GovernedCatalogSource)
