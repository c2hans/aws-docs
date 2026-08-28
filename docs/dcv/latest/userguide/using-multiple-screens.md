---
source_url: https://docs.aws.amazon.com/dcv/latest/userguide/using-multiple-screens.html
---

# Using multiple monitors
<a name="using-multiple-screens"></a>

**Note**
When collaborating on Amazon DCV sessions, the multiple monitor function is disabled.

Amazon DCV is capable of extending full screen resolution across a single monitor, a set of selected monitors, or all available monitors.

If the requested layout is not supported by the server, the layout might be adjusted to match the display limits of your server. If the layout cannot be adjusted, the request fails and the changes are not applied.

You can also manually specify custom display layouts. For more information, see [ Managing the Amazon DCV Session Display Layout](https://docs.aws.amazon.com/dcv/latest/adminguide/managing-session-display.html) in the *Amazon DCV Administrator Guide*.

Amazon DCV can configure a resolution according to the settings and the server system configuration.
+ Web client resolution is limited by default to 1920x1080 (from web-client-max-head-resolution server setting).
+ Native clients are limited by default to 4096x2160 (from max-head-resolution).

**Note**
Maximum supported per-monitor resolution is 4096x4096 for up to 4 monitors. Higher resolutions or more than 4 monitors are not supported in any configuration.

Make sure to follow the [prerequisites guide](https://docs.aws.amazon.com/dcv/latest/adminguide/setting-up-installing.html) to properly setup the system environment and drivers for best performance.

**Topics**
+ [Extending full-screen across all monitors](full-screen-all-monitors.md)
+ [Extending full-screen across selected monitors](full-screen-selected-monitors.md)
+ [Exiting full screen on multiple monitors](exiting-full-screen-multiple-monitors.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DCV. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dcv` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
