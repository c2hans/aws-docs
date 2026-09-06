---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_TopicRefreshDetails.html
---

# TopicRefreshDetails
<a name="API_TopicRefreshDetails"></a>

The details about the refresh of a topic.

## Contents
<a name="API_TopicRefreshDetails_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** RefreshArn **   <a name="QS-Type-TopicRefreshDetails-RefreshArn"></a>
The Amazon Resource Name (ARN) of the topic refresh.
Type: String
Required: No

 ** RefreshId **   <a name="QS-Type-TopicRefreshDetails-RefreshId"></a>
The ID of the refresh, which occurs as a result of topic creation or topic update.
Type: String
Required: No

 ** RefreshStatus **   <a name="QS-Type-TopicRefreshDetails-RefreshStatus"></a>
The status of the refresh job that indicates whether the job is still running, completed successfully, or failed.
Type: String
Valid Values: `INITIALIZED | RUNNING | FAILED | COMPLETED | CANCELLED`
Required: No

## See Also
<a name="API_TopicRefreshDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/TopicRefreshDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/TopicRefreshDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/TopicRefreshDetails)
