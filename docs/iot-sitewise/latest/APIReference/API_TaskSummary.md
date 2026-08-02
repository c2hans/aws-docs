---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_TaskSummary.html
---

# TaskSummary
<a name="API_TaskSummary"></a>

Contains summary information about a task.

## Contents
<a name="API_TaskSummary_Contents"></a>

 ** createdAt **   <a name="iotsitewise-Type-TaskSummary-createdAt"></a>
The time the task was created, in Unix epoch time.
Type: Timestamp
Required: Yes

 ** status **   <a name="iotsitewise-Type-TaskSummary-status"></a>
The current lifecycle status of the task.
Type: [ResourceStatus](API_ResourceStatus.md) object
Required: Yes

 ** taskArn **   <a name="iotsitewise-Type-TaskSummary-taskArn"></a>
The ARN of the task.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `^arn:aws(-cn|-us-gov)?:[a-zA-Z0-9-:\/_\.]+$`
Required: Yes

 ** taskName **   <a name="iotsitewise-Type-TaskSummary-taskName"></a>
The name of the task.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_-]+`
Required: Yes

 ** updatedAt **   <a name="iotsitewise-Type-TaskSummary-updatedAt"></a>
The time the task was last updated, in Unix epoch time.
Type: Timestamp
Required: Yes

 ** version **   <a name="iotsitewise-Type-TaskSummary-version"></a>
The version of the task.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 10.
Pattern: `^(0|([1-9]{1}\d*))$`
Required: Yes

 ** description **   <a name="iotsitewise-Type-TaskSummary-description"></a>
The description of the task.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^\u0000-\u001F\u007F]+`
Required: No

## See Also
<a name="API_TaskSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/TaskSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/TaskSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/TaskSummary)
