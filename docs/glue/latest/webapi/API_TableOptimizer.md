---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_TableOptimizer.html
---

# TableOptimizer
<a name="API_TableOptimizer"></a>

Contains details about an optimizer associated with a table.

## Contents
<a name="API_TableOptimizer_Contents"></a>

 ** configuration **   <a name="Glue-Type-TableOptimizer-configuration"></a>
A `TableOptimizerConfiguration` object that was specified when creating or updating a table optimizer.
Type: [TableOptimizerConfiguration](API_TableOptimizerConfiguration.md) object
Required: No

 ** configurationSource **   <a name="Glue-Type-TableOptimizer-configurationSource"></a>
 Specifies the source of the optimizer configuration. This indicates how the table optimizer was configured and which entity or service initiated the configuration.
Type: String
Valid Values: `catalog | table`
Required: No

 ** lastRun **   <a name="Glue-Type-TableOptimizer-lastRun"></a>
A `TableOptimizerRun` object representing the last run of the table optimizer.
Type: [TableOptimizerRun](API_TableOptimizerRun.md) object
Required: No

 ** type **   <a name="Glue-Type-TableOptimizer-type"></a>
The type of table optimizer. The valid values are:
+  `compaction`: for managing compaction with a table optimizer.
+  `retention`: for managing the retention of snapshot with a table optimizer.
+  `orphan_file_deletion`: for managing the deletion of orphan files with a table optimizer.
Type: String
Valid Values: `compaction | retention | orphan_file_deletion`
Required: No

## See Also
<a name="API_TableOptimizer_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/TableOptimizer)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/TableOptimizer)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/TableOptimizer)
