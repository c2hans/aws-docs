---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_MetricDataResult.html
---

# MetricDataResult
<a name="API_MetricDataResult"></a>

 Contains a single data point from a capacity metrics query, including the dimension values, timestamp, and metric values for that specific combination.

## Contents
<a name="API_MetricDataResult_Contents"></a>

 ** dimension **
 The dimension values that identify this specific data point, such as account ID, region, and instance family.
Type: [CapacityManagerDimension](API_CapacityManagerDimension.md) object
Required: No

 ** MetricValueSet.N **
 The metric values and statistics for this data point, containing the actual capacity usage numbers.
Type: Array of [MetricValue](API_MetricValue.md) objects
Required: No

 ** timestamp **
 The timestamp for this data point, indicating when the capacity usage occurred.
Type: Timestamp
Required: No

## See Also
<a name="API_MetricDataResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/MetricDataResult)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/MetricDataResult)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/MetricDataResult)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
