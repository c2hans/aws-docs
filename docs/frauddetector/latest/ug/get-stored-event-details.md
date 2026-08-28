---
source_url: https://docs.aws.amazon.com/frauddetector/latest/ug/get-stored-event-details.html
---

Amazon Fraud Detector is no longer open to new customers as of November 7, 2025. For capabilities similar to Amazon Fraud Detector, explore Amazon SageMaker, AutoGluon, and AWS WAF.

# Get details of a stored event data
<a name="get-stored-event-details"></a>

After you store event data in Amazon Fraud Detector, you can check the latest data that was stored for an event using the [GetEvent](https://docs.aws.amazon.com/frauddetector/latest/api/API_GetEvent.html) API. The following example code checks the latest data stored for the `sample_registration` event.

```
import boto3
fraudDetector = boto3.client('frauddetector')

fraudDetector.get_event(
            eventId        = '802454d3-f7d8-482d-97e8-c4b6db9a0428',
            eventTypeName  = 'sample_registration'
)
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Fraud Detector. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query frauddetector` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
