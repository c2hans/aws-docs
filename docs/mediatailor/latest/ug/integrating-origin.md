---
source_url: https://docs.aws.amazon.com/mediatailor/latest/ug/integrating-origin.html
---

# Integrating a content source for MediaTailor ad insertion
<a name="integrating-origin"></a>

This topic covers integrating different types of video content sources with MediaTailor. MediaTailor supports both HLS and DASH streaming protocols for live and on-demand content. The service can perform ad insertion or replacement during designated ad breaks, and has specific requirements for the structure and formatting of the input video manifests to enable these capabilities. The following topics provide details on the input source requirements and steps for integrating HLS and DASH content with MediaTailor to enable personalized ad experiences.

**Topics**
+ [Input source requirements for MediaTailor ad insertion](stream-reqmts.md)
+ [Integrating an HLS source](manifest-hls.md)
+ [Integrating an MPEG-DASH source](manifest-dash.md)
+ [Securing AWS Elemental MediaTailor origin interactions with SigV4](origin-sigv4.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaTailor. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediatailor` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
