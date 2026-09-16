---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/2012-06-01/APIReference/API_DisableAvailabilityZonesForLoadBalancer.html
---

# DisableAvailabilityZonesForLoadBalancer
<a name="API_DisableAvailabilityZonesForLoadBalancer"></a>

Removes the specified Availability Zones from the set of Availability Zones for the specified load balancer in EC2-Classic or a default VPC.

For load balancers in a non-default VPC, use [DetachLoadBalancerFromSubnets](API_DetachLoadBalancerFromSubnets.md).

There must be at least one Availability Zone registered with a load balancer at all times. After an Availability Zone is removed, all instances registered with the load balancer that are in the removed Availability Zone go into the `OutOfService` state. Then, the load balancer attempts to equally balance the traffic among its remaining Availability Zones.

## Request Parameters
<a name="API_DisableAvailabilityZonesForLoadBalancer_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 **AvailabilityZones.member.N**
The Availability Zones.
Type: Array of strings
Required: Yes

 ** LoadBalancerName **
The name of the load balancer.
Type: String
Required: Yes

## Response Elements
<a name="API_DisableAvailabilityZonesForLoadBalancer_ResponseElements"></a>

The following element is returned by the service.

 **AvailabilityZones.member.N**
The remaining Availability Zones for the load balancer.
Type: Array of strings

## Errors
<a name="API_DisableAvailabilityZonesForLoadBalancer_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidConfigurationRequest **
The requested configuration change is not valid.
HTTP Status Code: 409

 ** LoadBalancerNotFound **
The specified load balancer does not exist.
HTTP Status Code: 400

## Examples
<a name="API_DisableAvailabilityZonesForLoadBalancer_Examples"></a>

### Disable Availability Zones
<a name="API_DisableAvailabilityZonesForLoadBalancer_Example_1"></a>

This example disables the specified Availability Zone for the specified load balancer.

#### Sample Request
<a name="API_DisableAvailabilityZonesForLoadBalancer_Example_1_Request"></a>

```
https://elasticloadbalancing.amazonaws.com/?Action=DisableAvailabilityZonesForLoadBalancer
&LoadBalancerName=my-https-loadbalancer
&AvailabilityZones.member.1=us-east-1a
&Version=2012-06-01
&AUTHPARAMS
```

#### Sample Response
<a name="API_DisableAvailabilityZonesForLoadBalancer_Example_1_Response"></a>

```
<DisableAvailabilityZonesForLoadBalancerResponse xmlns="http://elasticloadbalancing.amazonaws.com/doc/2012-06-01/">
  <DisableAvailabilityZonesForLoadBalancerResult>
    <AvailabilityZones>
      <member>us-east-1b</member>
    </AvailabilityZones>
  </DisableAvailabilityZonesForLoadBalancerResult>
  <ResponseMetadata>
    <RequestId>ba6267d5-2566-11e3-9c6d-eb728EXAMPLE</RequestId>
  </ResponseMetadata>
</DisableAvailabilityZonesForLoadBalancerResponse>
```

## See Also
<a name="API_DisableAvailabilityZonesForLoadBalancer_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticloadbalancing-2012-06-01/DisableAvailabilityZonesForLoadBalancer)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticloadbalancing-2012-06-01/DisableAvailabilityZonesForLoadBalancer)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticloadbalancing-2012-06-01/DisableAvailabilityZonesForLoadBalancer)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticloadbalancing-2012-06-01/DisableAvailabilityZonesForLoadBalancer)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticloadbalancing-2012-06-01/DisableAvailabilityZonesForLoadBalancer)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticloadbalancing-2012-06-01/DisableAvailabilityZonesForLoadBalancer)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticloadbalancing-2012-06-01/DisableAvailabilityZonesForLoadBalancer)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticloadbalancing-2012-06-01/DisableAvailabilityZonesForLoadBalancer)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/elasticloadbalancing-2012-06-01/DisableAvailabilityZonesForLoadBalancer)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticloadbalancing-2012-06-01/DisableAvailabilityZonesForLoadBalancer)
