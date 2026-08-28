---
source_url: https://docs.aws.amazon.com/elemental-live/latest/ug/png-step-run-again.html
---

# Step D: Run the event again
<a name="png-step-run-again"></a>

You might want to run the same event again. If you do so, make sure that the motion overlay is set up correctly. You must do this because when you enter REST API commands to control the motion overlay when the event is running, the event XML for the motion overlay changes.

For example, you might set up the event with motion overlay A and a start time of 9:00 am. You then run the event and change the content and start time of the motion overlay several times. The last motion overlay to run in the event is motion overlay B with a start time of 4:00 pm. That is the information now in the event XML. Before you start the event the next day, review and modify the motion overlay information.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Live. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-live` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
