---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/2012-06-01/APIReference/API_LoadBalancerAttributes.html
---

# LoadBalancerAttributes
<a name="API_LoadBalancerAttributes"></a>

The attributes for a load balancer.

## Contents
<a name="API_LoadBalancerAttributes_Contents"></a>

 ** AccessLog **
If enabled, the load balancer captures detailed information of all requests and delivers the information to the Amazon S3 bucket that you specify.
For more information, see [Enable access logs](https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/enable-access-logs.html) in the *User Guide for Classic Load Balancers*.
Type: [AccessLog](API_AccessLog.md) object
Required: No

 ** AdditionalAttributes.member.N **
Any additional attributes.
Type: Array of [AdditionalAttribute](API_AdditionalAttribute.md) objects
Array Members: Maximum number of 10 items.
Required: No

 ** ConnectionDraining **
If enabled, the load balancer allows existing requests to complete before the load balancer shifts traffic away from a deregistered or unhealthy instance.
For more information, see [Configure connection draining](https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/config-conn-drain.html) in the *User Guide for Classic Load Balancers*.
Type: [ConnectionDraining](API_ConnectionDraining.md) object
Required: No

 ** ConnectionSettings **
If enabled, the load balancer allows the connections to remain idle (no data is sent over the connection) for the specified duration.
By default, Elastic Load Balancing maintains a 60-second idle connection timeout for both front-end and back-end connections of your load balancer. For more information, see [Configure idle connection timeout](https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/config-idle-timeout.html) in the *User Guide for Classic Load Balancers*.
Type: [ConnectionSettings](API_ConnectionSettings.md) object
Required: No

 ** CrossZoneLoadBalancing **
If enabled, the load balancer routes the request traffic evenly across all instances regardless of the Availability Zones.
For more information, see [Configure cross-zone load balancing](https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/enable-disable-crosszone-lb.html) in the *User Guide for Classic Load Balancers*.
Type: [CrossZoneLoadBalancing](API_CrossZoneLoadBalancing.md) object
Required: No

## See Also
<a name="API_LoadBalancerAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticloadbalancing-2012-06-01/LoadBalancerAttributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticloadbalancing-2012-06-01/LoadBalancerAttributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticloadbalancing-2012-06-01/LoadBalancerAttributes)
