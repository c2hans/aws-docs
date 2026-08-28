---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_GetMetricWidgetImage.html
---

# GetMetricWidgetImage
<a name="API_GetMetricWidgetImage"></a>

You can use the `GetMetricWidgetImage` API to retrieve a snapshot graph of one or more Amazon CloudWatch metrics as a bitmap image. You can then embed this image into your services and products, such as wiki pages, reports, and documents. You could also retrieve images regularly, such as every minute, and create your own custom live dashboard.

The graph you retrieve can include all CloudWatch metric graph features, including metric math and horizontal and vertical annotations.

There is a limit of 20 transactions per second for this API. Each `GetMetricWidgetImage` action has the following limits:
+ As many as 100 metrics in the graph.
+ Up to 100 KB uncompressed payload.

## Request Parameters
<a name="API_GetMetricWidgetImage_RequestParameters"></a>

 ** MetricWidget **
A JSON string that defines the bitmap graph to be retrieved. The string includes the metrics to include in the graph, statistics, annotations, title, axis limits, and so on. You can include only one `MetricWidget` parameter in each `GetMetricWidgetImage` call.
For more information about the syntax of `MetricWidget` see [GetMetricWidgetImage: Metric Widget Structure and Syntax](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Metric-Widget-Structure.html).
If any metric on the graph could not load all the requested data points, an orange triangle with an exclamation point appears next to the graph legend.
Type: String
Required: Yes

 ** OutputFormat **
The format of the resulting image. Only PNG images are supported.
The default is `png`. If you specify `png`, the API returns an HTTP response with the content-type set to `text/xml`. The image data is in a `MetricWidgetImage` field. For example:
 ` <GetMetricWidgetImageResponse xmlns=<URLstring>>`
 ` <GetMetricWidgetImageResult>`
 ` <MetricWidgetImage>`
 ` iVBORw0KGgoAAAANSUhEUgAAAlgAAAGQEAYAAAAip...`
 ` </MetricWidgetImage>`
 ` </GetMetricWidgetImageResult>`
 ` <ResponseMetadata>`
 ` <RequestId>6f0d4192-4d42-11e8-82c1-f539a07e0e3b</RequestId>`
 ` </ResponseMetadata>`
 `</GetMetricWidgetImageResponse>`
The `image/png` setting is intended only for custom HTTP requests. For most use cases, and all actions using an AWS SDK, you should use `png`. If you specify `image/png`, the HTTP response has a content-type set to `image/png`, and the body of the response is a PNG image.
Type: String
Required: No

## Response Elements
<a name="API_GetMetricWidgetImage_ResponseElements"></a>

The following element is returned by the service.

 ** MetricWidgetImage **
The image of the graph, in the output format specified. The output is base64-encoded.
Type: Base64-encoded binary data object

## Errors
<a name="API_GetMetricWidgetImage_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_GetMetricWidgetImage_Examples"></a>

### Example
<a name="API_GetMetricWidgetImage_Example_1"></a>

The following is an example of a `GetMetricWidgetImage` call. This example displays a graph showing an image of the `Average` statistic for the `CPUUtilization` metric for two Amazon EC2 instances, with both horizontal and vertical annotations.

```
{
   "OutputFormat":"png",
   "MetricWidget":"{\"width\":600,\"height\":395,\"metrics\":[[\"AWS/EC2\",\"CPUUtilization\",\"InstanceId\",\"i-1234567890abcdef0\",{\"stat\":\"Average\"}],[\"AWS/EC2\",\"CPUUtilization\",\"InstanceId\",\"i-0987654321abcdef0\",{\"stat\":\"Average\"}]],\"period\":300,\"start\":\"-P30D\",\"end\":\"PT0H\",\"stacked\":false,\"yAxis\":{\"left\":{\"min\":0.1,\"max\":1},\"right\":{\"min\":0}},\"title\":\"CPU for Two Instances\",\"annotations\":{\"horizontal\":[{\"color\":\"#ff6961\",\"label\":\"Trouble threshold start\",\"fill\":\"above\",\"value\":0.5}],\"vertical\":[{\"visible\":true,\"color\":\"#9467bd\",\"label\":\"Bug fix deployed\",\"value\":\"2018-08-28T15:25:26Z\",\"fill\":\"after\"}]}}"
}
```

## See Also
<a name="API_GetMetricWidgetImage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/monitoring-2010-08-01/GetMetricWidgetImage)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/monitoring-2010-08-01/GetMetricWidgetImage)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/monitoring-2010-08-01/GetMetricWidgetImage)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/monitoring-2010-08-01/GetMetricWidgetImage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/GetMetricWidgetImage)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/monitoring-2010-08-01/GetMetricWidgetImage)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/monitoring-2010-08-01/GetMetricWidgetImage)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/monitoring-2010-08-01/GetMetricWidgetImage)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/monitoring-2010-08-01/GetMetricWidgetImage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/GetMetricWidgetImage)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
