---
source_url: https://docs.aws.amazon.com/whitepapers/latest/advanced-multi-az-resilience-patterns/failure-detection-with-cloudwatch-composite-alarms.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Failure detection with CloudWatch composite alarms
<a name="failure-detection-with-cloudwatch-composite-alarms"></a>

 In CloudWatch metrics, each dimension set is a unique metric, and you can create a CloudWatch alarm on each one. You can then create [Amazon CloudWatch composite alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Create_Composite_Alarm.html) to aggregate these metrics.

 In order to accurately detect impact, the examples in this paper will use two different CloudWatch alarm structures for each dimension set they alarm on. Each alarm will use a **Period** of one-minute, meaning the metric is evaluated once per minute. The first approach is going to use three consecutive breaching data points by setting the **Evaluation Periods** and **Datapoints to Alarm** to three, meaning impact for three minutes total. The second approach is going to use an "M out of N" when any 3 data points in a five-minute window are breaching by setting the **Evaluation Periods** to five and **Datapoints to Alarm** to three. This provides an ability to detect a constant signal, as well as one that fluctuates over a short time. The time durations and number of data points contained here are a suggestion, use values that make sense for your workloads.

## Detect impact in a single Availability Zone
<a name="detect-impact-in-a-single-availability-zone"></a>

 Using this construct, consider a workload that uses `Controller`, `Action`, `InstanceId`, `AZ-ID`, and `Region` as dimensions. The workload has two controllers, Products and Home, and one action per controller, List and Index respectively. It operates in three Availability Zones in the `us-east-1` Region. You would create two alarms for availability for each `Controller` and `Action` combination in each Availability Zone as well as two alarms for latency for each. Then, you can optionally choose to create a composite alarm for availability for each `Controller` and `Action` combination. Finally, you create a composite alarm that aggregates all of the availability alarms for the Availability Zone. This is shown in the following figure for a single Availability Zone, `use1-az1`, using the optional composite alarm for each `Controller` and `Action` combination (similar alarms would exist for the `use1-az2` and `use1-az3` Availability Zones as well, but are not shown for simplicity).

![Diagram showing a composite alarm structure for availability in use1-az1](https://docs.aws.amazon.com/whitepapers/latest/advanced-multi-az-resilience-patterns/images/composite-alarm-structure-availability.png)

 You would also build a similar alarm structure for latency as well, shown in the next figure.

![A diagram showing a Composite alarm structure for latency in use1-az1](https://docs.aws.amazon.com/whitepapers/latest/advanced-multi-az-resilience-patterns/images/composite-alarm-structure-latency.png)

For the remainder of the figures in this section, only the `az1-availability` and `az1-latency` composite alarms will be shown at the top level. These composite alarms, `az1-availability` and `az1-latency`, will tell you if either availability drops below or latency rises above defined thresholds in a particular Availability Zone for any part of your workload. You might also want to consider measuring throughput to detect impact that prevents your workload in a single Availability Zone from receiving work. You can integrate alarms produced from the metrics emitted by your canaries into these composite alarms as well. That way, if either the server-side or client-side see impacts in availability or latency, the alarm will create an alert.

## Ensure the impact isn’t Regional
<a name="ensure-the-impact-isnt-regional"></a>

Another set of composite alarms can be used to ensure that only an isolated Availability Zone event causes the alarm to be activated. This is performed by ensuring that an Availability Zone composite alarm is in the `ALARM` state while the composite alarms for the other Availability Zones are in the `OK` state. This will result in one composite alarm per Availability Zone that you use. An example is shown in the following figure (remember that there are alarms for latency and availability in `use1-az2` and `use1-az3`, `az2-latency`, `az2-availability`, `az3-latency`, and `az3-availability`, that are not pictured for simplicity).

![A diagram showing a composite alarm structure to detect impact isolated to a single AZ](https://docs.aws.amazon.com/whitepapers/latest/advanced-multi-az-resilience-patterns/images/composite-alarm-structure-impact.png)

## Ensure the impact isn’t caused by a single instance
<a name="ensure-the-impact-isnt-caused-by-a-single-instance"></a>

A single instance (or a small percentage of your overall fleet) can cause disproportionate impact to availability and latency metrics that could make the whole Availability Zone appear to be affected, when in fact it is not. It is faster and just as effective to remove a single problematic instance than evacuate an Availability Zone.

Instances and containers are typically treated as ephemeral resources, frequently replaced with services such as [AWS Auto Scaling](https://aws.amazon.com/autoscaling/). It’s difficult to create a new CloudWatch alarm every time a new instance is created (but certainly possible using [Amazon EventBridge](https://docs.aws.amazon.com/autoscaling/ec2/userguide/cloud-watch-events.html) or [Amazon EC2 Auto Scaling lifecycle hooks](https://docs.aws.amazon.com/autoscaling/ec2/userguide/lifecycle-hooks.html)). Instead, you can use [CloudWatch Contributor Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ContributorInsights.html) to identify the quantity of contributors to availability and latency metrics.

As an example, for an HTTP web application, you can create a rule to identify top contributors for 5xx HTTP responses in each Availability Zone. This will identify which instances are contributing to a drop in availability (our availability metric defined above is driven by the presence of 5xx errors). Using the EMF log example, create a rule using a key of `InstanceId`. Then, filter the log by the `HttpResponseCode` field. This example is a rule for the `use1-az1` Availability Zone.

```
{
    "AggregateOn": "Count",
    "Contribution": {
        "Filters": [
            {
                "Match": "$.InstanceId",
                "IsPresent": true
            },
            {
                "Match": "$.HttpStatusCode",
                "IsPresent": true
            },
            {
                "Match": "$.HttpStatusCode",
                "GreaterThan": 499
            },
            {
                "Match": "$.HttpStatusCode",
                "LessThan": 600
            },
            {
                "Match": "$.AZ-ID",
                "In": ["use1-az1"]
            },
        ],
        "Keys": [
            "$.InstanceId"
        ]
    },
    "LogFormat": "JSON",
    "LogGroupNames": [
        "/loggroupname"
    ],
    "Schema": {
        "Name": "CloudWatchLogRule",
        "Version": 1
    }
}
```

CloudWatch alarms can be created based on these rules as well. You can create alarms based on Contributor Insights rules using [metric math](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/using-metric-math.html) and the `INSIGHT_RULE_METRIC` function with the `UniqueContributors` metric. You can also create additional Contributor Insights rules with CloudWatch alarms for metrics like latency or error counts in addition to ones for availability. These alarms can be used with the isolated Availability Zone impact composite alarms to ensure that single instances don’t activate the alarm. The metric for the insights rule for `use1-az1` might look like the following:

```
 INSIGHT_RULE_METRIC("5xx-errors-use1-az1", "UniqueContributors")
```

You can define an alarm when this metric is greater than a threshold; for this example, two. It is activated when the unique contributors to 5xx responses goes above that threshold, indicating the impact is originating from more than two instances. The reason this alarm uses a greater-than comparison instead of less-than is to make sure that a zero value for unique contributors doesn’t set off the alarm. This tells you that the impact is *not* from a single instance. Adjust this threshold for your individual workload. A general guide is to make this number 5% or more of the total resources in the Availability Zone. More than 5% of your resources being affected shows statistical significance, given a sufficient sample size.

## Putting it all together
<a name="putting-it-all-together"></a>

The following figure shows the complete composite alarm structure for a single Availability Zone:

![A diagram showing a complete composite alarm structure for determining single-AZ impact](https://docs.aws.amazon.com/whitepapers/latest/advanced-multi-az-resilience-patterns/images/composite-alarm-structure-complete.png)

 The final composite alarm, `use1-az1-isolated-impact`, is activated when the composite alarm indicating isolated Availability Zone impact from latency or availability, `use1-az1-aggregate-alarm`, is in `ALARM` state and when the alarm based on the Contributor Insights rule for that same Availability Zone, `not-single-instance-use1-az1`, is also in `ALARM` state (meaning that the impact is more than a single instance). You would create this stack of alarms for each Availability Zone that your workload uses.

You can attach an [Amazon Simple Notification Service](https://aws.amazon.com/sns/) (Amazon SNS) alert to this final alarm. All of the previous alarms are configured without an action. The alert could notify an operator via email to start manual investigation. It could also initiate automation to evacuate the Availability Zone. However, a word of caution on building automation to respond to these alerts. After an Availability Zone evacuation happens, the result should be that the increased error rates are mitigated and the alarm goes back to an `OK` state. If impact happens in another Availability Zone, it’s possible that the automation could evacuate a second or third Availability Zone, potentially removing all of the workload’s available capacity. The automation should check to see if an evacuation has already been performed before taking any action. You may also need to scale resources in other Availability Zones before an evacuation is successful.

When you add new controllers or actions to your MVC web app, or a new microservice, or in general, any additional functionality you want to separately monitor, you only need to modify a few alarms in this setup. You will create new availability and latency alarms for that new functionality and then add those to the appropriate Availability Zone aligned availability and latency composite alarms, `az1-latency` and `az1-availability` in the example we’ve been using here. The remaining composite alarms remain static after they have been configured. This makes onboarding new functionality with this approach a simpler process.
