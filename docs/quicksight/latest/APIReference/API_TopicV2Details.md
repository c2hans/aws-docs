---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_TopicV2Details.html
---

# TopicV2Details
<a name="API_TopicV2Details"></a>

The definition of a topic.

## Contents
<a name="API_TopicV2Details_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Name **   <a name="QS-Type-TopicV2Details-Name"></a>
The name of the topic.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** DataSetRelations **   <a name="QS-Type-TopicV2Details-DataSetRelations"></a>
The relations between the data sets that the topic is associated with.
Type: Array of [TopicV2DataSetRelation](API_TopicV2DataSetRelation.md) objects
Array Members: Maximum number of 100 items.
Required: No

 ** DataSets **   <a name="QS-Type-TopicV2Details-DataSets"></a>
The data sets that the topic is associated with.
Type: Array of [TopicV2DataSetReference](API_TopicV2DataSetReference.md) objects
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Required: No

 ** Description **   <a name="QS-Type-TopicV2Details-Description"></a>
The description of the topic.
Type: String
Length Constraints: Maximum length of 256.
Required: No

## See Also
<a name="API_TopicV2Details_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/TopicV2Details)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/TopicV2Details)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/TopicV2Details)
