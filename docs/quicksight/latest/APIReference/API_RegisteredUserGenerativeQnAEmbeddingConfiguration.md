---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_RegisteredUserGenerativeQnAEmbeddingConfiguration.html
---

# RegisteredUserGenerativeQnAEmbeddingConfiguration
<a name="API_RegisteredUserGenerativeQnAEmbeddingConfiguration"></a>

An object that provides information about the configuration of a Generative Q&A experience.

## Contents
<a name="API_RegisteredUserGenerativeQnAEmbeddingConfiguration_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** InitialTopicId **   <a name="QS-Type-RegisteredUserGenerativeQnAEmbeddingConfiguration-InitialTopicId"></a>
The ID of the new Q reader experience topic that you want to make the starting topic in the Generative Q&A experience. You can find a topic ID by navigating to the Topics pane in the Quick application and opening a topic. The ID is in the URL for the topic that you open.
If you don't specify an initial topic or you specify a legacy topic, a list of all shared new reader experience topics is shown in the Generative Q&A experience for your readers. When you select an initial new reader experience topic, you can specify whether or not readers are allowed to select other new reader experience topics from the available ones in the list.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[\w\-]+`
Required: No

## See Also
<a name="API_RegisteredUserGenerativeQnAEmbeddingConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/RegisteredUserGenerativeQnAEmbeddingConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/RegisteredUserGenerativeQnAEmbeddingConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/RegisteredUserGenerativeQnAEmbeddingConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
