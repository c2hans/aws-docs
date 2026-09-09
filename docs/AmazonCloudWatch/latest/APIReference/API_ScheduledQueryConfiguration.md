---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_ScheduledQueryConfiguration.html
---

# ScheduledQueryConfiguration
<a name="API_ScheduledQueryConfiguration"></a>

The configuration of the CloudWatch Logs scheduled query that backs a log alarm.

## Contents
<a name="API_ScheduledQueryConfiguration_Contents"></a>

 ** AggregationExpression **   <a name="ACW-Type-ScheduledQueryConfiguration-AggregationExpression"></a>
The expression that defines how to aggregate query results into one or more scalar values for alarm evaluation. For example, `count(*)` or `avg(latency) by host | sort desc`. Length constraints: minimum 1 character, maximum 2048 characters.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: Yes

 ** QueryString **   <a name="ACW-Type-ScheduledQueryConfiguration-QueryString"></a>
The CloudWatch Logs query to execute on each scheduled run. Length constraints: maximum of 10,000 characters.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 10000.
Required: Yes

 ** ScheduleConfiguration **   <a name="ACW-Type-ScheduledQueryConfiguration-ScheduleConfiguration"></a>
The schedule and time-range offset configuration for the underlying scheduled query.
Type: [ScheduleConfiguration](API_ScheduleConfiguration.md) object
Required: Yes

 ** ScheduledQueryRoleARN **   <a name="ACW-Type-ScheduledQueryConfiguration-ScheduledQueryRoleARN"></a>
The Amazon Resource Name (ARN) of the IAM role that CloudWatch assumes when executing the scheduled query against the configured log groups.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: Yes

 ** LogGroupIdentifiers **   <a name="ACW-Type-ScheduledQueryConfiguration-LogGroupIdentifiers"></a>
The log groups to query. Each entry can be a log group name or ARN. Use the ARN form when querying log groups in a different account (for example, when running cross-account queries from a monitoring account). The list must contain between 1 and 50 entries.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** QueryARN **   <a name="ACW-Type-ScheduledQueryConfiguration-QueryARN"></a>
The Amazon Resource Name (ARN) of the CloudWatch Logs scheduled query that the alarm uses. This field is populated in `DescribeAlarms` responses.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** Tags **   <a name="ACW-Type-ScheduledQueryConfiguration-Tags"></a>
A list of key-value pairs to associate with the underlying scheduled query resource.
Type: Array of [Tag](API_Tag.md) objects
Required: No

## See Also
<a name="API_ScheduledQueryConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/monitoring-2010-08-01/ScheduledQueryConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/ScheduledQueryConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/ScheduledQueryConfiguration)
