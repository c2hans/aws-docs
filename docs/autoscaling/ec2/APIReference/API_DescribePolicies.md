---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DescribePolicies.html
---

# DescribePolicies
<a name="API_DescribePolicies"></a>

Gets information about the scaling policies in the account and Region.

## Request Parameters
<a name="API_DescribePolicies_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** AutoScalingGroupName **
The name of the Auto Scaling group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 ** MaxRecords **
The maximum number of items to be returned with each call. The default value is `50` and the maximum value is `100`.
Type: Integer
Required: No

 ** NextToken **
The token for the next set of items to return. (You received this token from a previous call.)
Type: String
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 **PolicyNames.member.N**
The names of one or more policies. If you omit this property, all policies are described. If a group name is provided, the results are limited to that group. If you specify an unknown policy name, it is ignored with no error.
Array Members: Maximum number of 50 items.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 **PolicyTypes.member.N**
One or more policy types. The valid values are `SimpleScaling`, `StepScaling`, `TargetTrackingScaling`, and `PredictiveScaling`.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

## Response Elements
<a name="API_DescribePolicies_ResponseElements"></a>

The following elements are returned by the service.

 ** NextToken **
A string that indicates that the response contains more items than can be returned in a single response. To receive additional items, specify this string for the `NextToken` value when requesting the next set of items. This value is null when there are no more items to return.
Type: String
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`

 **ScalingPolicies.member.N**
The scaling policies.
Type: Array of [ScalingPolicy](API_ScalingPolicy.md) objects

## Errors
<a name="API_DescribePolicies_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidNextToken **
The `NextToken` value is not valid.
 ** message **

HTTP Status Code: 400

 ** ResourceContention **
You already have a pending update to an Amazon EC2 Auto Scaling resource (for example, an Auto Scaling group, instance, or load balancer).
 ** message **

HTTP Status Code: 500

 ** ServiceLinkedRoleFailure **
The service-linked role is not yet ready for use.
HTTP Status Code: 500

## Examples
<a name="API_DescribePolicies_Examples"></a>

### Example
<a name="API_DescribePolicies_Example_1"></a>

This example illustrates one usage of DescribePolicies.

#### Sample Request
<a name="API_DescribePolicies_Example_1_Request"></a>

```
https://autoscaling.amazonaws.com/?Action=DescribePolicies
&AutoScalingGroupName=my-asg
&Version=2011-01-01
&AUTHPARAMS
```

#### Sample Response
<a name="API_DescribePolicies_Example_1_Response"></a>

```
<DescribePoliciesResponse xmlns="https://autoscaling.amazonaws.com/doc/2011-01-01/">
  <DescribePoliciesResult>
    <ScalingPolicies>
      <member>
        <PolicyARN>arn:aws:autoscaling:us-east-1:123456789012:scalingPolicy:c322761b-3172-4d56-9a21-0ed9dEXAMPLE:autoScalingGroupName/my-asg:policyName/MyScaleInPolicy</PolicyARN>
        <AdjustmentType>ChangeInCapacity</AdjustmentType>
        <ScalingAdjustment>-1</ScalingAdjustment>
        <PolicyName>MyScaleInPolicy</PolicyName>
        <PolicyType>SimpleScaling</PolicyType>
        <AutoScalingGroupName>my-asg</AutoScalingGroupName>
        <Cooldown>60</Cooldown>
        <Alarms>
          <member>
            <AlarmName>TestQueue</AlarmName>
            <AlarmARN>arn:aws:cloudwatch:us-east-1:123456789012:alarm:TestQueue</AlarmARN>
          </member>
        </Alarms>
      </member>
      <member>
        <PolicyARN>arn:aws:autoscaling:us-east-1:123456789012:scalingPolicy:c55a5cdd-9be0-435b-b60b-a8dd3EXAMPLE:autoScalingGroupName/my-asg:policyName/MyScaleOutPolicy</PolicyARN>
        <AdjustmentType>ChangeInCapacity</AdjustmentType>
        <ScalingAdjustment>1</ScalingAdjustment>
        <PolicyName>MyScaleOutPolicy</PolicyName>
        <PolicyType>SimpleScaling</PolicyType>
        <AutoScalingGroupName>my-asg</AutoScalingGroupName>
        <Cooldown>60</Cooldown>
        <Alarms>
          <member>
            <AlarmName>TestQueue</AlarmName>
            <AlarmARN>arn:aws:cloudwatch:us-east-1:123456789012:alarm:TestQueue</AlarmARN>
          </member>
        </Alarms>
      </member>
    </ScalingPolicies>
  </DescribePoliciesResult>
  <ResponseMetadata>
    <RequestId>7c6e177f-f082-11e1-ac58-3714bEXAMPLE</RequestId>
  </ResponseMetadata>
</DescribePoliciesResponse>
```

## See Also
<a name="API_DescribePolicies_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/autoscaling-2011-01-01/DescribePolicies)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/autoscaling-2011-01-01/DescribePolicies)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/autoscaling-2011-01-01/DescribePolicies)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/autoscaling-2011-01-01/DescribePolicies)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/autoscaling-2011-01-01/DescribePolicies)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/autoscaling-2011-01-01/DescribePolicies)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/autoscaling-2011-01-01/DescribePolicies)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/autoscaling-2011-01-01/DescribePolicies)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/autoscaling-2011-01-01/DescribePolicies)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/autoscaling-2011-01-01/DescribePolicies)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Auto Scaling. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query autoscaling` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
