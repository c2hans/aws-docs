---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/setup-result-mp4.html
---

# Result of this procedure
<a name="setup-result-mp4"></a>

As a result of this setup, a MediaLive input exists that specifies one or two *source* URLs. These sources are the URLs for the source content on the upstream server.

When you start the channel, MediaLive will connect to the upstream system at this source location or locations and pull the content:
+ For a standard channel, MediaLive expects the upstream system to provide two sources and will therefore attempt to pull from both source locations.
+ For a single-pipeline channel, MediaLive expects the upstream system to provide one source and will therefore attempt to pull from one source location.

![Diagram showing MP4 input retrieval from two S3 bucket locations in MediaLive.](http://docs.aws.amazon.com/medialive/latest/ug/images/mp4-pull-uss-input.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
