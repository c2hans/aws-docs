---
source_url: https://docs.aws.amazon.com/elemental-live/latest/ug/multiple-overlays-and-layers.html
---

# Multiple overlays and layers
<a name="multiple-overlays-and-layers"></a>

You can set up the event to insert more than one static overlay. Overlays are stored in the event in a queue that has a maximum of 8 layers.

This means that you can display up to:
+ 8 static overlays if you are using only the web interface to set up the event.
+ As many static overlays as you want over the duration of the event if you are using the REST API. See [Step C: Manage overlays on a running event](step-c-manage-overlays-on-a-running-event.md). A maximum of 8 static overlays can be “queued” at one time (one in each layer).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Live. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-live` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
