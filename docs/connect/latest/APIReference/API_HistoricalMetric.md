---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_HistoricalMetric.html
---

# HistoricalMetric
<a name="API_HistoricalMetric"></a>

Contains information about a historical metric.

## Contents
<a name="API_HistoricalMetric_Contents"></a>

 ** Name **   <a name="connect-Type-HistoricalMetric-Name"></a>
The name of the metric. Following is a list of each supported metric mapped to the UI name, linked to a detailed description in the *Connect Customer Administrator Guide*.
ABANDON\_TIME
Unit: SECONDS
Statistic: AVG
UI name: [Average queue abandon time](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#average-queue-abandon-time)
AFTER\_CONTACT\_WORK\_TIME
Unit: SECONDS
Statistic: AVG
UI name: [After contact work time](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#after-contact-work-time)
API\_CONTACTS\_HANDLED
Unit: COUNT
Statistic: SUM
UI name: [API contacts handled](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#api-contacts-handled)
AVG\_HOLD\_TIME
Unit: SECONDS
Statistic: AVG
UI name: [Average customer hold time](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#average-customer-hold-time)
CALLBACK\_CONTACTS\_HANDLED
Unit: COUNT
Statistic: SUM
UI name: [Callback contacts handled](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#callback-contacts-handled)
CONTACTS\_ABANDONED
Unit: COUNT
Statistic: SUM
UI name: [Contacts abandoned](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#contacts-abandoned)
CONTACTS\_AGENT\_HUNG\_UP\_FIRST
Unit: COUNT
Statistic: SUM
UI name: [Contacts agent hung up first](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#contacts-agent-hung-up-first)
CONTACTS\_CONSULTED
Unit: COUNT
Statistic: SUM
UI name: [Contacts consulted](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#contacts-consulted)
CONTACTS\_HANDLED
Unit: COUNT
Statistic: SUM
UI name: [Contacts handled](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#contacts-handled)
CONTACTS\_HANDLED\_INCOMING
Unit: COUNT
Statistic: SUM
UI name: [Contacts handled incoming](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#contacts-handled-incoming)
CONTACTS\_HANDLED\_OUTBOUND
Unit: COUNT
Statistic: SUM
UI name: [Contacts handled outbound](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#contacts-handled-outbound)
CONTACTS\_HOLD\_ABANDONS
Unit: COUNT
Statistic: SUM
UI name: [Contacts hold disconnect](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#contacts-hold-disconnect)
CONTACTS\_MISSED
Unit: COUNT
Statistic: SUM
UI name: [AGENT\_NON\_RESPONSE](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#agent-non-response)
CONTACTS\_QUEUED
Unit: COUNT
Statistic: SUM
UI name: [Contacts queued](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#contacts-queued)
CONTACTS\_TRANSFERRED\_IN
Unit: COUNT
Statistic: SUM
UI name: [Contacts transferred in](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#contacts-transferred-in)
CONTACTS\_TRANSFERRED\_IN\_FROM\_QUEUE
Unit: COUNT
Statistic: SUM
UI name: [Contacts transferred out queue](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#contacts-transferred-out-queue)
CONTACTS\_TRANSFERRED\_OUT
Unit: COUNT
Statistic: SUM
UI name: [Contacts transferred out](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#contacts-transferred-out)
CONTACTS\_TRANSFERRED\_OUT\_FROM\_QUEUE
Unit: COUNT
Statistic: SUM
UI name: [Contacts transferred out queue](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#contacts-transferred-out-queue)
HANDLE\_TIME
Unit: SECONDS
Statistic: AVG
UI name: [Average handle time](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#average-handle-time)
INTERACTION\_AND\_HOLD\_TIME
Unit: SECONDS
Statistic: AVG
UI name: [Average agent interaction and customer hold time](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#average-agent-interaction-and-customer-hold-time)
INTERACTION\_TIME
Unit: SECONDS
Statistic: AVG
UI name: [Average agent interaction time](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#aaverage-agent-interaction-time)
OCCUPANCY
Unit: PERCENT
Statistic: AVG
UI name: [Occupancy](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#occupancy)
QUEUE\_ANSWER\_TIME
Unit: SECONDS
Statistic: AVG
UI name: [Average queue answer time](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html##average-queue-answer-time)
QUEUED\_TIME
Unit: SECONDS
Statistic: MAX
UI name: [Minimum flow time](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#minimum-flow-time)
SERVICE\_LEVEL
You can include up to 20 SERVICE\_LEVEL metrics in a request.
Unit: PERCENT
Statistic: AVG
Threshold: For `ThresholdValue`, enter any whole number from 1 to 604800 (inclusive), in seconds. For `Comparison`, you must enter `LT` (for "Less than").
UI name: [Service level X](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#service-level)
Type: String
Valid Values: `CONTACTS_QUEUED | CONTACTS_HANDLED | CONTACTS_ABANDONED | CONTACTS_CONSULTED | CONTACTS_AGENT_HUNG_UP_FIRST | CONTACTS_HANDLED_INCOMING | CONTACTS_HANDLED_OUTBOUND | CONTACTS_HOLD_ABANDONS | CONTACTS_TRANSFERRED_IN | CONTACTS_TRANSFERRED_OUT | CONTACTS_TRANSFERRED_IN_FROM_QUEUE | CONTACTS_TRANSFERRED_OUT_FROM_QUEUE | CONTACTS_MISSED | CALLBACK_CONTACTS_HANDLED | API_CONTACTS_HANDLED | OCCUPANCY | HANDLE_TIME | AFTER_CONTACT_WORK_TIME | QUEUED_TIME | ABANDON_TIME | QUEUE_ANSWER_TIME | HOLD_TIME | INTERACTION_TIME | INTERACTION_AND_HOLD_TIME | SERVICE_LEVEL`
Required: No

 ** Statistic **   <a name="connect-Type-HistoricalMetric-Statistic"></a>
The statistic for the metric.
Type: String
Valid Values: `SUM | MAX | AVG`
Required: No

 ** Threshold **   <a name="connect-Type-HistoricalMetric-Threshold"></a>
The threshold for the metric, used with service level metrics.
Type: [Threshold](API_Threshold.md) object
Required: No

 ** Unit **   <a name="connect-Type-HistoricalMetric-Unit"></a>
The unit for the metric.
Type: String
Valid Values: `SECONDS | COUNT | PERCENT`
Required: No

## See Also
<a name="API_HistoricalMetric_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/HistoricalMetric)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/HistoricalMetric)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/HistoricalMetric)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
