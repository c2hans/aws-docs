---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/billing-usage-type-format.html
---

# Usage type format
<a name="billing-usage-type-format"></a>

MediaLive usage types follow a general naming convention that encodes the channel configuration, region, and processing details into a single string.

The general format is:

```
{Tier}-{Region}-{Direction/Category}-{Codec}-{Resolution}-{Level/Framerate}-{Quality}-{Reservation}
```

Not all components appear in every usage type. The format varies by category. For example, input usage types include a bitrate level but not a framerate, while output usage types include a framerate but not a bitrate level.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
