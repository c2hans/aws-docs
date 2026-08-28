---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_TargetTableConfig.html
---

# TargetTableConfig
<a name="API_TargetTableConfig"></a>

Properties used by the target leg to partition the data on the target.

## Contents
<a name="API_TargetTableConfig_Contents"></a>

 ** PartitionSpec **   <a name="Glue-Type-TargetTableConfig-PartitionSpec"></a>
Determines the file layout on the target.
Type: Array of [IntegrationPartition](API_IntegrationPartition.md) objects
Required: No

 ** TargetTableName **   <a name="Glue-Type-TargetTableConfig-TargetTableName"></a>
The optional name of a target table.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** UnnestSpec **   <a name="Glue-Type-TargetTableConfig-UnnestSpec"></a>
Specifies how nested objects are flattened to top-level elements. Valid values are: "TOPLEVEL", "FULL", or "NOUNNEST".
Type: String
Valid Values: `TOPLEVEL | FULL | NOUNNEST`
Required: No

## See Also
<a name="API_TargetTableConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/TargetTableConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/TargetTableConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/TargetTableConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
