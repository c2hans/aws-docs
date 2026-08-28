---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/2012-06-01/APIReference/API_EnableAvailabilityZonesForLoadBalancer.html
---

# EnableAvailabilityZonesForLoadBalancer
<a name="API_EnableAvailabilityZonesForLoadBalancer"></a>

Adds the specified Availability Zones to the set of Availability Zones for the specified load balancer in EC2-Classic or a default VPC.

For load balancers in a non-default VPC, use [AttachLoadBalancerToSubnets](API_AttachLoadBalancerToSubnets.md).

The load balancer evenly distributes requests across all its registered Availability Zones that contain instances.

## Request Parameters
<a name="API_EnableAvailabilityZonesForLoadBalancer_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 **AvailabilityZones.member.N**
The Availability Zones. These must be in the same region as the load balancer.
Type: Array of strings
Required: Yes

 ** LoadBalancerName **
The name of the load balancer.
Type: String
Required: Yes

## Response Elements
<a name="API_EnableAvailabilityZonesForLoadBalancer_ResponseElements"></a>

The following element is returned by the service.

 **AvailabilityZones.member.N**
The updated list of Availability Zones for the load balancer.
Type: Array of strings

## Errors
<a name="API_EnableAvailabilityZonesForLoadBalancer_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** LoadBalancerNotFound **
The specified load balancer does not exist.
HTTP Status Code: 400

## Examples
<a name="API_EnableAvailabilityZonesForLoadBalancer_Examples"></a>

### Enable Availability Zones
<a name="API_EnableAvailabilityZonesForLoadBalancer_Example_1"></a>

This example enables the specified Availability Zone for the specified load balancer.

#### Sample Request
<a name="API_EnableAvailabilityZonesForLoadBalancer_Example_1_Request"></a>

```
https://elasticloadbalancing.amazonaws.com/?Action=EnableAvailabilityZonesForLoadBalancer
&LoadBalancerName=my-loadbalancer
&AvailabilityZones.member.1=us-east-1c
&Version=2012-06-01
&AUTHPARAMS
```

#### Sample Response
<a name="API_EnableAvailabilityZonesForLoadBalancer_Example_1_Response"></a>

```
<EnableAvailabilityZonesForLoadBalancerResponse xmlns="http://elasticloadbalancing.amazonaws.com/doc/2012-06-01/">
  <EnableAvailabilityZonesForLoadBalancerResult>
    <AvailabilityZones>
      <member>us-east-1a</member>
      <member>us-east-1c</member>
    </AvailabilityZones>
  </EnableAvailabilityZonesForLoadBalancerResult>
  <ResponseMetadata>
    <RequestId>83c88b9d-12b7-11e3-8b82-87b12EXAMPLE</RequestId>
  </ResponseMetadata>
</EnableAvailabilityZonesForLoadBalancerResponse>
```

## See Also
<a name="API_EnableAvailabilityZonesForLoadBalancer_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticloadbalancing-2012-06-01/EnableAvailabilityZonesForLoadBalancer)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticloadbalancing-2012-06-01/EnableAvailabilityZonesForLoadBalancer)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticloadbalancing-2012-06-01/EnableAvailabilityZonesForLoadBalancer)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticloadbalancing-2012-06-01/EnableAvailabilityZonesForLoadBalancer)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticloadbalancing-2012-06-01/EnableAvailabilityZonesForLoadBalancer)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticloadbalancing-2012-06-01/EnableAvailabilityZonesForLoadBalancer)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticloadbalancing-2012-06-01/EnableAvailabilityZonesForLoadBalancer)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticloadbalancing-2012-06-01/EnableAvailabilityZonesForLoadBalancer)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elasticloadbalancing-2012-06-01/EnableAvailabilityZonesForLoadBalancer)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticloadbalancing-2012-06-01/EnableAvailabilityZonesForLoadBalancer)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Elastic Load Balancing. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elasticloadbalancing` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
