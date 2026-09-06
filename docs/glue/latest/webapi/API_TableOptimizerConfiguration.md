---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_TableOptimizerConfiguration.html
---

# TableOptimizerConfiguration
<a name="API_TableOptimizerConfiguration"></a>

Contains details on the configuration of a table optimizer. You pass this configuration when creating or updating a table optimizer.

## Contents
<a name="API_TableOptimizerConfiguration_Contents"></a>

 ** compactionConfiguration **   <a name="Glue-Type-TableOptimizerConfiguration-compactionConfiguration"></a>
The configuration for a compaction optimizer. This configuration defines how data files in your table will be compacted to improve query performance and reduce storage costs.
Type: [CompactionConfiguration](API_CompactionConfiguration.md) object
Required: No

 ** enabled **   <a name="Glue-Type-TableOptimizerConfiguration-enabled"></a>
Whether table optimization is enabled.
Type: Boolean
Required: No

 ** orphanFileDeletionConfiguration **   <a name="Glue-Type-TableOptimizerConfiguration-orphanFileDeletionConfiguration"></a>
The configuration for an orphan file deletion optimizer.
Type: [OrphanFileDeletionConfiguration](API_OrphanFileDeletionConfiguration.md) object
Required: No

 ** retentionConfiguration **   <a name="Glue-Type-TableOptimizerConfiguration-retentionConfiguration"></a>
The configuration for a snapshot retention optimizer.
Type: [RetentionConfiguration](API_RetentionConfiguration.md) object
Required: No

 ** roleArn **   <a name="Glue-Type-TableOptimizerConfiguration-roleArn"></a>
A role passed by the caller which gives the service permission to update the resources associated with the optimizer on the caller's behalf.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Required: No

 ** vpcConfiguration **   <a name="Glue-Type-TableOptimizerConfiguration-vpcConfiguration"></a>
A `TableOptimizerVpcConfiguration` object representing the VPC configuration for a table optimizer.
This configuration is necessary to perform optimization on tables that are in a customer VPC.
Type: [TableOptimizerVpcConfiguration](API_TableOptimizerVpcConfiguration.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

## See Also
<a name="API_TableOptimizerConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/TableOptimizerConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/TableOptimizerConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/TableOptimizerConfiguration)
