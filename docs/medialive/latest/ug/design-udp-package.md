---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/design-udp-package.html
---

# Organize encodes in a UDP output group
<a name="design-udp-package"></a>

A UDP output group can contain the following:
+ One or more outputs.

Each output can contain the following:
+ One video encode.
+ One or more audio encodes.
+ One or more captions encodes. The captions are either embedded or object-style captions.

Each output represents one SPTS. Each output (SPTS) has its own destination..

This diagram illustrates a UDP output group with one output. The captions are embedded in the video encode.

![Output group container showing one output with embedded video and two outputs labeled A.](http://docs.aws.amazon.com/medialive/latest/ug/images/output3-nonABR-Ve-2A.png)

This diagram illustrates a UDP output group with one output. The captions are object-style captions.

![Output group labeled Output containing five elements: V, A, A, C, and C in oval shapes.](http://docs.aws.amazon.com/medialive/latest/ug/images/output4-nonABR-V-2A-2C.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
