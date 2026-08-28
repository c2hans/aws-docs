---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DescribeMetricCollectionTypes.html
---

# DescribeMetricCollectionTypes
<a name="API_DescribeMetricCollectionTypes"></a>

Describes the available CloudWatch metrics for Amazon EC2 Auto Scaling.

## Response Elements
<a name="API_DescribeMetricCollectionTypes_ResponseElements"></a>

The following elements are returned by the service.

 **Granularities.member.N**
The granularities for the metrics.
Type: Array of [MetricGranularityType](API_MetricGranularityType.md) objects

 **Metrics.member.N**
The metrics.
Type: Array of [MetricCollectionType](API_MetricCollectionType.md) objects

## Errors
<a name="API_DescribeMetricCollectionTypes_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceContention **
You already have a pending update to an Amazon EC2 Auto Scaling resource (for example, an Auto Scaling group, instance, or load balancer).
 ** message **

HTTP Status Code: 500

## Examples
<a name="API_DescribeMetricCollectionTypes_Examples"></a>

### Example
<a name="API_DescribeMetricCollectionTypes_Example_1"></a>

This example illustrates one usage of DescribeMetricCollectionTypes.

#### Sample Request
<a name="API_DescribeMetricCollectionTypes_Example_1_Request"></a>

```
https://autoscaling.amazonaws.com/?Version=2011-01-01&Action=DescribeMetricCollectionTypes
&Version=2011-01-01
&AUTHPARAMS
```

#### Sample Response
<a name="API_DescribeMetricCollectionTypes_Example_1_Response"></a>

```
<DescribeMetricCollectionTypesResponse xmlns="https://autoscaling.amazonaws.com/doc/2011-01-01/">
  <DescribeMetricCollectionTypesResult>
    <Granularities>
      <member>
        <Granularity>1Minute</Granularity>
      </member>
    </Granularities>
    <Metrics>
      <member>
        <Metric>GroupMinSize</Metric>
      </member>
      <member>
        <Metric>GroupMaxSize</Metric>
      </member>
      <member>
        <Metric>GroupDesiredCapacity</Metric>
      </member>
      <member>
        <Metric>GroupInServiceInstances</Metric>
      </member>
      <member>
        <Metric>GroupPendingInstances</Metric>
      </member>
      <member>
        <Metric>GroupTerminatingInstances</Metric>
      </member>
      <member>
        <Metric>GroupStandbyInstances</Metric>
      </member>
      <member>
        <Metric>GroupTotalInstances</Metric>
      </member>
      <member>
        <Metric>GroupInServiceCapacity</Metric>
      </member>
      <member>
        <Metric>GroupPendingCapacity</Metric>
      </member>
      <member>
        <Metric>GroupStandbyCapacity</Metric>
      </member>
      <member>
        <Metric>GroupTerminatingCapacity</Metric>
      </member>
      <member>
        <Metric>GroupTotalCapacity</Metric>
      </member>
      <member>
        <Metric>WarmPoolDesiredCapacity</Metric>
      </member>
      <member>
        <Metric>WarmPoolWarmedCapacity</Metric>
      </member>
      <member>
        <Metric>WarmPoolPendingCapacity</Metric>
      </member>
      <member>
        <Metric>WarmPoolTerminatingCapacity</Metric>
      </member>
      <member>
        <Metric>WarmPoolTotalCapacity</Metric>
      </member>
      <member>
        <Metric>GroupAndWarmPoolDesiredCapacity</Metric>
      </member>
      <member>
        <Metric>GroupAndWarmPoolTotalCapacity</Metric>
      </member>
    </Metrics>
  </DescribeMetricCollectionTypesResult>
  <ResponseMetadata>
    <RequestId>7c6e177f-f082-11e1-ac58-3714bEXAMPLE</RequestId>
  </ResponseMetadata>
</DescribeMetricCollectionTypesResponse>
```

## See Also
<a name="API_DescribeMetricCollectionTypes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/autoscaling-2011-01-01/DescribeMetricCollectionTypes)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/autoscaling-2011-01-01/DescribeMetricCollectionTypes)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/autoscaling-2011-01-01/DescribeMetricCollectionTypes)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/autoscaling-2011-01-01/DescribeMetricCollectionTypes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/autoscaling-2011-01-01/DescribeMetricCollectionTypes)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/autoscaling-2011-01-01/DescribeMetricCollectionTypes)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/autoscaling-2011-01-01/DescribeMetricCollectionTypes)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/autoscaling-2011-01-01/DescribeMetricCollectionTypes)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/autoscaling-2011-01-01/DescribeMetricCollectionTypes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/autoscaling-2011-01-01/DescribeMetricCollectionTypes)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Auto Scaling. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query autoscaling` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
