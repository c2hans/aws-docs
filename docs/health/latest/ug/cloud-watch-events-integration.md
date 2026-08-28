---
source_url: https://docs.aws.amazon.com/health/latest/ug/cloud-watch-events-integration.html
---

# Configuring Amazon EventBridge
<a name="cloud-watch-events-integration"></a>

Use EventBridge to detect and react to changes for AWS Health events. You can monitor specific AWS Health events that occur in your account, and then set up rules so that AWS Health notifies you, or you take action, when events change.

**Use EventBridge with AWS Health**

1. Open your AWS Health Dashboard at [https://health.aws.amazon.com/health/home](https://health.aws.amazon.com/health/).

1. To navigate to the EventBridge console to create a rule, do one of the following:
   + From the navigation pane, under **Health Integrations**, choose **Amazon EventBridge**.
   + Under **Configure EventBridge**, choose **Go to EventBridge**.

1. Follow this procedure to create rules and monitor for events. See [Monitoring events in AWS Health with Amazon EventBridge](cloudwatch-events-health.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Health. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query health` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
