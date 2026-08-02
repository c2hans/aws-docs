---
source_url: https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/examples-cloudwatch-create-alarms.html
---

# Work with CloudWatch alarms
<a name="examples-cloudwatch-create-alarms"></a>

## Create an alarm
<a name="create-an-alarm"></a>

To create an alarm based on a CloudWatch metric, call the CloudWatchClient’s `putMetricAlarm` method with a [PutMetricAlarmRequest](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/cloudwatch/model/PutMetricAlarmRequest.html) filled with the alarm conditions.

 **Imports**

```
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.cloudwatch.CloudWatchClient;
import software.amazon.awssdk.services.cloudwatch.model.Dimension;
import software.amazon.awssdk.services.cloudwatch.model.PutMetricAlarmRequest;
import software.amazon.awssdk.services.cloudwatch.model.ComparisonOperator;
import software.amazon.awssdk.services.cloudwatch.model.Statistic;
import software.amazon.awssdk.services.cloudwatch.model.StandardUnit;
import software.amazon.awssdk.services.cloudwatch.model.CloudWatchException;
```

 **Code**

```
    public static void putMetricAlarm(CloudWatchClient cw, String alarmName, String instanceId) {

        try {
            Dimension dimension = Dimension.builder()
                .name("InstanceId")
                .value(instanceId).build();

            PutMetricAlarmRequest request = PutMetricAlarmRequest.builder()
                .alarmName(alarmName)
                .comparisonOperator(
                        ComparisonOperator.GREATER_THAN_THRESHOLD)
                .evaluationPeriods(1)
                .metricName("CPUUtilization")
                .namespace("AWS/EC2")
                .period(60)
                .statistic(Statistic.AVERAGE)
                .threshold(70.0)
                .actionsEnabled(false)
                .alarmDescription(
                        "Alarm when server CPU utilization exceeds 70%")
                .unit(StandardUnit.SECONDS)
                .dimensions(dimension)
                .build();

            cw.putMetricAlarm(request);
            System.out.printf(
                    "Successfully created alarm with name %s", alarmName);

        } catch (CloudWatchException e) {
            System.err.println(e.awsErrorDetails().errorMessage());
            System.exit(1);
        }
    }
```

See the [complete example](https://github.com/awsdocs/aws-doc-sdk-examples/blob/f4eaf2b2971805cfb2b87a8e5ab408f83169432e/javav2/example_code/cloudwatch/src/main/java/com/example/cloudwatch/PutMetricAlarm.java) on GitHub.

## List alarms
<a name="list-alarms"></a>

To list the CloudWatch alarms that you have created, call the CloudWatchClient’s `describeAlarms` method with a [DescribeAlarmsRequest](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/cloudwatch/model/DescribeAlarmsRequest.html) that you can use to set options for the result.

 **Imports**

```
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.cloudwatch.CloudWatchClient;
import software.amazon.awssdk.services.cloudwatch.model.CloudWatchException;
import software.amazon.awssdk.services.cloudwatch.model.DescribeAlarmsRequest;
import software.amazon.awssdk.services.cloudwatch.model.DescribeAlarmsResponse;
import software.amazon.awssdk.services.cloudwatch.model.MetricAlarm;
```

 **Code**

```
    public static void desCWAlarms( CloudWatchClient cw) {

        try {

            boolean done = false;
            String newToken = null;

            while(!done) {
                DescribeAlarmsResponse response;

                if (newToken == null) {
                    DescribeAlarmsRequest request = DescribeAlarmsRequest.builder().build();
                    response = cw.describeAlarms(request);
                } else {
                    DescribeAlarmsRequest request = DescribeAlarmsRequest.builder()
                        .nextToken(newToken)
                        .build();
                    response = cw.describeAlarms(request);
                }

                for(MetricAlarm alarm : response.metricAlarms()) {
                    System.out.printf("\n Retrieved alarm %s", alarm.alarmName());
                }

                if(response.nextToken() == null) {
                    done = true;
                } else {
                    newToken = response.nextToken();
                }
            }

        } catch (CloudWatchException e) {
            System.err.println(e.awsErrorDetails().errorMessage());
            System.exit(1);
        }
        System.out.printf("Done");
    }
```

The list of alarms can be obtained by calling `MetricAlarms` on the [DescribeAlarmsResponse](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/cloudwatch/model/DescribeAlarmsResponse.html) that is returned by `describeAlarms`.

The results may be *paged*. To retrieve the next batch of results, call `nextToken` on the response object and use the token value to build a new request object. Then call the `describeAlarms` method again with the new request.

**Note**
You can also retrieve alarms for a specific metric by using the CloudWatchClient’s `describeAlarmsForMetric` method. Its use is similar to `describeAlarms`.

See the [complete example](https://github.com/awsdocs/aws-doc-sdk-examples/blob/f4eaf2b2971805cfb2b87a8e5ab408f83169432e/javav2/example_code/cloudwatch/src/main/java/com/example/cloudwatch/DescribeAlarms.java) on GitHub.

## Delete alarms
<a name="delete-alarms"></a>

To delete CloudWatch alarms, call the CloudWatchClient’s `deleteAlarms` method with a [DeleteAlarmsRequest](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/cloudwatch/model/DeleteAlarmsRequest.html) containing one or more names of alarms that you want to delete.

 **Imports**

```
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.cloudwatch.CloudWatchClient;
import software.amazon.awssdk.services.cloudwatch.model.CloudWatchException;
import software.amazon.awssdk.services.cloudwatch.model.DeleteAlarmsRequest;
```

 **Code**

```
    public static void deleteCWAlarm(CloudWatchClient cw, String alarmName) {

        try {
            DeleteAlarmsRequest request = DeleteAlarmsRequest.builder()
                    .alarmNames(alarmName)
                    .build();

            cw.deleteAlarms(request);
            System.out.printf("Successfully deleted alarm %s", alarmName);

        } catch (CloudWatchException e) {
            System.err.println(e.awsErrorDetails().errorMessage());
            System.exit(1);
        }
    }
```

See the [complete example](https://github.com/awsdocs/aws-doc-sdk-examples/blob/f4eaf2b2971805cfb2b87a8e5ab408f83169432e/javav2/example_code/cloudwatch/src/main/java/com/example/cloudwatch/DeleteAlarm.java) on GitHub.

## More information
<a name="more-information"></a>
+  [Using Amazon CloudWatch alarms](https://docs.aws.amazon.com//AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html) in the Amazon CloudWatch User Guide
+  [PutMetricAlarm](https://docs.aws.amazon.com//AmazonCloudWatch/latest/APIReference/API_PutMetricAlarm.html) in the Amazon CloudWatch API Reference
+  [DescribeAlarms](https://docs.aws.amazon.com//AmazonCloudWatch/latest/APIReference/API_DescribeAlarms.html) in the Amazon CloudWatch API Reference
+  [DeleteAlarms](https://docs.aws.amazon.com//AmazonCloudWatch/latest/APIReference/API_DeleteAlarms.html) in the Amazon CloudWatch API Reference
