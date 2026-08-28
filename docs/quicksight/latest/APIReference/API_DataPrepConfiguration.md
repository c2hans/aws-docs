---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DataPrepConfiguration.html
---

# DataPrepConfiguration
<a name="API_DataPrepConfiguration"></a>

Configuration for data preparation operations, defining the complete pipeline from source tables through transformations to destination tables.

## Contents
<a name="API_DataPrepConfiguration_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** DestinationTableMap **   <a name="QS-Type-DataPrepConfiguration-DestinationTableMap"></a>
A map of destination tables that receive the final prepared data.
Type: String to [DestinationTable](API_DestinationTable.md) object map
Map Entries: Maximum number of 1 item.
Key Length Constraints: Minimum length of 1. Maximum length of 64.
Key Pattern: `[0-9a-zA-Z-]*`
Required: Yes

 ** SourceTableMap **   <a name="QS-Type-DataPrepConfiguration-SourceTableMap"></a>
A map of source tables that provide information about underlying sources.
Type: String to [SourceTable](API_SourceTable.md) object map
Map Entries: Maximum number of 32 items.
Key Length Constraints: Minimum length of 1. Maximum length of 64.
Key Pattern: `[0-9a-zA-Z-]*`
Required: Yes

 ** TransformStepMap **   <a name="QS-Type-DataPrepConfiguration-TransformStepMap"></a>
A map of transformation steps that process the data.
Type: String to [TransformStep](API_TransformStep.md) object map
Map Entries: Maximum number of 256 items.
Key Length Constraints: Minimum length of 1. Maximum length of 64.
Key Pattern: `[0-9a-zA-Z-]*`
Required: Yes

## See Also
<a name="API_DataPrepConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/DataPrepConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/DataPrepConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/DataPrepConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
