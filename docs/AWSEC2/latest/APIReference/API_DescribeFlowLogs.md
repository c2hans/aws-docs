---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeFlowLogs.html
---

# DescribeFlowLogs
<a name="API_DescribeFlowLogs"></a>

Describes one or more flow logs.

To view the published flow log records, you must view the log destination. For example, the CloudWatch Logs log group, the Amazon S3 bucket, or the Kinesis Data Firehose delivery stream.

## Request Parameters
<a name="API_DescribeFlowLogs_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **Filter.N**
One or more filters.
+  `deliver-log-status` - The status of the logs delivery (`SUCCESS` \| `FAILED`).
+  `log-destination-type` - The type of destination for the flow log data (`cloud-watch-logs` \| `s3` \| `kinesis-data-firehose`).
+  `flow-log-id` - The ID of the flow log.
+  `log-group-name` - The name of the log group.
+  `resource-id` - The ID of the VPC, subnet, or network interface.
+  `traffic-type` - The type of traffic (`ACCEPT` \| `REJECT` \| `ALL`).
+  `tag`:<key> - The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key `Owner` and the value `TeamA`, specify `tag:Owner` for the filter name and `TeamA` for the filter value.
+  `tag-key` - The key of a tag assigned to the resource. Use this filter to find all resources assigned a tag with a specific key, regardless of the tag value.
Type: Array of [Filter](API_Filter.md) objects
Required: No

 **FlowLogId.N**
One or more flow log IDs.
Constraint: Maximum of 1000 flow log IDs.
Type: Array of strings
Required: No

 **MaxResults**
The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output. For more information, see [Pagination](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Query-Requests.html#api-pagination).
Type: Integer
Required: No

 **NextToken**
The token to request the next page of items. Pagination continues from the end of the items returned by the previous request.
Type: String
Required: No

## Response Elements
<a name="API_DescribeFlowLogs_ResponseElements"></a>

The following elements are returned by the service.

 **flowLogSet**
Information about the flow logs.
Type: Array of [FlowLog](API_FlowLog.md) objects

 **nextToken**
The token to request the next page of items. This value is `null` when there are no more items to return.
Type: String

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_DescribeFlowLogs_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_DescribeFlowLogs_Examples"></a>

### Example
<a name="API_DescribeFlowLogs_Example_1"></a>

This example describes all of your flow logs.

#### Sample Request
<a name="API_DescribeFlowLogs_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=DescribeFlowLogs
&AUTHPARAMS
```

#### Sample Response
<a name="API_DescribeFlowLogs_Example_1_Response"></a>

```
<DescribeFlowLogsResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>3cb46f23-099e-4bf0-891c-EXAMPLE</requestId>
    <flowLogSet>
        <item>
            <logDestination>arn:aws:s3:::my-log-bucket/my-logs/</logDestination>
            <resourceId>vpc-001234183afc7cabc</resourceId>
            <logDestinationType>s3</logDestinationType>
            <creationTime>2020-02-04T11:46:13.831Z</creationTime>
            <trafficType>ALL</trafficType>
            <deliverLogsStatus>SUCCESS</deliverLogsStatus>
            <logFormat>${version} ${instance-id} ${interface-id} ${type} ${pkt-srcaddr} ${pkt-dstaddr} ${protocol} ${bytes} ${start} ${end} ${action}</logFormat>
            <flowLogStatus>ACTIVE</flowLogStatus>
            <flowLogId>fl-1234c5499532dbabc</flowLogId>
            <maxAggregationInterval>60</maxAggregationInterval>
            <tagSet>
                <item>
                    <key>Name</key>
                    <value>FlowsForVpcA</value>
                </item>
            </tagSet>
        </item>
        <item>
            <resourceId>vpc-1122e8183afc74455</resourceId>
            <logDestinationType>cloud-watch-logs</logDestinationType>
            <deliverLogsPermissionArn>arn:aws:iam::123456789101:role/flowlogsrole</deliverLogsPermissionArn>
            <creationTime>2019-07-24T13:11:42.383Z</creationTime>
            <trafficType>ALL</trafficType>
            <deliverLogsStatus>SUCCESS</deliverLogsStatus>
            <logFormat>${version} ${account-id} ${interface-id} ${srcaddr} ${dstaddr} ${srcport} ${dstport} ${protocol} ${packets} ${bytes} ${start} ${end} ${action} ${log-status}</logFormat>
            <flowLogStatus>ACTIVE</flowLogStatus>
            <logGroupName>FlowLogsForSubnetB</logGroupName>
            <flowLogId>fl-0abc1235983d13123</flowLogId>
            <maxAggregationInterval>600</maxAggregationInterval>
            <tagSet>
                <item>
                    <key>Name</key>
                    <value>FlowsForVpcB</value>
                </item>
            </tagSet>
        </item>
    </flowLogSet>
</DescribeFlowLogsResponse>
```

## See Also
<a name="API_DescribeFlowLogs_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/DescribeFlowLogs)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/DescribeFlowLogs)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/DescribeFlowLogs)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/DescribeFlowLogs)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/DescribeFlowLogs)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/DescribeFlowLogs)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/DescribeFlowLogs)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/DescribeFlowLogs)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/DescribeFlowLogs)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/DescribeFlowLogs)
