---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_GetMetricDataV2.html
---

# GetMetricDataV2
<a name="API_GetMetricDataV2"></a>

Gets metric data from the specified Connect Customer instance.

 `GetMetricDataV2` offers more features than [GetMetricData](https://docs.aws.amazon.com/connect/latest/APIReference/API_GetMetricData.html), the previous version of this API. It has new metrics, offers filtering at a metric level, and offers the ability to filter and group data by channels, queues, routing profiles, agents, and agent hierarchy levels. It can retrieve historical data for the last 3 months, at varying intervals. It does not support agent queues.

For a description of the historical metrics that are supported by `GetMetricDataV2` and `GetMetricData`, see [Metrics definitions](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html) in the *Connect Customer Administrator Guide*.

**Note**
When you make a successful API request, you can expect the following metric values in the response:
 **Metric value is null**: The calculation cannot be performed due to divide by zero or insufficient data
 **Metric value is a number (including 0) of defined type**: The number provided is the calculation result
 **MetricResult list is empty**: The request cannot find any data in the system
The following guidelines can help you work with the API:
Each dimension in the metric response must contain a value
Each item in MetricResult must include all requested metrics
If the response is slow due to large result sets, try these approaches:
Narrow the time range of your request
Add filters to reduce the amount of data returned

## Request Syntax
<a name="API_GetMetricDataV2_RequestSyntax"></a>

```
POST /metrics/data HTTP/1.1
Content-type: application/json

{
   "EndTime": {{number}},
   "Filters": [
      {
         "FilterKey": "{{string}}",
         "FilterValues": [ "{{string}}" ],
         "StringCondition": {
            "Comparison": "{{string}}"
         }
      }
   ],
   "Groupings": [ "{{string}}" ],
   "Interval": {
      "IntervalPeriod": "{{string}}",
      "TimeZone": "{{string}}"
   },
   "MaxResults": {{number}},
   "Metrics": [
      {
         "MetricFilters": [
            {
               "MetricFilterKey": "{{string}}",
               "MetricFilterValues": [ "{{string}}" ],
               "Negate": {{boolean}}
            }
         ],
         "MetricId": "{{string}}",
         "Name": "{{string}}",
         "Threshold": [
            {
               "Comparison": "{{string}}",
               "ThresholdValue": {{number}}
            }
         ]
      }
   ],
   "NextToken": "{{string}}",
   "ResourceArn": "{{string}}",
   "StartTime": {{number}}
}
```

## URI Request Parameters
<a name="API_GetMetricDataV2_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetMetricDataV2_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [EndTime](#API_GetMetricDataV2_RequestSyntax) **   <a name="connect-GetMetricDataV2-request-EndTime"></a>
The timestamp, in UNIX Epoch time format, at which to end the reporting interval for the retrieval of historical metrics data. The time must be later than the start time timestamp. It cannot be later than the current timestamp.
Type: Timestamp
Required: Yes

 ** [Filters](#API_GetMetricDataV2_RequestSyntax) **   <a name="connect-GetMetricDataV2-request-Filters"></a>
Filtering is an operation that selects records that match a set of specified criteria. By narrowing the dataset before aggregation, filters ensure that only relevant records are included in the computation.
 **Filter keys**
The following are valid filter keys for a `GetMetricDataV2` request:
 `AGENT` \| `AI_AGENT` \| `AI_AGENT_ID` \| `AI_AGENT_NAME` \| `AI_AGENT_TYPE` \| `AI_PROMPT` \| `AI_PROMPT_ID` \| `AI_PROMPT_NAME` \| `AI_PROMPT_TYPE` \| `AI_TOOL_ID` \| `AI_TOOL_NAME` \| `AI_TOOL_TYPE` \| `AI_USE_CASE` \| `AGENT_HIERARCHY_LEVEL_ONE` \| `AGENT_HIERARCHY_LEVEL_TWO` \| `AGENT_HIERARCHY_LEVEL_THREE` \| `AGENT_HIERARCHY_LEVEL_FOUR` \| `AGENT_HIERARCHY_LEVEL_FIVE` \| `ANSWERING_MACHINE_DETECTION_STATUS` \| `BOT_ALIAS` \| `BOT_ID` \| `BOT_INTENT_NAME` \| `BOT_LOCALE` \| `BOT_VERSION` \| `BROWSER_NAME` \| `CAMPAIGN` \| `CAMPAIGN_DELIVERY_EVENT_TYPE` \| `CAMPAIGN_EXCLUDED_EVENT_TYPE` \| `CASE_STATUS` \| `CASE_TEMPLATE_ARN` \| `CHANNEL` \| `contact/segmentAttributes/connect:Subtype` \| `contact/segmentAttributes/connect:ValidationTestType` \| `DEVICE_MODEL` \| `DEVICE_TYPE` \| `DISCONNECT_REASON` \| `EVALUATION_FORM` \| `EVALUATION_QUESTION` \| `EVALUATION_SECTION` \| `EVALUATION_SOURCE` \| `EVALUATOR_ID` \| `FEATURE` \| `FLOW_ACTION_ID` \| `FLOW_TYPE` \| `FLOWS_MODULE_RESOURCE_ID` \| `FLOWS_NEXT_RESOURCE_ID` \| `FLOWS_NEXT_RESOURCE_QUEUE_ID` \| `FLOWS_OUTCOME_TYPE` \| `FLOWS_RESOURCE_ID` \| `FORM_VERSION` \| `INITIATING_FLOW` \| `INITIATION_METHOD` \| `INVOKING_RESOURCE_PUBLISHED_TIMESTAMP` \| `INVOKING_RESOURCE_TYPE` \| `KNOWLEDGE_BASE_NAME` \| `PARENT_FLOWS_RESOURCE_ID` \| `Q_CONNECT_ENABLED` \| `QUEUE` \| `RESOURCE_PUBLISHED_TIMESTAMP` \| `ROUTING_PROFILE` \| `ROUTING_STEP_EXPRESSION` \| `SESSION_ID` \| `TEST_CASE` \| `TEST_CASE_EXECUTION_FAILURE_REASON` \| `TEST_CASE_EXECUTION_RESULT` \| `TEST_CASE_EXECUTION_STATE` \| `WEB_NOTIFICATION_TYPE`
The following filter keys correspond to Connect Customer resources and are used for authorizing requests. A `GetMetricDataV2` request requires at least one of these filters:
 `QUEUE`, `ROUTING_PROFILE`, `AGENT`, `AGENT_HIERARCHY_LEVEL_ONE`, `AGENT_HIERARCHY_LEVEL_TWO`, `AGENT_HIERARCHY_LEVEL_THREE`, `AGENT_HIERARCHY_LEVEL_FOUR`, `AGENT_HIERARCHY_LEVEL_FIVE`, `CAMPAIGN`, `EVALUATION_FORM`, `EVALUATOR_ID`
You can use up to 5 filter keys in a single request, and up to 100 filter values across all filter keys.
 **Filter values**
+ VOICE, CHAT, TASK, and EMAIL are valid filter values for the `CHANNEL` filter key. They do not count towards the limit of 100 filter values. For example, a `GetMetricDataV2` request can filter by 50 queues, 35 agents, and 15 routing profiles for a total of 100 filter values, along with 4 channel filters.
+  `contact_lens_conversational_analytics` is a valid filter value for the `FEATURE` filter key. It is available only for contacts analyzed by Contact Lens conversational analytics.
+  `connect:Chat`, `connect:SMS`, `connect:Telephony`, and `connect:WebRTC` are valid filter value examples (not exhaustive) for the `contact/segmentAttributes/connect:Subtype` filter key.
+  `ROUTING_STEP_EXPRESSION` accepts a filter value up to 3,000 characters in length. Filter values are case-sensitive. JSON object key order and whitespace may be arbitrary; array order and tree structure must be preserved.
+ TRUE and FALSE are the only valid filter values for the `Q_CONNECT_ENABLED` filter key.
  + TRUE includes all contacts that had Connect AI Agents enabled as part of the flow.
  + FALSE includes all contacts that did not have Connect AI Agents enabled as part of the flow.
+  `EXPERIENCE_VALIDATION` and `FLOW_VALIDATION` are the only valid filter values for the `contact/segmentAttributes/connect:ValidationTestType` filter key. This filter is available only for contact record-driven metrics.
+  [Campaign](https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-outbound-campaigns_Campaign.html) ARNs are valid filter values for the `CAMPAIGN` filter key.
+ To filter by phone number, see [Create a historical metrics report](https://docs.aws.amazon.com/connect/latest/adminguide/create-historical-metrics-report.html) in the *Connect Customer Administrator Guide*.
Type: Array of [FilterV2](API_FilterV2.md) objects
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Required: Yes

 ** [Groupings](#API_GetMetricDataV2_RequestSyntax) **   <a name="connect-GetMetricDataV2-request-Groupings"></a>
The grouping applied to the metrics that are returned. For example, when results are grouped by queue, the metrics returned are grouped by queue. The values that are returned apply to the metrics for each queue. They are not aggregated for all queues.
If no grouping is specified, a summary of all metrics is returned.
Valid grouping keys: `AGENT` \| `AI_AGENT` \| `AI_AGENT_ID` \| `AI_AGENT_NAME` \| `AI_AGENT_NAME_VERSION` \| `AI_AGENT_TYPE` \| `AI_PROMPT` \| `AI_PROMPT_ID` \| `AI_PROMPT_NAME` \| `AI_PROMPT_NAME_VERSION` \| `AI_PROMPT_TYPE` \| `AI_TOOL_ID` \| `AI_TOOL_NAME` \| `AI_TOOL_TYPE` \| `AI_USE_CASE` \| `AGENT_HIERARCHY_LEVEL_ONE` \| `AGENT_HIERARCHY_LEVEL_TWO` \| `AGENT_HIERARCHY_LEVEL_THREE` \| `AGENT_HIERARCHY_LEVEL_FOUR` \| `AGENT_HIERARCHY_LEVEL_FIVE` \| `ANSWERING_MACHINE_DETECTION_STATUS` \| `BOT_ID` \| `BOT_ALIAS` \| `BOT_VERSION` \| `BOT_LOCALE` \| `BOT_INTENT_NAME` \| `BROWSER_NAME` \| `CAMPAIGN` \| `CAMPAIGN_DELIVERY_EVENT_TYPE` \| `CAMPAIGN_EXCLUDED_EVENT_TYPE` \| `CAMPAIGN_EXECUTION_TIMESTAMP` \| `CASE_TEMPLATE_ARN` \| `CASE_STATUS` \| `CHANNEL` \| `contact/segmentAttributes/connect:Subtype` \| `DEVICE_MODEL` \| `DEVICE_TYPE` \| `DISCONNECT_REASON` \| `EVALUATION_FORM` \| `EVALUATION_SECTION` \| `EVALUATION_QUESTION` \| `EVALUATION_SOURCE` \| `EVALUATOR_ID` \| `FLOWS_RESOURCE_ID` \| `FLOWS_MODULE_RESOURCE_ID` \| `FLOW_ACTION_ID` \| `FLOW_TYPE` \| `FLOWS_OUTCOME_TYPE` \| `FORM_VERSION` \| `INITIATION_METHOD` \| `INVOKING_RESOURCE_PUBLISHED_TIMESTAMP` \| `INVOKING_RESOURCE_TYPE` \| `KNOWLEDGE_ARTICLE_NAME` \| `KNOWLEDGE_BASE_NAME` \| `PARENT_FLOWS_RESOURCE_ID` \| `Q_CONNECT_ENABLED` \| `QUEUE` \| `RESOURCE_PUBLISHED_TIMESTAMP` \| `ROUTING_PROFILE` \| `ROUTING_STEP_EXPRESSION` \| `SESSION_ID` \| `TEST_CASE` \| `TEST_CASE_EXECUTION_FAILURE_REASON` \| `TEST_CASE_INVOCATION_METHOD` \| `WEB_NOTIFICATION_TYPE`
 `AI_AGENT_NAME_VERSION`, `AI_PROMPT_NAME_VERSION`, and `KNOWLEDGE_ARTICLE_NAME` are valid groupings but not valid filters.
API, SCHEDULE, and EVENT are the only valid filterValues for TEST\_CASE\_INVOCATION\_METHOD.
OBSERVE\_EVENT, SEND\_INSTRUCTION, ASSERT\_DATA, and OVERRIDE\_SYSTEM\_BEHAVIOR are the only valid filterValues for TEST\_CASE\_EXECUTION\_FAILURE\_REASON
Type: Array of strings
Array Members: Maximum number of 4 items
Required: No
Type: Array of strings
Array Members: Maximum number of 4 items.
Required: No

 ** [Interval](#API_GetMetricDataV2_RequestSyntax) **   <a name="connect-GetMetricDataV2-request-Interval"></a>
The interval period and timezone to apply to returned metrics.
+  `IntervalPeriod`: An aggregated grouping applied to request metrics. Valid `IntervalPeriod` values are: `FIFTEEN_MIN` \| `THIRTY_MIN` \| `HOUR` \| `DAY` \| `WEEK` \| `TOTAL`.

  For example, if `IntervalPeriod` is selected `THIRTY_MIN`, `StartTime` and `EndTime` differs by 1 day, then Connect Customer returns 48 results in the response. Each result is aggregated by the THIRTY\_MIN period. By default Connect Customer aggregates results based on the `TOTAL` interval period.

  The following list describes restrictions on `StartTime` and `EndTime` based on which `IntervalPeriod` is requested.
  +  `FIFTEEN_MIN`: The difference between `StartTime` and `EndTime` must be less than 3 days.
  +  `THIRTY_MIN`: The difference between `StartTime` and `EndTime` must be less than 3 days.
  +  `HOUR`: The difference between `StartTime` and `EndTime` must be less than 3 days.
  +  `DAY`: The difference between `StartTime` and `EndTime` must be less than 35 days.
  +  `WEEK`: The difference between `StartTime` and `EndTime` must be less than 35 days.
  +  `TOTAL`: The difference between `StartTime` and `EndTime` must be less than 35 days.
+  `TimeZone`: The timezone applied to requested metrics.
Type: [IntervalDetails](API_IntervalDetails.md) object
Required: No

 ** [MaxResults](#API_GetMetricDataV2_RequestSyntax) **   <a name="connect-GetMetricDataV2-request-MaxResults"></a>
The maximum number of results to return per page.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [Metrics](#API_GetMetricDataV2_RequestSyntax) **   <a name="connect-GetMetricDataV2-request-Metrics"></a>
The metrics to retrieve. Specify the name or metricId, groupings, and filters for each metric. The following historical metrics are available. For a description of each metric, see [Metrics definition](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html) in the *Connect Customer Administrator Guide*.
MetricId should be used to reference custom metrics or out of the box metrics as Arn. If using MetricId, the limit is 20 MetricId per request.
ABANDONMENT\_RATE
Unit: Percent
Valid groupings and filters: Queue, Channel, Routing Profile, Agent, Agent Hierarchy, Feature, contact/segmentAttributes/connect:Subtype, Q in Connect
UI name: [Abandonment rate](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#abandonment-rate)
AGENT\_ADHERENT\_TIME
This metric is available only in AWS Regions where [Forecasting, capacity planning, and scheduling](https://docs.aws.amazon.com/connect/latest/adminguide/regions.html#optimization_region) is available.
Unit: Seconds
Valid groupings and filters: Queue, Channel, Routing Profile, Agent, Agent Hierarchy
UI name: [Adherent time](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#adherent-time)
AGENT\_ANSWER\_RATE
Unit: Percent
Valid groupings and filters: Queue, Channel, Routing Profile, Agent, Agent Hierarchy
UI name: [Agent answer rate](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#agent-answer-rate)
AGENT\_NON\_ADHERENT\_TIME
Unit: Seconds
Valid groupings and filters: Queue, Channel, Routing Profile, Agent, Agent Hierarchy
UI name: [Non-adherent time](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#non-adherent-time)
AGENT\_NON\_RESPONSE
Unit: Count
Valid groupings and filters: Queue, Channel, Routing Profile, Agent, Agent Hierarchy
UI name: [Agent non-response](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#agent-non-response)
AGENT\_NON\_RESPONSE\_WITHOUT\_CUSTOMER\_ABANDONS
Unit: Count
Valid groupings and filters: Queue, Channel, Routing Profile, Agent, Agent Hierarchy
Data for this metric is available starting from October 1, 2023 0:00:00 GMT.
UI name: [Agent non-response without customer abandons](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#agent-non-response-without-customer-abandons)
AGENT\_OCCUPANCY
Unit: Percentage
Valid groupings and filters: Routing Profile, Agent, Agent Hierarchy
UI name: [Occupancy](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#occupancy)
AGENT\_SCHEDULE\_ADHERENCE
This metric is available only in AWS Regions where [Forecasting, capacity planning, and scheduling](https://docs.aws.amazon.com/connect/latest/adminguide/regions.html#optimization_region) is available.
Unit: Percent
Valid groupings and filters: Queue, Channel, Routing Profile, Agent, Agent Hierarchy
UI name: [Adherence](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#adherence)
AGENT\_SCHEDULED\_TIME
This metric is available only in AWS Regions where [Forecasting, capacity planning, and scheduling](https://docs.aws.amazon.com/connect/latest/adminguide/regions.html#optimization_region) is available.
Unit: Seconds
Valid groupings and filters: Queue, Channel, Routing Profile, Agent, Agent Hierarchy
UI name: [Scheduled time](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#scheduled-time)
AVG\_ABANDON\_TIME
Unit: Seconds
Valid groupings and filters: Queue, Channel, Routing Profile, Agent, Agent Hierarchy, Feature, contact/segmentAttributes/connect:Subtype, Q in Connect
Valid metric filter key: `INITIATION_METHOD`
UI name: [Average queue abandon time](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#average-queue-abandon-time)
AVG\_ACTIVE\_TIME
Unit: Seconds
Valid groupings and filters: Queue, Channel, Routing Profile, Agent, Agent Hierarchy, Q in Connect
UI name: [Average active time](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#average-active-time)
AVG\_AFTER\_CONTACT\_WORK\_TIME
Unit: Seconds
Valid metric filter key: `INITIATION_METHOD`
Valid groupings and filters: Queue, Channel, Routing Profile, Agent, Agent Hierarchy, Feature, contact/segmentAttributes/connect:Subtype, Q in Connect
UI name: [Average after contact work time](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#after-contact-work-time)
Feature is a valid filter but not a valid grouping.
AVG\_AGENT\_CONCURRENCY
Unit: Count
Valid groupings and filters: Queue, Channel, Routing Profile, Agent, Agent Hierarchy, Q in Connect
UI name: [Average agent concurrency](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#average-agent-concurrency)
AVG\_AGENT\_CONNECTING\_TIME
Unit: Seconds
Valid metric filter key: `INITIATION_METHOD`. For now, this metric only supports the following as `INITIATION_METHOD`: `INBOUND` \| `OUTBOUND` \| `CALLBACK` \| `API`
Valid groupings and filters: Queue, Channel, Routing Profile, Agent, Agent Hierarchy
UI name: [Average agent API connecting time](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#average-agent-api-connecting-time)
The `Negate` key in metric-level filters is not applicable for this metric.
AVG\_AGENT\_PAUSE\_TIME
Unit: Seconds
Valid groupings and filters: Queue, Channel, Routing Profile, Agent, Agent Hierarchy, Q in Connect
UI name: [Average agent pause time](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#average-agent-pause-time)
AVG\_BOT\_CONVERSATION\_TIME
Unit: Seconds
Valid groupings and filters: Channel, contact/segmentAttributes/connect:Subtype, Bot ID, Bot alias, Bot version, Bot locale, Flows resource ID, Flows module resource ID, Flow type, Flow action ID, Invoking resource published timestamp, Initiation method, Invoking resource type, Parent flows resource ID
UI name: [Average bot conversation time](https://docs.aws.amazon.com/connect/latest/adminguide/bot-metrics.html#average-bot-conversation-time)
AVG\_BOT\_CONVERSATION\_TURNS
Unit: Count
Valid groupings and filters: Channel, contact/segmentAttributes/connect:Subtype, Bot ID, Bot alias, Bot version, Bot locale, Flows resource ID, Flows module resource ID, Flow type, Flow action ID, Invoking resource published timestamp, Initiation method, Invoking resource type, Parent flows resource ID
UI name: [Average bot conversation turns](https://docs.aws.amazon.com/connect/latest/adminguide/bot-metrics.html#average-bot-conversation-turns)
AVG\_CASE\_RELATED\_CONTACTS
Unit: Count
Required filter key: CASE\_TEMPLATE\_ARN
Valid groupings and filters: CASE\_TEMPLATE\_ARN, CASE\_STATUS
UI name: [Average contacts per case](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#average-contacts-per-case)
AVG\_CASE\_RESOLUTION\_TIME
Unit: Seconds
Required filter key: CASE\_TEMPLATE\_ARN
Valid groupings and filters: CASE\_TEMPLATE\_ARN, CASE\_STATUS
UI name: [Average case resolution time](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#average-case-resolution-time)
AVG\_CONTACT\_DURATION
Unit: Seconds
Valid groupings and filters: Queue, Channel, Routing Profile, Agent, Agent Hierarchy, Feature, contact/segmentAttributes/connect:Subtype, Q in Connect
UI name: [Average contact duration](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#average-contact-duration)
Feature is a valid filter but not a valid grouping.
AVG\_CONTACT\_FIRST\_RESPONSE\_TIME\_AGENT
Unit: Seconds
Valid groupings and filters: Agent, Agent Hierarchy, Channel, contact/segmentAttributes/connect:Subtype, Disconnect Reason, Feature, RoutingStepExpression, Initiation method, Routing Profile, Queue, Q in Connect
UI name: [Agent average contact first response wait time](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#agent-average-contact-first-response-wait-time)
AVG\_CONVERSATION\_CLOSE\_TIME
Unit: Seconds
Valid groupings and filters: Agent, Agent Hierarchy, Channel, contact/segmentAttributes/connect:Subtype, Disconnect Reason, Feature, RoutingStepExpression, Initiation method, Routing Profile, Queue, Q in Connect
UI name: [Average conversation close time](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#average-conversation-close-time)
AVG\_CONVERSATION\_DURATION
Unit: Seconds
Valid groupings and filters: Queue, Channel, Routing Profile, Agent, Agent Hierarchy, Feature, contact/segmentAttributes/connect:Subtype, Q in Connect
UI name: [Average conversation duration](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#average-conversation-duration)
AVG\_DIALS\_PER\_MINUTE
This metric is available only for outbound campaigns that use the agent assisted voice and automated voice delivery modes.
Unit: Count
Valid groupings and filters: Agent, Campaign, Queue, Routing Profile
UI name: [Average dials per minute](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#average-dials-per-minute)
AVG\_EVALUATION\_SCORE
Unit: Percent
Valid groupings and filters: Agent, Agent Hierarchy, Channel, Evaluation Form ID, Evaluation Section ID, Evaluation Question ID, Evaluation Source, Form Version, Queue, Routing Profile
UI name: [Average evaluation score](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#average-evaluation-score)
AVG\_FIRST\_RESPONSE\_TIME\_AGENT
Unit: Seconds
Valid groupings and filters: Agent, Agent Hierarchy, Channel, contact/segmentAttributes/connect:Subtype, Disconnect Reason, Feature, RoutingStepExpression, Initiation method, Routing Profile, Queue, Q in Connect
UI name: [Average agent first response time](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#average-agent-first-response-time)
AVG\_FLOW\_TIME
Unit: Seconds
Valid groupings and filters: Channel, contact/segmentAttributes/connect:Subtype, Flow type, Flows module resource ID, Flows next resource ID, Flows next resource queue ID, Flows outcome type, Flows resource ID, Initiation method, Resource published timestamp
UI name: [Average flow time](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#average-flow-time)
AVG\_GREETING\_TIME\_AGENT
This metric is available only for contacts analyzed by Contact Lens conversational analytics.
Unit: Seconds
Valid groupings and filters: Queue, Channel, Routing Profile, Agent, Agent Hierarchy, contact/segmentAttributes/connect:Subtype, Q in Connect
UI name: [Average agent greeting time](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#average-agent-greeting-time)
AVG\_HANDLE\_TIME
Unit: Seconds
Valid groupings and filters: Queue, Channel, Routing Profile, Agent, Agent Hierarchy, AI Use Case, Feature, contact/segmentAttributes/connect:Subtype, RoutingStepExpression
UI name: [Average handle time](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#average-handle-time)
Feature is a valid filter but not a valid grouping.
ACTIVE\_AI\_AGENTS
Unit: Count
Valid groupings and filters: AI Agent, AI Agent Name, AI Agent Type, AI Use Case, Channel, Queue, Routing Profile
UI name: [Active AI Agents](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#active-ai-agents)
AI\_HANDOFF\_RATE
Unit: Percent
Valid groupings and filters: AI Agent ID, AI Agent Name, AI Agent Type, AI Use Case, Channel, Queue, Routing Profile
UI name: [AI Handoff Rate](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#ai-handoff-rate)
AI\_HANDOFFS
Unit: Count
Valid groupings and filters: AI Agent ID, AI Agent Name, AI Agent Type, AI Use Case, Channel, Queue, Routing Profile
UI name: [AI Handoff Count](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#ai-handoffs)
AI\_AGENT\_INVOCATION\_SUCCESS
Unit: Count
Valid groupings and filters: AI Agent, AI Agent Name, AI Agent Name Version, AI Agent Type, AI Use Case, Channel, Queue, Routing Profile
UI name: [AI Agent Invocation Success](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#ai-agent-invocation-success)
AI Agent Name Version is not a valid filter but a valid grouping.
AI\_AGENT\_INVOCATION\_SUCCESS\_RATE
Unit: Percent
Valid groupings and filters: AI Agent, AI Agent Name, AI Agent Name Version, AI Agent Type, AI Use Case, Channel, Queue, Routing Profile
UI name: [AI Agent Invocation Success Rate](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#ai-agent-invocation-success-rate)
AI Agent Name Version is not a valid filter but a valid grouping.
AI\_AGENT\_INVOCATIONS
Unit: Count
Valid groupings and filters: AI Agent, AI Agent Name, AI Agent Type, AI Agent Name Version, AI Use Case, Channel, Queue, Routing Profile
UI name: [AI Agent Invocation Count](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#ai-agent-invocations)
AI Agent Name Version is not a valid filter but a valid grouping.
AI\_AGENT\_RESPONSE\_HELPFUL
Unit: Count
Valid groupings and filters: AI Agent, AI Agent ID, AI Agent Name, AI Agent Name Version, AI Agent Type, AI Use Case, Channel, Queue, Routing Profile
UI name: [AI Agent Response Helpful](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#ai-agent-response-helpful)
AI Agent Name Version is not a valid filter but a valid grouping.
AI\_AGENT\_RESPONSE\_NOT\_HELPFUL
Unit: Count
Valid groupings and filters: AI Agent, AI Agent ID, AI Agent Name, AI Agent Name Version, AI Agent Type, AI Use Case, Channel, Queue, Routing Profile
UI name: [AI Agent Response Not Helpful](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#ai-agent-response-not-helpful)
AI Agent Name Version is not a valid filter but a valid grouping.
AI\_RESPONSE\_COMPLETION\_RATE
Unit: Percent
Valid groupings and filters: AI Agent ID, AI Agent Name, AI Agent Type, AI Use Case, Channel, Queue, Routing Profile
UI name: [AI Response Completion Rate](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#ai-response-completion-rate)
AI\_INVOLVED\_CONTACTS
Unit: Count
Valid groupings and filters: AI Agent ID, AI Agent Name, AI Agent Type, AI Use Case, Channel, Queue, Routing Profile
UI name: [AI Involved Contacts](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#ai-involved-contacts)
AI\_PROMPT\_INVOCATION\_SUCCESS
Unit: Count
Valid groupings and filters: AI Agent, AI Agent Name, AI Agent Name Version, AI Agent Type, AI Prompt, AI Prompt ID, AI Prompt Name, AI Prompt Type, AI Use Case, Channel, Queue, Routing Profile
UI name: [AI Prompt Invocation Success](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#ai-prompt-invocation-success)
AI Agent Name Version is not a valid filter but a valid grouping.
AI\_PROMPT\_INVOCATION\_SUCCESS\_RATE
Unit: Percent
Valid groupings and filters: AI Agent, AI Agent Name, AI Agent Name Version, AI Agent Type, AI Prompt, AI Prompt ID, AI Prompt Name, AI Prompt Type, AI Use Case, Channel, Queue, Routing Profile
UI name: [AI Prompt Invocation Success Rate](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#ai-prompt-invocation-success-rate)
AI Agent Name Version is not a valid filter but a valid grouping.
AI\_PROMPT\_INVOCATIONS
Unit: Count
Valid groupings and filters: AI Agent, AI Agent Name, AI Agent Name Version, AI Agent Type, AI Prompt, AI Prompt ID, AI Prompt Name, AI Prompt Type, AI Use Case, Channel, Queue, Routing Profile
UI name: [AI Prompt Invocations](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#ai-prompt-invocations)
AI Agent Name Version is not a valid filter but a valid grouping.
AI\_TOOL\_INVOCATION\_SUCCESS
Unit: Count
Valid groupings and filters: AI Agent, AI Agent Name, AI Agent Name Version, AI Agent Type, AI Tool ID, AI Tool Name, AI Tool Type, AI Use Case, Channel, Queue, Routing Profile
UI name: [AI Tool Invocation Success](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#ai-tool-invocation-success)
AI Agent Name Version is not a valid filter but a valid grouping.
AI\_TOOL\_INVOCATION\_SUCCESS\_RATE
Unit: Percent
Valid groupings and filters: AI Agent, AI Agent Name, AI Agent Name Version, AI Agent Type, AI Tool ID, AI Tool Name, AI Tool Type, AI Use Case, Channel, Queue, Routing Profile
UI name: [AI Tool Invocation Success Rate](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#ai-tool-invocation-success-rate)
AI Agent Name Version is not a valid filter but a valid grouping.
AI\_TOOL\_INVOCATIONS
Unit: Count
Valid groupings and filters: AI Agent, AI Agent Name, AI Agent Name Version, AI Agent Type, AI Tool ID, AI Tool Name, AI Tool Type, AI Use Case, Channel, Queue, Routing Profile
UI name: [AI Tool Invocations](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#ai-tool-invocations)
AI Agent Name Version is not a valid filter but a valid grouping.
AVG\_AI\_AGENT\_CONVERSATION\_TURNS
Unit: Count
Valid groupings and filters: AI Agent, AI Agent Name, AI Agent Name Version, AI Agent Type, AI Use Case, Channel, Queue, Routing Profile
UI name: [Average AI Agent Conversation Turns](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#average-ai-agent-conversation-turns)
AI Agent Name Version is not a valid filter but a valid grouping.
AVG\_AI\_CONVERSATION\_TURNS
Unit: Count
Valid groupings and filters: AI Agent ID, AI Agent Name, AI Agent Type, AI Use Case, Channel, Queue, Routing Profile
UI name: [Average AI Conversation Turns](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#average-ai-conversation-turns)
AVG\_AI\_PROMPT\_INVOCATION\_LATENCY
Unit: Milliseconds
Valid groupings and filters: AI Agent, AI Agent Name, AI Agent Name Version, AI Agent Type, AI Prompt, AI Prompt ID, AI Prompt Name, AI Prompt Type, AI Use Case, Channel, Queue, Routing Profile
UI name: [Average AI Prompt Invocation Latency](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#average-ai-prompt-invocation-latency)
AI Agent Name Version is not a valid filter but a valid grouping.
AVG\_AI\_TOOL\_INVOCATION\_LATENCY
Unit: Milliseconds
Valid groupings and filters: AI Agent, AI Agent Name, AI Agent Name Version, AI Agent Type, AI Tool ID, AI Tool Name, AI Tool Type, AI Use Case, Channel, Queue, Routing Profile
UI name: [Average AI Tool Invocation Latency](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#average-ai-tool-invocation-latency)
AI Agent Name Version is not a valid filter but a valid grouping.
AI\_TOOL\_PARAMETER\_ACCURACY
Unit: Double
Valid groupings and filters: AI Agent, AI Agent ID, AI Agent Name, AI Agent Name Version, AI Agent Type, AI Tool ID, AI Tool Name, AI Tool Type, AI Use Case, Channel, Queue, Routing Profile
UI name: [AI Tool Parameter Accuracy](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#ai-tool-parameter-accuracy)
AI Agent Name Version is not a valid filter but a valid grouping.
AI\_TOOL\_SELECTION\_ACCURACY
Unit: Double
Valid groupings and filters: AI Agent, AI Agent ID, AI Agent Name, AI Agent Name Version, AI Agent Type, AI Tool ID, AI Tool Name, AI Tool Type, AI Use Case, Channel, Queue, Routing Profile
UI name: [AI Tool Selection Accuracy](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#ai-tool-selection-accuracy)
AI Agent Name Version is not a valid filter but a valid grouping.
AI\_TOOL\_UTILIZATION\_ACCURACY
Unit: Double
Valid groupings and filters: AI Agent, AI Agent ID, AI Agent Name, AI Agent Name Version, AI Agent Type, AI Tool ID, AI Tool Name, AI Tool Type, AI Use Case, Channel, Queue, Routing Profile, Session ID
UI name: [AI Tool Utilization Accuracy](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#ai-tool-utilization-accuracy)
AI Agent Name Version is not a valid filter but a valid grouping.
COMPLETENESS\_SCORE
Unit: Double
Valid groupings and filters: AI Agent ID, AI Agent Name, AI Agent Type, AI Use Case, Channel, Queue, Routing Profile, Session ID
UI name: [Completeness Score](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#completeness-score)
FAITHFULNESS\_SCORE
Unit: Double
Valid groupings and filters: AI Agent ID, AI Agent Name, AI Agent Type, AI Use Case, Channel, Queue, Routing Profile, Session ID
UI name: [Faithfulness Score](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#faithfulness-score)
GOAL\_SUCCESS\_RATE
Unit: Double
Valid groupings and filters: AI Agent ID, AI Agent Name, AI Agent Type, AI Use Case, Channel, Queue, Routing Profile, Session ID
UI name: [Goal Success Rate](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#goal-success-rate)
KNOWLEDGE\_CONTENT\_REFERENCES
Unit: Count
Valid groupings and filters: AI Agent, AI Agent Name, AI Agent Type, AI Use Case, Channel, Knowledge Base Name, Queue, Routing Profile
UI name: [Knowledge Content References](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#knowledge-content-references)
PROACTIVE\_INTENT\_ENGAGEMENT\_RATE
Unit: Percent
Valid groupings and filters: AI Agent ID, AI Agent Name, AI Agent Type, AI Use Case, Channel, Queue, Routing Profile
UI name: [Proactive Intent Engagement Rate](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#proactive-intents-engagement-rate)
PROACTIVE\_INTENT\_RESPONSE\_RATE
Unit: Percent
Valid groupings and filters: AI Agent ID, AI Agent Name, AI Agent Type, AI Use Case, Channel, Queue, Routing Profile
UI name: [Proactive Intent Response Rate](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#proactive-intents-response-rate)
PROACTIVE\_INTENTS\_ANSWERED
Unit: Count
Valid groupings and filters: AI Agent ID, AI Agent Name, AI Agent Type, AI Use Case, Channel, Queue, Routing Profile
UI name: [Proactive Intents Answered](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#proactive-intents-answered)
PROACTIVE\_INTENTS\_DETECTED
Unit: Count
Valid groupings and filters: AI Agent ID, AI Agent Name, AI Agent Type, AI Use Case, Channel, Queue, Routing Profile
UI name: [Proactive Intents Detected](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#proactive-intents-detected)
PROACTIVE\_INTENTS\_ENGAGED
Unit: Count
Valid groupings and filters: AI Agent ID, AI Agent Name, AI Agent Type, AI Use Case, Channel, Queue, Routing Profile
UI name: [Proactive Intents Engaged](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#proactive-intents-engaged)
AVG\_HOLD\_TIME
Unit: Seconds
Valid groupings and filters: Queue, Channel, Routing Profile, Agent, Agent Hierarchy, Feature, contact/segmentAttributes/connect:Subtype, Q in Connect
UI name: [Average customer hold time](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#average-customer-hold-time)
Feature is a valid filter but not a valid grouping.
AVG\_HOLD\_TIME\_ALL\_CONTACTS
Unit: Seconds
Valid groupings and filters: Queue, Channel, Routing Profile, Agent, Agent Hierarchy, contact/segmentAttributes/connect:Subtype, Q in Connect
UI name: [Average customer hold time all contacts](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#average-customer-hold-time-all-contacts)
AVG\_HOLDS
Unit: Count
Valid groupings and filters: Queue, Channel, Routing Profile, Agent, Agent Hierarchy, Feature, contact/segmentAttributes/connect:Subtype, Q in Connect
UI name: [Average holds](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#average-holds)
Feature is a valid filter but not a valid grouping.
AVG\_INTERACTION\_AND\_HOLD\_TIME
Unit: Seconds
Valid groupings and filters: Queue, Channel, Routing Profile, Agent, Agent Hierarchy, contact/segmentAttributes/connect:Subtype, Q in Connect
UI name: [Average agent interaction and customer hold time](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#average-agent-interaction-and-customer-hold-time)
AVG\_INTERACTION\_TIME
Unit: Seconds
Valid metric filter key: `INITIATION_METHOD`
Valid groupings and filters: Queue, Channel, Routing Profile, Feature, contact/segmentAttributes/connect:Subtype, Q in Connect
UI name: [Average agent interaction time](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#average-agent-interaction-time)
Feature is a valid filter but not a valid grouping.
AVG\_INTERRUPTIONS\_AGENT
This metric is available only for contacts analyzed by Contact Lens conversational analytics.
Unit: Count
Valid groupings and filters: Queue, Channel, Routing Profile, Agent, Agent Hierarchy, contact/segmentAttributes/connect:Subtype, Q in Connect
UI name: [Average agent interruptions](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#average-agent-interruptions)
AVG\_INTERRUPTION\_TIME\_AGENT
This metric is available only for contacts analyzed by Contact Lens conversational analytics.
Unit: Seconds
Valid groupings and filters: Queue, Channel, Routing Profile, Agent, Agent Hierarchy, contact/segmentAttributes/connect:Subtype, Q in Connect
UI name: [Average agent interruption time](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#average-agent-interruption-time)
AVG\_MESSAGE\_LENGTH\_AGENT
Unit: Count
Valid groupings and filters: Agent, Agent Hierarchy, Channel, contact/segmentAttributes/connect:Subtype, Disconnect Reason, Feature, RoutingStepExpression, Initiation method, Routing Profile, Queue, Q in Connect
UI name: [Average agent message length](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#average-agent-message-length)
AVG\_MESSAGE\_LENGTH\_CUSTOMER
Unit: Count
Valid groupings and filters: Agent, Agent Hierarchy, Channel, contact/segmentAttributes/connect:Subtype, Disconnect Reason, Feature, RoutingStepExpression, Initiation method, Routing Profile, Queue, Q in Connect
UI name: [Average customer message length](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#average-customer-message-length)
AVG\_MESSAGES
Unit: Count
Valid groupings and filters: Agent, Agent Hierarchy, Channel, contact/segmentAttributes/connect:Subtype, Disconnect Reason, Feature, RoutingStepExpression, Initiation method, Routing Profile, Queue, Q in Connect
UI name: [Average messages](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#average-messages)
AVG\_MESSAGES\_AGENT
Unit: Count
Valid groupings and filters: Agent, Agent Hierarchy, Channel, contact/segmentAttributes/connect:Subtype, Disconnect Reason, Feature, RoutingStepExpression, Initiation method, Routing Profile, Queue, Q in Connect
UI name: [Average agent messages](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#average-agent-messages)
AVG\_MESSAGES\_BOT
Unit: Count
Valid groupings and filters: Agent, Agent Hierarchy, Channel, contact/segmentAttributes/connect:Subtype, Disconnect Reason, Feature, RoutingStepExpression, Initiation method, Routing Profile, Queue, Q in Connect
UI name: [Average bot messages](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#average-bot-messages)
AVG\_MESSAGES\_CUSTOMER
Unit: Count
Valid groupings and filters: Agent, Agent Hierarchy, Channel, contact/segmentAttributes/connect:Subtype, Disconnect Reason, Feature, RoutingStepExpression, Initiation method, Routing Profile, Queue, Q in Connect
UI name: [Average customer messages](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#average-customer-messages)
AVG\_NON\_TALK\_TIME
This metric is available only for contacts analyzed by Contact Lens conversational analytics.
Unit: Seconds
Valid groupings and filters: Queue, Channel, Routing Profile, Agent, Agent Hierarchy, contact/segmentAttributes/connect:Subtype, Q in Connect
UI name: [Average non-talk time](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#average-non-talk-time)
AVG\_QUEUE\_ANSWER\_TIME
Unit: Seconds
Valid groupings and filters: Queue, Channel, Routing Profile, Feature, contact/segmentAttributes/connect:Subtype, Q in Connect
UI name: [Average queue answer time](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#average-queue-answer-time)
Valid metric level filters: `INITIATION_METHOD`, `FEATURE`, `DISCONNECT_REASON`
Feature is a valid filter but not a valid grouping.
AVG\_QUEUE\_ANSWER\_TIME\_CUSTOMER\_FIRST\_CALLBACK
Unit: Seconds
Valid groupings and filters: Queue, Channel, Routing Profile, Agent, Feature, contact/segmentAttributes/connect:Subtype, Q in Connect, Agent Hierarchy
UI name: [Avg. queue answer time - customer first callback](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#average-queue-answer-time-customer-first-callback)
AVG\_RESPONSE\_TIME\_AGENT
Unit: Seconds
Valid groupings and filters: Agent, Agent Hierarchy, Channel, contact/segmentAttributes/connect:Subtype, Disconnect Reason, Feature, RoutingStepExpression, Initiation method, Routing Profile, Queue, Q in Connect
UI name: [Average agent response time](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#average-response-time-agent)
AVG\_RESPONSE\_TIME\_CUSTOMER
Unit: Seconds
Valid groupings and filters: Agent, Agent Hierarchy, Channel, contact/segmentAttributes/connect:Subtype, Disconnect Reason, Feature, RoutingStepExpression, Initiation method, Routing Profile, Queue, Q in Connect
UI name: [Average customer response time](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#average-customer-time-agent)
AVG\_RESOLUTION\_TIME
Unit: Seconds
Valid groupings and filters: Queue, Channel, Routing Profile, contact/segmentAttributes/connect:Subtype, Q in Connect
UI name: [Average resolution time](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#average-resolution-time)
AVG\_TALK\_TIME
This metric is available only for contacts analyzed by Contact Lens conversational analytics.
Unit: Seconds
Valid groupings and filters: Queue, Channel, Routing Profile, Agent, Agent Hierarchy, contact/segmentAttributes/connect:Subtype, Q in Connect
UI name: [Average talk time](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#average-talk-time)
AVG\_TALK\_TIME\_AGENT
This metric is available only for contacts analyzed by Contact Lens conversational analytics.
Unit: Seconds
Valid groupings and filters: Queue, Channel, Routing Profile, Agent, Agent Hierarchy, contact/segmentAttributes/connect:Subtype, Q in Connect
UI name: [Average agent talk time](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#average-agent-talk-time)
AVG\_TALK\_TIME\_CUSTOMER
This metric is available only for contacts analyzed by Contact Lens conversational analytics.
Unit: Seconds
Valid groupings and filters: Queue, Channel, Routing Profile, Agent, Agent Hierarchy, contact/segmentAttributes/connect:Subtype, Q in Connect
UI name: [Average customer talk time](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#average-customer-talk-time)
AVG\_WAIT\_TIME\_AFTER\_CUSTOMER\_CONNECTION
This metric is available only for outbound campaigns that use the agent assisted voice and automated voice delivery modes.
Unit: Seconds
Valid groupings and filters: Campaign
UI name: [Average wait time after customer connection](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#average-wait-time-after-customer-connection)
AVG\_WAIT\_TIME\_AFTER\_CUSTOMER\_FIRST\_CALLBACK\_CONNECTION
Unit: Seconds
Valid groupings and filters: Queue, Channel, Routing Profile, Agent, Feature, contact/segmentAttributes/connect:Subtype, Q in Connect, Agent Hierarchy
UI name: [Avg. wait time after customer connection - customer first callback](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#average-wait-time-after-customer-connection-customer-first-callback)
AVG\_WEIGHTED\_EVALUATION\_SCORE
Unit: Percent
Valid groupings and filters: Agent, Agent Hierarchy, Channel, Evaluation Form Id, Evaluation Section ID, Evaluation Question ID, Evaluation Source, Form Version, Queue, Routing Profile
UI name: [Average weighted evaluation score](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#average-weighted-evaluation-score)
BOT\_CONVERSATIONS\_COMPLETED
Unit: Count
Valid groupings and filters: Channel, contact/segmentAttributes/connect:Subtype, Bot ID, Bot alias, Bot version, Bot locale, Flows resource ID, Flows module resource ID, Flow type, Flow action ID, Invoking resource published timestamp, Initiation method, Invoking resource type, Parent flows resource ID
UI name: [Bot conversations completed](https://docs.aws.amazon.com/connect/latest/adminguide/bot-metrics.html#bot-conversations-completed)
BOT\_INTENTS\_COMPLETED
Unit: Count
Valid groupings and filters: Channel, contact/segmentAttributes/connect:Subtype, Bot ID, Bot alias, Bot version, Bot locale, Bot intent name, Flows resource ID, Flows module resource ID, Flow type, Flow action ID, Invoking resource published timestamp, Initiation method, Invoking resource type, Parent flows resource ID
UI name: [Bot intents completed](https://docs.aws.amazon.com/connect/latest/adminguide/bot-metrics.html#bot-intents-completed)
CAMPAIGN\_CONTACTS\_ABANDONED\_AFTER\_X
This metric is available only for outbound campaigns using the agent assisted voice and automated voice delivery modes.
Unit: Count
Valid groupings and filters: Agent, Campaign
Threshold: For `ThresholdValue`, enter any whole number from 1 to 604800 (inclusive), in seconds. For `Comparison`, you must enter `GT` (for *Greater than*).
UI name: [Campaign contacts abandoned after X](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#campaign-contacts-abandoned-after-x)
CAMPAIGN\_CONTACTS\_ABANDONED\_AFTER\_X\_RATE
This metric is available only for outbound campaigns using the agent assisted voice and automated voice delivery modes.
Unit: Percent
Valid groupings and filters: Agent, Campaign
Threshold: For `ThresholdValue`, enter any whole number from 1 to 604800 (inclusive), in seconds. For `Comparison`, you must enter `GT` (for *Greater than*).
UI name: [Campaign contacts abandoned after X rate](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#campaign-contacts-abandoned-after-x-rate)
CAMPAIGN\_INTERACTIONS
This metric is available only for outbound campaigns using the email, WhatsApp, and web notification delivery modes.
Unit: Count
Valid metric filter key: CAMPAIGN\_INTERACTION\_EVENT\_TYPE
Valid groupings and filters: Browser Name, Campaign, Channel, contact/segmentAttributes/connect:Subtype, Device Model, Device Type, Web Notification Type
UI name: [Campaign interactions](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#campaign-interactions)
CAMPAIGN\_PROGRESS\_RATE
This metric is only available for outbound campaigns initiated using a customer segment. It is not available for event triggered campaigns.
Unit: Percent
Valid groupings and filters: Campaign, Campaign Execution Timestamp
UI name: [Campaign progress rate](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#campaign-progress-rate)
CAMPAIGN\_SEND\_ATTEMPTS
This metric is available only for outbound campaigns.
Unit: Count
Valid groupings and filters: Campaign, Channel, contact/segmentAttributes/connect:Subtype
UI name: [Campaign send attempts](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#campaign-send-attempts)
CAMPAIGN\_SEND\_EXCLUSIONS
This metric is available only for outbound campaigns.
Valid metric filter key: CAMPAIGN\_EXCLUDED\_EVENT\_TYPE
Unit: Count
Valid groupings and filters: Campaign, Campaign Excluded Event Type, Campaign Execution Timestamp
UI name: [Campaign send exclusions](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#campaign-send-exclusions)
CASES\_CREATED
Unit: Count
Required filter key: CASE\_TEMPLATE\_ARN
Valid groupings and filters: CASE\_TEMPLATE\_ARN, CASE\_STATUS
UI name: [Cases created](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#cases-created)
CONTACTS\_CREATED
Unit: Count
Valid metric filter key: `INITIATION_METHOD`
Valid groupings and filters: Queue, Channel, Routing Profile, Feature, contact/segmentAttributes/connect:Subtype, Q in Connect
UI name: [Contacts created](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#contacts-created)
Feature is a valid filter but not a valid grouping.
CONTACTS\_HANDLED
Unit: Count
Valid metric filter key: `INITIATION_METHOD`, `DISCONNECT_REASON`
Valid groupings and filters: Queue, Channel, Routing Profile, Agent, Agent Hierarchy, Feature, contact/segmentAttributes/connect:Subtype, RoutingStepExpression, Q in Connect
UI name: [Contacts handled](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#contacts-handled)
Feature is a valid filter but not a valid grouping.
CONTACTS\_HANDLED\_BY\_CONNECTED\_TO\_AGENT
Unit: Count
Valid metric filter key: `INITIATION_METHOD`
Valid groupings and filters: Queue, Channel, Agent, Agent Hierarchy, contact/segmentAttributes/connect:Subtype, Q in Connect
UI name: [Contacts handled (connected to agent timestamp)](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#contacts-handled-by-connected-to-agent-timestamp)
CONTACTS\_HOLD\_ABANDONS
Unit: Count
Valid groupings and filters: Queue, Channel, Routing Profile, Agent, Agent Hierarchy, contact/segmentAttributes/connect:Subtype, Q in Connect
UI name: [Contacts hold disconnect](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#contacts-hold-disconnect)
CONTACTS\_ON\_HOLD\_AGENT\_DISCONNECT
Unit: Count
Valid groupings and filters: Queue, Channel, Routing Profile, Agent, Agent Hierarchy, Q in Connect
UI name: [Contacts hold agent disconnect](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#contacts-hold-agent-disconnect)
CONTACTS\_ON\_HOLD\_CUSTOMER\_DISCONNECT
Unit: Count
Valid groupings and filters: Queue, Channel, Routing Profile, Agent, Agent Hierarchy, Q in Connect
UI name: [Contacts hold customer disconnect](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#contacts-hold-customer-disconnect)
CONTACTS\_PUT\_ON\_HOLD
Unit: Count
Valid groupings and filters: Queue, Channel, Routing Profile, Agent, Agent Hierarchy, Q in Connect
UI name: [Contacts put on hold](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#contacts-put-on-hold)
CONTACTS\_TRANSFERRED\_OUT\_EXTERNAL
Unit: Count
Valid groupings and filters: Queue, Channel, Routing Profile, Agent, Agent Hierarchy, Q in Connect
UI name: [Contacts transferred out external](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#contacts-transferred-out-external)
CONTACTS\_TRANSFERRED\_OUT\_INTERNAL
Unit: Percent
Valid groupings and filters: Queue, Channel, Routing Profile, Agent, Agent Hierarchy, Q in Connect
UI name: [Contacts transferred out internal](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#contacts-transferred-out-internal)
CONTACTS\_QUEUED
Unit: Count
Valid groupings and filters: Queue, Channel, Routing Profile, Agent, Agent Hierarchy, contact/segmentAttributes/connect:Subtype, Q in Connect
UI name: [Contacts queued](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#contacts-queued)
CONTACTS\_QUEUED\_BY\_ENQUEUE
Unit: Count
Valid groupings and filters: Queue, Channel, Agent, Agent Hierarchy, contact/segmentAttributes/connect:Subtype
UI name: [Contacts queued (enqueue timestamp)](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#contacts-queued-by-enqueue)
CONTACTS\_REMOVED\_FROM\_QUEUE\_IN\_X
Unit: Count
Valid groupings and filters: Queue, Channel, Routing Profile, Q in Connect
Threshold: For `ThresholdValue`, enter any whole number from 1 to 604800 (inclusive), in seconds. For `Comparison`, you can use `LT` (for "Less than") or `LTE` (for "Less than equal").
UI name: [Contacts removed from queue in X seconds](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#contacts-removed-from-queue)
CONTACTS\_RESOLVED\_IN\_X
Unit: Count
Valid groupings and filters: Queue, Channel, Routing Profile, contact/segmentAttributes/connect:Subtype, Q in Connect
Threshold: For `ThresholdValue`, enter any whole number from 1 to 604800 (inclusive), in seconds. For `Comparison`, you can use `LT` (for "Less than") or `LTE` (for "Less than equal").
UI name: [Contacts resolved in X](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#contacts-resolved)
CONTACTS\_TRANSFERRED\_OUT
Unit: Count
Valid groupings and filters: Queue, Channel, Routing Profile, Agent, Agent Hierarchy, Feature, contact/segmentAttributes/connect:Subtype, Q in Connect
UI name: [Contacts transferred out](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#contacts-transferred-out)
Feature is a valid filter but not a valid grouping.
CONTACTS\_TRANSFERRED\_OUT\_BY\_AGENT
Unit: Count
Valid groupings and filters: Queue, Channel, Routing Profile, Agent, Agent Hierarchy, contact/segmentAttributes/connect:Subtype, Q in Connect
UI name: [Contacts transferred out by agent](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#contacts-transferred-out-by-agent)
CONTACTS\_TRANSFERRED\_OUT\_FROM\_QUEUE
Unit: Count
Valid groupings and filters: Queue, Channel, Routing Profile, Agent, Agent Hierarchy, contact/segmentAttributes/connect:Subtype, Q in Connect
UI name: [Contacts transferred out queue](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#contacts-transferred-out-queue)
CURRENT\_CASES
Unit: Count
Required filter key: CASE\_TEMPLATE\_ARN
Valid groupings and filters: CASE\_TEMPLATE\_ARN, CASE\_STATUS
UI name: [Current cases](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#current-cases)
CONVERSATIONS\_ABANDONED
Unit: Count
Valid groupings and filters: Agent, Agent Hierarchy, Channel, contact/segmentAttributes/connect:Subtype, Disconnect Reason, Feature, RoutingStepExpression, Initiation method, Routing Profile, Queue, Q in Connect
UI name: [Conversations abandoned](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#conversations-abandoned)
DELIVERY\_ATTEMPTS
This metric is available only for outbound campaigns.
Unit: Count
Valid metric filter key: `ANSWERING_MACHINE_DETECTION_STATUS`, `CAMPAIGN_DELIVERY_EVENT_TYPE`, `DISCONNECT_REASON`
Valid groupings and filters: Agent, Answering Machine Detection Status, Browser Name, Campaign, Campaign Delivery EventType, Channel, contact/segmentAttributes/connect:Subtype, Device Model, Device Type, Disconnect Reason, Queue, Routing Profile, Web Notification Type
UI name: [Delivery attempts](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#delivery-attempts)
Campaign Delivery EventType filter and grouping are only available for SMS, Email, WhatsApp, and web notification campaign delivery modes. Agent, Queue, Routing Profile, Answering Machine Detection Status and Disconnect Reason are only available for agent assisted voice and automated voice delivery modes.
DELIVERY\_ATTEMPT\_DISPOSITION\_RATE
This metric is available only for outbound campaigns. Dispositions for the agent assisted voice and automated voice delivery modes are only available with answering machine detection enabled.
Unit: Percent
Valid metric filter key: `ANSWERING_MACHINE_DETECTION_STATUS`, `CAMPAIGN_DELIVERY_EVENT_TYPE`, `DISCONNECT_REASON`
Valid groupings and filters: Agent, Answering Machine Detection Status, Browser Name, Campaign, Channel, contact/segmentAttributes/connect:Subtype, Device Model, Device Type, Disconnect Reason, Queue, Routing Profile, Web Notification Type
UI name: [Delivery attempt disposition rate](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#delivery-attempt-disposition-rate)
Campaign Delivery Event Type filter and grouping are only available for SMS, Email, WhatsApp, and web notification campaign delivery modes. Agent, Queue, Routing Profile, Answering Machine Detection Status and Disconnect Reason are only available for agent assisted voice and automated voice delivery modes.
EVALUATIONS\_PERFORMED
Unit: Count
Valid groupings and filters: Agent, Agent Hierarchy, Channel, Evaluation Form ID, Evaluation Source, Form Version, Queue, Routing Profile
UI name: [Evaluations performed](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#evaluations-performed)
FLOWS\_OUTCOME
Unit: Count
Valid groupings and filters: Channel, contact/segmentAttributes/connect:Subtype, Flow type, Flows module resource ID, Flows next resource ID, Flows next resource queue ID, Flows outcome type, Flows resource ID, Initiation method, Resource published timestamp
UI name: [Flows outcome](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#flows-outcome)
FLOWS\_STARTED
Unit: Count
Valid groupings and filters: Channel, contact/segmentAttributes/connect:Subtype, Flow type, Flows module resource ID, Flows resource ID, Initiation method, Resource published timestamp
UI name: [Flows started](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#flows-started)
HUMAN\_ANSWERED\_CALLS
This metric is available only for outbound campaigns. Dispositions for the agent assisted voice and automated voice delivery modes are only available with answering machine detection enabled.
Unit: Count
Valid groupings and filters: Agent, Campaign
UI name: [Human answered](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#human-answered)
MAX\_FLOW\_TIME
Unit: Seconds
Valid groupings and filters: Channel, contact/segmentAttributes/connect:Subtype, Flow type, Flows module resource ID, Flows next resource ID, Flows next resource queue ID, Flows outcome type, Flows resource ID, Initiation method, Resource published timestamp
UI name: [Maximum flow time](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#maximum-flow-time)
MAX\_QUEUED\_TIME
Unit: Seconds
Valid groupings and filters: Queue, Channel, Routing Profile, Agent, Agent Hierarchy, contact/segmentAttributes/connect:Subtype, Q in Connect
UI name: [Maximum queued time](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#maximum-queued-time)
MIN\_FLOW\_TIME
Unit: Seconds
Valid groupings and filters: Channel, contact/segmentAttributes/connect:Subtype, Flow type, Flows module resource ID, Flows next resource ID, Flows next resource queue ID, Flows outcome type, Flows resource ID, Initiation method, Resource published timestamp
UI name: [Minimum flow time](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#minimum-flow-time)
PERCENT\_AUTOMATIC\_FAILS
Unit: Percent
Valid groupings and filters: Agent, Agent Hierarchy, Channel, Evaluation Form ID, Evaluation Source, Form Version, Queue, Routing Profile
UI name: [Automatic fails percent](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#automatic-fails-percent)
PERCENT\_BOT\_CONVERSATIONS\_OUTCOME
Unit: Percent
Valid groupings and filters: Channel, contact/segmentAttributes/connect:Subtype, Bot ID, Bot alias, Bot version, Bot locale, Flows resource ID, Flows module resource ID, Flow type, Flow action ID, Invoking resource published timestamp, Initiation method, Invoking resource type, Parent flows resource ID
UI name: [Percent bot conversations outcome](https://docs.aws.amazon.com/connect/latest/adminguide/bot-metrics.html#percent-bot-conversations-outcome)
PERCENT\_BOT\_INTENTS\_OUTCOME
Unit: Percent
Valid groupings and filters: Channel, contact/segmentAttributes/connect:Subtype, Bot ID, Bot alias, Bot version, Bot locale, Bot intent name, Flows resource ID, Flows module resource ID, Flow type, Flow action ID, Invoking resource published timestamp, Initiation method, Invoking resource type, Parent flows resource ID
UI name: [Percent bot intents outcome](https://docs.aws.amazon.com/connect/latest/adminguide/bot-metrics.html#percent-bot-intents-outcome)
PERCENT\_CASES\_FIRST\_CONTACT\_RESOLVED
Unit: Percent
Required filter key: CASE\_TEMPLATE\_ARN
Valid groupings and filters: CASE\_TEMPLATE\_ARN, CASE\_STATUS
UI name: [Cases resolved on first contact](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#cases-resolved-on-first-contact)
PERCENT\_CONTACTS\_STEP\_EXPIRED
Unit: Percent
Valid groupings and filters: Queue, RoutingStepExpression
UI name: This metric is available in Real-time Metrics UI but not on the Historical Metrics UI.
PERCENT\_CONTACTS\_STEP\_JOINED
Unit: Percent
Valid groupings and filters: Queue, RoutingStepExpression
UI name: This metric is available in Real-time Metrics UI but not on the Historical Metrics UI.
PERCENT\_FLOWS\_OUTCOME
Unit: Percent
Valid metric filter key: `FLOWS_OUTCOME_TYPE`
Valid groupings and filters: Channel, contact/segmentAttributes/connect:Subtype, Flow type, Flows module resource ID, Flows next resource ID, Flows next resource queue ID, Flows outcome type, Flows resource ID, Initiation method, Resource published timestamp
UI name: [Flows outcome percentage](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#flows-outcome-percentage).
The `FLOWS_OUTCOME_TYPE` is not a valid grouping.
PERCENT\_NON\_TALK\_TIME
This metric is available only for contacts analyzed by Contact Lens conversational analytics.
Unit: Percentage
Valid groupings and filters: Queue, Channel, Routing Profile, Agent, Agent Hierarchy, contact/segmentAttributes/connect:Subtype, Q in Connect
UI name: [Non-talk time percent](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#non-talk-time-percent)
PERCENT\_TALK\_TIME
This metric is available only for contacts analyzed by Contact Lens conversational analytics.
Unit: Percentage
Valid groupings and filters: Queue, Channel, Routing Profile, Agent, Agent Hierarchy, contact/segmentAttributes/connect:Subtype, Q in Connect
UI name: [Talk time percent](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#talk-time-percent)
PERCENT\_TALK\_TIME\_AGENT
This metric is available only for contacts analyzed by Contact Lens conversational analytics.
Unit: Percentage
Valid groupings and filters: Queue, Channel, Routing Profile, Agent, Agent Hierarchy, contact/segmentAttributes/connect:Subtype, Q in Connect
UI name: [Agent talk time percent](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#agent-talk-time-percent)
PERCENT\_TALK\_TIME\_CUSTOMER
This metric is available only for contacts analyzed by Contact Lens conversational analytics.
Unit: Percentage
Valid groupings and filters: Queue, Channel, Routing Profile, Agent, Agent Hierarchy, contact/segmentAttributes/connect:Subtype, Q in Connect
UI name: [Customer talk time percent](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#customer-talk-time-percent)
RECIPIENTS\_ATTEMPTED
This metric is only available for outbound campaigns initiated using a customer segment. It is not available for event triggered campaigns.
Unit: Count
Valid groupings and filters: Campaign, Campaign Execution Timestamp
UI name: [Recipients attempted](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#recipients-attempted)
RECIPIENTS\_INTERACTED
This metric is only available for outbound campaigns initiated using a customer segment. It is not available for event triggered campaigns.
Valid metric filter key: CAMPAIGN\_INTERACTION\_EVENT\_TYPE
Unit: Count
Valid groupings and filters: Campaign, Channel, contact/segmentAttributes/connect:Subtype, Campaign Execution Timestamp
UI name: [Recipients interacted](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#recipients-interacted)
RECIPIENTS\_TARGETED
This metric is only available for outbound campaigns initiated using a customer segment. It is not available for event triggered campaigns.
Unit: Count
Valid groupings and filters: Campaign, Campaign Execution Timestamp
UI name: [Recipients targeted](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#recipients-targeted)
REOPENED\_CASE\_ACTIONS
Unit: Count
Required filter key: CASE\_TEMPLATE\_ARN
Valid groupings and filters: CASE\_TEMPLATE\_ARN, CASE\_STATUS
UI name: [Cases reopened](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#cases-reopened)
RESOLVED\_CASE\_ACTIONS
Unit: Count
Required filter key: CASE\_TEMPLATE\_ARN
Valid groupings and filters: CASE\_TEMPLATE\_ARN, CASE\_STATUS
UI name: [Cases resolved](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#cases-resolved)
SERVICE\_LEVEL
You can include up to 20 SERVICE\_LEVEL metrics in a request.
Unit: Percent
Valid groupings and filters: Queue, Channel, Routing Profile, Q in Connect
Threshold: For `ThresholdValue`, enter any whole number from 1 to 604800 (inclusive), in seconds. For `Comparison`, you can use `LT` (for "Less than") or `LTE` (for "Less than equal").
UI name: [Service level X](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#service-level)
STEP\_CONTACTS\_QUEUED
Unit: Count
Valid groupings and filters: Queue, RoutingStepExpression
UI name: This metric is available in Real-time Metrics UI but not on the Historical Metrics UI.
SUM\_AFTER\_CONTACT\_WORK\_TIME
Unit: Seconds
Valid groupings and filters: Queue, Channel, Routing Profile, Agent, Agent Hierarchy, Q in Connect
UI name: [After contact work time](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#after-contact-work-time)
SUM\_CONNECTING\_TIME\_AGENT
Unit: Seconds
Valid metric filter key: `INITIATION_METHOD`. This metric only supports the following filter keys as `INITIATION_METHOD`: `INBOUND` \| `OUTBOUND` \| `CALLBACK` \| `API` \| `CALLBACK_CUSTOMER_FIRST_DIALED`
Valid groupings and filters: Queue, Channel, Routing Profile, Agent, Agent Hierarchy
UI name: [Agent API connecting time](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#agent-api-connecting-time)
The `Negate` key in metric-level filters is not applicable for this metric.
CONTACTS\_ABANDONED
Unit: Count
Metric filter:
+ Valid values: `API`\| `INCOMING` \| `OUTBOUND` \| `TRANSFER` \| `CALLBACK` \| `QUEUE_TRANSFER`\| `Disconnect` \| `CALLBACK_CUSTOMER_FIRST_DIALED`
Valid groupings and filters: Queue, Channel, Routing Profile, Agent, Agent Hierarchy, contact/segmentAttributes/connect:Subtype, RoutingStepExpression, Q in Connect
UI name: [Contact abandoned](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#contacts-abandoned)
SUM\_CONTACTS\_ABANDONED\_IN\_X
Unit: Count
Valid groupings and filters: Queue, Channel, Routing Profile, contact/segmentAttributes/connect:Subtype, Q in Connect
Threshold: For `ThresholdValue`, enter any whole number from 1 to 604800 (inclusive), in seconds. For `Comparison`, you can use `LT` (for "Less than") or `LTE` (for "Less than equal").
UI name: [Contacts abandoned in X seconds](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#contacts-abandoned-in-x-seconds)
SUM\_CONTACTS\_ANSWERED\_IN\_X
Unit: Count
Valid groupings and filters: Queue, Channel, Routing Profile, contact/segmentAttributes/connect:Subtype, Q in Connect
Threshold: For `ThresholdValue`, enter any whole number from 1 to 604800 (inclusive), in seconds. For `Comparison`, you can use `LT` (for "Less than") or `LTE` (for "Less than equal").
UI name: [Contacts answered in X seconds](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#contacts-answered-in-x-seconds)
SUM\_CONTACT\_FLOW\_TIME
Unit: Seconds
Valid groupings and filters: Queue, Channel, Routing Profile, Agent, Agent Hierarchy, Q in Connect
UI name: [Contact flow time](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#contact-flow-time)
SUM\_CONTACT\_TIME\_AGENT
Unit: Seconds
Valid groupings and filters: Routing Profile, Agent, Agent Hierarchy
UI name: [Agent on contact time](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#agent-on-contact-time)
SUM\_CONTACTS\_DISCONNECTED
Valid metric filter key: `DISCONNECT_REASON`
Unit: Count
Valid groupings and filters: Queue, Channel, Routing Profile, Agent, Agent Hierarchy, contact/segmentAttributes/connect:Subtype, Q in Connect
UI name: [Contact disconnected](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#contact-disconnected)
SUM\_ERROR\_STATUS\_TIME\_AGENT
Unit: Seconds
Valid groupings and filters: Routing Profile, Agent, Agent Hierarchy
UI name: [Error status time](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#error-status-time)
SUM\_HANDLE\_TIME
Unit: Seconds
Valid groupings and filters: Queue, Channel, Routing Profile, Agent, Agent Hierarchy, Q in Connect
UI name: [Contact handle time](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#contact-handle-time)
SUM\_HOLD\_TIME
Unit: Count
Valid groupings and filters: Queue, Channel, Routing Profile, Agent, Agent Hierarchy, Q in Connect
UI name: [Customer hold time](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#customer-hold-time)
SUM\_IDLE\_TIME\_AGENT
Unit: Seconds
Valid groupings and filters: Routing Profile, Agent, Agent Hierarchy
UI name: [Agent idle time](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#agent-idle-time)
SUM\_INTERACTION\_AND\_HOLD\_TIME
Unit: Seconds
Valid groupings and filters: Queue, Channel, Routing Profile, Agent, Agent Hierarchy, Q in Connect
UI name: [Agent interaction and hold time](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#agent-interaction-and-hold-time)
SUM\_INTERACTION\_TIME
Unit: Seconds
Valid groupings and filters: Queue, Channel, Routing Profile, Agent, Agent Hierarchy
UI name: [Agent interaction time](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#agent-interaction-time)
SUM\_NON\_PRODUCTIVE\_TIME\_AGENT
Unit: Seconds
Valid groupings and filters: Routing Profile, Agent, Agent Hierarchy
UI name: [Agent non-productive time](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#agent-non-productive-time)
SUM\_ONLINE\_TIME\_AGENT
Unit: Seconds
Valid groupings and filters: Routing Profile, Agent, Agent Hierarchy
UI name: [Online time](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#online-time)
SUM\_RETRY\_CALLBACK\_ATTEMPTS
Unit: Count
Valid groupings and filters: Queue, Channel, Routing Profile, contact/segmentAttributes/connect:Subtype, Q in Connect
UI name: [Callback attempts](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#callback-attempts)
Type: Array of [MetricV2](API_MetricV2.md) objects
Required: Yes

 ** [NextToken](#API_GetMetricDataV2_RequestSyntax) **   <a name="connect-GetMetricDataV2-request-NextToken"></a>
The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2500.
Required: No

 ** [ResourceArn](#API_GetMetricDataV2_RequestSyntax) **   <a name="connect-GetMetricDataV2-request-ResourceArn"></a>
The Amazon Resource Name (ARN) of the resource. This includes the `instanceId` an Connect Customer instance.
Type: String
Required: Yes

 ** [StartTime](#API_GetMetricDataV2_RequestSyntax) **   <a name="connect-GetMetricDataV2-request-StartTime"></a>
The timestamp, in UNIX Epoch time format, at which to start the reporting interval for the retrieval of historical metrics data. The time must be before the end time timestamp. The start and end time depends on the `IntervalPeriod` selected. By default the time range between start and end time is 35 days. Historical metrics are available for 3 months.
Type: Timestamp
Required: Yes

## Response Syntax
<a name="API_GetMetricDataV2_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "MetricResults": [
      {
         "Collections": [
            {
               "Metric": {
                  "MetricFilters": [
                     {
                        "MetricFilterKey": "string",
                        "MetricFilterValues": [ "string" ],
                        "Negate": boolean
                     }
                  ],
                  "MetricId": "string",
                  "Name": "string",
                  "Threshold": [
                     {
                        "Comparison": "string",
                        "ThresholdValue": number
                     }
                  ]
               },
               "Value": number
            }
         ],
         "Dimensions": {
            "string" : "string"
         },
         "MetricInterval": {
            "EndTime": number,
            "Interval": "string",
            "StartTime": number
         }
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_GetMetricDataV2_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [MetricResults](#API_GetMetricDataV2_ResponseSyntax) **   <a name="connect-GetMetricDataV2-response-MetricResults"></a>
Information about the metrics requested in the API request If no grouping is specified, a summary of metric data is returned.
Type: Array of [MetricResultV2](API_MetricResultV2.md) objects

 ** [NextToken](#API_GetMetricDataV2_ResponseSyntax) **   <a name="connect-GetMetricDataV2-response-NextToken"></a>
If there are additional results, this is the token for the next set of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2500.

## Errors
<a name="API_GetMetricDataV2_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServiceException **
Request processing failed because of an error or failure with the service.
 ** Message **
The message.
HTTP Status Code: 500

 ** InvalidParameterException **
One or more of the specified parameters are not valid.
 ** Message **
The message about the parameters.
HTTP Status Code: 400

 ** InvalidRequestException **
The request is not valid.
 ** Message **
The message about the request.
 ** Reason **
Reason why the request was invalid.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Message **
The message about the resource.
HTTP Status Code: 404

 ** ThrottlingException **
The throttling limit has been exceeded.
HTTP Status Code: 429

## See Also
<a name="API_GetMetricDataV2_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/GetMetricDataV2)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/GetMetricDataV2)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/GetMetricDataV2)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/GetMetricDataV2)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/GetMetricDataV2)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/GetMetricDataV2)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/GetMetricDataV2)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/GetMetricDataV2)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/GetMetricDataV2)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/GetMetricDataV2)
