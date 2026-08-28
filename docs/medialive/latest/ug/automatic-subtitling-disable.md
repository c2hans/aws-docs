---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/automatic-subtitling-disable.html
---

# Disabling Smart Subtitles
<a name="automatic-subtitling-disable"></a>

To disable Smart Subtitles and stop incurring charges:

1. Stop the channel.

1. Edit the channel and remove the Smart Subtitles caption selector from the input.

1. Remove or update any caption descriptions and outputs that reference the removed Smart Subtitles caption selector.

1. Save and restart the channel.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
