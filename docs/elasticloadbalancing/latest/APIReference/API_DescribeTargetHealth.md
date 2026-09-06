---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_DescribeTargetHealth.html
---

# DescribeTargetHealth
<a name="API_DescribeTargetHealth"></a>

Describes the health of the specified targets or all of your targets.

## Request Parameters
<a name="API_DescribeTargetHealth_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 **Include.member.N**
Used to include anomaly detection information.
Type: Array of strings
Valid Values: `AnomalyDetection | All`
Required: No

 ** TargetGroupArn **
The Amazon Resource Name (ARN) of the target group.
Type: String
Required: Yes

 **Targets.member.N**
The targets.
Type: Array of [TargetDescription](API_TargetDescription.md) objects
Required: No

## Response Elements
<a name="API_DescribeTargetHealth_ResponseElements"></a>

The following element is returned by the service.

 **TargetHealthDescriptions.member.N**
Information about the health of the targets.
Type: Array of [TargetHealthDescription](API_TargetHealthDescription.md) objects

## Errors
<a name="API_DescribeTargetHealth_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** HealthUnavailable **
The health of the specified targets could not be retrieved due to an internal error.
HTTP Status Code: 500

 ** InvalidTarget **
The specified target does not exist, is not in the same VPC as the target group, or has an unsupported instance type.
HTTP Status Code: 400

 ** TargetGroupNotFound **
The specified target group does not exist.
HTTP Status Code: 400

## Examples
<a name="API_DescribeTargetHealth_Examples"></a>

### Describe the health of the targets for a target group
<a name="API_DescribeTargetHealth_Example_1"></a>

This example describes the health of the targets for the specified target group. These targets are healthy.

#### Sample Request
<a name="API_DescribeTargetHealth_Example_1_Request"></a>

```
https://elasticloadbalancing.amazonaws.com/?Action=DescribeTargetHealth
&TargetGroupArn=arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-targets/73e2d6bc24d8a067
&Version=2015-12-01
&AUTHPARAMS
```

#### Sample Response
<a name="API_DescribeTargetHealth_Example_1_Response"></a>

```
<DescribeTargetHealthResponse xmlns="http://elasticloadbalancing.amazonaws.com/doc/2015-12-01/">
  <DescribeTargetHealthResult>
    <TargetHealthDescriptions>
      <member>
        <HealthCheckPort>80</HealthCheckPort>
        <TargetHealth>
          <State>healthy</State>
        </TargetHealth>
        <Target>
          <Port>80</Port>
          <Id>i-0f76fade</Id>
        </Target>
      </member>
      <member>
        <HealthCheckPort>80</HealthCheckPort>
        <TargetHealth>
          <State>healthy</State>
        </TargetHealth>
        <Target>
          <Port>80</Port>
          <Id>i-0f76fade</Id>
        </Target>
      </member>
    </TargetHealthDescriptions>
  </DescribeTargetHealthResult>
  <ResponseMetadata>
    <RequestId>c534f810-f389-11e5-9192-3fff33344cfa</RequestId>
  </ResponseMetadata>
</DescribeTargetHealthResponse>
```

### Describe the health of the specified target
<a name="API_DescribeTargetHealth_Example_2"></a>

This example describes the health of the specified target. This target is healthy.

#### Sample Request
<a name="API_DescribeTargetHealth_Example_2_Request"></a>

```
https://elasticloadbalancing.amazonaws.com/?Action=DescribeTargetHealth
&TargetGroupArn=arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-targets/73e2d6bc24d8a067
&Targets.member.1.Id=i-0f76fade
&Targets.member.1.Port=80
&Version=2015-12-01
&AUTHPARAMS
```

#### Sample Response
<a name="API_DescribeTargetHealth_Example_2_Response"></a>

```
<DescribeTargetHealthResponse xmlns="http://elasticloadbalancing.amazonaws.com/doc/2015-12-01/">
  <DescribeTargetHealthResult>
    <TargetHealthDescriptions>
      <member>
        <HealthCheckPort>80</HealthCheckPort>
        <TargetHealth>
          <State>healthy</State>
        </TargetHealth>
        <Target>
          <Port>80</Port>
          <Id>i-0f76fade</Id>
        </Target>
      </member>
    </TargetHealthDescriptions>
  </DescribeTargetHealthResult>
  <ResponseMetadata>
    <RequestId>c534f810-f389-11e5-9192-3fff33344cfa</RequestId>
  </ResponseMetadata>
</DescribeTargetHealthResponse>
```

## See Also
<a name="API_DescribeTargetHealth_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticloadbalancingv2-2015-12-01/DescribeTargetHealth)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticloadbalancingv2-2015-12-01/DescribeTargetHealth)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticloadbalancingv2-2015-12-01/DescribeTargetHealth)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticloadbalancingv2-2015-12-01/DescribeTargetHealth)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticloadbalancingv2-2015-12-01/DescribeTargetHealth)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticloadbalancingv2-2015-12-01/DescribeTargetHealth)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticloadbalancingv2-2015-12-01/DescribeTargetHealth)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticloadbalancingv2-2015-12-01/DescribeTargetHealth)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elasticloadbalancingv2-2015-12-01/DescribeTargetHealth)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticloadbalancingv2-2015-12-01/DescribeTargetHealth)
