---
source_url: https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_LogGroup.html
---

# LogGroup
<a name="API_LogGroup"></a>

Represents a log group.

## Contents
<a name="API_LogGroup_Contents"></a>

 ** arn **   <a name="CWL-Type-LogGroup-arn"></a>
The Amazon Resource Name (ARN) of the log group. This version of the ARN includes a trailing `:*` after the log group name.
Use this version to refer to the ARN in IAM policies when specifying permissions for most API actions. The exception is when specifying permissions for [TagResource](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_TagResource.html), [UntagResource](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_UntagResource.html), and [ListTagsForResource](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_ListTagsForResource.html). The permissions for those three actions require the ARN version that doesn't include a trailing `:*`.
Type: String
Required: No

 ** bearerTokenAuthenticationEnabled **   <a name="CWL-Type-LogGroup-bearerTokenAuthenticationEnabled"></a>
Indicates whether bearer token authentication is enabled for this log group. When enabled, bearer token authentication is allowed on operations until it is explicitly disabled.
Type: Boolean
Required: No

 ** creationTime **   <a name="CWL-Type-LogGroup-creationTime"></a>
The creation time of the log group, expressed as the number of milliseconds after Jan 1, 1970 00:00:00 UTC.
Type: Long
Valid Range: Minimum value of 0.
Required: No

 ** dataProtectionStatus **   <a name="CWL-Type-LogGroup-dataProtectionStatus"></a>
Displays whether this log group has a protection policy, or whether it had one in the past. For more information, see [PutDataProtectionPolicy](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutDataProtectionPolicy.html).
Type: String
Valid Values: `ACTIVATED | DELETED | ARCHIVED | DISABLED`
Required: No

 ** deletionProtectionEnabled **   <a name="CWL-Type-LogGroup-deletionProtectionEnabled"></a>
Indicates whether deletion protection is enabled for this log group. When enabled, deletion protection blocks all deletion operations until it is explicitly disabled.
Type: Boolean
Required: No

 ** inheritedProperties **   <a name="CWL-Type-LogGroup-inheritedProperties"></a>
Displays all the properties that this log group has inherited from account-level settings.
Type: Array of strings
Valid Values: `ACCOUNT_DATA_PROTECTION`
Required: No

 ** kmsKeyId **   <a name="CWL-Type-LogGroup-kmsKeyId"></a>
The Amazon Resource Name (ARN) of the AWS KMS key to use when encrypting log data.
Type: String
Length Constraints: Maximum length of 256.
Required: No

 ** logGroupArn **   <a name="CWL-Type-LogGroup-logGroupArn"></a>
The Amazon Resource Name (ARN) of the log group. This version of the ARN doesn't include a trailing `:*` after the log group name.
Use this version to refer to the ARN in the following situations:
+ In the `logGroupIdentifier` input field in many CloudWatch Logs APIs.
+ In the `resourceArn` field in tagging APIs
+ In IAM policies, when specifying permissions for [TagResource](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_TagResource.html), [UntagResource](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_UntagResource.html), and [ListTagsForResource](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_ListTagsForResource.html).
Type: String
Required: No

 ** logGroupClass **   <a name="CWL-Type-LogGroup-logGroupClass"></a>
This specifies the log group class for this log group. There are three classes:
+ The `Standard` log class supports all CloudWatch Logs features.
+ The `Infrequent Access` log class supports a subset of CloudWatch Logs features and incurs lower costs.
+ Use the `Delivery` log class only for delivering AWS Lambda logs to store in Amazon S3 or Amazon Data Firehose. Log events in log groups in the Delivery class are kept in CloudWatch Logs for only one day. This log class doesn't offer rich CloudWatch Logs capabilities such as CloudWatch Logs Insights queries.
For details about the features supported by the Standard and Infrequent Access classes, see [Log classes](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch_Logs_Log_Classes.html)
Type: String
Valid Values: `STANDARD | INFREQUENT_ACCESS | DELIVERY`
Required: No

 ** logGroupName **   <a name="CWL-Type-LogGroup-logGroupName"></a>
The name of the log group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\.\-_/#A-Za-z0-9]+`
Required: No

 ** metricFilterCount **   <a name="CWL-Type-LogGroup-metricFilterCount"></a>
The number of metric filters.
Type: Integer
Required: No

 ** retentionInDays **   <a name="CWL-Type-LogGroup-retentionInDays"></a>
The number of days to retain the log events in the specified log group. Possible values are: 1, 3, 5, 7, 14, 30, 60, 90, 120, 150, 180, 365, 400, 545, 731, 1096, 1827, 2192, 2557, 2922, 3288, and 3653.
To set a log group so that its log events do not expire, use [DeleteRetentionPolicy](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_DeleteRetentionPolicy.html).
Type: Integer
Required: No

 ** storedBytes **   <a name="CWL-Type-LogGroup-storedBytes"></a>
The number of bytes stored.
Type: Long
Valid Range: Minimum value of 0.
Required: No

## See Also
<a name="API_LogGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/logs-2014-03-28/LogGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/logs-2014-03-28/LogGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/logs-2014-03-28/LogGroup)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch Logs. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatchLogs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
