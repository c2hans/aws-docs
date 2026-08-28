---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/input-caller-srt-result.html
---

# Result of this procedure
<a name="input-caller-srt-result"></a>

As a result of this setup, an SRT caller input exists that specifies one or two *source* URLs. These sources are the URLs for the source content on the upstream system.

At runtime of the channel, MediaLive (the caller) will perform a handshake with the upstream system (the listener). MediaLive will connect to two URLs (for a standard channel) or one URL (for a single-pipeline channel), and pull the source content into the channel.

![Diagram showing upstream systems sending data packets to two SRT caller input URLs in MediaLive.](http://docs.aws.amazon.com/medialive/latest/ug/images/srt-pull-uss-input.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
