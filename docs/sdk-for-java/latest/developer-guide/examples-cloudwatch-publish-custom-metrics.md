---
source_url: https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/examples-cloudwatch-publish-custom-metrics.html
---

# Publish custom metric data to CloudWatch
<a name="examples-cloudwatch-publish-custom-metrics"></a>

A number of AWS services publish [their own metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/aws-services-cloudwatch-metrics.html) in namespaces beginning with " `AWS` " You can also publish custom metric data using your own namespace (as long as it doesn’t begin with " `AWS` ").

## Publish custom metric data
<a name="cwid1"></a>

To publish your own metric data, call the CloudWatchClient’s `putMetricData` method with a [PutMetricDataRequest](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/cloudwatch/model/PutMetricDataRequest.html). The `PutMetricDataRequest` must include the custom namespace to use for the data, and information about the data point itself in a [MetricDatum](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/cloudwatch/model/MetricDatum.html) object.

**Note**
You cannot specify a namespace that begins with " `AWS` ". Namespaces that begin with " `AWS` " are reserved for use by Amazon Web Services products.

 **Imports**

```
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.cloudwatch.CloudWatchClient;
import software.amazon.awssdk.services.cloudwatch.model.Dimension;
import software.amazon.awssdk.services.cloudwatch.model.MetricDatum;
import software.amazon.awssdk.services.cloudwatch.model.StandardUnit;
import software.amazon.awssdk.services.cloudwatch.model.PutMetricDataRequest;
import software.amazon.awssdk.services.cloudwatch.model.CloudWatchException;
import java.time.Instant;
import java.time.ZoneOffset;
import java.time.ZonedDateTime;
import java.time.format.DateTimeFormatter;
```

 **Code**

```
    public static void putMetData(CloudWatchClient cw, Double dataPoint ) {

        try {
            Dimension dimension = Dimension.builder()
                    .name("UNIQUE_PAGES")
                    .value("URLS")
                    .build();

            // Set an Instant object
            String time = ZonedDateTime.now( ZoneOffset.UTC ).format( DateTimeFormatter.ISO_INSTANT );
            Instant instant = Instant.parse(time);

            MetricDatum datum = MetricDatum.builder()
                .metricName("PAGES_VISITED")
                .unit(StandardUnit.NONE)
                .value(dataPoint)
                .timestamp(instant)
                .dimensions(dimension).build();

            PutMetricDataRequest request = PutMetricDataRequest.builder()
                .namespace("SITE/TRAFFIC")
                .metricData(datum).build();

            cw.putMetricData(request);

        } catch (CloudWatchException e) {
            System.err.println(e.awsErrorDetails().errorMessage());
            System.exit(1);
        }
        System.out.printf("Successfully put data point %f", dataPoint);
     }
```

See the [complete example](https://github.com/awsdocs/aws-doc-sdk-examples/blob/f4eaf2b2971805cfb2b87a8e5ab408f83169432e/javav2/example_code/cloudwatch/src/main/java/com/example/cloudwatch/PutMetricData.java) on GitHub.

## More information
<a name="more-information"></a>
+  [Use Amazon CloudWatch Metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/working_with_metrics.html) in the Amazon CloudWatch User Guide.
+  [AWS Namespaces](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/aws-services-cloudwatch-metrics.html) in the Amazon CloudWatch User Guide.
+  [PutMetricData](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_PutMetricData.html) in the Amazon CloudWatch API Reference.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for Java. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-java` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
