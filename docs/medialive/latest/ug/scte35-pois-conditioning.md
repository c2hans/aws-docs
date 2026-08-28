---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/scte35-pois-conditioning.html
---

# POIS signal conditioning
<a name="scte35-pois-conditioning"></a>

You can configure an AWS Elemental MediaLive channel so that your POIS server can perform *signal conditioning* on SCTE 35 messages that are in the content. Each time MediaLive encounters a SCTE 35 message in the content, MediaLive sends the message to the POIS server. The POIS server sends back a response to create a new SCTE 35 message, to replace the original message with different content, to delete the existing message, or to do nothing.

**Note**
To implement POIS signal conditioning, your organization must have access to a POIS server.

**Topics**
+ [Supported version of the specification](scte35-pois-about-spec.md)
+ [About POIS signal conditioning](scte35-pois-about.md)
+ [Setting up for POIS signal conditioning](scte35-pois-setup.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
