---
source_url: https://docs.aws.amazon.com/elemental-live/latest/ug/static-overlay-creating-and-modifying-a-non-running-event.html
---

# Static overlay, creating and modifying a non-running event
<a name="static-overlay-creating-and-modifying-a-non-running-event"></a>

## Overlays at top level
<a name="overlays-at-top-level"></a>

|  |  |  |  |
| --- |--- |--- |--- |
| <image\_inserter> |   |   |   |
|   | enable\_rest |   |   |
|   | <insertable\_image> |   |   |
|   |   | duration |   |
|   |   | fade\_in |   |
|   |   | fade\_out |   |
|   |   | height |   |
|   |   | image\_x |   |
|   |   | image\_y |   |
|   |   | layer |   |
|   |   | opacity |   |
|   |   | start\_time |   |
|   |   | width |   |
|   |   | <image\_inserter\_input> |   |
|   |   |   | certificate\_file |
|   |   |   | interface |
|   |   |   | password |
|   |   |   | uri |
|   |   |   | username |
|   |   | </image\_inserter\_input> |   |
|   | </insertable\_image> |   |   |
| </image\_inserter> |   |   |   |

## Overlays in input section
<a name="overlays-in-input-section"></a>

**Data in <input> element **

|  |  |  |  |  |
| --- |--- |--- |--- |--- |
| <input> |   |   |   |   |
|   | <image\_inserter> |   |   |   |
|   |   | enable\_rest |   |   |
|   |   | <insertable\_image> |   |   |
|   |   |   | duration |   |
|   |   |   | fade\_in |   |
|   |   |   | fade\_out |   |
|   |   |   | height |   |
|   |   |   | image\_x |   |
|   |   |   | image\_y |   |
|   |   |   | layer |   |
|   |   |   | opacity |   |
|   |   |   | start\_time |   |
|   |   |   | width |   |
|   |   |   | <image\_inserter\_input> |   |
|   |   |   |   | certificate\_file |
|   |   |   |   | interface |
|   |   |   |   | password |
|   |   |   |   | uri |
|   |   |   |   | username |
|   |   |   | </image\_inserter\_input> |   |
|   |   | </insertable\_image> |   |   |

## Overlays in Ssream assembly section
<a name="overlays-in-stream-assembly-section"></a>

**Data in <stream\_assembly> **

|  |  |  |  |  |  |  |
| --- |--- |--- |--- |--- |--- |--- |
| <stream\_assembly> |   |   |   |   |   |   |
|   | <video\_description> |   |   |   |   |   |
|   |   | <video\_preprocessors> |   |   |   |   |
|   |   |   | <image\_inserter> |   |   |   |
|   |   |   |   | enable\_rest |   |   |
|   |   |   |   | <insertable\_image> |   |   |
|   |   |   |   |   | duration |   |
|   |   |   |   |   | fade\_in |   |
|   |   |   |   |   | fade\_out |   |
|   |   |   |   |   | height |   |
|   |   |   |   |   | image\_x |   |
|   |   |   |   |   | image\_y |   |
|   |   |   |   |   | layer |   |
|   |   |   |   |   | opacity |   |
|   |   |   |   |   | start\_time |   |
|   |   |   |   |   | width |   |
|   |   |   |   |   | <image\_inserter<br />\_input> |   |
|   |   |   |   |   |   | certificate\_file |
|   |   |   |   |   |   | interface |
|   |   |   |   |   |   | password |
|   |   |   |   |   |   | uri |
|   |   |   |   |   |   | username |
|   |   |   |   |   | </image\_inserter<br />\_input> |   |
|   |   |   |   | </insertable\_image> |   |   |
|   |   |   | <image\_inserter> |   |   |   |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Live. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-live` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
