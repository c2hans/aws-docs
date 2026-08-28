---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_BatchGetTableOptimizerError.html
---

# BatchGetTableOptimizerError
<a name="API_BatchGetTableOptimizerError"></a>

Contains details on one of the errors in the error list returned by the `BatchGetTableOptimizer` operation.

## Contents
<a name="API_BatchGetTableOptimizerError_Contents"></a>

 ** catalogId **   <a name="Glue-Type-BatchGetTableOptimizerError-catalogId"></a>
The Catalog ID of the table.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** databaseName **   <a name="Glue-Type-BatchGetTableOptimizerError-databaseName"></a>
The name of the database in the catalog in which the table resides.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** error **   <a name="Glue-Type-BatchGetTableOptimizerError-error"></a>
An `ErrorDetail` object containing code and message details about the error.
Type: [ErrorDetail](API_ErrorDetail.md) object
Required: No

 ** tableName **   <a name="Glue-Type-BatchGetTableOptimizerError-tableName"></a>
The name of the table.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** type **   <a name="Glue-Type-BatchGetTableOptimizerError-type"></a>
The type of table optimizer.
Type: String
Valid Values: `compaction | retention | orphan_file_deletion`
Required: No

## See Also
<a name="API_BatchGetTableOptimizerError_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/BatchGetTableOptimizerError)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/BatchGetTableOptimizerError)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/BatchGetTableOptimizerError)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
