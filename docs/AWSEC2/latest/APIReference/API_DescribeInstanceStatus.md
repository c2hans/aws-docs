---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeInstanceStatus.html
---

# DescribeInstanceStatus
<a name="API_DescribeInstanceStatus"></a>

Describes the status of the specified instances or all of your instances. By default, only running instances are described, unless you specifically indicate to return the status of all instances.

Instance status includes the following components:
+  **Status checks** - Amazon EC2 performs status checks on running EC2 instances to identify hardware and software issues. For more information, see [Status checks for your instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/monitoring-system-instance-status-check.html) and [Troubleshoot instances with failed status checks](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/TroubleshootingInstances.html) in the *Amazon EC2 User Guide*.
+  **Scheduled events** - Amazon EC2 can schedule events (such as reboot, stop, or terminate) for your instances related to hardware issues, software updates, or system maintenance. For more information, see [Scheduled events for your instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/monitoring-instances-status-check_sched.html) in the *Amazon EC2 User Guide*.
+  **Instance state** - You can manage your instances from the moment you launch them through their termination. For more information, see [Instance lifecycle](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-lifecycle.html) in the *Amazon EC2 User Guide*.

The Amazon EC2 API follows an eventual consistency model. This means that the result of an API command you run that creates or modifies resources might not be immediately available to all subsequent commands you run. For guidance on how to manage eventual consistency, see [Eventual consistency in the Amazon EC2 API](https://docs.aws.amazon.com/ec2/latest/devguide/eventual-consistency.html) in the *Amazon EC2 Developer Guide*.

**Note**
The order of the elements in the response, including those within nested structures, might vary. Applications should not assume the elements appear in a particular order.

## Request Parameters
<a name="API_DescribeInstanceStatus_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
Checks whether you have the required permissions for the operation, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **Filter.N**
The filters.
+  `availability-zone` - The Availability Zone of the instance.
+  `availability-zone-id` - The ID of the Availability Zone of the instance.
+  `event.code` - The code for the scheduled event (`instance-reboot` \| `system-reboot` \| `system-maintenance` \| `instance-retirement` \| `instance-stop`).
+  `event.description` - A description of the event.
+  `event.instance-event-id` - The ID of the event whose date and time you are modifying.
+  `event.not-after` - The latest end time for the scheduled event (for example, `2014-09-15T17:15:20.000Z`).
+  `event.not-before` - The earliest start time for the scheduled event (for example, `2014-09-15T17:15:20.000Z`).
+  `event.not-before-deadline` - The deadline for starting the event (for example, `2014-09-15T17:15:20.000Z`).
+  `instance-state-code` - The code for the instance state, as a 16-bit unsigned integer. The high byte is used for internal purposes and should be ignored. The low byte is set based on the state represented. The valid values are 0 (pending), 16 (running), 32 (shutting-down), 48 (terminated), 64 (stopping), and 80 (stopped).
+  `instance-state-name` - The state of the instance (`pending` \| `running` \| `shutting-down` \| `terminated` \| `stopping` \| `stopped`).
+  `instance-status.reachability` - Filters on instance status where the name is `reachability` (`passed` \| `failed` \| `initializing` \| `insufficient-data`).
+  `instance-status.status` - The status of the instance (`ok` \| `impaired` \| `initializing` \| `insufficient-data` \| `not-applicable`).
+  `operator.managed` - A Boolean that indicates whether this is a managed instance.
+  `operator.principal` - The principal that manages the instance. Only valid for managed instances, where `managed` is `true`.
+  `system-status.reachability` - Filters on system status where the name is `reachability` (`passed` \| `failed` \| `initializing` \| `insufficient-data`).
+  `system-status.status` - The system status of the instance (`ok` \| `impaired` \| `initializing` \| `insufficient-data` \| `not-applicable`).
+  `attached-ebs-status.status` - The status of the attached EBS volume for the instance (`ok` \| `impaired` \| `initializing` \| `insufficient-data` \| `not-applicable`).
Type: Array of [Filter](API_Filter.md) objects
Required: No

 **IncludeAllInstances**
When `true`, includes the health status for all instances. When `false`, includes the health status for running instances only.
Default: `false`
Type: Boolean
Required: No

 **IncludeManagedResources**
Indicates whether to include managed resources in the output. If this parameter is set to `true`, the output includes resources that are managed by AWS services, even if managed resource visibility is set to hidden.
Type: Boolean
Required: No

 **InstanceId.N**
The instance IDs.
Default: Describes all your instances.
Constraints: Maximum 100 explicitly specified instance IDs.
Type: Array of strings
Required: No

 **MaxResults**
The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output. For more information, see [Pagination](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Query-Requests.html#api-pagination).
You cannot specify this parameter and the instance IDs parameter in the same request.
Type: Integer
Required: No

 **NextToken**
The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.
Type: String
Required: No

## Response Elements
<a name="API_DescribeInstanceStatus_ResponseElements"></a>

The following elements are returned by the service.

 **instanceStatusSet**
Information about the status of the instances.
Type: Array of [InstanceStatus](API_InstanceStatus.md) objects

 **nextToken**
The token to include in another request to get the next page of items. This value is `null` when there are no more items to return.
Type: String

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_DescribeInstanceStatus_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_DescribeInstanceStatus_Examples"></a>

### Example 1
<a name="API_DescribeInstanceStatus_Example_1"></a>

This example returns instance status descriptions for all running instances.

#### Sample Request
<a name="API_DescribeInstanceStatus_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?
Action=DescribeInstanceStatus
&AUTHPARAMS
```

### Example 2
<a name="API_DescribeInstanceStatus_Example_2"></a>

This example returns instance status descriptions for the specified instances.

#### Sample Request
<a name="API_DescribeInstanceStatus_Example_2_Request"></a>

```
https://ec2.amazonaws.com/?
Action=DescribeInstanceStatus
&InstanceId.1=i-1234567890abcdef0
&InstanceId.2=i-0598c7d356eba48d7
&AUTHPARAMS
```

### Example 3
<a name="API_DescribeInstanceStatus_Example_3"></a>

This example returns instance status descriptions for all instances specified by supported DescribeInstanceStatus filters.

#### Sample Request
<a name="API_DescribeInstanceStatus_Example_3_Request"></a>

```
https://ec2.amazonaws.com/?
Action=DescribeInstanceStatus
&Filter.1.Name=system-status.reachability
&Filter.1.Value.failed
&AUTHPARAMS
```

#### Sample Response
<a name="API_DescribeInstanceStatus_Example_3_Response"></a>

```
<DescribeInstanceStatusResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>3be1508e-c444-4fef-89cc-0b1223c4f02fEXAMPLE</requestId>
    <instanceStatusSet>
        <item>
            <instanceId>i-1234567890abcdef0</instanceId>
            <availabilityZone>us-east-1d</availabilityZone>
            <instanceState>
                <code>16</code>
                <name>running</name>
            </instanceState>
            <systemStatus>
                <status>impaired</status>
                <details>
                    <item>
                        <name>reachability</name>
                        <status>failed</status>
                        <impairedSince>YYYY-MM-DDTHH:MM:SS.000Z</impairedSince>
                    </item>
                </details>
            </systemStatus>
            <instanceStatus>
                <status>impaired</status>
                <details>
                    <item>
                        <name>reachability</name>
                        <status>failed</status>
                        <impairedSince>YYYY-MM-DDTHH:MM:SS.000Z</impairedSince>
                    </item>
                </details>
            </instanceStatus>
            <eventsSet>
              <item>
                <code>instance-retirement</code>
                <description>The instance is running on degraded hardware</description>
                <notBefore>YYYY-MM-DDTHH:MM:SS+0000</notBefore>
                <notAfter>YYYY-MM-DDTHH:MM:SS+0000</notAfter>
              </item>
            </eventsSet>
        </item>
        <item>
            <instanceId>i-0598c7d356eba48d7</instanceId>
            <availabilityZone>us-east-1d</availabilityZone>
            <instanceState>
                <code>16</code>
                <name>running</name>
            </instanceState>
            <systemStatus>
                <status>ok</status>
                <details>
                    <item>
                        <name>reachability</name>
                        <status>passed</status>
                    </item>
                </details>
            </systemStatus>
            <instanceStatus>
                <status>ok</status>
                <details>
                    <item>
                        <name>reachability</name>
                        <status>passed</status>
                    </item>
                </details>
            </instanceStatus>
            <eventsSet>
              <item>
                <code>instance-reboot</code>
                <description>The instance is scheduled for a reboot</description>
                <notBefore>YYYY-MM-DDTHH:MM:SS+0000</notBefore>
                <notAfter>YYYY-MM-DDTHH:MM:SS+0000</notAfter>
              </item>
            </eventsSet>
        </item>
        <item>
            <instanceId>i-0987654321abcdef0</instanceId>
            <availabilityZone>us-east-1d</availabilityZone>
            <instanceState>
                <code>16</code>
                <name>running</name>
            </instanceState>
            <systemStatus>
                <status>ok</status>
                <details>
                    <item>
                        <name>reachability</name>
                        <status>passed</status>
                    </item>
                </details>
            </systemStatus>
            <instanceStatus>
                <status>ok</status>
                <details>
                    <item>
                        <name>reachability</name>
                        <status>passed</status>
                    </item>
                </details>
            </instanceStatus>
        </item>
        <item>
            <instanceId>i-0598c7d356eba48d8</instanceId>
            <availabilityZone>us-east-1d</availabilityZone>
            <instanceState>
                <code>16</code>
                <name>running</name>
            </instanceState>
            <systemStatus>
                <status>ok</status>
                <details>
                    <item>
                        <name>reachability</name>
                        <status>passed</status>
                    </item>
                </details>
            </systemStatus>
            <instanceStatus>
                <status>insufficient-data</status>
                <details>
                    <item>
                        <name>reachability</name>
                        <status>insufficient-data</status>
                    </item>
                </details>
            </instanceStatus>
         </item>
    </instanceStatusSet>
</DescribeInstanceStatusResponse>
```

## See Also
<a name="API_DescribeInstanceStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/DescribeInstanceStatus)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/DescribeInstanceStatus)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/DescribeInstanceStatus)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/DescribeInstanceStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/DescribeInstanceStatus)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/DescribeInstanceStatus)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/DescribeInstanceStatus)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/DescribeInstanceStatus)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/DescribeInstanceStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/DescribeInstanceStatus)
