---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/event-clip-disable.html
---

# Disabling event clipping
<a name="event-clip-disable"></a>

You can disable event clipping in a channel.

On the **Create channel** or **Edit channel page**, choose **AWS Elemental Inference settings**. Choose the appropriate action:
+ To disable all Elemental Inference features, set the **State** field for Elemental Inference to **Disabled**.
+ To disable only the event clipping feature, set the **State** field in **Event clipping** to **Disabled**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
