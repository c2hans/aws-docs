---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/2012-06-01/APIReference/API_DescribeLoadBalancers.html
---

# DescribeLoadBalancers
<a name="API_DescribeLoadBalancers"></a>

Describes the specified load balancers. If no load balancers are specified, the call describes all of your load balancers.

## Request Parameters
<a name="API_DescribeLoadBalancers_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 **LoadBalancerNames.member.N**
The names of the load balancers.
Type: Array of strings
Required: No

 ** Marker **
The marker for the next set of results. (You received this marker from a previous call.)
Type: String
Required: No

 ** PageSize **
The maximum number of results to return with this call (a number from 1 to 400). The default is 400.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 400.
Required: No

## Response Elements
<a name="API_DescribeLoadBalancers_ResponseElements"></a>

The following elements are returned by the service.

 **LoadBalancerDescriptions.member.N**
Information about the load balancers.
Type: Array of [LoadBalancerDescription](API_LoadBalancerDescription.md) objects

 ** NextMarker **
The marker to use when requesting the next set of results. If there are no additional results, the string is empty.
Type: String

## Errors
<a name="API_DescribeLoadBalancers_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DependencyThrottle **
A request made by Elastic Load Balancing to another service exceeds the maximum request rate permitted for your account.
HTTP Status Code: 400

 ** LoadBalancerNotFound **
The specified load balancer does not exist.
HTTP Status Code: 400

## Examples
<a name="API_DescribeLoadBalancers_Examples"></a>

### Describe a Classic Load Balancer
<a name="API_DescribeLoadBalancers_Example_1"></a>

This example describes the specified load balancer.

#### Sample Request
<a name="API_DescribeLoadBalancers_Example_1_Request"></a>

```
https://elasticloadbalancing.amazonaws.com/?Action=DescribeLoadBalancers
&LoadBalancerNames.member.1=my-loadbalancer
&Version=2012-06-01
&AUTHPARAMS
```

#### Sample Response
<a name="API_DescribeLoadBalancers_Example_1_Response"></a>

```
<DescribeLoadBalancersResponse xmlns="http://elasticloadbalancing.amazonaws.com/doc/2012-06-01/">
  <DescribeLoadBalancersResult>
    <LoadBalancerDescriptions>
      <member>
        <SecurityGroups/>
        <LoadBalancerName>my-loadbalancer</LoadBalancerName>
        <CreatedTime>2013-05-24T21:15:31.280Z</CreatedTime>
        <HealthCheck>
          <Interval>90</Interval>
          <Target>HTTP:80/</Target>
          <HealthyThreshold>2</HealthyThreshold>
          <Timeout>60</Timeout>
          <UnhealthyThreshold>10</UnhealthyThreshold>
        </HealthCheck>
        <ListenerDescriptions>
          <member>
            <PolicyNames/>
            <Listener>
              <Protocol>HTTP</Protocol>
              <LoadBalancerPort>80</LoadBalancerPort>
              <InstanceProtocol>HTTP</InstanceProtocol>
              <InstancePort>80</InstancePort>
            </Listener>
          </member>
        </ListenerDescriptions>
        <Instances>
          <member>
            <InstanceId>i-e4cbe38d</InstanceId>
          </member>
        </Instances>
        <Policies>
          <AppCookieStickinessPolicies/>
          <OtherPolicies/>
          <LBCookieStickinessPolicies/>
        </Policies>
        <AvailabilityZones>
          <member>us-east-1a</member>
        </AvailabilityZones>
        <CanonicalHostedZoneNameID>ZZZZZZZZZZZ123X</CanonicalHostedZoneNameID>
        <CanonicalHostedZoneName>my-loadbalancer-123456789.us-east-1.elb.amazonaws.com</CanonicalHostedZoneName>
        <Scheme>internet-facing</Scheme>
        <SourceSecurityGroup>
          <OwnerAlias>amazon-elb</OwnerAlias>
          <GroupName>amazon-elb-sg</GroupName>
        </SourceSecurityGroup>
        <DNSName>my-loadbalancer-123456789.us-east-1.elb.amazonaws.com</DNSName>
        <BackendServerDescriptions/>
        <Subnets/>
      </member>
    </LoadBalancerDescriptions>
  </DescribeLoadBalancersResult>
  <ResponseMetadata>
    <RequestId>83c88b9d-12b7-11e3-8b82-87b12EXAMPLE</RequestId>
  </ResponseMetadata>
</DescribeLoadBalancersResponse>
```

## See Also
<a name="API_DescribeLoadBalancers_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticloadbalancing-2012-06-01/DescribeLoadBalancers)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticloadbalancing-2012-06-01/DescribeLoadBalancers)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticloadbalancing-2012-06-01/DescribeLoadBalancers)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticloadbalancing-2012-06-01/DescribeLoadBalancers)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticloadbalancing-2012-06-01/DescribeLoadBalancers)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticloadbalancing-2012-06-01/DescribeLoadBalancers)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticloadbalancing-2012-06-01/DescribeLoadBalancers)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticloadbalancing-2012-06-01/DescribeLoadBalancers)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elasticloadbalancing-2012-06-01/DescribeLoadBalancers)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticloadbalancing-2012-06-01/DescribeLoadBalancers)
