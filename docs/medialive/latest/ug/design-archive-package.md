---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/design-archive-package.html
---

# Organize encodes in an Archive output group
<a name="design-archive-package"></a>

An Archive output group can contain the following:
+ One or more outputs.

The output contains the following:
+ One video encode.
+ Zero or more audio encodes.
+ Zero or more captions encodes. The captions are either embedded or object-style captions.

Typically, the Archive output group mirrors the output structure of another output group. For example, it might mirror the ABR stack in an HLS output group.

This diagram illustrates an Archive output group that contains one output that holds one video encode with embedded captions, and two audio encodes.

![Output group containing one output with video encode and two audio encodes labeled A.](http://docs.aws.amazon.com/medialive/latest/ug/images/output3-nonABR-Ve-2A.png)

This diagram illustrates an Archive output group that contains one output that holds one video encode, two audio encodes, and two object-style captions encode.

![Output group labeled Output containing five elements: V, A, A, C, and C.](http://docs.aws.amazon.com/medialive/latest/ug/images/output4-nonABR-V-2A-2C.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
