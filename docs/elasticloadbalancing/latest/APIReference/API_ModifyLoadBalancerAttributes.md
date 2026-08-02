---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_ModifyLoadBalancerAttributes.html
---

# ModifyLoadBalancerAttributes
<a name="API_ModifyLoadBalancerAttributes"></a>

Modifies the specified attributes of the specified Application Load Balancer, Network Load Balancer, or Gateway Load Balancer.

If any of the specified attributes can't be modified as requested, the call fails. Any existing attributes that you do not modify retain their current values.

## Request Parameters
<a name="API_ModifyLoadBalancerAttributes_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 **Attributes.member.N**
The load balancer attributes.
Type: Array of [LoadBalancerAttribute](API_LoadBalancerAttribute.md) objects
Array Members: Maximum number of 20 items.
Required: Yes

 ** LoadBalancerArn **
The Amazon Resource Name (ARN) of the load balancer.
Type: String
Required: Yes

## Response Elements
<a name="API_ModifyLoadBalancerAttributes_ResponseElements"></a>

The following element is returned by the service.

 **Attributes.member.N**
Information about the load balancer attributes.
Type: Array of [LoadBalancerAttribute](API_LoadBalancerAttribute.md) objects
Array Members: Maximum number of 20 items.

## Errors
<a name="API_ModifyLoadBalancerAttributes_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidConfigurationRequest **
The requested configuration is not valid.
HTTP Status Code: 400

 ** LoadBalancerNotFound **
The specified load balancer does not exist.
HTTP Status Code: 400

## Examples
<a name="API_ModifyLoadBalancerAttributes_Examples"></a>

### Enable deletion protection
<a name="API_ModifyLoadBalancerAttributes_Example_1"></a>

This example enables deletion protection for the specified load balancer.

#### Sample Request
<a name="API_ModifyLoadBalancerAttributes_Example_1_Request"></a>

```
https://elasticloadbalancing.amazonaws.com/?Action=ModifyLoadBalancerAttributes
&LoadBalancerArn=arn:aws:elasticloadbalancing:us-west-2:123456789012:loadbalancer/app/my-load-balancer/50dc6c495c0c9188
&Attributes.member.1.Key=deletion_protection.enabled
&Attributes.member.1.Value=true
&Version=2015-12-01
&AUTHPARAMS
```

#### Sample Response
<a name="API_ModifyLoadBalancerAttributes_Example_1_Response"></a>

```
<ModifyLoadBalancerAttributesResponse xmlns="http://elasticloadbalancing.amazonaws.com/doc/2015-12-01/">
  <ModifyLoadBalancerAttributesResult>
    <Attributes>
      <member>
        <Value>true</Value>
        <Key>deletion_protection.enabled</Key>
      </member>
      <member>
        <Value>false</Value>
        <Key>access_logs.s3.enabled</Key>
      </member>
      <member>
        <Value>60</Value>
        <Key>idle_timeout.timeout_seconds</Key>
      </member>
      <member>
        <Value />
        <Key>access_logs.s3.prefix</Key>
      </member>
      <member>
        <Value />
        <Key>access_logs.s3.bucket</Key>
      </member>
    </Attributes>
  </ModifyLoadBalancerAttributesResult>
  <ResponseMetadata>
    <RequestId>b2066529-f42c-11e5-b543-9f2c3fbb9bee</RequestId>
  </ResponseMetadata>
</ModifyLoadBalancerAttributesResponse>
```

### Change the idle timeout
<a name="API_ModifyLoadBalancerAttributes_Example_2"></a>

This example changes the idle timeout value for the specified Application Load Balancer.

#### Sample Request
<a name="API_ModifyLoadBalancerAttributes_Example_2_Request"></a>

```
https://elasticloadbalancing.amazonaws.com/?Action=ModifyLoadBalancerAttributes
&LoadBalancerArn=arn:aws:elasticloadbalancing:us-west-2:123456789012:loadbalancer/app/my-load-balancer/50dc6c495c0c9188
&Attributes.member.1.Key=idle_timeout.timeout_seconds
&Attributes.member.1.Value=30
&Version=2015-12-01
&AUTHPARAMS
```

#### Sample Response
<a name="API_ModifyLoadBalancerAttributes_Example_2_Response"></a>

```
<ModifyLoadBalancerAttributesResponse xmlns="http://elasticloadbalancing.amazonaws.com/doc/2015-12-01/">
  <ModifyLoadBalancerAttributesResult>
    <Attributes>
      <member>
        <Value>30</Value>
        <Key>idle_timeout.timeout_seconds</Key>
      </member>
      <member>
        <Value>false</Value>
        <Key>access_logs.s3.enabled</Key>
      </member>
      <member>
        <Value />
        <Key>access_logs.s3.prefix</Key>
      </member>
      <member>
        <Value>false</Value>
        <Key>deletion_protection.enabled</Key>
      </member>
      <member>
        <Value />
        <Key>access_logs.s3.bucket</Key>
      </member>
    </Attributes>
  </ModifyLoadBalancerAttributesResult>
  <ResponseMetadata>
    <RequestId>d3f6e6dc-f42c-11e5-b5ae-8bfaf16614ac</RequestId>
  </ResponseMetadata>
</ModifyLoadBalancerAttributesResponse>
```

### Enable access logs
<a name="API_ModifyLoadBalancerAttributes_Example_3"></a>

This example enables access logs for the specified Application Load Balancer. The S3 bucket must exist in the same Region as the load balancer and must have a bucket policy that grants Elastic Load Balancing permissions to write to the bucket.

#### Sample Request
<a name="API_ModifyLoadBalancerAttributes_Example_3_Request"></a>

```
https://elasticloadbalancing.amazonaws.com/?Action=ModifyLoadBalancerAttributes
&LoadBalancerArn=arn:aws:elasticloadbalancing:us-west-2:123456789012:loadbalancer/app/my-load-balancer/50dc6c495c0c9188
&Attributes.member.1.Key=access_logs.s3.enabled
&Attributes.member.1.Value=true
&Attributes.member.2.Key=access_logs.s3.bucket
&Attributes.member.2.Value=my-loadbalancer-logs
&Attributes.member.3.Key=access_logs.s3.prefix
&Attributes.member.3.Value=myapp
&Version=2015-12-01
&AUTHPARAMS
```

#### Sample Response
<a name="API_ModifyLoadBalancerAttributes_Example_3_Response"></a>

```
<ModifyLoadBalancerAttributesResponse xmlns="http://elasticloadbalancing.amazonaws.com/doc/2015-12-01/">
  <ModifyLoadBalancerAttributesResult>
    <Attributes>
      <member>
        <Value>true</Value>
        <Key>access_logs.s3.enabled</Key>
      </member>
      <member>
        <Value>my-loadbalancer-logs</Value>
        <Key>access_logs.s3.bucket</Key>
      </member>
      <member>
        <Value>myapp</Value>
        <Key>access_logs.s3.prefix</Key>
      </member>
      <member>
        <Value>60</Value>
        <Key>idle_timeout.timeout_seconds</Key>
      </member>
      <member>
        <Value>false</Value>
        <Key>deletion_protection.enabled</Key>
      </member>
    </Attributes>
  </ModifyLoadBalancerAttributesResult>
  <ResponseMetadata>
    <RequestId>095cb76d-f52e-11e5-bb98-57195a6eb84a</RequestId>
  </ResponseMetadata>
</ModifyLoadBalancerAttributesResponse>
```

### Enable connection logs.
<a name="API_ModifyLoadBalancerAttributes_Example_4"></a>

This example enables connection logs, setting the specified S3 bucket and prefix location.

#### Sample Request
<a name="API_ModifyLoadBalancerAttributes_Example_4_Request"></a>

```
https://elasticloadbalancing.amazonaws.com/?Action=ModifyLoadBalancerAttributes
&LoadBalancerArn=arn:aws:elasticloadbalancing:us-west-2:123456789012:loadbalancer/app/my-load-balancer/50dc6c495c0c9188
&Attributes.member.1.Key=connection_logs.s3.enabled
&Attributes.member.1.Value=true
&Attributes.member.2.Key=connection_logs.s3.bucket
&Attributes.member.2.Value=my-loadbalancer-connection-logs
&Attributes.member.3.Key=connection_logs.s3.prefix
&Attributes.member.3.Value=myapp-connections
&Version=2015-12-01
&AUTHPARAMS
```

### Enable health check logs.
<a name="API_ModifyLoadBalancerAttributes_Example_5"></a>

This example enables health check logs, setting the specified S3 bucket and prefix location.

#### Sample Request
<a name="API_ModifyLoadBalancerAttributes_Example_5_Request"></a>

```
https://elasticloadbalancing.amazonaws.com/?Action=ModifyLoadBalancerAttributes
&LoadBalancerArn=arn:aws:elasticloadbalancing:us-west-2:123456789012:loadbalancer/app/my-load-balancer/50dc6c495c0c9188
&Attributes.member.1.Key=health_check_logs.s3.enabled
&Attributes.member.1.Value=true
&Attributes.member.2.Key=health_check_logs.s3.bucket
&Attributes.member.2.Value=my-loadbalancer-connection-logs
&Attributes.member.3.Key=health_check_logs.s3.prefix
&Attributes.member.3.Value=mylb-health
&Version=2015-12-01
&AUTHPARAMS
```

## See Also
<a name="API_ModifyLoadBalancerAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticloadbalancingv2-2015-12-01/ModifyLoadBalancerAttributes)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticloadbalancingv2-2015-12-01/ModifyLoadBalancerAttributes)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticloadbalancingv2-2015-12-01/ModifyLoadBalancerAttributes)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticloadbalancingv2-2015-12-01/ModifyLoadBalancerAttributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticloadbalancingv2-2015-12-01/ModifyLoadBalancerAttributes)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticloadbalancingv2-2015-12-01/ModifyLoadBalancerAttributes)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticloadbalancingv2-2015-12-01/ModifyLoadBalancerAttributes)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticloadbalancingv2-2015-12-01/ModifyLoadBalancerAttributes)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elasticloadbalancingv2-2015-12-01/ModifyLoadBalancerAttributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticloadbalancingv2-2015-12-01/ModifyLoadBalancerAttributes)
