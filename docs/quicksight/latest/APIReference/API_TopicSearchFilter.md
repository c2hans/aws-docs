---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_TopicSearchFilter.html
---

# TopicSearchFilter
<a name="API_TopicSearchFilter"></a>

The filter that is used to search for a topic.

## Contents
<a name="API_TopicSearchFilter_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Name **   <a name="QS-Type-TopicSearchFilter-Name"></a>
The name of the topic search filter.
Type: String
Valid Values: `QUICKSIGHT_USER | QUICKSIGHT_VIEWER_OR_OWNER | DIRECT_QUICKSIGHT_VIEWER_OR_OWNER | QUICKSIGHT_OWNER | DIRECT_QUICKSIGHT_OWNER | DIRECT_QUICKSIGHT_SOLE_OWNER | TOPIC_NAME`
Required: Yes

 ** Operator **   <a name="QS-Type-TopicSearchFilter-Operator"></a>
The operator like equals or like.
Type: String
Valid Values: `StringEquals | StringLike`
Required: Yes

 ** Value **   <a name="QS-Type-TopicSearchFilter-Value"></a>
The value of the topic search filter.
Type: String
Required: Yes

## See Also
<a name="API_TopicSearchFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/TopicSearchFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/TopicSearchFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/TopicSearchFilter)
