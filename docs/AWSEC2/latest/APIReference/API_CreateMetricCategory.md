---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateMetricCategory.html
---

# CreateMetricCategory
<a name="API_CreateMetricCategory"></a>

Creates a metric category. A metric category is a set of additional metrics that you can associate with an instance that has detailed monitoring enabled.

For more information, see [Use metric categories for additional metrics](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/manage-detailed-monitoring.html#detailed-monitoring-metric-categories) in the *Amazon EC2 User Guide*.

## Request Parameters
<a name="API_CreateMetricCategory_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **ClientToken**
Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see [Ensure Idempotency](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html).
Type: String
Required: No

 **DryRun**
Checks whether you have the required permissions for the operation, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **Metric.N**
The names of the metrics to include in the metric category.
Specify each metric by its Amazon CloudWatch metric name or its OpenTelemetry metric name. The two names for a measurement are separate entries, and you can include both.
In Regions where Amazon CloudWatch OpenTelemetry metrics aren't available, you can't specify OpenTelemetry metric names.
Type: Array of strings
Required: Yes

 **TagSpecification.N**
The tags to apply to the metric category during creation.
Type: Array of [TagSpecification](API_TagSpecification.md) objects
Required: No

## Response Elements
<a name="API_CreateMetricCategory_ResponseElements"></a>

The following elements are returned by the service.

 **metricCategory**
Information about the metric category.
Type: [MetricCategory](API_MetricCategory.md) object

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_CreateMetricCategory_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_CreateMetricCategory_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/CreateMetricCategory)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/CreateMetricCategory)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/CreateMetricCategory)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/CreateMetricCategory)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/CreateMetricCategory)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/CreateMetricCategory)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/CreateMetricCategory)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/CreateMetricCategory)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/CreateMetricCategory)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/CreateMetricCategory)
