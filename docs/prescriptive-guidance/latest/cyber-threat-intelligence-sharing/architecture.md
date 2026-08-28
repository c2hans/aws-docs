---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/cyber-threat-intelligence-sharing/architecture.html
---

# CTI architecture
<a name="architecture"></a>

The following figure depicts a generalized architecture for using a threat feed to integrate cyber threat intelligence (CTI) into your AWS environment. The CTI is shared between your threat intelligence platform in the AWS Cloud, the selected cyber authority, and other trust community members.

![CTI sharing between a global authority, community members, and your threat intelligence platform.](http://docs.aws.amazon.com/prescriptive-guidance/latest/cyber-threat-intelligence-sharing/images/guide-img/65270b8a-43a4-49d2-8123-9467febf488a/images/4e45c7e3-991a-4406-97ef-09300968cbf2.png)

It shows the following workflow:

1. The threat intelligence platform receives actionable CTI from the cyber authority or from other trust community members.

1. The threat intelligence platform tasks AWS security services to detect and prevent events.

1. The threat intelligence platform receives threat intelligence from AWS services.

1. If an event occurs, the threat intelligence platform curates new CTI.

1. The threat intelligence platform shares the new CTI with the cyber authority. It can also share the CTI with other trust community members.

There are many cyber authorities that offer CTI feeds. Examples include the [Australian Cyber Security Centre (ACSC)](https://www.cyber.gov.au/), the [Connect Inform Share Protect (CISP)](https://www.ncsc.gov.uk/cisp/home) program offered by the UK National Cyber Security Centre, and the [Malware Free Networks (MFN)](https://www.ncsc.govt.nz/what-we-do/services-we-offer/malware-free-networks/) program offered by the New Zealand Government Communications Security Bureau. Many AWS Partners also offer CTI sharing feeds.

To get started with CTI sharing, we recommend that you do the following:

1. [Deploying a threat intelligence platform](architecture-threat-intelligence-platform.md) – Deploy a platform that ingests, aggregates and organizes threat intelligence data from multiple sources and in different formats.

1. [Ingesting cyber threat intelligence](architecture-ingest-cti.md) – Integrate your threat intelligence platform with one or more threat feed providers. When you're receiving a threat feed, use your threat intelligence platform to process the new CTI and identify the actionable intelligence that is relevant to the security operations in your environment. Automate as much as possible, but there are some situations that require a human-in-the-loop decision.

1. [Automating preventative and detective security controls](architecture-automate-controls.md) – Deploy CTI to security services in your architecture that provide preventative and detective controls. These services are commonly known as intrusion prevention systems (IPS). On AWS, you use service APIs to configure block lists that deny access from the IP addresses and domain names provided in the threat feeds.

1. [Gaining visibility with observability mechanisms](architecture-gain-visibility.md) – While security operations take place in your environment, you are collecting new CTI. For example, you might observe a threat that was included in the threat feed, or you might observe indicators of compromise associated with an intrusion (such as a zero-day exploit). Centralizing threat intelligence provides increased situational awareness across your environment, so that you can review existing CTI and newly discovered CTI in one system.

1. [Sharing CTI with your trust community](architecture-share.md) – To complete the CTI sharing life cycle, generate your own CTI and share it back into your trust community.

The following video, [Scaling cyber threat intelligence sharing with the AUS Cyber Security Center](https://www.youtube.com/watch?v=0P8snWhCN4I), discusses these steps in more detail. Although this video discusses the CTI sharing capabilities of the Australian Cyber Security Centre, the steps are the same regardless of the threat feed you choose or your location.

[https://www.youtube-nocookie.com/embed/0P8snWhCN4I?controls=0](https://www.youtube-nocookie.com/embed/0P8snWhCN4I?controls=0)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
