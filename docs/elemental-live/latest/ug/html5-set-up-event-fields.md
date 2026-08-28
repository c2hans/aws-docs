---
source_url: https://docs.aws.amazon.com/elemental-live/latest/ug/html5-set-up-event-fields.html
---

# Fields for an HTML5 asset
<a name="html5-set-up-event-fields"></a>

| Field on web interface | Tag in the XML | Type | Description |
| --- | --- | --- | --- |
| Insertion Mode | <insertion\_mode> | String | Choose HTML. |
| Input | <uri> | String |  |
| Username Password | <username><password> | String |  |
| Active | <active> | Boolean | Always select this box. |
| Enable REST Control | <enable\_rest> | Boolean | Select this field only if you chose to use the REST API to [control the asset](step-design-controls-html5.md). |
| Enable SCTE 35 Control | <enable\_scte35> | Boolean | Select this field only if you chose to use SCTE 35 messages in the source content to [control the asset](step-design-controls-html5.md). |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Live. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-live` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
