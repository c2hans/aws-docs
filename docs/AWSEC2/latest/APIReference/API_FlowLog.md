---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_FlowLog.html
---

# FlowLog
<a name="API_FlowLog"></a>

Describes a flow log.

## Contents
<a name="API_FlowLog_Contents"></a>

 ** creationTime **
The date and time the flow log was created.
Type: Timestamp
Required: No

 ** deliverCrossAccountRole **
The ARN of the IAM role that allows the service to publish flow logs across accounts.
Type: String
Required: No

 ** deliverLogsErrorMessage **
Information about the error that occurred. `Rate limited` indicates that CloudWatch Logs throttling has been applied for one or more network interfaces, or that you've reached the limit on the number of log groups that you can create. `Access error` indicates that the IAM role associated with the flow log does not have sufficient permissions to publish to CloudWatch Logs. `Unknown error` indicates an internal error.
Type: String
Required: No

 ** deliverLogsPermissionArn **
The ARN of the IAM role allows the service to publish logs to CloudWatch Logs.
Type: String
Required: No

 ** deliverLogsStatus **
The status of the logs delivery (`SUCCESS` \| `FAILED`).
Type: String
Required: No

 ** destinationOptions **
The destination options.
Type: [DestinationOptionsResponse](API_DestinationOptionsResponse.md) object
Required: No

 ** flowLogId **
The ID of the flow log.
Type: String
Required: No

 ** flowLogStatus **
The status of the flow log (`ACTIVE`).
Type: String
Required: No

 ** logDestination **
The Amazon Resource Name (ARN) of the destination for the flow log data.
Type: String
Required: No

 ** logDestinationType **
The type of destination for the flow log data.
Type: String
Valid Values: `cloud-watch-logs | s3 | kinesis-data-firehose`
Required: No

 ** logFormat **
The format of the flow log record.
Type: String
Required: No

 ** logGroupName **
The name of the flow log group.
Type: String
Required: No

 ** maxAggregationInterval **
The maximum interval of time, in seconds, during which a flow of packets is captured and aggregated into a flow log record.
When a network interface is attached to a [Nitro-based instance](https://docs.aws.amazon.com/ec2/latest/instancetypes/ec2-nitro-instances.html), the aggregation interval is always 60 seconds (1 minute) or less, regardless of the specified value.
Valid Values: `60` \| `600`
Type: Integer
Required: No

 ** resourceId **
The ID of the resource being monitored.
Type: String
Required: No

 ** TagFieldSpecificationSet.N **
The tag configuration associated with the Flow Logs Amazon EC2 Tags feature fields in your custom log format.
Type: Array of [TagFieldSpecificationResponse](API_TagFieldSpecificationResponse.md) objects
Array Members: Minimum number of 1 item. Maximum number of 3 items.
Required: No

 ** TagSet.N **
The tags for the flow log.
Type: Array of [Tag](API_Tag.md) objects
Required: No

 ** trafficType **
The type of traffic captured for the flow log.
Type: String
Valid Values: `ACCEPT | REJECT | ALL`
Required: No

## See Also
<a name="API_FlowLog_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/FlowLog)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/FlowLog)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/FlowLog)
