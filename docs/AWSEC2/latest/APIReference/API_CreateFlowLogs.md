---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateFlowLogs.html
---

# CreateFlowLogs
<a name="API_CreateFlowLogs"></a>

Creates one or more flow logs to capture information about IP traffic for a specific network interface, subnet, or VPC.

Flow log data for a monitored network interface is recorded as flow log records, which are log events consisting of fields that describe the traffic flow. For more information, see [Flow log records](https://docs.aws.amazon.com/vpc/latest/userguide/flow-log-records.html) in the *Amazon VPC User Guide*.

When publishing to CloudWatch Logs, flow log records are published to a log group, and each network interface has a unique log stream in the log group. When publishing to Amazon S3, flow log records for all of the monitored network interfaces are published to a single log file object that is stored in the specified bucket.

For more information, see [VPC Flow Logs](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html) in the *Amazon VPC User Guide*.

## Request Parameters
<a name="API_CreateFlowLogs_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **ClientToken**
Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see [How to ensure idempotency](https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html).
Type: String
Required: No

 **DeliverCrossAccountRole**
The ARN of the IAM role that allows Amazon EC2 to publish flow logs across accounts.
Type: String
Required: No

 **DeliverLogsPermissionArn**
The ARN of the IAM role that allows Amazon EC2 to publish flow logs to the log destination.
This parameter is required if the destination type is `cloud-watch-logs`, or if the destination type is `kinesis-data-firehose` and the delivery stream and the resources to monitor are in different accounts.
Type: String
Required: No

 **DestinationOptions**
The destination options.
Type: [DestinationOptionsRequest](API_DestinationOptionsRequest.md) object
Required: No

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **LogDestination**
The destination for the flow log data. The meaning of this parameter depends on the destination type.
+ If the destination type is `cloud-watch-logs`, specify the ARN of a CloudWatch Logs log group. For example:

  arn:aws:logs:*region*:*account\_id*:log-group:*my\_group*

  Alternatively, use the `LogGroupName` parameter.
+ If the destination type is `s3`, specify the ARN of an S3 bucket. For example:

  arn:aws:s3:::*my\_bucket*/*my\_subfolder*/

  The subfolder is optional. Note that you can't use `AWSLogs` as a subfolder name.
+ If the destination type is `kinesis-data-firehose`, specify the ARN of a Kinesis Data Firehose delivery stream. For example:

  arn:aws:firehose:*region*:*account\_id*:deliverystream:*my\_stream*
Type: String
Required: No

 **LogDestinationType**
The type of destination for the flow log data.
Default: `cloud-watch-logs`
Type: String
Valid Values: `cloud-watch-logs | s3 | kinesis-data-firehose`
Required: No

 **LogFormat**
The fields to include in the flow log record. List the fields in the order in which they should appear. If you omit this parameter, the flow log is created using the default format. If you specify this parameter, you must include at least one field. For more information about the available fields, see [Flow log records](https://docs.aws.amazon.com/vpc/latest/userguide/flow-log-records.html) in the *Amazon VPC User Guide* or [Transit Gateway Flow Log records](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-flow-logs.html#flow-log-records) in the * AWS Transit Gateway Guide*.
Specify the fields using the `${field-id}` format, separated by spaces.
Type: String
Required: No

 **LogGroupName**
The name of a new or existing CloudWatch Logs log group where Amazon EC2 publishes your flow logs.
This parameter is valid only if the destination type is `cloud-watch-logs`.
Type: String
Required: No

 **MaxAggregationInterval**
The maximum interval of time during which a flow of packets is captured and aggregated into a flow log record. The possible values are 60 seconds (1 minute) or 600 seconds (10 minutes). This parameter must be 60 seconds for transit gateway resource types.
When a network interface is attached to a [Nitro-based instance](https://docs.aws.amazon.com/ec2/latest/instancetypes/ec2-nitro-instances.html), the aggregation interval is always 60 seconds or less, regardless of the value that you specify.
Default: 600
Type: Integer
Required: No

 **ResourceId.N**
The IDs of the resources to monitor. For example, if the resource type is `VPC`, specify the IDs of the VPCs.
Constraints: Maximum of 25 for transit gateway resource types. Maximum of 300 for the other resource types.
Type: Array of strings
Required: Yes

 **ResourceType**
The type of resource to monitor.
Type: String
Valid Values: `VPC | Subnet | NetworkInterface | TransitGateway | TransitGatewayAttachment | RegionalNatGateway`
Required: Yes

 **TagFieldSpecification.N**
The tag configuration associated with the Flow Logs Amazon EC2 Tags feature fields in your custom log format.
Type: Array of [TagFieldSpecificationRequest](API_TagFieldSpecificationRequest.md) objects
Array Members: Minimum number of 1 item. Maximum number of 3 items.
Required: No

 **TagSpecification.N**
The tags to apply to the flow logs.
Type: Array of [TagSpecification](API_TagSpecification.md) objects
Required: No

 **TrafficType**
The type of traffic to monitor (accepted traffic, rejected traffic, or all traffic). This parameter is not supported for transit gateway resource types. It is required for the other resource types.
Type: String
Valid Values: `ACCEPT | REJECT | ALL`
Required: No

## Response Elements
<a name="API_CreateFlowLogs_ResponseElements"></a>

The following elements are returned by the service.

 **clientToken**
Unique, case-sensitive identifier that you provide to ensure the idempotency of the request.
Type: String

 **flowLogIdSet**
The IDs of the flow logs.
Type: Array of strings

 **requestId**
The ID of the request.
Type: String

 **unsuccessful**
Information about the flow logs that could not be created successfully.
Type: Array of [UnsuccessfulItem](API_UnsuccessfulItem.md) objects

## Errors
<a name="API_CreateFlowLogs_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_CreateFlowLogs_Examples"></a>

### Example 1
<a name="API_CreateFlowLogs_Example_1"></a>

(CloudWatch Logs) This example creates a flow log that captures all rejected traffic for network interface eni-aa22bb33 and publishes the data to an CloudWatch Logs log group named `my-flow-logs` in account `123456789101`, using the IAM role `publishFlowLogs`.

#### Sample Request
<a name="API_CreateFlowLogs_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=CreateFlowLogs
&ResourceType=NetworkInterface
&TrafficType=REJECT
&ResourceId.1=eni-aa22bb33
&DeliverLogsPermissionArn=arn:aws:iam::123456789101:role/publishFlowLogs
&LogDestinationType=cloud-watch-logs
&LogDestination=arn:aws:logs:us-east-1:123456789101:log-group:my-flow-logs
&AUTHPARAMS
```

#### Sample Response
<a name="API_CreateFlowLogs_Example_1_Response"></a>

```
<CreateFlowLogsResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>2d96dae3-504b-4fc4-bf50-266EXAMPLE</requestId>
    <unsuccessful/>
    <flowLogIdSet>
        <item>fl-1a2b3c4d</item>
    </flowLogIdSet>
</CreateFlowLogsResponse>
```

### Example 2
<a name="API_CreateFlowLogs_Example_2"></a>

(Amazon S3) This example creates a flow log that captures all traffic for the specified network interface and publishes the data to an Amazon S3 bucket named amzn-s3-demo-bucket.

#### Sample Request
<a name="API_CreateFlowLogs_Example_2_Request"></a>

```
https://ec2.amazonaws.com/?Action=CreateFlowLogs
&ResourceType=NetworkInterface
&TrafficType=ALL
&ResourceId.1=eni-1235b8ca123456789
&LogDestinationType=s3
&LogDestination=arn:aws:s3:::amzn-s3-demo-bucket
&AUTHPARAMS
```

### Example 3
<a name="API_CreateFlowLogs_Example_3"></a>

(Amazon S3) This example creates a flow log with a custom flow log format that captures the version, instance ID, network interface ID, type, packet source address, packet destination address, protocol, bytes, the start time, the end time, and the action of the traffic, in that order. The flow log is published to an Amazon S3 bucket named amzn-s3-demo-bucket.

#### Sample Request
<a name="API_CreateFlowLogs_Example_3_Request"></a>

```
https://ec2.amazonaws.com/?Action=CreateFlowLogs
&ResourceType=NetworkInterface
&TrafficType=ALL
&ResourceId.1=eni-1235b8ca123456789
&LogDestinationType=s3
&LogDestination=arn:aws:s3:::amzn-s3-demo-bucket
&LogFormat='${version} ${instance-id} ${interface-id} ${type} ${pkt-srcaddr} ${pkt-dstaddr} ${protocol} ${bytes} ${start} ${end} ${action}'
&AUTHPARAMS
```

## See Also
<a name="API_CreateFlowLogs_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/CreateFlowLogs)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/CreateFlowLogs)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/CreateFlowLogs)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/CreateFlowLogs)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/CreateFlowLogs)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/CreateFlowLogs)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/CreateFlowLogs)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/CreateFlowLogs)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/CreateFlowLogs)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/CreateFlowLogs)
