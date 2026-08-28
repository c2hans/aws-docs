---
source_url: https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_SubscriptionFilter.html
---

# SubscriptionFilter
<a name="API_SubscriptionFilter"></a>

Represents a subscription filter.

## Contents
<a name="API_SubscriptionFilter_Contents"></a>

 ** applyOnTransformedLogs **   <a name="CWL-Type-SubscriptionFilter-applyOnTransformedLogs"></a>
This parameter is valid only for log groups that have an active log transformer. For more information about log transformers, see [PutTransformer](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutTransformer.html).
If this value is `true`, the subscription filter is applied on the transformed version of the log events instead of the original ingested log events.
Type: Boolean
Required: No

 ** creationTime **   <a name="CWL-Type-SubscriptionFilter-creationTime"></a>
The creation time of the subscription filter, expressed as the number of milliseconds after `Jan 1, 1970 00:00:00 UTC`.
Type: Long
Valid Range: Minimum value of 0.
Required: No

 ** destinationArn **   <a name="CWL-Type-SubscriptionFilter-destinationArn"></a>
The Amazon Resource Name (ARN) of the destination.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** distribution **   <a name="CWL-Type-SubscriptionFilter-distribution"></a>
The method used to distribute log data to the destination, which can be either random or grouped by log stream.
Type: String
Valid Values: `Random | ByLogStream`
Required: No

 ** emitSystemFields **   <a name="CWL-Type-SubscriptionFilter-emitSystemFields"></a>
The list of system fields that are included in the log events sent to the subscription destination. Returns the `emitSystemFields` value if it was specified when the subscription filter was created.
Type: Array of strings
Required: No

 ** fieldSelectionCriteria **   <a name="CWL-Type-SubscriptionFilter-fieldSelectionCriteria"></a>
The filter expression that specifies which log events are processed by this subscription filter based on system fields. Returns the `fieldSelectionCriteria` value if it was specified when the subscription filter was created.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2000.
Required: No

 ** filterName **   <a name="CWL-Type-SubscriptionFilter-filterName"></a>
The name of the subscription filter.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[^:*]*`
Required: No

 ** filterPattern **   <a name="CWL-Type-SubscriptionFilter-filterPattern"></a>
A symbolic description of how CloudWatch Logs should interpret the data in each log event. For example, a log event can contain timestamps, IP addresses, strings, and so on. You use the filter pattern to specify what to look for in the log event message.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** logGroupName **   <a name="CWL-Type-SubscriptionFilter-logGroupName"></a>
The name of the log group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\.\-_/#A-Za-z0-9]+`
Required: No

 ** roleArn **   <a name="CWL-Type-SubscriptionFilter-roleArn"></a>

Type: String
Length Constraints: Minimum length of 1.
Required: No

## See Also
<a name="API_SubscriptionFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/logs-2014-03-28/SubscriptionFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/logs-2014-03-28/SubscriptionFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/logs-2014-03-28/SubscriptionFilter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch Logs. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatchLogs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
