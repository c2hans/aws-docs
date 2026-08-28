---
source_url: https://docs.aws.amazon.com/acm/latest/userguide/configure-auto-renewals-events.html
---

# Configure automatic renewal events
<a name="configure-auto-renewals-events"></a>

With AWS Certificate Manager exportable public certificates and Amazon EventBridge, you can configure automatic certificate renewals events.

1. Set up an Amazon EventBridge event to monitor certificate renewals. For more information, see [Amazon EventBridge support for ACM](https://docs.aws.amazon.com/acm/latest/userguide/cloudwatch-events.html).

1. Create automation to handle certificate deployment when renewals occur. For more information, see [Initiating actions with Amazon EventBridge in ACM](example-actions.md).

1. Configure EventBridge events to alert you of any renewal or deployment failures.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Certificate Manager (ACM). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query acm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
