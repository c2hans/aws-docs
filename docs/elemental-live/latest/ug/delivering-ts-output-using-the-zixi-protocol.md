---
source_url: https://docs.aws.amazon.com/elemental-live/latest/ug/delivering-ts-output-using-the-zixi-protocol.html
---

# Delivering TS output using the Zixi protocol
<a name="delivering-ts-output-using-the-zixi-protocol"></a>

In AWS Elemental Live , you can deliver TS output using the Zixi protocol. The destination is considered to be a *Zixi broadcaster*. You can choose to encrypt the content with AES. This Zixi delivery option is part of the Reliable TS output group.

**Note**
The Zixi option is intended for sending to a downstream system other than AWS Elemental MediaConnect.
To send to a Zixi flow on MediaConnect, we recommend that you use the Reliable TS output group with the AWS Elemental MediaConnect option. See [Setting up Elemental Live as a Contribution Encoder for AWS Elemental MediaConnect](setting-up-live-as-contribution-encoder-for-mediaconnect.md).

The Zixi protocol involves two roles—the Zixi *feeder* (also known as the caller) and the Zixi *receiver* (the listener). The Zixi feeder always initiates the handshake that precedes successful transmission of the output. The Zixi receiver accepts or rejects the handshake.

With the Zixi option in the Reliable TS output group, Elemental Live is always the Zixi feeder, which means the downstream system must be the Zixi receiver.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Live. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-live` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
