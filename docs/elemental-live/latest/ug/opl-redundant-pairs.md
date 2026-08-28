---
source_url: https://docs.aws.amazon.com/elemental-live/latest/ug/opl-redundant-pairs.html
---

# Output locking pairs
<a name="opl-redundant-pairs"></a>

In an output redundancy implementation, there are also redundant pairs of events, outputs, and encodes. Encode pairs are typically identical.

If you have a workflow with several types of output groups, it's important to keep track of the pairs. If you don't keep track of the pairs, you might break the rules for output locking.

The following diagram illustrates the event setup to produce a redundant HLS output and a Microsoft Smooth Streaming output, all from the same source. The following pairs exist:
+ Events A and B are a redundant pair of events. Events C and D are another redundant pair.
+ Outputs A1 and B1 are a redundant pair of outputs. Outputs C1 and C1 are another redundant pair.
+ Videos 1 and 2 are a redundant pair of encodes. Videos 3 and 4 are another redundant pair.

![Four events with output groups routing to video destinations, including HLS and MS Smooth outputs.](http://docs.aws.amazon.com/elemental-live/latest/ug/images/opl-pairs.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Live. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-live` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
