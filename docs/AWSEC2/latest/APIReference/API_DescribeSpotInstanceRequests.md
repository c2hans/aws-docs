---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeSpotInstanceRequests.html
---

# DescribeSpotInstanceRequests
<a name="API_DescribeSpotInstanceRequests"></a>

Describes the specified Spot Instance requests.

You can use `DescribeSpotInstanceRequests` to find a running Spot Instance by examining the response. If the status of the Spot Instance is `fulfilled`, the instance ID appears in the response and contains the identifier of the instance. Alternatively, you can use [DescribeInstances](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeInstances) with a filter to look for instances where the instance lifecycle is `spot`.

We recommend that you set `MaxResults` to a value between 5 and 1000 to limit the number of items returned. This paginates the output, which makes the list more manageable and returns the items faster. If the list of items exceeds your `MaxResults` value, then that number of items is returned along with a `NextToken` value that can be passed to a subsequent `DescribeSpotInstanceRequests` request to retrieve the remaining items.

Spot Instance requests are deleted four hours after they are canceled and their instances are terminated.

## Request Parameters
<a name="API_DescribeSpotInstanceRequests_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **Filter.N**
The filters.
+  `availability-zone-group` - The Availability Zone group.
+  `create-time` - The time stamp when the Spot Instance request was created.
+  `fault-code` - The fault code related to the request.
+  `fault-message` - The fault message related to the request.
+  `instance-id` - The ID of the instance that fulfilled the request.
+  `launch-group` - The Spot Instance launch group.
+  `launch.block-device-mapping.delete-on-termination` - Indicates whether the EBS volume is deleted on instance termination.
+  `launch.block-device-mapping.device-name` - The device name for the volume in the block device mapping (for example, `/dev/sdh` or `xvdh`).
+  `launch.block-device-mapping.snapshot-id` - The ID of the snapshot for the EBS volume.
+  `launch.block-device-mapping.volume-size` - The size of the EBS volume, in GiB.
+  `launch.block-device-mapping.volume-type` - The type of EBS volume: `gp2` or `gp3` for General Purpose SSD, `io1` or `io2` for Provisioned IOPS SSD, `st1` for Throughput Optimized HDD, `sc1` for Cold HDD, or `standard` for Magnetic.
+  `launch.group-id` - The ID of the security group for the instance.
+  `launch.group-name` - The name of the security group for the instance.
+  `launch.image-id` - The ID of the AMI.
+  `launch.instance-type` - The type of instance (for example, `m3.medium`).
+  `launch.kernel-id` - The kernel ID.
+  `launch.key-name` - The name of the key pair the instance launched with.
+  `launch.monitoring-enabled` - Whether detailed monitoring is enabled for the Spot Instance.
+  `launch.ramdisk-id` - The RAM disk ID.
+  `launched-availability-zone` - The Availability Zone in which the request is launched.
+  `launched-availability-zone-id` - The ID of the Availability Zone in which the request is launched.
+  `network-interface.addresses.primary` - Indicates whether the IP address is the primary private IP address.
+  `network-interface.delete-on-termination` - Indicates whether the network interface is deleted when the instance is terminated.
+  `network-interface.description` - A description of the network interface.
+  `network-interface.device-index` - The index of the device for the network interface attachment on the instance.
+  `network-interface.group-id` - The ID of the security group associated with the network interface.
+  `network-interface.network-interface-id` - The ID of the network interface.
+  `network-interface.private-ip-address` - The primary private IP address of the network interface.
+  `network-interface.subnet-id` - The ID of the subnet for the instance.
+  `product-description` - The product description associated with the instance (`Linux/UNIX` \| `Windows`).
+  `spot-instance-request-id` - The Spot Instance request ID.
+  `spot-price` - The maximum hourly price for any Spot Instance launched to fulfill the request.
+  `state` - The state of the Spot Instance request (`open` \| `active` \| `closed` \| `cancelled` \| `failed`). Spot request status information can help you track your Amazon EC2 Spot Instance requests. For more information, see [Spot request status](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-request-status.html) in the *Amazon EC2 User Guide*.
+  `status-code` - The short code describing the most recent evaluation of your Spot Instance request.
+  `status-message` - The message explaining the status of the Spot Instance request.
+  `tag:<key>` - The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key `Owner` and the value `TeamA`, specify `tag:Owner` for the filter name and `TeamA` for the filter value.
+  `tag-key` - The key of a tag assigned to the resource. Use this filter to find all resources assigned a tag with a specific key, regardless of the tag value.
+  `type` - The type of Spot Instance request (`one-time` \| `persistent`).
+  `valid-from` - The start date of the request.
+  `valid-until` - The end date of the request.
Type: Array of [Filter](API_Filter.md) objects
Required: No

 **MaxResults**
The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output. For more information, see [Pagination](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Query-Requests.html#api-pagination).
Type: Integer
Required: No

 **NextToken**
The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.
Type: String
Required: No

 **SpotInstanceRequestId.N**
The IDs of the Spot Instance requests.
Type: Array of strings
Required: No

## Response Elements
<a name="API_DescribeSpotInstanceRequests_ResponseElements"></a>

The following elements are returned by the service.

 **nextToken**
The token to include in another request to get the next page of items. This value is `null` when there are no more items to return.
Type: String

 **requestId**
The ID of the request.
Type: String

 **spotInstanceRequestSet**
The Spot Instance requests.
Type: Array of [SpotInstanceRequest](API_SpotInstanceRequest.md) objects

## Errors
<a name="API_DescribeSpotInstanceRequests_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_DescribeSpotInstanceRequests_Examples"></a>

### Example for DescribeSpotInstanceRequests
<a name="API_DescribeSpotInstanceRequests_Example_1"></a>

This example returns information about current Spot Instance requests. In the response, if the status of the Spot Instance is `fulfilled`, the instance ID appears in the response and contains the identifier of the instance.

#### Sample Request
<a name="API_DescribeSpotInstanceRequests_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=DescribeSpotInstanceRequests
&AUTHPARAMS
```

#### Sample Response
<a name="API_DescribeSpotInstanceRequests_Example_1_Response"></a>

```
<DescribeSpotInstanceRequestsResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
  <requestId>59dbff89-35bd-4eac-99ed-be587EXAMPLE</requestId>
  <spotInstanceRequestSet>
    <item>
      <spotInstanceRequestId>sir-1a2b3c4d</spotInstanceRequestId>
      <spotPrice>0.09</spotPrice>
      <type>one-time</type>
      <state>active</state>
      <status>
        <code>fulfilled</code>
        <updateTime>YYYY-MM-DDTHH:MM:SS.000Z</updateTime>
        <message>Your Spot request is fulfilled.</message>
      </status>
      <launchSpecification>
        <imageId>ami-1a2b3c4d</imageId>
        <keyName>my-key-pair</keyName>
        <groupSet>
          <item>
            <groupId>sg-1a2b3c4d</groupId>
            <groupName>websrv</groupName>
          </item>
        </groupSet>
        <instanceType>m3.medium</instanceType>
        <monitoring>
          <enabled>false</enabled>
        </monitoring>
        <ebsOptimized>false</ebsOptimized>
      </launchSpecification>
      <instanceId>i-1234567890abcdef0</instanceId>
      <createTime>YYYY-MM-DDTHH:MM:SS.000Z</createTime>
      <productDescription>Linux/UNIX</productDescription>
      <launchedAvailabilityZone>us-west-2a</launchedAvailabilityZone>
    </item>
  <spotInstanceRequestSet/>
<DescribeSpotInstanceRequestsResponse>
```

### Example for DescribeSpotInstanceRequests
<a name="API_DescribeSpotInstanceRequests_Example_2"></a>

This example describes all persistent Spot Instance requests that have resulted in the launch of at least one instance, that has been fulfilled in the us-west-2a Availability Zone, and that also has monitoring enabled.

#### Sample Request
<a name="API_DescribeSpotInstanceRequests_Example_2_Request"></a>

```
https://ec2.amazonaws.com/?Action=DescribeSpotInstanceRequests
&Filter.1.Name=type
&Filter.1.Value.1=persistent
&Filter.2.Name=instance-type
&Filter.2.Value.1=m3.medium
&Filter.3.Name=monitoring-enabled
&Filter.3.Value.1=true
&Filter.4.Name=launched-availability-zone
&Filter.4.Value.1=us-west-2a
&AUTHPARAMS
```

### Example for DescribeInstances
<a name="API_DescribeSpotInstanceRequests_Example_3"></a>

Alternatively, you can use [DescribeInstances](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeInstances) and use a filter to look for instances where the instance lifecycle contains `spot`.

#### Sample Request
<a name="API_DescribeSpotInstanceRequests_Example_3_Request"></a>

```
https://ec2.amazonaws.com/?Action=DescribeInstances
&Filter.1.Name=instance-lifecycle
&Filter.1.Value.1=spot
&AUTHPARAMS
```

## See Also
<a name="API_DescribeSpotInstanceRequests_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/DescribeSpotInstanceRequests)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/DescribeSpotInstanceRequests)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/DescribeSpotInstanceRequests)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/DescribeSpotInstanceRequests)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/DescribeSpotInstanceRequests)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/DescribeSpotInstanceRequests)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/DescribeSpotInstanceRequests)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/DescribeSpotInstanceRequests)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/DescribeSpotInstanceRequests)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/DescribeSpotInstanceRequests)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
