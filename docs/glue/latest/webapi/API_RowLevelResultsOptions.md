---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_RowLevelResultsOptions.html
---

# RowLevelResultsOptions
<a name="API_RowLevelResultsOptions"></a>

The configuration for writing row-level evaluation results.

## Contents
<a name="API_RowLevelResultsOptions_Contents"></a>

 ** CatalogTableConfig **   <a name="Glue-Type-RowLevelResultsOptions-CatalogTableConfig"></a>
The AWS Glue Data Catalog table configuration for storing the results.
Type: [CatalogTableConfigOptions](API_CatalogTableConfigOptions.md) object
Required: No

 ** MaxRowsToWrite **   <a name="Glue-Type-RowLevelResultsOptions-MaxRowsToWrite"></a>
The maximum number of rows to write in the results.
Type: Integer
Required: No

 ** ResultType **   <a name="Glue-Type-RowLevelResultsOptions-ResultType"></a>
The result type to include in the row-level results output.
Type: String
Valid Values: `ALL | PASSED_ONLY | FAILED_ONLY`
Required: No

## See Also
<a name="API_RowLevelResultsOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/RowLevelResultsOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/RowLevelResultsOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/RowLevelResultsOptions)
