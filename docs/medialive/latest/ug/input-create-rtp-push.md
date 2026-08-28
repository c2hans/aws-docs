---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/input-create-rtp-push.html
---

# Setting up an RTP push input
<a name="input-create-rtp-push"></a>

This section describes how to set up an upstream system that uses the RTP Push protocol to deliver source content from an upstream system that is in your VPC from Amazon VPC. It describes how to set up the source content on the upstream system, and how to create an input that connects the upstream system to MediaLive.

With an RTP push source, the upstream system *pushes* the content to MediaLive.

To perform this setup, you must work with an operator at the upstream system.

**Topics**
+ [Obtain information](setup-rtp-push-obtain-info.md)
+ [Create an input security group](setup-isg-rtp-push.md)
+ [Create an RTP input](setup-input-rtp-push.md)
+ [Ensure correct setup on the upstream system](setup-uss-rtp-push.md)
+ [Result of this procedure](setup-result-rtp-push.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
