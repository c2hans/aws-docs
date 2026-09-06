---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DescribeAutoScalingGroups.html
---

# DescribeAutoScalingGroups
<a name="API_DescribeAutoScalingGroups"></a>

Gets information about the Auto Scaling groups in the account and Region.

If you specify Auto Scaling group names, the output includes information for only the specified Auto Scaling groups. If you specify filters, the output includes information for only those Auto Scaling groups that meet the filter criteria. If you do not specify group names or filters, the output includes information for all Auto Scaling groups.

This operation also returns information about instances in Auto Scaling groups. To retrieve information about the instances in a warm pool, you must call the [DescribeWarmPool](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DescribeWarmPool.html) API.

## Request Parameters
<a name="API_DescribeAutoScalingGroups_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 **AutoScalingGroupNames.member.N**
The names of the Auto Scaling groups. By default, you can only specify up to 50 names. You can optionally increase this limit using the `MaxRecords` property.
If you omit this property, all Auto Scaling groups are described.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 **Filters.member.N**
One or more filters to limit the results based on specific tags.
Type: Array of [Filter](API_Filter.md) objects
Required: No

 ** IncludeInstances **
 Specifies whether to include information about Amazon EC2 instances in the response. When set to `true` (default), the response includes instance details.
Type: Boolean
Required: No

 ** MaxRecords **
The maximum number of items to return with this call. The default value is `50` and the maximum value is `100`.
Type: Integer
Required: No

 ** NextToken **
The token for the next set of items to return. (You received this token from a previous call.)
Type: String
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

## Response Elements
<a name="API_DescribeAutoScalingGroups_ResponseElements"></a>

The following elements are returned by the service.

 **AutoScalingGroups.member.N**
The groups.
Type: Array of [AutoScalingGroup](API_AutoScalingGroup.md) objects

 ** NextToken **
A string that indicates that the response contains more items than can be returned in a single response. To receive additional items, specify this string for the `NextToken` value when requesting the next set of items. This value is null when there are no more items to return.
Type: String
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`

## Errors
<a name="API_DescribeAutoScalingGroups_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidNextToken **
The `NextToken` value is not valid.
 ** message **

HTTP Status Code: 400

 ** ResourceContention **
You already have a pending update to an Amazon EC2 Auto Scaling resource (for example, an Auto Scaling group, instance, or load balancer).
 ** message **

HTTP Status Code: 500

## Examples
<a name="API_DescribeAutoScalingGroups_Examples"></a>

### Example 1: Describe an Auto Scaling group
<a name="API_DescribeAutoScalingGroups_Example_1"></a>

This example describes the specified Auto Scaling group.

#### Sample Request
<a name="API_DescribeAutoScalingGroups_Example_1_Request"></a>

```
https://autoscaling.amazonaws.com/?Action=DescribeAutoScalingGroups
&AutoScalingGroupNames.member.1=my-asg
&Version=2011-01-01
&AUTHPARAMS
```

#### Sample Response
<a name="API_DescribeAutoScalingGroups_Example_1_Response"></a>

```
<DescribeAutoScalingGroupsResponse xmlns="https://autoscaling.amazonaws.com/doc/2011-01-01/">
  <DescribeAutoScalingGroupsResult>
    <AutoScalingGroups>
      <member>
        <AutoScalingGroupName>my-asg</AutoScalingGroupName>
        <AutoScalingGroupARN>arn:aws:autoscaling:us-east-1:123456789012:autoScalingGroup:12345678-1234-1234-1234-123456789012:autoScalingGroupName/my-asg</AutoScalingGroupARN>
        <LaunchConfigurationName>my-lc</LaunchConfigurationName>
        <LaunchTemplate />
        <MixedInstancesPolicy />
        <MinSize>2</MinSize>
        <MaxSize>10</MaxSize>
        <DesiredCapacity>2</DesiredCapacity>
        <DefaultCooldown>300</DefaultCooldown>
        <AvailabilityZones>
          <member>us-east-1a</member>
          <member>us-east-1b</member>
        </AvailabilityZones>
        <LoadBalancerNames />
        <TargetGroupARNs />
        <HealthCheckType>ELB</HealthCheckType>
        <HealthCheckGracePeriod>300</HealthCheckGracePeriod>
        <Instances>
          <member>
            <ProtectedFromScaleIn>false</ProtectedFromScaleIn>
            <AvailabilityZone>us-east-1c</AvailabilityZone>
            <LaunchConfigurationName>my-lc</LaunchConfigurationName>
            <LaunchTemplate />
            <InstanceId>i-1234567890abcdef0</InstanceId>
            <InstanceType>t3.micro</InstanceType>
            <HealthStatus>Healthy</HealthStatus>
            <LifecycleState>InService</LifecycleState>
            <WeightedCapacity />
          </member>
        </Instances>
        <CreatedTime>2023-05-06T17:47:15.107Z</CreatedTime>
        <SuspendedProcesses />
        <PlacementGroup />
        <VPCZoneIdentifier>subnet-057fa0918fEXAMPLE,subnet-610acd08EXAMPLE</VPCZoneIdentifier>
        <EnabledMetrics />
        <Status />
        <Tags>
          <member>
            <ResourceId>my-asg</ResourceId>
            <PropagateAtLaunch>true</PropagateAtLaunch>
            <Value>test</Value>
            <Key>environment</Key>
            <ResourceType>auto-scaling-group</ResourceType>
          </member>
        </Tags>
        <TerminationPolicies>
          <member>Default</member>
        </TerminationPolicies>
        <NewInstancesProtectedFromScaleIn>false</NewInstancesProtectedFromScaleIn>
        <ServiceLinkedRoleARN>arn:aws:iam::123456789012:role/aws-service-role/autoscaling.amazonaws.com/AWSServiceRoleForAutoScaling</ServiceLinkedRoleARN>
        <MaxInstanceLifetime />
        <CapacityRebalance />
        <WarmPoolConfiguration />
        <WarmPoolSize />
        <DesiredCapacityType />
        <DefaultInstanceWarmup />
        <TrafficSources />
      </member>
    </AutoScalingGroups>
  </DescribeAutoScalingGroupsResult>
  <ResponseMetadata>
    <RequestId>7c6e177f-f082-11e1-ac58-3714bEXAMPLE</RequestId>
  </ResponseMetadata>
</DescribeAutoScalingGroupsResponse>
```

### Example 2: Describe Auto Scaling groups with a specific tag key and value pair
<a name="API_DescribeAutoScalingGroups_Example_2"></a>

This example describes any Auto Scaling groups with the tag key and value pair of `environment=production`.

#### Sample Request
<a name="API_DescribeAutoScalingGroups_Example_2_Request"></a>

```
https://autoscaling.amazonaws.com/?Action=DescribeAutoScalingGroups
&Filters.member.1.Name=tag-key
&Filters.member.1.Values.member.1=environment
&Filters.member.2.Name=tag-value
&Filters.member.2.Values.member.1=production
&Version=2011-01-01
&AUTHPARAMS
```

### Example 3: Describe Auto Scaling groups with tags that match multiple tag keys and values
<a name="API_DescribeAutoScalingGroups_Example_3"></a>

This example combines filters to do more complex filtering. It describes any Auto Scaling groups with a specific set of tags. One tag key is `environment` and the tag value is `production` or `development`, and the other tag key is `costcenter` and the tag value is `cc123`.

#### Sample Request
<a name="API_DescribeAutoScalingGroups_Example_3_Request"></a>

```
https://autoscaling.amazonaws.com/?Action=DescribeAutoScalingGroups
&Filter.member.1.Name=tag:environment
&Filter.member.1.Values.member.1=production
&Filter.member.1.Values.member.2=development
&Filter.member.2.Name=tag:costcenter
&Filter.member.2.Values.member.1=cc123
&Version=2011-01-01
&AUTHPARAMS
```

## See Also
<a name="API_DescribeAutoScalingGroups_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/autoscaling-2011-01-01/DescribeAutoScalingGroups)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/autoscaling-2011-01-01/DescribeAutoScalingGroups)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/autoscaling-2011-01-01/DescribeAutoScalingGroups)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/autoscaling-2011-01-01/DescribeAutoScalingGroups)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/autoscaling-2011-01-01/DescribeAutoScalingGroups)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/autoscaling-2011-01-01/DescribeAutoScalingGroups)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/autoscaling-2011-01-01/DescribeAutoScalingGroups)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/autoscaling-2011-01-01/DescribeAutoScalingGroups)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/autoscaling-2011-01-01/DescribeAutoScalingGroups)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/autoscaling-2011-01-01/DescribeAutoScalingGroups)
