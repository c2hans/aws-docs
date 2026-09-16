---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/2012-06-01/APIReference/API_ConfigureHealthCheck.html
---

# ConfigureHealthCheck
<a name="API_ConfigureHealthCheck"></a>

Specifies the health check settings to use when evaluating the health state of your EC2 instances.

For more information, see [Configure health checks for your load balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-healthchecks.html) in the *User Guide for Classic Load Balancers*.

## Request Parameters
<a name="API_ConfigureHealthCheck_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** HealthCheck **
The configuration information.
Type: [HealthCheck](API_HealthCheck.md) object
Required: Yes

 ** LoadBalancerName **
The name of the load balancer.
Type: String
Required: Yes

## Response Elements
<a name="API_ConfigureHealthCheck_ResponseElements"></a>

The following element is returned by the service.

 ** HealthCheck **
The updated health check.
Type: [HealthCheck](API_HealthCheck.md) object

## Errors
<a name="API_ConfigureHealthCheck_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** LoadBalancerNotFound **
The specified load balancer does not exist.
HTTP Status Code: 400

## Examples
<a name="API_ConfigureHealthCheck_Examples"></a>

### Configure health check settings
<a name="API_ConfigureHealthCheck_Example_1"></a>

This example specifies the health check settings used to evaluate the health of your EC2 instances.

#### Sample Request
<a name="API_ConfigureHealthCheck_Example_1_Request"></a>

```
https://elasticloadbalancing.amazonaws.com/?Action=ConfigureHealthCheck
&LoadBalancerName=my-loadbalancer
&HealthCheck.HealthyThreshold=2
&HealthCheck.UnhealthyThreshold=2
&HealthCheck.Target=HTTP:80/ping
&HealthCheck.Interval=30
&HealthCheck.Timeout=3
&Version=2012-06-01
&AUTHPARAMS
```

#### Sample Response
<a name="API_ConfigureHealthCheck_Example_1_Response"></a>

```
<ConfigureHealthCheckResponse xmlns="http://elasticloadbalancing.amazonaws.com/doc/2012-06-01/">
  <ConfigureHealthCheckResult>
    <HealthCheck>
      <Interval>30</Interval>
      <Target>HTTP:80/ping</Target>
      <HealthyThreshold>2</HealthyThreshold>
      <Timeout>3</Timeout>
      <UnhealthyThreshold>2</UnhealthyThreshold>
    </HealthCheck>
  </ConfigureHealthCheckResult>
  <ResponseMetadata>
    <RequestId>83c88b9d-12b7-11e3-8b82-87b12EXAMPLE</RequestId>
  </ResponseMetadata>
</ConfigureHealthCheckResponse>
```

## See Also
<a name="API_ConfigureHealthCheck_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticloadbalancing-2012-06-01/ConfigureHealthCheck)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticloadbalancing-2012-06-01/ConfigureHealthCheck)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticloadbalancing-2012-06-01/ConfigureHealthCheck)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticloadbalancing-2012-06-01/ConfigureHealthCheck)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticloadbalancing-2012-06-01/ConfigureHealthCheck)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticloadbalancing-2012-06-01/ConfigureHealthCheck)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticloadbalancing-2012-06-01/ConfigureHealthCheck)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticloadbalancing-2012-06-01/ConfigureHealthCheck)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/elasticloadbalancing-2012-06-01/ConfigureHealthCheck)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticloadbalancing-2012-06-01/ConfigureHealthCheck)
