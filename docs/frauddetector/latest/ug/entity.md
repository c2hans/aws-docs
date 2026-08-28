---
source_url: https://docs.aws.amazon.com/frauddetector/latest/ug/entity.html
---

Amazon Fraud Detector is no longer open to new customers as of November 7, 2025. For capabilities similar to Amazon Fraud Detector, explore Amazon SageMaker, AutoGluon, and AWS WAF.

# Entity
<a name="entity"></a>

An entity represents a person or thing that's performing the event. An entity type classifies the entity. Example classifications include customer, merchant, user, or account. You provide the entity type (ENTITY\_TYPE) and an entity identifier (ENTITY\_ID) as part of your event dataset to indicate the specific entity that performed the event.

Amazon Fraud Detector uses the entity type when generating fraud prediction for an event to indicate who performed the event. The entity type you want to use in your fraud predictions must first be created in Amazon Fraud Detector and then added to the event when creating your event type.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Fraud Detector. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query frauddetector` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
