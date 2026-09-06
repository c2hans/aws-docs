---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_TopicDetails.html
---

# TopicDetails
<a name="API_TopicDetails"></a>

A structure that describes the details of a topic, such as its name, description, and associated data sets.

## Contents
<a name="API_TopicDetails_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ConfigOptions **   <a name="QS-Type-TopicDetails-ConfigOptions"></a>
Configuration options for a `Topic`.
Type: [TopicConfigOptions](API_TopicConfigOptions.md) object
Required: No

 ** DataSets **   <a name="QS-Type-TopicDetails-DataSets"></a>
The data sets that the topic is associated with.
Type: Array of [DatasetMetadata](API_DatasetMetadata.md) objects
Required: No

 ** Description **   <a name="QS-Type-TopicDetails-Description"></a>
The description of the topic.
Type: String
Length Constraints: Maximum length of 256.
Required: No

 ** Name **   <a name="QS-Type-TopicDetails-Name"></a>
The name of the topic.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** UserExperienceVersion **   <a name="QS-Type-TopicDetails-UserExperienceVersion"></a>
The user experience version of a topic.
Type: String
Valid Values: `LEGACY | NEW_READER_EXPERIENCE`
Required: No

## See Also
<a name="API_TopicDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/TopicDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/TopicDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/TopicDetails)
