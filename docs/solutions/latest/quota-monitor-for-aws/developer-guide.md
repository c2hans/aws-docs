---
source_url: https://docs.aws.amazon.com/solutions/latest/quota-monitor-for-aws/developer-guide.html
---

# Developer guide
<a name="developer-guide"></a>

This section provides the source code for the solution and additional customizations.

## Source code
<a name="source-code"></a>

Visit our [GitHub repository](https://github.com/aws-solutions/quota-monitor-for-aws/) to download the source files for this solution and to share your customizations with others. The Quota Monitor for AWS templates are generated using the AWS CDK. Refer to the [README.md](https://github.com/aws-solutions/quota-monitor-for-aws/#readme) file for more information.

## Understanding Solution Components
<a name="understanding-solution-components"></a>

### Monitored Services and Quotas
<a name="monitored-services-and-quotas"></a>

**Note**
The solution only monitors quotas that have utilization metrics available through the AWS Service Quotas API.

The solution uses two main DynamoDB tables to manage services and quotas:

 **SQServiceTable**

This table contains all AWS services that support Service Quotas. Note that a service being in this table doesn’t necessarily mean it has quotas with utilization metrics. The **Monitored** flag indicates if the solution is actively tracking quotas for a service.

 **SQQuotaTable**

This table contains the quotas actively monitored by the solution. You can filter by services or quotas to view detailed monitoring information. Note that if a service in SQServiceTable is marked as 'Monitored' but has no corresponding quotas in SQQuotaTable, it indicates that the service lacks quotas supporting utilization metrics and is therefore not monitored by the solution.

To modify monitoring:

1. Login to spoke acocunt and in **SQServiceTable**, find the service and set **Monitored** to true/false.

1. The solution automatically updates **SQQuotaTable** accordingly.

### Summary DynamoDB Table
<a name="summary-dynamodb-table"></a>

A table in the hub account (named 'QM-Table') stores quota utilization events.

Key features:
+ Collects data from all monitored accounts and regions
+ Fields: AccountId, Region, Service, Resource, LimitCode, LimitName, CurrentUsage, LimitAmount, Status
+ TTL: 15 days

This table allows for historical analysis of quota usage across the organization.

## Change the Lambda interval
<a name="change-the-lambda-interval"></a>

By default, a Lambda function runs once every 24 hours to refresh the Trusted Advisor service quota checks. You can change how often the Lambda function is invoked by changing the mapping in the `quota-monitor-ta-spoke.template` CloudFormation template.

**Note**
If you set the Lambda function to run more than once every 12 hours, you may experience a delay in your events arriving in DynamoDB.

To change the interval, modify the following mapping in the CloudFormation template:

```
RefreshRate:
    CronSchedule:
      Default: rate(1 day)
```

For more information about acceptable rate expressions, refer to [Rate Expressions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/ScheduledEvents.html#RateExpressions) in the *Amazon EventBridge User Guide.*

The same value is exposed as a template parameter for the `quota-monitor-sq-spoke.template` CloudFormation template.

## Testing notifications using test events
<a name="testing-notifications-using-test-events"></a>

This solution allows you to send test events using Lambda test events in the same way that a Service Quotas event would be captured. Follow these steps to send a test event:

1. Navigate to the [Lambda Console](https://console.aws.amazon.com/lambda/home) in the AWS account you want to test.

1. Locate and select the `CW Poller` Lambda function.

1. Choose the **Test** tab.

1. In the **Event JSON** window, input the following event (set test-type to either `ERROR` or `WARN`):

   ```
   {
     "detail-type": "QM Lambda Test Event",
     "test-type": "WARN"
   }
   ```

1. Choose **Test**.

The event should send a notification to subscribers of the SNS topic.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Quota Monitor for AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
