---
source_url: https://docs.aws.amazon.com/cleanrooms-ml/latest/APIReference/API_DatasetInputConfig.html
---

# DatasetInputConfig
<a name="API_DatasetInputConfig"></a>

Defines the Glue data source and schema mapping information.

## Contents
<a name="API_DatasetInputConfig_Contents"></a>

 ** dataSource **   <a name="API-Type-DatasetInputConfig-dataSource"></a>
A DataSource object that specifies the Glue data source for the training data.
Type: [DataSource](API_DataSource.md) object
Required: Yes

 ** schema **   <a name="API-Type-DatasetInputConfig-schema"></a>
The schema information for the training data.
Type: Array of [ColumnSchema](API_ColumnSchema.md) objects
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Required: Yes

## See Also
<a name="API_DatasetInputConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanroomsml-2023-09-06/DatasetInputConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanroomsml-2023-09-06/DatasetInputConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanroomsml-2023-09-06/DatasetInputConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms ML. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cleanrooms-ml` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
