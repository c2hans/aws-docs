---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DescribeTrafficSources.html
---

# DescribeTrafficSources
<a name="API_DescribeTrafficSources"></a>

Gets information about the traffic sources for the specified Auto Scaling group.

You can optionally provide a traffic source type. If you provide a traffic source type, then the results only include that traffic source type.

If you do not provide a traffic source type, then the results include all the traffic sources for the specified Auto Scaling group.

## Request Parameters
<a name="API_DescribeTrafficSources_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** AutoScalingGroupName **
The name of the Auto Scaling group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: Yes

 ** MaxRecords **
The maximum number of items to return with this call. The maximum value is `50`.
Type: Integer
Required: No

 ** NextToken **
The token for the next set of items to return. (You received this token from a previous call.)
Type: String
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 ** TrafficSourceType **
The traffic source type that you want to describe.
The following lists the valid values:
+  `elb` if the traffic source is a Classic Load Balancer.
+  `elbv2` if the traffic source is a Application Load Balancer, Gateway Load Balancer, or Network Load Balancer.
+  `vpc-lattice` if the traffic source is VPC Lattice.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

## Response Elements
<a name="API_DescribeTrafficSources_ResponseElements"></a>

The following elements are returned by the service.

 ** NextToken **
This string indicates that the response contains more items than can be returned in a single response. To receive additional items, specify this string for the `NextToken` value when requesting the next set of items. This value is null when there are no more items to return.
Type: String
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`

 **TrafficSources.member.N**
Information about the traffic sources.
Type: Array of [TrafficSourceState](API_TrafficSourceState.md) objects

## Errors
<a name="API_DescribeTrafficSources_Errors"></a>

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
<a name="API_DescribeTrafficSources_Examples"></a>

### Example
<a name="API_DescribeTrafficSources_Example_1"></a>

This example illustrates one usage of DescribeTrafficSources.

#### Sample Request
<a name="API_DescribeTrafficSources_Example_1_Request"></a>

```
https://autoscaling.amazonaws.com/?Action=DescribeTrafficSources
&AutoScalingGroupName=my-asg
&Version=2011-01-01
&AUTHPARAMS
```

#### Sample Response
<a name="API_DescribeTrafficSources_Example_1_Response"></a>

```
<DescribeTrafficSourcesResponse xmlns="https://autoscaling.amazonaws.com/doc/2011-01-01/">
  <DescribeTrafficSourcesResult>
    <TrafficSources>
      <Identifier>arn:aws:vpc-lattice:us-west-2:123456789012:targetgroup/tg-0e2f2665eEXAMPLE</Identifier>
      <State>InService</State>
      <Type>vpc-lattice</Type>
    </TrafficSources>
  </DescribeTrafficSourcesResult>
  <ResponseMetadata>
    <RequestId>9351b5ea-b4c0-4a88-b873-c51e4EXAMPLE</RequestId>
  </ResponseMetadata>
</DescribeTrafficSourcesResponse>
```

## See Also
<a name="API_DescribeTrafficSources_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/autoscaling-2011-01-01/DescribeTrafficSources)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/autoscaling-2011-01-01/DescribeTrafficSources)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/autoscaling-2011-01-01/DescribeTrafficSources)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/autoscaling-2011-01-01/DescribeTrafficSources)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/autoscaling-2011-01-01/DescribeTrafficSources)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/autoscaling-2011-01-01/DescribeTrafficSources)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/autoscaling-2011-01-01/DescribeTrafficSources)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/autoscaling-2011-01-01/DescribeTrafficSources)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/autoscaling-2011-01-01/DescribeTrafficSources)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/autoscaling-2011-01-01/DescribeTrafficSources)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Auto Scaling. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query autoscaling` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
