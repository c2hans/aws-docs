---
source_url: https://docs.aws.amazon.com/ivs/latest/BroadcastSWIntegAPIReference/structures-Framerate.html
---

# Framerate
<a name="structures-Framerate"></a>

Object specifying a framerate.

## Contents
<a name="structures-Framerate-contente"></a>
+ **denominator**
  + Number of seconds for the calculation of frames per second.
  + Type: Integer
  + Valid Values: `1`
  + Required: Yes
+ **numerator**
  + Number of frames for the calculation of frames per second.
  + Type: Integer
  + Valid Values: `24 | 25 | 30 | 48 | 50 | 60`
  + Required: Yes

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon IVS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ivs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
