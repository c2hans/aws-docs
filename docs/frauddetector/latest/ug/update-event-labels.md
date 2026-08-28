---
source_url: https://docs.aws.amazon.com/frauddetector/latest/ug/update-event-labels.html
---

Amazon Fraud Detector is no longer open to new customers as of November 7, 2025. For capabilities similar to Amazon Fraud Detector, explore Amazon SageMaker, AutoGluon, and AWS WAF.

# Updating event labels in event data stored in Amazon Fraud Detector
<a name="update-event-labels"></a>

You might need to add or update fraud labels for events that are already stored in Amazon Fraud Detector, such as when you perform an offline fraud investigation for an event and want to close the machine learning feed back loop. To update the label for an event that is already stored in Amazon Fraud Detector, use the `UpdateEventLabel` API operation. The following shows an example UpdateEventLabel API call.

```
import boto3
fraudDetector = boto3.client('frauddetector')

fraudDetector.update_event_label(
            eventId        = '802454d3-f7d8-482d-97e8-c4b6db9a0428',
            eventTypeName  = 'sample_registration',
            assignedLabel  = 'fraud',
            labelTimestamp = '2020-07-13T23:18:21Z'
)
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Fraud Detector. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query frauddetector` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
