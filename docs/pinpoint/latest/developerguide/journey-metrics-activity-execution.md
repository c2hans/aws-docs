---
source_url: https://docs.aws.amazon.com/pinpoint/latest/developerguide/journey-metrics-activity-execution.html
---

**End of support notice:** On October 30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints, segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of support](https://docs.aws.amazon.com/console/pinpoint/migration-guide). **Note:** APIs related to SMS, voice, mobile push, OTP, and phone number validate are not impacted by this change and are supported by AWS End User Messaging.

# Amazon Pinpoint journey activity execution metrics
<a name="journey-metrics-activity-execution"></a>

The following table lists and describes standard execution metrics that you can query to assess the status of participants in each type of individual activity for an Amazon Pinpoint journey. To query data for these metrics, use the [Journey activity execution metrics](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-journeys-journey-id-activities-journey-activity-id-execution-metrics.html) resource of the Amazon Pinpoint API. The **Metrics** column in the table lists the fields that appear in the query results for each type of activity. It also provides a brief description of each field.

| Activity type | Metrics |
| --- | --- |
| Yes/No split (`CONDITIONAL_SPLIT`) | The metrics are: [See the AWS documentation website for more details](http://docs.aws.amazon.com/pinpoint/latest/developerguide/journey-metrics-activity-execution.html)<br />Additional metrics are available for the activity on each path. For information about those metrics, see the row in this table for that type of activity. |
| Holdout (`HOLDOUT`) | The metrics are:[See the AWS documentation website for more details](http://docs.aws.amazon.com/pinpoint/latest/developerguide/journey-metrics-activity-execution.html) |
| Email (`MESSAGE`) | The metrics are:[See the AWS documentation website for more details](http://docs.aws.amazon.com/pinpoint/latest/developerguide/journey-metrics-activity-execution.html) |
| Multivariate split (`MULTI_CONDITIONAL_SPLIT`) | For each path of the activity, the number of participants who proceeded to the activity on the path.<br />The query results for this metric are grouped by path, `Branch_{{#}}` where {{\#}} is the numeric identifier for a path—for example, `Branch_1` for the first path of the activity.<br />Additional metrics are available for the activity on each path. For information about those metrics, see the row in this table for that type of activity. |
| Random split (`RANDOM_SPLIT`) | For each path of the activity, the number of participants who proceeded to the activity on the path.<br />The query results for this metric are grouped by path, `Branch_{{#}}` where {{\#}} is the numeric identifier for a path—for example, `Branch_1` for the first path of the activity.<br />Additional metrics are available for the activity on each path. For information about those metrics, see the row in this table for that type of activity. |
| Wait (`WAIT`) | The metrics are:[See the AWS documentation website for more details](http://docs.aws.amazon.com/pinpoint/latest/developerguide/journey-metrics-activity-execution.html) |
| Contact Center (`CONTACT_CENTER`) | The metrics are:[See the AWS documentation website for more details](http://docs.aws.amazon.com/pinpoint/latest/developerguide/journey-metrics-activity-execution.html) |
