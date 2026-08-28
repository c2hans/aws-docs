---
source_url: https://docs.aws.amazon.com/mediapackage/latest/ug/live-content.html
---

# Delivering live content from AWS Elemental MediaPackage
<a name="live-content"></a>

AWS Elemental MediaPackage uses the following resources for live content:
+ *Channels* are the entry point for your live streams from upstream encoders.

  For supported live inputs and codecs, see [Live supported codecs and input types](supported-inputs-live.md).
+ *Endpoints* tell MediaPackage how to package outbound content. Endpoints are associated with channels and hold encryption, stream, and packaging settings.

The following sections describe how to use these resources to manage live content in MediaPackage.

**Topics**
+ [Working with channels in AWS Elemental MediaPackage](channels.md)
+ [Working with endpoints in AWS Elemental MediaPackage](endpoints.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaPackage V1. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediapackage` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
