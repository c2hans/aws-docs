---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/design-mediaconnect-router-package.html
---

# Organize encodes in a MediaConnect Router output group
<a name="design-mediaconnect-router-package"></a>

A MediaConnect Router output group uses the M2TS (MPEG-2 Transport Stream) container. Each output can contain the following:
+ One video encode.
+ Zero or more audio encodes.
+ Zero or more captions encodes. The captions are embedded captions or sidecar captions.

You can have up to five outputs per MediaConnect Router output group.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
