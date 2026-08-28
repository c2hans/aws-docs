---
source_url: https://docs.aws.amazon.com/elemental-live/latest/ug/monitoring-activity-via-web.html
---

# Monitoring activity through the web interface
<a name="monitoring-activity-via-web"></a>

The operator can monitor dynamic playlist activity through the Elemental Live web interface.

1. On the web interface, display the Event Control tab.

1. If the blue button specifies Control Panel, then the Details panel is currently displayed. Click the Control Panel button.

1. On the Control Panel, click Input Controls (below the Preview panel) to expand that section. The dynamic playlist appears.

![GUI input controls.](http://docs.aws.amazon.com/elemental-live/latest/ug/images/playlist_GUI_input_controls.png)

## Status information
<a name="status-information"></a>

| Input background | Icon in control column | State |
| --- | --- | --- |
| Green | Spinner icon | Active |
| Green | Arrow icon | Prepared |
| Brown | Arrow icon | Being prepared |
| Gray | Arrow icon | Idle |

The orange numbers down the left side are on-screen numbers, for display purposes only.

The numbers in the ID column are the REST IDs of the inputs.

## Controls
<a name="controls"></a>

The operator can click the triangle to switch to that input. The input will become Active. Processing will stop on the current Active input.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Live. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-live` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
