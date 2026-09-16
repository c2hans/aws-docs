---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeHosts.html
---

# DescribeHosts
<a name="API_DescribeHosts"></a>

Describes the specified Dedicated Hosts or all your Dedicated Hosts.

The results describe only the Dedicated Hosts in the Region you're currently using. All listed instances consume capacity on your Dedicated Host. Dedicated Hosts that have recently been released are listed with the state `released`.

## Request Parameters
<a name="API_DescribeHosts_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **Filter.N**
The filters.
+  `auto-placement` - Whether auto-placement is enabled or disabled (`on` \| `off`).
+  `availability-zone` - The Availability Zone of the host.
+  `client-token` - The idempotency token that you provided when you allocated the host.
+  `host-reservation-id` - The ID of the reservation assigned to this host.
+  `instance-type` - The instance type size that the Dedicated Host is configured to support.
+  `state` - The allocation state of the Dedicated Host (`available` \| `under-assessment` \| `permanent-failure` \| `released` \| `released-permanent-failure`).
+  `tag-key` - The key of a tag assigned to the resource. Use this filter to find all resources assigned a tag with a specific key, regardless of the tag value.
Type: Array of [Filter](API_Filter.md) objects
Required: No

 **HostId.N**
The IDs of the Dedicated Hosts. The IDs are used for targeted instance launches.
Type: Array of strings
Required: No

 **MaxResults**
The maximum number of results to return for the request in a single page. The remaining results can be seen by sending another request with the returned `nextToken` value. This value can be between 5 and 500. If `maxResults` is given a larger value than 500, you receive an error.
You cannot specify this parameter and the host IDs parameter in the same request.
Type: Integer
Required: No

 **NextToken**
The token to use to retrieve the next page of results.
Type: String
Required: No

## Response Elements
<a name="API_DescribeHosts_ResponseElements"></a>

The following elements are returned by the service.

 **hostSet**
Information about the Dedicated Hosts.
Type: Array of [Host](API_Host.md) objects

 **nextToken**
The token to use to retrieve the next page of results. This value is `null` when there are no more results to return.
Type: String

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_DescribeHosts_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_DescribeHosts_Examples"></a>

### Example 1
<a name="API_DescribeHosts_Example_1"></a>

This example describes the Dedicated Hosts in your account.

#### Sample Request
<a name="API_DescribeHosts_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=DescribeHosts
&AUTHPARAMS
```

#### Sample Response
<a name="API_DescribeHosts_Example_1_Response"></a>

```
<DescribeHostsResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
<requestId>d4904fd9-82c2-4ea5-adfe-a9cc3EXAMPLE</requestId>
<hostSet>
    <item>
        <availableCapacity>
            <availableVCpus>96</availableVCpus>
            <availableInstanceCapacity>
                <item>
                    <availableCapacity>48</availableCapacity>
                    <totalCapacity>48</totalCapacity>
                    <instanceType>m5.large</instanceType>
                </item>
            </availableInstanceCapacity>
        </availableCapacity>
        <instances/>
        <autoPlacement>off</autoPlacement>
        <hostRecovery>off</hostRecovery>
        <hostId>h-05abcdd96ee9ca123</hostId>
        <allocationTime>2018-01-23T12:33:31.692Z</allocationTime>
        <state>available</state>
        <hostProperties>
            <totalVCpus>96</totalVCpus>
            <cores>48</cores>
            <sockets>2</sockets>
            <instanceType>m5.large</instanceType>
        </hostProperties>
        <availabilityZone>us-east-1a</availabilityZone>
        </item>
    </hostSet>
</DescribeHostsResponse>
```

### Example 2
<a name="API_DescribeHosts_Example_2"></a>

This example describes a released Dedicated Host in your account using the `state` filter to show only hosts with a state of `released`.

#### Sample Request
<a name="API_DescribeHosts_Example_2_Request"></a>

```
https://ec2.amazonaws.com/?Action=DescribeHosts
&Filter.1.Name=state
&Filter.1.Value=released
&AUTHPARAMS
```

#### Sample Response
<a name="API_DescribeHosts_Example_2_Response"></a>

```
<DescribeHostsResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
<requestId>d4904fd9-82c2-4ea5-adfe-a9983EXAMPLE</requestId>
<hostSet>
     item>
        <releaseTime>2018-04-06T14:48:40.068Z</releaseTime>
        <instances/>
        <autoPlacement>on</autoPlacement>
        <hostRecovery>off</hostRecovery>
        <hostId>h-0abcd595047722123</hostId>
        <state>released</state>
        <allocationTime>2018-01-23T12:23:01.501Z</allocationTime>
        <hostProperties>
            <totalVCpus>96</totalVCpus>
            <cores>48</cores>
            <sockets>2</sockets>
            <instanceType>m5.large</instanceType>
        </hostProperties>
        <availabilityZone>us-east-1a</availabilityZone>
    </item>
</hostSet>
</DescribeHostsResponse>
```

## See Also
<a name="API_DescribeHosts_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/DescribeHosts)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/DescribeHosts)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/DescribeHosts)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/DescribeHosts)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/DescribeHosts)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/DescribeHosts)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/DescribeHosts)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/DescribeHosts)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/DescribeHosts)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/DescribeHosts)
