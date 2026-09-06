---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DatasetMetadata.html
---

# DatasetMetadata
<a name="API_DatasetMetadata"></a>

A structure that represents a dataset.

## Contents
<a name="API_DatasetMetadata_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** DatasetArn **   <a name="QS-Type-DatasetMetadata-DatasetArn"></a>
The Amazon Resource Name (ARN) of the dataset.
Type: String
Required: Yes

 ** CalculatedFields **   <a name="QS-Type-DatasetMetadata-CalculatedFields"></a>
The list of calculated field definitions.
Type: Array of [TopicCalculatedField](API_TopicCalculatedField.md) objects
Required: No

 ** Columns **   <a name="QS-Type-DatasetMetadata-Columns"></a>
The list of column definitions.
Type: Array of [TopicColumn](API_TopicColumn.md) objects
Required: No

 ** DataAggregation **   <a name="QS-Type-DatasetMetadata-DataAggregation"></a>
The definition of a data aggregation.
Type: [DataAggregation](API_DataAggregation.md) object
Required: No

 ** DatasetDescription **   <a name="QS-Type-DatasetMetadata-DatasetDescription"></a>
The description of the dataset.
Type: String
Length Constraints: Maximum length of 256.
Required: No

 ** DatasetName **   <a name="QS-Type-DatasetMetadata-DatasetName"></a>
The name of the dataset.
Type: String
Length Constraints: Maximum length of 256.
Required: No

 ** Filters **   <a name="QS-Type-DatasetMetadata-Filters"></a>
The list of filter definitions.
Type: Array of [TopicFilter](API_TopicFilter.md) objects
Required: No

 ** NamedEntities **   <a name="QS-Type-DatasetMetadata-NamedEntities"></a>
The list of named entities definitions.
Type: Array of [TopicNamedEntity](API_TopicNamedEntity.md) objects
Required: No

## See Also
<a name="API_DatasetMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/DatasetMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/DatasetMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/DatasetMetadata)
