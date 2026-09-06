---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/2012-06-01/APIReference/API_ModifyLoadBalancerAttributes.html
---

# ModifyLoadBalancerAttributes
<a name="API_ModifyLoadBalancerAttributes"></a>

Modifies the attributes of the specified load balancer.

You can modify the load balancer attributes, such as `AccessLogs`, `ConnectionDraining`, and `CrossZoneLoadBalancing` by either enabling or disabling them. Or, you can modify the load balancer attribute `ConnectionSettings` by specifying an idle connection timeout value for your load balancer.

For more information, see the following in the *User Guide for Classic Load Balancers*:
+  [Cross-zone load balancing](https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/enable-disable-crosszone-lb.html)
+  [Connection draining](https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/config-conn-drain.html)
+  [Access logs](https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/access-log-collection.html)
+  [Idle connection timeout](https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/config-idle-timeout.html)

## Request Parameters
<a name="API_ModifyLoadBalancerAttributes_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** LoadBalancerAttributes **
The attributes for the load balancer.
Type: [LoadBalancerAttributes](API_LoadBalancerAttributes.md) object
Required: Yes

 ** LoadBalancerName **
The name of the load balancer.
Type: String
Required: Yes

## Response Elements
<a name="API_ModifyLoadBalancerAttributes_ResponseElements"></a>

The following elements are returned by the service.

 ** LoadBalancerAttributes **
Information about the load balancer attributes.
Type: [LoadBalancerAttributes](API_LoadBalancerAttributes.md) object

 ** LoadBalancerName **
The name of the load balancer.
Type: String

## Errors
<a name="API_ModifyLoadBalancerAttributes_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidConfigurationRequest **
The requested configuration change is not valid.
HTTP Status Code: 409

 ** LoadBalancerAttributeNotFound **
The specified load balancer attribute does not exist.
HTTP Status Code: 400

 ** LoadBalancerNotFound **
The specified load balancer does not exist.
HTTP Status Code: 400

## Examples
<a name="API_ModifyLoadBalancerAttributes_Examples"></a>

### Enable cross-zone load balancing
<a name="API_ModifyLoadBalancerAttributes_Example_1"></a>

This example modifies the CrossZoneLoadBalancing attribute of the specified load balancer.

#### Sample Request
<a name="API_ModifyLoadBalancerAttributes_Example_1_Request"></a>

```
https://elasticloadbalancing.amazonaws.com/?Action=ModifyLoadBalancerAttributes
&LoadBalancerAttributes.CrossZoneLoadBalancing.Enabled=true
&LoadBalancerName=my-loadbalancer
&Version=2012-06-01
&AUTHPARAMS
```

#### Sample Response
<a name="API_ModifyLoadBalancerAttributes_Example_1_Response"></a>

```
<ModifyLoadBalancerAttributesResponse xmlns="http://elasticloadbalancing.amazonaws.com/doc/2012-06-01/">
  <ModifyLoadBalancerAttributesResult>
  <LoadBalancerName>my-loadbalancer</LoadBalancerName>
    <LoadBalancerAttributes>
      <CrossZoneLoadBalancing>
        <Enabled>true</Enabled>
      </CrossZoneLoadBalancing>
    </LoadBalancerAttributes>
  </ModifyLoadBalancerAttributesResult>
  <ResponseMetadata>
    <RequestId>83c88b9d-12b7-11e3-8b82-87b12EXAMPLE</RequestId>
  </ResponseMetadata>
</ModifyLoadBalancerAttributesResponse>
```

### Enable access logs
<a name="API_ModifyLoadBalancerAttributes_Example_2"></a>

This example enables access logs for the specified load balancer.

#### Sample Request
<a name="API_ModifyLoadBalancerAttributes_Example_2_Request"></a>

```
https://elasticloadbalancing.amazonaws.com/?Action=ModifyLoadBalancerAttributes
&LoadBalancerAttributes.AccessLog.Enabled=true
&LoadBalancerAttributes.AccessLog.S3BucketName=my-loadbalancer-logs
&LoadBalancerAttributes.AccessLog.S3BucketPrefix=my-bucket-prefix/prod
&LoadBalancerAttributes.AccessLog.EmitInterval=60
&LoadBalancerName=my-loadbalancer
&Version=2012-06-01
&AUTHPARAMS
```

#### Sample Response
<a name="API_ModifyLoadBalancerAttributes_Example_2_Response"></a>

```
<<ModifyLoadBalancerAttributesResponse xmlns="http://elasticloadbalancing.amazonaws.com/doc/2012-06-01/">
<ModifyLoadBalancerAttributesResult>
    <LoadBalancerName>my-loadbalancer</LoadBalancerName>
    <LoadBalancerAttributes>
      <AccessLog>
        <Enabled>true</Enabled>
        <S3BucketName>my-loadbalancer-logs</S3BucketName>
        <S3BucketPrefix>my-bucket-prefix/prod</S3BucketPrefix>
        <EmitInterval>60</EmitInterval>
      </AccessLog>
    </LoadBalancerAttributes>
  </ModifyLoadBalancerAttributesResult>
<ResponseMetadata>
    <RequestId>83c88b9d-12b7-11e3-8b82-87b12EXAMPLE</RequestId>
</ResponseMetadata>
</ModifyLoadBalancerAttributesResponse>
```

### Enable connection draining
<a name="API_ModifyLoadBalancerAttributes_Example_3"></a>

This example modifies the ConnectionDraining attribute of the specified load balancer.

#### Sample Request
<a name="API_ModifyLoadBalancerAttributes_Example_3_Request"></a>

```
https://elasticloadbalancing.amazonaws.com/?Action=ModifyLoadBalancerAttributes
&LoadBalancerName=my-loadbalancer
&LoadBalancerAttributes.ConnectionDraining.Enabled=true
&LoadBalancerAttributes.ConnectionDraining.Timeout=60
&Version=2012-06-01
&AUTHPARAMS
```

#### Sample Response
<a name="API_ModifyLoadBalancerAttributes_Example_3_Response"></a>

```
<<ModifyLoadBalancerAttributesResponse xmlns="http://elasticloadbalancing.amazonaws.com/doc/2012-06-01/">
<ModifyLoadBalancerAttributesResult>
    <LoadBalancerName>my-loadbalancer</LoadBalancerName>
    <LoadBalancerAttributes>
      <ConnectionDraining>
        <Enabled>true</Enabled>
        <Timeout>60</Timeout>
      </ConnectionDraining>
    </LoadBalancerAttributes>
  </ModifyLoadBalancerAttributesResult>
<ResponseMetadata>
    <RequestId>83c88b9d-12b7-11e3-8b82-87b12EXAMPLE</RequestId>
</ResponseMetadata>
</ModifyLoadBalancerAttributesResponse>
```

### Configure idle timeout
<a name="API_ModifyLoadBalancerAttributes_Example_4"></a>

This example modifies the idle timeout value of the specified load balancer.

#### Sample Request
<a name="API_ModifyLoadBalancerAttributes_Example_4_Request"></a>

```
https://elasticloadbalancing.amazonaws.com/?Action=ModifyLoadBalancerAttributes
&LoadBalancerAttributes.ConnectionSettings.IdleTimeout=30
&LoadBalancerName=my-loadbalancer
&Version=2012-06-01
&AUTHPARAMS
```

#### Sample Response
<a name="API_ModifyLoadBalancerAttributes_Example_4_Response"></a>

```
<<ModifyLoadBalancerAttributesResponse xmlns="http://elasticloadbalancing.amazonaws.com/doc/2012-06-01/">
<ModifyLoadBalancerAttributesResult>
    <LoadBalancerName>my-loadbalancer</LoadBalancerName>
    <LoadBalancerAttributes>
       <ConnectionSettings>
          <IdleTimeout>30</IdleTimeout>
       </ConnectionSettings>
    </LoadBalancerAttributes>
  </ModifyLoadBalancerAttributesResult>
<ResponseMetadata>
    <RequestId>83c88b9d-12b7-11e3-8b82-87b12EXAMPLE</RequestId>
</ResponseMetadata>
</ModifyLoadBalancerAttributesResponse>
```

## See Also
<a name="API_ModifyLoadBalancerAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticloadbalancing-2012-06-01/ModifyLoadBalancerAttributes)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticloadbalancing-2012-06-01/ModifyLoadBalancerAttributes)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticloadbalancing-2012-06-01/ModifyLoadBalancerAttributes)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticloadbalancing-2012-06-01/ModifyLoadBalancerAttributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticloadbalancing-2012-06-01/ModifyLoadBalancerAttributes)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticloadbalancing-2012-06-01/ModifyLoadBalancerAttributes)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticloadbalancing-2012-06-01/ModifyLoadBalancerAttributes)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticloadbalancing-2012-06-01/ModifyLoadBalancerAttributes)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elasticloadbalancing-2012-06-01/ModifyLoadBalancerAttributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticloadbalancing-2012-06-01/ModifyLoadBalancerAttributes)
