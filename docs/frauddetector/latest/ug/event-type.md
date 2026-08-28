---
source_url: https://docs.aws.amazon.com/frauddetector/latest/ug/event-type.html
---

Amazon Fraud Detector is no longer open to new customers as of November 7, 2025. For capabilities similar to Amazon Fraud Detector, explore Amazon SageMaker, AutoGluon, and AWS WAF.

# Event type
<a name="event-type"></a>

With Amazon Fraud Detector you generate fraud predictions for events. An event type defines the structure for an individual event sent to Amazon Fraud Detector. Once defined, you can build models and detectors that evaluate the risk for specific event types.

The structure of an event includes the following:
+ Entity Type: Classifies who is performing the event. During prediction, specify the entity type and entity Id to define who performed the event.
+ Variables: Defines what variables can be sent as part of the event. Variables are used by models and rules to evaluate fraud risk. Once added, variables cannot be removed from an event type.
+ Labels: Classifies an event as fraudulent or legitimate. Used during model training. Once added, labels cannot be removed from an event type.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Fraud Detector. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query frauddetector` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
