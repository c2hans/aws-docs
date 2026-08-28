---
source_url: https://docs.aws.amazon.com/frauddetector/latest/ug/disable-event-orchestration.html
---

Amazon Fraud Detector is no longer open to new customers as of November 7, 2025. For capabilities similar to Amazon Fraud Detector, explore Amazon SageMaker, AutoGluon, and AWS WAF.

# Disable event orchestration in Amazon Fraud Detector
<a name="disable-event-orchestration"></a>

You can disable event orchestration for an event anytime in the Amazon Fraud Detector console, using the `put-event-type` command, using the `PutEventType` API, or using the AWS SDK for Python (Boto3).

## Disable event orchestration in the Amazon Fraud Detector console
<a name="disable-event-orchestration-console"></a>

**To disable event orchestration**

1. Open the [AWS Management Console](https://console.aws.amazon.com) and sign in to your account. Navigate to Amazon Fraud Detector.

1. In the left navigation pane, choose **Events**.

1. In the **Events type** page, choose your event type.

1. Turn off **Enable event orchestration with Amazon EventBridge**.

## Disable event orchestration using the AWS SDK for Python (Boto3)
<a name="disable-event-orchestration-using-the-aws-python-sdk"></a>

The following example shows a sample request for updating an event type `sample_registration` to disable event orchestration using the `PutEventType` API.

```
import boto3
fraudDetector = boto3.client('frauddetector')
fraud_detector.put_event_type(
  name = 'sample_registration',
  eventVariables = ['ip_address', 'email_address'],
  eventOrchestration = {'eventBridgeEnabled': False},
  entityTypes = ['sample_customer'])
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Fraud Detector. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query frauddetector` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
