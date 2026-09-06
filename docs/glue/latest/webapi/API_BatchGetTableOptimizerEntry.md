---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_BatchGetTableOptimizerEntry.html
---

# BatchGetTableOptimizerEntry
<a name="API_BatchGetTableOptimizerEntry"></a>

Represents a table optimizer to retrieve in the `BatchGetTableOptimizer` operation.

## Contents
<a name="API_BatchGetTableOptimizerEntry_Contents"></a>

 ** catalogId **   <a name="Glue-Type-BatchGetTableOptimizerEntry-catalogId"></a>
The Catalog ID of the table.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** databaseName **   <a name="Glue-Type-BatchGetTableOptimizerEntry-databaseName"></a>
The name of the database in the catalog in which the table resides.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** tableName **   <a name="Glue-Type-BatchGetTableOptimizerEntry-tableName"></a>
The name of the table.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** type **   <a name="Glue-Type-BatchGetTableOptimizerEntry-type"></a>
The type of table optimizer.
Type: String
Valid Values: `compaction | retention | orphan_file_deletion`
Required: No

## See Also
<a name="API_BatchGetTableOptimizerEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/BatchGetTableOptimizerEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/BatchGetTableOptimizerEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/BatchGetTableOptimizerEntry)
