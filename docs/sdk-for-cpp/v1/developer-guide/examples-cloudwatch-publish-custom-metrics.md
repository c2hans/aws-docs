---
source_url: https://docs.aws.amazon.com/sdk-for-cpp/v1/developer-guide/examples-cloudwatch-publish-custom-metrics.html
---

# Publishing Custom Metric Data
<a name="examples-cloudwatch-publish-custom-metrics"></a>

A number of AWS services publish [their own metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/aws-namespaces.html) in namespaces beginning with `AWS/` You can also publish custom metric data using your own namespace (as long as it doesn’t begin with `AWS/`).

## Prerequisites
<a name="codeExamplePrereq"></a>

Before you begin, we recommend you read [Getting started using the AWS SDK for C\+\+](getting-started.md).

Download the example code and build the solution as described in [Getting started on code examples](getting-started-code-examples.md).

To run the examples, the user profile your code uses to make the requests must have proper permissions in AWS (for the service and the action). For more information, see [Providing AWS credentials](credentials.md).

## Publish Custom Metric Data
<a name="publish-custom-metric-data"></a>

To publish your own metric data, call the CloudWatchClient’s `PutMetricData` function with a [PutMetricDataRequest](https://docs.aws.amazon.com/sdk-for-cpp/latest/api/aws-cpp-sdk-monitoring/html/class_aws_1_1_cloud_watch_1_1_model_1_1_put_metric_data_request.html). The `PutMetricDataRequest` must include the custom namespace to use for the data, and information about the data point itself in a [MetricDatum](https://docs.aws.amazon.com/sdk-for-cpp/latest/api/aws-cpp-sdk-monitoring/html/class_aws_1_1_cloud_watch_1_1_model_1_1_metric_datum.html) object.

**Note**
You cannot specify a namespace that begins with `AWS/`. Namespaces that begin with `AWS/` are reserved for use by Amazon Web Services products.

 **Includes**

```
#include <aws/core/Aws.h>
#include <aws/monitoring/CloudWatchClient.h>
#include <aws/monitoring/model/PutMetricDataRequest.h>
#include <iostream>
```

 **Code**

```
        Aws::CloudWatch::CloudWatchClient cw;

        Aws::CloudWatch::Model::Dimension dimension;
        dimension.SetName("UNIQUE_PAGES");
        dimension.SetValue("URLS");

        Aws::CloudWatch::Model::MetricDatum datum;
        datum.SetMetricName("PAGES_VISITED");
        datum.SetUnit(Aws::CloudWatch::Model::StandardUnit::None);
        datum.SetValue(data_point);
        datum.AddDimensions(dimension);

        Aws::CloudWatch::Model::PutMetricDataRequest request;
        request.SetNamespace("SITE/TRAFFIC");
        request.AddMetricData(datum);

        auto outcome = cw.PutMetricData(request);
        if (!outcome.IsSuccess())
        {
            std::cout << "Failed to put sample metric data:" <<
                outcome.GetError().GetMessage() << std::endl;
        }
        else
        {
            std::cout << "Successfully put sample metric data" << std::endl;
        }
```

See the [complete example](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/cpp/example_code/cloudwatch/put_metric_data.cpp).

## More Information
<a name="more-information"></a>
+  [Using Amazon CloudWatch Metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/working_with_metrics.html) in the Amazon CloudWatch User Guide.
+  [AWS Namespaces](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/aws-namespaces.html) in the Amazon CloudWatch User Guide.
+  [PutMetricData](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/PutMetricData.html) in the Amazon CloudWatch API Reference.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for C++. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-cpp` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
