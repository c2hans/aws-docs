---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/ips-plan-action-names.html
---

# Plan the action names
<a name="ips-plan-action-names"></a>

You should plan the names for the input switch action in the MediaLive schedule. Action names must be unique in the schedule for each channel.

For a static input, you might want to name the actions so that they indicate which input applies. For example, for each switch to the input named static-live-studio-feed:
+ `static-live-studio-feed-action-1`
+ `static-live-studio-feed-action-2`
+ `static-live-studio-feed-action-3`

For the input switch action for a dynamic input, you might use the input name (or part of the name) plus the URL (or part of the URL) of the file. For example:
+ `dyn-preroll-EN-FR-ES-DE-ad-ward-cars-1`
+ `dyn-preroll-EN-FR-ES-DE-ad-zel-cafe`
+ `dyn-preroll-EN-FR-ES-DE-ad-ward-cars-2`

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
