---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_IcebergTarget.html
---

# IcebergTarget
<a name="API_IcebergTarget"></a>

Specifies an Apache Iceberg data source where Iceberg tables are stored in Amazon S3.

## Contents
<a name="API_IcebergTarget_Contents"></a>

 ** ConnectionName **   <a name="Glue-Type-IcebergTarget-ConnectionName"></a>
The name of the connection to use to connect to the Iceberg target.
Type: String
Required: No

 ** Exclusions **   <a name="Glue-Type-IcebergTarget-Exclusions"></a>
A list of glob patterns used to exclude from the crawl. For more information, see [Catalog Tables with a Crawler](https://docs.aws.amazon.com/glue/latest/dg/add-crawler.html).
Type: Array of strings
Required: No

 ** MaximumTraversalDepth **   <a name="Glue-Type-IcebergTarget-MaximumTraversalDepth"></a>
The maximum depth of Amazon S3 paths that the crawler can traverse to discover the Iceberg metadata folder in your Amazon S3 path. Used to limit the crawler run time.
Type: Integer
Required: No

 ** Paths **   <a name="Glue-Type-IcebergTarget-Paths"></a>
One or more Amazon S3 paths that contains Iceberg metadata folders as `s3://bucket/prefix`.
Type: Array of strings
Required: No

## See Also
<a name="API_IcebergTarget_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/IcebergTarget)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/IcebergTarget)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/IcebergTarget)
