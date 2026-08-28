---
source_url: https://docs.aws.amazon.com/redshift-serverless/latest/APIReference/API_Schedule.html
---

# Schedule
<a name="API_Schedule"></a>

The schedule of when Amazon Redshift Serverless should run the scheduled action.

## Contents
<a name="API_Schedule_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** at **   <a name="redshiftserverless-Type-Schedule-at"></a>
The timestamp of when Amazon Redshift Serverless should run the scheduled action. Timestamp is in UTC. Format of at expression is `yyyy-mm-ddThh:mm:ss`. For example, `2016-03-04T17:27:00`.
Type: Timestamp
Required: No

 ** cron **   <a name="redshiftserverless-Type-Schedule-cron"></a>
The cron expression to use to schedule a recurring scheduled action. Schedule invocations must be separated by at least one hour. Times are in UTC.
Format of cron expressions is `(Minutes Hours Day-of-month Month Day-of-week Year)`. For example, `"(0 10 ? * MON *)"`. For more information, see [Cron Expressions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/ScheduledEvents.html#CronExpressions) in the *Amazon CloudWatch Events User Guide*.
Type: String
Required: No

## See Also
<a name="API_Schedule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-serverless-2021-04-21/Schedule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-serverless-2021-04-21/Schedule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-serverless-2021-04-21/Schedule)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Redshift Serverless. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query redshift-serverless` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
