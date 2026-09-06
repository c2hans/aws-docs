---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/2012-06-01/APIReference/API_CreateLoadBalancer.html
---

# CreateLoadBalancer
<a name="API_CreateLoadBalancer"></a>

Creates a Classic Load Balancer.

You can add listeners, security groups, subnets, and tags when you create your load balancer, or you can add them later using [CreateLoadBalancerListeners](API_CreateLoadBalancerListeners.md), [ApplySecurityGroupsToLoadBalancer](API_ApplySecurityGroupsToLoadBalancer.md), [AttachLoadBalancerToSubnets](API_AttachLoadBalancerToSubnets.md), and [AddTags](API_AddTags.md).

To describe your current load balancers, see [DescribeLoadBalancers](API_DescribeLoadBalancers.md). When you are finished with a load balancer, you can delete it using [DeleteLoadBalancer](API_DeleteLoadBalancer.md).

You can create up to 20 load balancers per region per account. You can request an increase for the number of load balancers for your account. For more information, see [Quotas for your Classic Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-limits.html) in the *User Guide for Classic Load Balancers*.

## Request Parameters
<a name="API_CreateLoadBalancer_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 **AvailabilityZones.member.N**
One or more Availability Zones from the same region as the load balancer.
You must specify at least one Availability Zone.
You can add more Availability Zones after you create the load balancer using [EnableAvailabilityZonesForLoadBalancer](API_EnableAvailabilityZonesForLoadBalancer.md).
Type: Array of strings
Required: No

 **Listeners.member.N**
The listeners.
For more information, see [Listeners for your Classic Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-listener-config.html) in the *User Guide for Classic Load Balancers*.
Type: Array of [Listener](API_Listener.md) objects
Required: Yes

 ** LoadBalancerName **
The name of the load balancer.
This name must be unique within your set of load balancers for the region, must have a maximum of 32 characters, must contain only alphanumeric characters or hyphens, and cannot begin or end with a hyphen.
Type: String
Required: Yes

 ** Scheme **
The type of a load balancer. Valid only for load balancers in a VPC.
By default, Elastic Load Balancing creates an Internet-facing load balancer with a DNS name that resolves to public IP addresses. For more information about Internet-facing and Internal load balancers, see [Load balancer scheme](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/how-elastic-load-balancing-works.html#load-balancer-scheme) in the *Elastic Load Balancing User Guide*.
Specify `internal` to create a load balancer with a DNS name that resolves to private IP addresses.
Type: String
Required: No

 **SecurityGroups.member.N**
The IDs of the security groups to assign to the load balancer.
Type: Array of strings
Required: No

 **Subnets.member.N**
The IDs of the subnets in your VPC to attach to the load balancer. Specify one subnet per Availability Zone specified in `AvailabilityZones`.
Type: Array of strings
Required: No

 **Tags.member.N**
A list of tags to assign to the load balancer.
For more information about tagging your load balancer, see [Tag your Classic Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/add-remove-tags.html) in the *User Guide for Classic Load Balancers*.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 1 item.
Required: No

## Response Elements
<a name="API_CreateLoadBalancer_ResponseElements"></a>

The following element is returned by the service.

 ** DNSName **
The DNS name of the load balancer.
Type: String

## Errors
<a name="API_CreateLoadBalancer_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** CertificateNotFound **
The specified ARN does not refer to a valid SSL certificate in AWS Identity and Access Management (IAM) or AWS Certificate Manager (ACM). Note that if you recently uploaded the certificate to IAM, this error might indicate that the certificate is not fully available yet.
HTTP Status Code: 400

 ** DuplicateLoadBalancerName **
The specified load balancer name already exists for this account.
HTTP Status Code: 400

 ** DuplicateTagKeys **
A tag key was specified more than once.
HTTP Status Code: 400

 ** InvalidConfigurationRequest **
The requested configuration change is not valid.
HTTP Status Code: 409

 ** InvalidScheme **
The specified value for the schema is not valid. You can only specify a scheme for load balancers in a VPC.
HTTP Status Code: 400

 ** InvalidSecurityGroup **
One or more of the specified security groups do not exist.
HTTP Status Code: 400

 ** InvalidSubnet **
The specified VPC has no associated Internet gateway.
HTTP Status Code: 400

 ** OperationNotPermitted **
This operation is not allowed.
HTTP Status Code: 400

 ** SubnetNotFound **
One or more of the specified subnets do not exist.
HTTP Status Code: 400

 ** TooManyLoadBalancers **
The quota for the number of load balancers has been reached.
HTTP Status Code: 400

 ** TooManyTags **
The quota for the number of tags that can be assigned to a load balancer has been reached.
HTTP Status Code: 400

 ** UnsupportedProtocol **
The specified protocol or signature version is not supported.
HTTP Status Code: 400

## Examples
<a name="API_CreateLoadBalancer_Examples"></a>

### Create a Classic Load Balancer
<a name="API_CreateLoadBalancer_Example_1"></a>

This example creates an HTTP load balancer in the specified subnet.

#### Sample Request
<a name="API_CreateLoadBalancer_Example_1_Request"></a>

```
https://elasticloadbalancing.amazonaws.com/?Action=CreateLoadBalancer
&LoadBalancerName=my-vpc-loadbalancer
&Listeners.member.1.LoadBalancerPort=80
&Listeners.member.1.InstancePort=80
&Listeners.member.1.Protocol=http
&Listeners.member.1.InstanceProtocol=http
&Subnets.member.1=subnet-6dec9f03
&SecurityGroups.member.1=sg-6801da07
&Version=2012-06-01
&AUTHPARAMS
```

#### Sample Response
<a name="API_CreateLoadBalancer_Example_1_Response"></a>

```
<CreateLoadBalancerResponse xmlns="http://elasticloadbalancing.amazonaws.com/doc/2012-06-01/">
  <CreateLoadBalancerResult>
    <DNSName>my-vpc-loadbalancer-1234567890.us-east-1.elb.amazonaws.com</DNSName>
  </CreateLoadBalancerResult>
  <ResponseMetadata>
    <RequestId>1549581b-12b7-11e3-895e-1334aEXAMPLE</RequestId>
  </ResponseMetadata>
</CreateLoadBalancerResponse>
```

### Create an internal load balancer
<a name="API_CreateLoadBalancer_Example_2"></a>

This example creates an internal HTTP load balancer in the specified subnet.

#### Sample Request
<a name="API_CreateLoadBalancer_Example_2_Request"></a>

```
https://elasticloadbalancing.amazonaws.com/?Action=CreateLoadBalancer
&LoadBalancerName=my-internal-loadbalancer
&Scheme=internal
&SecurityGroups.member.1=sg-706cb61f
&Listeners.member.1.LoadBalancerPort=80
&Listeners.member.1.InstancePort=80
&Listeners.member.1.Protocol=http
&Listeners.member.1.InstanceProtocol=http
&Subnets.member.1=subnet-9edc97f0
&Version=2012-06-01
&AUTHPARAMS
```

#### Sample Response
<a name="API_CreateLoadBalancer_Example_2_Response"></a>

```
<CreateLoadBalancerResponse xmlns="http://elasticloadbalancing.amazonaws.com/doc/2012-06-01/">
  <CreateLoadBalancerResult>
    <DNSName>internal-my-internal-loadbalancer-1234567890.us-east-1.elb.amazonaws.com</DNSName>
  </CreateLoadBalancerResult>
  <ResponseMetadata>
    <RequestId>1549581b-12b7-11e3-895e-1334aEXAMPLE</RequestId>
  </ResponseMetadata>
</CreateLoadBalancerResponse>
```

### Create a load balancer in a default VPC
<a name="API_CreateLoadBalancer_Example_3"></a>

This example creates a load balancer in the default VPC for the specified Region.

#### Sample Request
<a name="API_CreateLoadBalancer_Example_3_Request"></a>

```
https://elasticloadbalancing.amazonaws.com/?Action=CreateLoadBalancer
&LoadBalancerName=my-defaultvpc-loadbalancer
&AvailabilityZones.member.1=sa-east-1b
&Listeners.member.1.LoadBalancerPort=80
&Listeners.member.1.InstancePort=80
&Listeners.member.1.Protocol=http
&Listeners.member.1.InstanceProtocol=http
&Version=2012-06-01
&AUTHPARAMS
```

#### Sample Response
<a name="API_CreateLoadBalancer_Example_3_Response"></a>

```
<CreateLoadBalancerResponse xmlns="http://elasticloadbalancing.amazonaws.com/doc/2012-06-01/">
  <CreateLoadBalancerResult>
    <DNSName>my-defaultvpc-loadbalancer-1234567890.sa.east-1.elb.amazonaws.com</DNSName>
  </CreateLoadBalancerResult>
  <ResponseMetadata>
    <RequestId>1549581b-12b7-11e3-895e-1334aEXAMPLE</RequestId>
  </ResponseMetadata>
</CreateLoadBalancerResponse>
```

### Create a load balancer and assign a tag
<a name="API_CreateLoadBalancer_Example_4"></a>

This example creates an HTTP load balancer and assigns it a tag.

#### Sample Request
<a name="API_CreateLoadBalancer_Example_4_Request"></a>

```
https://elasticloadbalancing.amazonaws.com/?Action=CreateLoadBalancer
&LoadBalancerName=my-loadbalancer
&AvailabilityZones.member.1=us-east-1c;
&Listeners.member.1.LoadBalancerPort=80
&Listeners.member.1.InstancePort=80
&Listeners.member.1.Protocol=http
&Listeners.member.1.InstanceProtocol=http
&Tags.member.1.Value=digital-media
&Tags.member.1.Key=department
&Version=2012-06-01
&AUTHPARAMS
```

#### Sample Response
<a name="API_CreateLoadBalancer_Example_4_Response"></a>

```
<CreateLoadBalancerResponse xmlns="http://elasticloadbalancing.amazonaws.com/doc/2012-06-01/">
  <CreateLoadBalancerResult>
    <DNSName>my-loadbalancer-1234567890.us-east-1.elb.amazonaws.com</DNSName>
  </CreateLoadBalancerResult>
  <ResponseMetadata>
    <RequestId>1549581b-12b7-11e3-895e-1334aEXAMPLE</RequestId>
  </ResponseMetadata>
</CreateLoadBalancerResponse>
```

## See Also
<a name="API_CreateLoadBalancer_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticloadbalancing-2012-06-01/CreateLoadBalancer)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticloadbalancing-2012-06-01/CreateLoadBalancer)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticloadbalancing-2012-06-01/CreateLoadBalancer)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticloadbalancing-2012-06-01/CreateLoadBalancer)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticloadbalancing-2012-06-01/CreateLoadBalancer)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticloadbalancing-2012-06-01/CreateLoadBalancer)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticloadbalancing-2012-06-01/CreateLoadBalancer)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticloadbalancing-2012-06-01/CreateLoadBalancer)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elasticloadbalancing-2012-06-01/CreateLoadBalancer)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticloadbalancing-2012-06-01/CreateLoadBalancer)
