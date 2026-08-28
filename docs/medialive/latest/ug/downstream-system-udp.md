---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/downstream-system-udp.html
---

# Coordinate with the downstream system
<a name="downstream-system-udp"></a>

You and the operator of the downstream system must agree about the destination for each output of the UDP output group.

A UDP output group requires one set of destination addresses for each output.

1. Decide if you need two destinations for the output:
   + If the MediaLive channel is a [standard channel](plan-redundancy.md), you need two destinations.
   + If the MediaLive channel is a single-pipeline channel, you need one destination.

1. Speak to the operator who manages the downstream system that will receive UDP content. Make sure that the operator sets up to expect one or two MediaLive outputs, as appropriate.

1. Obtain the following information from the operator:
   + Whether the protocol is UDP or RTP
   + The URLs
   + The port numbers

   Each URL will look like this, for example:

   `udp://203.0.113.28:5000`

   `udp://203.0.113.33:5005`

   Note that in this example, the port numbers are not sequential. These non-sequential numbers are important if you plan to enable FEC in the outputs (this field is in the **Output** pane of the UDP output group). With FEC, you must leave space between the port numbers for the two destinations. For example, if one destination is **rtp://203.0.113.28:5000**, assume that FEC also uses port 5002 and 5004. So the lowest possible port number for the other destination is 5005.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
