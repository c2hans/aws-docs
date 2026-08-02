---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/2012-06-01/APIReference/API_DescribeInstanceHealth.html
---

# DescribeInstanceHealth
<a name="API_DescribeInstanceHealth"></a>

Describes the state of the specified instances with respect to the specified load balancer. If no instances are specified, the call describes the state of all instances that are currently registered with the load balancer. If instances are specified, their state is returned even if they are no longer registered with the load balancer. The state of terminated instances is not returned.

## Request Parameters
<a name="API_DescribeInstanceHealth_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 **Instances.member.N**
The IDs of the instances.
Type: Array of [Instance](API_Instance.md) objects
Required: No

 ** LoadBalancerName **
The name of the load balancer.
Type: String
Required: Yes

## Response Elements
<a name="API_DescribeInstanceHealth_ResponseElements"></a>

The following element is returned by the service.

 **InstanceStates.member.N**
Information about the health of the instances.
Type: Array of [InstanceState](API_InstanceState.md) objects

## Errors
<a name="API_DescribeInstanceHealth_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidInstance **
The specified endpoint is not valid.
HTTP Status Code: 400

 ** LoadBalancerNotFound **
The specified load balancer does not exist.
HTTP Status Code: 400

## Examples
<a name="API_DescribeInstanceHealth_Examples"></a>

### Describe instance health
<a name="API_DescribeInstanceHealth_Example_1"></a>

This example describes the health of the instances for the specified load balancer.

#### Sample Request
<a name="API_DescribeInstanceHealth_Example_1_Request"></a>

```
https://elasticloadbalancing.amazonaws.com/?Action=DescribeInstanceHealth
&LoadBalancerName=my-loadbalancer
&Version=2012-06-01
&AUTHPARAMS
```

### Response for a healthy instance
<a name="API_DescribeInstanceHealth_Example_2"></a>

This following example response describes a healthy instance.

#### Sample Response
<a name="API_DescribeInstanceHealth_Example_2_Response"></a>

```
<DescribeInstanceHealthResponse xmlns="http://elasticloadbalancing.amazonaws.com/doc/2012-06-01/">
  <DescribeInstanceHealthResult>
    <InstanceStates>
      <member>
        <Description>N/A</Description>
        <InstanceId>i-90d8c2a5</InstanceId>
        <State>InService</State>
        <ReasonCode>N/A</ReasonCode>
      </member>
    </InstanceStates>
  </DescribeInstanceHealthResult>
  <ResponseMetadata>
    <RequestId>1549581b-12b7-11e3-895e-1334aEXAMPLE</RequestId>
  </ResponseMetadata>
</DescribeInstanceHealthResponse>
```

### Response for an instance not registered
<a name="API_DescribeInstanceHealth_Example_3"></a>

The following example response describes an instance that is still being registered.

#### Sample Response
<a name="API_DescribeInstanceHealth_Example_3_Response"></a>

```
<DescribeInstanceHealthResponse xmlns="http://elasticloadbalancing.amazonaws.com/doc/2012-06-01/">
  <DescribeInstanceHealthResult>
    <InstanceStates>
      <member>
        <Description>Instance registration is still in progress.</Description>
        <InstanceId>i-315b7e51</InstanceId>
        <State>OutOfService</State>
        <ReasonCode>ELB</ReasonCode>
      </member>
    </InstanceStates>
  </DescribeInstanceHealthResult>
  <ResponseMetadata>
    <RequestId>1549581b-12b7-11e3-895e-1334aEXAMPLE</RequestId>
  </ResponseMetadata>
</DescribeInstanceHealthResponse>
```

### Response for an unhealthy instance
<a name="API_DescribeInstanceHealth_Example_4"></a>

This following example response describes an unhealthy instance.

#### Sample Response
<a name="API_DescribeInstanceHealth_Example_4_Response"></a>

```
<DescribeInstanceHealthResponse xmlns="http://elasticloadbalancing.amazonaws.com/doc/2012-06-01/">
  <DescribeInstanceHealthResult>
    <InstanceStates>
      <member>
        <Description>Instance has failed at least the UnhealthyThreshold number of health checks consecutively.</Description>
        <InstanceId>i-fda142c9</InstanceId>
        <State>OutOfService</State>
        <ReasonCode>Instance</ReasonCode>
      </member>
    </InstanceStates>
  </DescribeInstanceHealthResult>
  <ResponseMetadata>
    <RequestId>83c88b9d-12b7-11e3-8b82-87b12EXAMPLE</RequestId>
</ResponseMetadata>
</DescribeInstanceHealthResponse>
```

### Response for an instance in an unknown state
<a name="API_DescribeInstanceHealth_Example_5"></a>

This following example response describes an instance in an unknown state.

#### Sample Response
<a name="API_DescribeInstanceHealth_Example_5_Response"></a>

```
<DescribeInstanceHealthResponse xmlns="http://elasticloadbalancing.amazonaws.com/doc/2012-06-01/">
  <DescribeInstanceHealthResult>
    <InstanceStates>
      <member>
        <Description>A transient error occurred. Please try again later.</Description>
        <InstanceId>i-7f12e649</InstanceId>
        <State>Unknown</State>
        <ReasonCode>ELB</ReasonCode>
      </member>
    </InstanceStates>
  </DescribeInstanceHealthResult>
  <ResponseMetadata>
    <RequestId>83c88b9d-12b7-11e3-8b82-87b12EXAMPLE</RequestId>
</ResponseMetadata>
</DescribeInstanceHealthResponse>
```

## See Also
<a name="API_DescribeInstanceHealth_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticloadbalancing-2012-06-01/DescribeInstanceHealth)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticloadbalancing-2012-06-01/DescribeInstanceHealth)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticloadbalancing-2012-06-01/DescribeInstanceHealth)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticloadbalancing-2012-06-01/DescribeInstanceHealth)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticloadbalancing-2012-06-01/DescribeInstanceHealth)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticloadbalancing-2012-06-01/DescribeInstanceHealth)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticloadbalancing-2012-06-01/DescribeInstanceHealth)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticloadbalancing-2012-06-01/DescribeInstanceHealth)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elasticloadbalancing-2012-06-01/DescribeInstanceHealth)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticloadbalancing-2012-06-01/DescribeInstanceHealth)
