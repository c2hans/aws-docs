---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_RegisteredUserQSearchBarEmbeddingConfiguration.html
---

# RegisteredUserQSearchBarEmbeddingConfiguration
<a name="API_RegisteredUserQSearchBarEmbeddingConfiguration"></a>

Information about the Q search bar embedding experience.

## Contents
<a name="API_RegisteredUserQSearchBarEmbeddingConfiguration_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** InitialTopicId **   <a name="QS-Type-RegisteredUserQSearchBarEmbeddingConfiguration-InitialTopicId"></a>
The ID of the legacy Q topic that you want to use as the starting topic in the Q search bar. To locate the topic ID of the topic that you want to use, open the [Quick Sight console](https://quicksight.aws.amazon.com/), navigate to the **Topics** pane, and choose thre topic that you want to use. The `TopicID` is located in the URL of the topic that opens. When you select an initial topic, you can specify whether or not readers are allowed to select other topics from the list of available topics.
If you don't specify an initial topic or if you specify a new reader experience topic, a list of all shared legacy topics is shown in the Q bar.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[\w\-]+`
Required: No

## See Also
<a name="API_RegisteredUserQSearchBarEmbeddingConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/RegisteredUserQSearchBarEmbeddingConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/RegisteredUserQSearchBarEmbeddingConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/RegisteredUserQSearchBarEmbeddingConfiguration)
