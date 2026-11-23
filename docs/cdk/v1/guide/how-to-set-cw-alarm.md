---
source_url: https://docs.aws.amazon.com/cdk/v1/guide/how-to-set-cw-alarm.html
---

This is the AWS CDK v1 Developer Guide. The older CDK v1 entered maintenance on June 1, 2022 and will now only receive critical bug fixes and security patches. New features will be developed for CDK v2 exclusively. Support for CDK v1 will end entirely on June 1, 2023. [Migrate to CDK v2](work-with-cdk-v2.md) to have access to the latest features and fixes.

# Set a CloudWatch alarm

The [aws-cloudwatch](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cloudwatch-readme.html) package supports setting CloudWatch alarms on CloudWatch metrics. So the first thing you need is a metric. You can use a predefined metric or you can create your own.

## Using an existing metric
<a name="how-to-set-cw-alarm-use-metric"></a>

Many AWS Construct Library modules let you set an alarm on an existing metric by passing the metric's name to a convenience method on an instance of an object that has metrics. For example, given an Amazon SQS queue, you can get the metric **ApproximateNumberOfMessagesVisible** from the queue's [metric()](https://docs.aws.amazon.com/cdk/api/v2/docs/@aws-cdk_aws-sqs.Queue.html#metricmetricname-props) method.

------
#### [ TypeScript ]

```javascript
const metric = queue.metric("ApproximateNumberOfMessagesVisible");
```

------
#### [ JavaScript ]

```javascript
const metric = queue.metric("ApproximateNumberOfMessagesVisible");
```

------
#### [ Python ]

```python
metric = queue.metric("ApproximateNumberOfMessagesVisible")
```

------
#### [ Java ]

```java
Metric metric = queue.metric("ApproximateNumberOfMessagesVisible");
```

------
#### [ C\# ]

```csharp
var metric = queue.Metric("ApproximateNumberOfMessagesVisible");
```

------

## Creating your own metric
<a name="how-to-set-cw-alarm-new-metric"></a>

Create your own [metric](https://docs.aws.amazon.com/cdk/api/v2/docs/@aws-cdk_aws-cloudwatch.Metric.html) as follows, where the *namespace* value should be something like **AWS/SQS** for an Amazon SQS queue. You also need to specify your metric's name and dimension.

------
#### [ TypeScript ]

```javascript
const metric = new cloudwatch.Metric({
  namespace: 'MyNamespace',
  metricName: 'MyMetric',
  dimensions: { MyDimension: 'MyDimensionValue' }
});
```

------
#### [ JavaScript ]

```javascript
const metric = new cloudwatch.Metric({
  namespace: 'MyNamespace',
  metricName: 'MyMetric',
  dimensions: { MyDimension: 'MyDimensionValue' }
});
```

------
#### [ Python ]

```python
metric = cloudwatch.Metric(
    namespace="MyNamespace",
    metric_name="MyMetric",
    dimensions=dict(MyDimension="MyDimensionValue")
)
```

------
#### [ Java ]

```java
Metric metric = Metric.Builder.create()
        .namespace("MyNamespace")
        .metricName("MyMetric")
        .dimensionsMap(java.util.Map.of(    // Java 9 or later
            "MyDimension", "MyDimensionValue"))
        .build();
```

------
#### [ C\# ]

```csharp
var metric = new Metric(this, "Metric", new MetricProps
{
    Namespace = "MyNamespace",
    MetricName = "MyMetric",
    Dimensions = new Dictionary<string, object>
    {
        { "MyDimension", "MyDimensionValue" }
    }
});
```

------

## Creating the alarm
<a name="how-to-set-cw-alarm-create"></a>

Once you have a metric, either an existing one or one you defined, you can create an alarm. In this example, the alarm is raised when there are more than 100 of your metric in two of the last three evaluation periods. You can use comparisons such as less-than in your alarms via the `comparisonOperator` property; greater-than-or-equal-to is the AWS CDK default, so we don't need to specify it.

------
#### [ TypeScript ]

```javascript
const alarm = new cloudwatch.Alarm(this, 'Alarm', {
  metric: metric,
  threshold: 100,
  evaluationPeriods: 3,
  datapointsToAlarm: 2,
});
```

------
#### [ JavaScript ]

```javascript
const alarm = new cloudwatch.Alarm(this, 'Alarm', {
  metric: metric,
  threshold: 100,
  evaluationPeriods: 3,
  datapointsToAlarm: 2
});
```

------
#### [ Python ]

```python
alarm = cloudwatch.Alarm(self, "Alarm",
    metric=metric,
    threshold=100,
    evaluation_periods=3,
    datapoints_to_alarm=2
)
```

------
#### [ Java ]

```java
import software.amazon.awscdk.services.cloudwatch.Alarm;
import software.amazon.awscdk.services.cloudwatch.Metric;

Alarm alarm = Alarm.Builder.create(this, "Alarm")
        .metric(metric)
        .threshold(100)
        .evaluationPeriods(3)
        .datapointsToAlarm(2).build();
```

------
#### [ C\# ]

```csharp
var alarm = new Alarm(this, "Alarm", new AlarmProps
{
    Metric = metric,
    Threshold = 100,
    EvaluationPeriods = 3,
    DatapointsToAlarm = 2
});
```

------

An alternative way to create an alarm is using the metric's [createAlarm()](https://docs.aws.amazon.com/cdk/api/v2/docs/@aws-cdk_aws-cloudwatch.Metric.html#create-wbr-alarmscope-id-props) method, which takes essentially the same properties as the `Alarm` constructor; you just don't need to pass in the metric, since it's already known.

------
#### [ TypeScript ]

```javascript
metric.createAlarm(this, 'Alarm', {
  threshold: 100,
  evaluationPeriods: 3,
  datapointsToAlarm: 2,
});
```

------
#### [ JavaScript ]

```javascript
metric.createAlarm(this, 'Alarm', {
  threshold: 100,
  evaluationPeriods: 3,
  datapointsToAlarm: 2,
});
```

------
#### [ Python ]

```python
metric.create_alarm(self, "Alarm",
    threshold=100,
    evaluation_periods=3,
    datapoints_to_alarm=2
)
```

------
#### [ Java ]

```java
metric.createAlarm(this, "Alarm", new CreateAlarmOptions.Builder()
        .threshold(100)
        .evaluationPeriods(3)
        .datapointsToAlarm(2)
        .build());
```

------
#### [ C\# ]

```csharp
metric.CreateAlarm(this, "Alarm", new CreateAlarmOptions
{
    Threshold = 100,
    EvaluationPeriods = 3,
    DatapointsToAlarm = 2
});
```

------
