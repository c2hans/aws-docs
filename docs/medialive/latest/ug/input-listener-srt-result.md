---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/input-listener-srt-result.html
---

# Result of this procedure
<a name="input-listener-srt-result"></a>

As a result of this setup, an SRT Listener input exists with one or two *destination* URLs. These destinations are the URLs that MediaLive allocated for receiving the source content.

At runtime of the channel, the upstream system (the caller) will perform a handshake with MediaLive (the listener). The upstream system will connect to two URLs (for a standard channel) or one URL (for a single-pipeline channel), and push the source content into the channel.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
