---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/rtmp-push-vpc-input.html
---

# Setting up an RTMP VPC input
<a name="rtmp-push-vpc-input"></a>

This section describes how to set up content that uses the RTMP Push protocol to deliver source content from an upstream system that is in your VPC from Amazon Virtual Private Cloud (Amazon VPC). This section describes how to set up the source content on the upstream system, and how to create an input that connects the upstream system to MediaLive.

With an RTMP Push input, the upstream system *pushes* the content to MediaLive.

To perform this setup, you must work with an Amazon VPC user, and with an operator at the upstream system.

**Topics**
+ [Request setup on the VPC](setup-vpc-rtmp-vpc.md)
+ [Create an RTMP input](setup-input-rtmp-vpc.md)
+ [Ensure correct setup on the upstream system](setup-uss-rtmp-vpc.md)
+ [Result of this procedure](setup-rtmp-vpc-result.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
