---
source_url: https://docs.aws.amazon.com/reference-architecture-diagrams/latest/siemens-nx-appstream/siemens-nx-appstream.html
---

# Siemens NX on Amazon WorkSpaces Applications
<a name="siemens-nx-appstream"></a>

Publication date: **2021 ([Diagram history](#snxa-diagram-history))**

With these architectures, you can stream Siemens NX securely through [Amazon WorkSpaces Applications](https://docs.aws.amazon.com/appstream2/latest/developerguide/) hosted in AWS Cloud. Three deployment options address different storage, identity, and latency requirements.

The following diagrams describe the architecture:
+ [Siemens NX with Amazon EBS shared folders](snxa-ebs-shared-folders.md) — Use Amazon EBS volumes as shared folders for Siemens NX users.
+ [Siemens NX connected to Siemens Teamcenter](snxa-teamcenter-fsx.md) — Connect to Siemens Teamcenter with Amazon FSx storage.
+ [Siemens NX multi-Region deployment](snxa-multi-region.md) — Minimize latency with cross-Region storage replication.

## Further reading
<a name="snxa-further-reading"></a>

For additional information, see the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)

## Diagram history
<a name="snxa-diagram-history"></a>

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date |
| --- |--- |--- |
| [Initial publication](#snxa-diagram-history) | Reference architecture diagram first published. | January 1, 2021 |

**RSS subscription**
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser that you are using.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Reference Architecture Diagrams. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query reference-architecture-diagrams` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
