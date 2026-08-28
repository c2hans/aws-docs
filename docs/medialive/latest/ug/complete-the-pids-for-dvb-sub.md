---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/complete-the-pids-for-dvb-sub.html
---

# PIDs for DVB-Sub
<a name="complete-the-pids-for-dvb-sub"></a>

This section applies if you are [setting up DVB-Sub captions](output-embedded-and-more.md) in an output group that supports a transport stream. For example, UDP or SRT. You must specify the output PID.
+ In the relevant UDP output group, choose the output that has the DVB-Sub captions.
+ For **PID settings**, in **DVB-Sub PIDs**, enter the PID for the DVB-Sub captions in this output. Or keep the default.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
