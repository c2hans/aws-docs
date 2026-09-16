---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeVpcEndpointServiceConfigurations.html
---

# DescribeVpcEndpointServiceConfigurations
<a name="API_DescribeVpcEndpointServiceConfigurations"></a>

Describes the VPC endpoint service configurations in your account (your services).

## Request Parameters
<a name="API_DescribeVpcEndpointServiceConfigurations_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **Filter.N**
The filters.
+  `service-name` - The name of the service.
+  `service-id` - The ID of the service.
+  `service-state` - The state of the service (`Pending` \| `Available` \| `Deleting` \| `Deleted` \| `Failed`).
+  `supported-ip-address-types` - The IP address type (`ipv4` \| `ipv6`).
+  `tag`:<key> - The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key `Owner` and the value `TeamA`, specify `tag:Owner` for the filter name and `TeamA` for the filter value.
+  `tag-key` - The key of a tag assigned to the resource. Use this filter to find all resources assigned a tag with a specific key, regardless of the tag value.
Type: Array of [Filter](API_Filter.md) objects
Required: No

 **MaxResults**
The maximum number of results to return for the request in a single page. The remaining results of the initial request can be seen by sending another request with the returned `NextToken` value. This value can be between 5 and 1,000; if `MaxResults` is given a value larger than 1,000, only 1,000 results are returned.
Type: Integer
Required: No

 **NextToken**
The token to retrieve the next page of results.
Type: String
Required: No

 **ServiceId.N**
The IDs of the endpoint services.
Type: Array of strings
Required: No

## Response Elements
<a name="API_DescribeVpcEndpointServiceConfigurations_ResponseElements"></a>

The following elements are returned by the service.

 **nextToken**
The token to use to retrieve the next page of results. This value is `null` when there are no more results to return.
Type: String

 **requestId**
The ID of the request.
Type: String

 **serviceConfigurationSet**
Information about the services.
Type: Array of [ServiceConfiguration](API_ServiceConfiguration.md) objects

## Errors
<a name="API_DescribeVpcEndpointServiceConfigurations_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_DescribeVpcEndpointServiceConfigurations_Examples"></a>

### Example
<a name="API_DescribeVpcEndpointServiceConfigurations_Example_1"></a>

This example describes all of your VPC endpoint service configurations.

#### Sample Request
<a name="API_DescribeVpcEndpointServiceConfigurations_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=DescribeVpcEndpointServiceConfigurations
&AUTHPARAMS
```

#### Sample Response
<a name="API_DescribeVpcEndpointServiceConfigurations_Example_1_Response"></a>

```
<DescribeVpcEndpointServiceConfigurationsResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>d5bad480-0167-4a7f-a1c6-2651example</requestId>
    <serviceConfigurationSet>
        <item>
            <serviceState>Available</serviceState>
            <serviceType>
                <item>
                    <serviceType>Interface</serviceType>
                </item>
            </serviceType>
            <baseEndpointDnsNameSet>
                <item>vpce-svc-0799b7d1c483b0123.us-east-1.vpce.amazonaws.com</item>
            </baseEndpointDnsNameSet>
            <acceptanceRequired>true</acceptanceRequired>
            <availabilityZoneSet>
                <item>us-east-1d</item>
            </availabilityZoneSet>
            <serviceId>vpce-svc-0799b7d1c483b0123</serviceId>
            <serviceName>com.amazonaws.vpce.us-east-1.vpce-svc-0799b7d1c483b0123</serviceName>
            <networkLoadBalancerArnSet>
                <item>arn:aws:elasticloadbalancing:us-east-1:123456789012:loadbalancer/net/mynlb/1238753950b25123</item>
            </networkLoadBalancerArnSet>
            <tagSet>
                <item>
                    <key>Name</key>
                    <value>TeamA</value>
                </item>
            </tagSet>
        </item>
        <item>
            <serviceState>Available</serviceState>
            <serviceType>
                <item>
                    <serviceType>GatewayLoadBalancer</serviceType>
                </item>
            </serviceType>
            <acceptanceRequired>false</acceptanceRequired>
            <availabilityZoneSet>
                <item>us-east-1d</item>
            </availabilityZoneSet>
            <serviceId>vpce-svc-123abcc1298abc123</serviceId>
            <serviceName>com.amazonaws.vpce.us-east-1.vpce-svc-123abcc1298abc123</serviceName>
            <gatewayLoadBalancerArnSet>
                <item>arn:aws:elasticloadbalancing:us-east-1:123456789012:loadbalancer/gwy/GWLBService/abc210844e429abc</item>
            </gatewayLoadBalancerArnSet>
            <tagSet>
                <item>
                    <key>Name</key>
                    <value>SecurityAppliance</value>
                </item>
            </tagSet>
        </item>
    </serviceConfigurationSet>
</DescribeVpcEndpointServiceConfigurationsResponse>
```

## See Also
<a name="API_DescribeVpcEndpointServiceConfigurations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/DescribeVpcEndpointServiceConfigurations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/DescribeVpcEndpointServiceConfigurations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/DescribeVpcEndpointServiceConfigurations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/DescribeVpcEndpointServiceConfigurations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/DescribeVpcEndpointServiceConfigurations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/DescribeVpcEndpointServiceConfigurations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/DescribeVpcEndpointServiceConfigurations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/DescribeVpcEndpointServiceConfigurations)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/DescribeVpcEndpointServiceConfigurations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/DescribeVpcEndpointServiceConfigurations)
