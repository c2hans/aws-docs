---
source_url: https://docs.aws.amazon.com/frauddetector/latest/ug/storing-events-geteventprediction-api.html
---

Amazon Fraud Detector is no longer open to new customers as of November 7, 2025. For capabilities similar to Amazon Fraud Detector, explore Amazon SageMaker, AutoGluon, and AWS WAF.

# Store event data using the GetEventPredictions API operation
<a name="storing-events-geteventprediction-api"></a>

By default, all events sent to the `GetEventPrediction` API for evaluation are stored in Amazon Fraud Detector. This means that Amazon Fraud Detector will automatically store event data when you generate a prediction and use that data to update calculated variables in near-real time. You can disable data storage by navigating to the event type in the Amazon Fraud Detector console and setting **Event ingestion** OFF or updating the EventIngestion value to DISABLED using the `PutEventType` API operation. For more information about the `GetEventPrediction` API operation, see [Fraud predictions](getting-fraud-predictions.md).

**Important**
We highly recommend that once you enable *Event ingestion* for an Event type, keep it enabled. Disabling the Event ingestion for the same Event type and then generating predictions might result in inconsistent behavior.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Fraud Detector. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query frauddetector` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
