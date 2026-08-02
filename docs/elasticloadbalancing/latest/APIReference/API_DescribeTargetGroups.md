---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_DescribeTargetGroups.html
---

# DescribeTargetGroups
<a name="API_DescribeTargetGroups"></a>

Describes the specified target groups or all of your target groups. By default, all target groups are described. Alternatively, you can specify one of the following to filter the results: the ARN of the load balancer, the names of one or more target groups, or the ARNs of one or more target groups.

To describe the targets for a target group, use [DescribeTargetHealth](API_DescribeTargetHealth.md). To describe the attributes of a target group, use [DescribeTargetGroupAttributes](API_DescribeTargetGroupAttributes.md).

## Request Parameters
<a name="API_DescribeTargetGroups_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** LoadBalancerArn **
The Amazon Resource Name (ARN) of the load balancer.
Type: String
Required: No

 ** Marker **
The marker for the next set of results. (You received this marker from a previous call.)
Type: String
Required: No

 **Names.member.N**
The names of the target groups.
Type: Array of strings
Required: No

 ** PageSize **
The maximum number of results to return with this call.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 400.
Required: No

 **TargetGroupArns.member.N**
The Amazon Resource Names (ARN) of the target groups.
Type: Array of strings
Required: No

## Response Elements
<a name="API_DescribeTargetGroups_ResponseElements"></a>

The following elements are returned by the service.

 ** NextMarker **
If there are additional results, this is the marker for the next set of results. Otherwise, this is null.
Type: String

 **TargetGroups.member.N**
Information about the target groups.
Type: Array of [TargetGroup](API_TargetGroup.md) objects

## Errors
<a name="API_DescribeTargetGroups_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** LoadBalancerNotFound **
The specified load balancer does not exist.
HTTP Status Code: 400

 ** TargetGroupNotFound **
The specified target group does not exist.
HTTP Status Code: 400

## Examples
<a name="API_DescribeTargetGroups_Examples"></a>

### Describe a target group
<a name="API_DescribeTargetGroups_Example_1"></a>

This example describes the specified target group.

#### Sample Request
<a name="API_DescribeTargetGroups_Example_1_Request"></a>

```
https://elasticloadbalancing.amazonaws.com/?Action=DescribeTargetGroups
&TargetGroupArns.member.1=arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-targets/73e2d6bc24d8a067
&Version=2015-12-01
&AUTHPARAMS
```

#### Sample Response
<a name="API_DescribeTargetGroups_Example_1_Response"></a>

```
<DescribeTargetGroupsResponse xmlns="http://elasticloadbalancing.amazonaws.com/doc/2015-12-01/">
  <DescribeTargetGroupsResult>
    <TargetGroups>
      <member>
        <TargetGroupArn>arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-targets/73e2d6bc24d8a067</TargetGroupArn>
        <HealthCheckTimeoutSeconds>5</HealthCheckTimeoutSeconds>
        <HealthCheckPort>traffic-port</HealthCheckPort>
        <Matcher>
          <HttpCode>200</HttpCode>
        </Matcher>
        <TargetGroupName>my-targets</TargetGroupName>
        <HealthCheckProtocol>HTTP</HealthCheckProtocol>
        <HealthCheckPath>/</HealthCheckPath>
        <Protocol>HTTP</Protocol>
        <Port>80</Port>
        <VpcId>vpc-3ac0fb5f</VpcId>
        <HealthyThresholdCount>5</HealthyThresholdCount>
        <HealthCheckIntervalSeconds>30</HealthCheckIntervalSeconds>
        <LoadBalancerArns>
          <member>arn:aws:elasticloadbalancing:us-west-2:123456789012:loadbalancer/app/my-load-balancer/50dc6c495c0c9188</member>
        </LoadBalancerArns>
        <UnhealthyThresholdCount>2</UnhealthyThresholdCount>
      </member>
    </TargetGroups>
  </DescribeTargetGroupsResult>
  <ResponseMetadata>
    <RequestId>70092c0e-f3a9-11e5-ae48-cff02092876b</RequestId>
  </ResponseMetadata>
</DescribeTargetGroupsResponse>
```

### Describe all target groups for a load balancer
<a name="API_DescribeTargetGroups_Example_2"></a>

This example describes all target groups for the specified load balancer.

#### Sample Request
<a name="API_DescribeTargetGroups_Example_2_Request"></a>

```
https://elasticloadbalancing.amazonaws.com/?Action=DescribeTargetGroups
&LoadBalancerArn=arn:aws:elasticloadbalancing:us-west-2:123456789012:loadbalancer/app/my-load-balancer/50dc6c495c0c9188
&Version=2015-12-01
&AUTHPARAMS
```

### Describe all target groups
<a name="API_DescribeTargetGroups_Example_3"></a>

This example describes all of your target groups.

#### Sample Request
<a name="API_DescribeTargetGroups_Example_3_Request"></a>

```
https://elasticloadbalancing.amazonaws.com/?Action=DescribeTargetGroups
&Version=2015-12-01
&AUTHPARAMS
```

## See Also
<a name="API_DescribeTargetGroups_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticloadbalancingv2-2015-12-01/DescribeTargetGroups)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticloadbalancingv2-2015-12-01/DescribeTargetGroups)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticloadbalancingv2-2015-12-01/DescribeTargetGroups)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticloadbalancingv2-2015-12-01/DescribeTargetGroups)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticloadbalancingv2-2015-12-01/DescribeTargetGroups)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticloadbalancingv2-2015-12-01/DescribeTargetGroups)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticloadbalancingv2-2015-12-01/DescribeTargetGroups)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticloadbalancingv2-2015-12-01/DescribeTargetGroups)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elasticloadbalancingv2-2015-12-01/DescribeTargetGroups)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticloadbalancingv2-2015-12-01/DescribeTargetGroups)
