---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/model-registry-staging-construct-event-bridge.html
---

# Get event notifications for ModelLifeCycle
<a name="model-registry-staging-construct-event-bridge"></a>

You can get the ModelLifeCycle update notifications and events with EventBridge in your account. The following is an example of an EventBridge rule, to be configured in your account, in order to get the ModelLifeCycle event notifications.

```
{
  "source": ["aws.sagemaker"],
  "detail-type": ["SageMaker Model Package State Change"]
}
```

For an example EventBridge payload you may receive, see [SageMaker model package state change](automating-sagemaker-with-eventbridge.md#eventbridge-model-package).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
