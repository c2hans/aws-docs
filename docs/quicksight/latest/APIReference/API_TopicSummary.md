---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_TopicSummary.html
---

# TopicSummary
<a name="API_TopicSummary"></a>

A topic summary.

## Contents
<a name="API_TopicSummary_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Arn **   <a name="QS-Type-TopicSummary-Arn"></a>
The Amazon Resource Name (ARN) of the topic.
Type: String
Required: No

 ** Name **   <a name="QS-Type-TopicSummary-Name"></a>
The name of the topic.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** TopicId **   <a name="QS-Type-TopicSummary-TopicId"></a>
The ID for the topic. This ID is unique per AWS Region for each AWS account.
Type: String
Length Constraints: Maximum length of 256.
Pattern: `^[A-Za-z0-9-_.\\+]*$`
Required: No

 ** UserExperienceVersion **   <a name="QS-Type-TopicSummary-UserExperienceVersion"></a>
The user experience version of the topic.
Type: String
Valid Values: `LEGACY | NEW_READER_EXPERIENCE`
Required: No

## See Also
<a name="API_TopicSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/TopicSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/TopicSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/TopicSummary)
