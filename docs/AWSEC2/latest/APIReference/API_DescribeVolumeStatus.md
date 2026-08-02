---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeVolumeStatus.html
---

# DescribeVolumeStatus
<a name="API_DescribeVolumeStatus"></a>

Describes the status of the specified volumes. Volume status provides the result of the checks performed on your volumes to determine events that can impair the performance of your volumes. The performance of a volume can be affected if an issue occurs on the volume's underlying host. If the volume's underlying host experiences a power outage or system issue, after the system is restored, there could be data inconsistencies on the volume. Volume events notify you if this occurs. Volume actions notify you if any action needs to be taken in response to the event.

The `DescribeVolumeStatus` operation provides the following information about the specified volumes:

 *Status*: Reflects the current status of the volume. The possible values are `ok`, `impaired` , `warning`, or `insufficient-data`. If all checks pass, the overall status of the volume is `ok`. If the check fails, the overall status is `impaired`. If the status is `insufficient-data`, then the checks might still be taking place on your volume at the time. We recommend that you retry the request. For more information about volume status, see [Monitor the status of your volumes](https://docs.aws.amazon.com/ebs/latest/userguide/monitoring-volume-status.html) in the *Amazon EBS User Guide*.

 *Events*: Reflect the cause of a volume status and might require you to take action. For example, if your volume returns an `impaired` status, then the volume event might be `potential-data-inconsistency`. This means that your volume has been affected by an issue with the underlying host, has all I/O operations disabled, and might have inconsistent data.

 *Actions*: Reflect the actions you might have to take in response to an event. For example, if the status of the volume is `impaired` and the volume event shows `potential-data-inconsistency`, then the action shows `enable-volume-io`. This means that you may want to enable the I/O operations for the volume and then check the volume for data consistency. For more information, see [Work with an impaired EBS volume](https://docs.aws.amazon.com/ebs/latest/userguide/work_volumes_impaired.html).

Volume status is based on the volume status checks, and does not reflect the volume state. Therefore, volume status does not indicate volumes in the `error` state (for example, when a volume is incapable of accepting I/O.)

**Note**
The order of the elements in the response, including those within nested structures, might vary. Applications should not assume the elements appear in a particular order.

## Request Parameters
<a name="API_DescribeVolumeStatus_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **Filter.N**
The filters.
+  `action.code` - The action code for the event (for example, `enable-volume-io`).
+  `action.description` - A description of the action.
+  `action.event-id` - The event ID associated with the action.
+  `availability-zone` - The Availability Zone of the instance.
+  `event.description` - A description of the event.
+  `event.event-id` - The event ID.
+  `event.event-type` - The event type (for `io-enabled`: `passed` \| `failed`; for `io-performance`: `io-performance:degraded` \| `io-performance:severely-degraded` \| `io-performance:stalled`).
+  `event.not-after` - The latest end time for the event.
+  `event.not-before` - The earliest start time for the event.
+  `volume-status.details-name` - The cause for `volume-status.status` (`io-enabled` \| `io-performance`).
+  `volume-status.details-status` - The status of `volume-status.details-name` (for `io-enabled`: `passed` \| `failed`; for `io-performance`: `normal` \| `degraded` \| `severely-degraded` \| `stalled`).
+  `volume-status.status` - The status of the volume (`ok` \| `impaired` \| `warning` \| `insufficient-data`).
Type: Array of [Filter](API_Filter.md) objects
Required: No

 **IncludeManagedResources**
Indicates whether to include managed resources in the output. If this parameter is set to `true`, the output includes resources that are managed by AWS services, even if managed resource visibility is set to hidden.
Type: Boolean
Required: No

 **MaxResults**
The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output. For more information, see [Pagination](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Query-Requests.html#api-pagination).
Type: Integer
Required: No

 **NextToken**
The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.
Type: String
Required: No

 **VolumeId.N**
The IDs of the volumes.
Default: Describes all your volumes.
Type: Array of strings
Required: No

## Response Elements
<a name="API_DescribeVolumeStatus_ResponseElements"></a>

The following elements are returned by the service.

 **nextToken**
The token to include in another request to get the next page of items. This value is `null` when there are no more items to return.
Type: String

 **requestId**
The ID of the request.
Type: String

 **volumeStatusSet**
Information about the status of the volumes.
Type: Array of [VolumeStatusItem](API_VolumeStatusItem.md) objects

## Errors
<a name="API_DescribeVolumeStatus_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_DescribeVolumeStatus_Examples"></a>

### Example
<a name="API_DescribeVolumeStatus_Example_1"></a>

This example describes the status of all the volumes associated with your account.

#### Sample Request
<a name="API_DescribeVolumeStatus_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=DescribeVolumeStatus
&AUTHPARAMS
```

#### Sample Response
<a name="API_DescribeVolumeStatus_Example_1_Response"></a>

```
<DescribeVolumeStatus xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
   <requestId>5jkdf074-37ed-4004-8671-a78ee82bf1cbEXAMPLE</requestId>
  <volumeStatusSet>
    <item>
      <VolumeId>vol-1234567890abcdef0</volumeId>
      <availabilityZone>us-east-1d</availabilityZone>
      <volumeStatus>
        <status>ok</status>
        <details>
          <item>
            <title>io-enabled</title>
            <status>passed</status>
          </item>
        </details>
      </volumeStatus>
      </item>
    <item>
      <volumeId>vol-1234567890abcdef1</volumeId>
      <availabilityZone>us-east-1d</availabilityZone>
      <volumeStatus>
        <status>impaired</status>
        <details>
          <item>
            <title>io-enabled</title>
            <status>failed</status>
          </item>
        </details>
      </volumeStatus>
      <eventsSet>
             <item>
               <eventId>evol-61a54008</eventId>
               <eventType>potential-data-inconsistency</eventType>
               <description>THIS IS AN EXAMPLE</description>
               <notBefore>2011-12-01T14:00:00.000Z</notBefore>
               <notAfter>2011-12-01T15:00:00.000Z</notAfter>
             </item>
            </eventsSet>
      <actionsSet>
        <item>
          <code>enable-volume-io</code>
          <eventId> evol-61a54008</eventId>
          <eventType>potential-data-inconsistency</eventType>
          <description>THIS IS AN EXAMPLE</description>
        </item>
      </actionsSet>
    </item>
    </volumeStatusSet>
</DescribeVolumesStatusResponse>
```

### Example
<a name="API_DescribeVolumeStatus_Example_2"></a>

This example describes all the volumes in the `us-east-1d` Availability Zone with `failed` `io-enabled` status.

#### Sample Request
<a name="API_DescribeVolumeStatus_Example_2_Request"></a>

```
https://ec2.amazonaws.com/?Action=DescribeVolumeStatus
&Filter.1.Name=availability-zone
&Filter.1.Value.1=us-east-1d
&Filter.2.Name=volume-status.details-name
&Filter.2.Value.1=io-enabled
&Filter.3.Name=volume-status.details-status
&Filter.3.Value.1=failed
&AUTHPARAMS
```

## See Also
<a name="API_DescribeVolumeStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/DescribeVolumeStatus)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/DescribeVolumeStatus)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/DescribeVolumeStatus)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/DescribeVolumeStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/DescribeVolumeStatus)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/DescribeVolumeStatus)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/DescribeVolumeStatus)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/DescribeVolumeStatus)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/DescribeVolumeStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/DescribeVolumeStatus)
