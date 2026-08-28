---
source_url: https://docs.aws.amazon.com/connect/latest/adminguide/journey-flow-block-wait.html
---

# Wait
<a name="journey-flow-block-wait"></a>

## Description
<a name="journey-flow-block-wait-description"></a>
+ This block pauses the flow for the specified wait time or for the specified event.
+ For example, you want to send a SMS reminder after an initial introduction email. You can either set up a fixed duration (for example, 3 days) or Wait until specific time and date. The next activity block will execute after the wait time expires.

## How to configure this block
<a name="journey-flow-block-wait-configure"></a>

You can configure the **Wait** block in the admin website or using the Wait action.

### Common properties
<a name="journey-flow-block-wait-common-properties"></a>

| Property | Description |
| --- | --- |
| Set duration | Enter a fixed delay (for example, 3 hours or 2 days). |
| Wait until | Specify an exact date/time within 7 days. |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
