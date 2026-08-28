---
source_url: https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_StorageOptimizer.html
---

# StorageOptimizer
<a name="API_StorageOptimizer"></a>

A structure describing the configuration and details of a storage optimizer.

## Contents
<a name="API_StorageOptimizer_Contents"></a>

 ** Config **   <a name="lakeformation-Type-StorageOptimizer-Config"></a>
A map of the storage optimizer configuration. Currently contains only one key-value pair: `is_enabled` indicates true or false for acceleration.
Type: String to string map
Required: No

 ** ErrorMessage **   <a name="lakeformation-Type-StorageOptimizer-ErrorMessage"></a>
A message that contains information about any error (if present).
When an acceleration result has an enabled status, the error message is empty.
When an acceleration result has a disabled status, the message describes an error or simply indicates "disabled by the user".
Type: String
Required: No

 ** LastRunDetails **   <a name="lakeformation-Type-StorageOptimizer-LastRunDetails"></a>
When an acceleration result has an enabled status, contains the details of the last job run.
Type: String
Required: No

 ** StorageOptimizerType **   <a name="lakeformation-Type-StorageOptimizer-StorageOptimizerType"></a>
The specific type of storage optimizer. The supported value is `compaction`.
Type: String
Valid Values: `COMPACTION | GARBAGE_COLLECTION | ALL`
Required: No

 ** Warnings **   <a name="lakeformation-Type-StorageOptimizer-Warnings"></a>
A message that contains information about any warnings (if present).
Type: String
Required: No

## See Also
<a name="API_StorageOptimizer_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lakeformation-2017-03-31/StorageOptimizer)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lakeformation-2017-03-31/StorageOptimizer)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lakeformation-2017-03-31/StorageOptimizer)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Lake Formation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lake-formation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
