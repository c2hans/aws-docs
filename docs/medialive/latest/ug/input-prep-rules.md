---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/input-prep-rules.html
---

# Rules and limits for input prepare in MediaLive
<a name="input-prep-rules"></a>

**One active prepare at a time**
The MediaLive schedule can contain any number of input prepare actions, but only one input prepare action can be active at one time.

**Start time at least 10 seconds in advance**
Set up each input prepare action in the MediaLive schedule so that it starts at least 10 seconds before the associated switch.

**No RTMP pull inputs**
A MediaLive channel cannot both have RTMP pull inputs and have the input prepare feature enabled. (RTMP push inputs are acceptable.) You must choose which feature is more important—the input prepare or the RTMP pull input.
+ If you want to use the input prepare feature and the channel already has an RTMP pull input, you must first remove the input.
+ If you want to add an RTMP pull input and the channel already has input prepare actions in the schedule, see [Enabling and disabling the input prepare feature](input-prep-enable.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
