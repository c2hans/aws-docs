---
source_url: https://docs.aws.amazon.com/whitepapers/latest/classic-intrusion-analysis-frameworks-for-aws-environments/introduction.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Introduction
<a name="introduction"></a>

 Cybersecurity threats continue to challenge organizations around the world. Many of the cybersecurity strategies that organizations have employed over the past two decades have failed to stop network compromises and data breaches. This has led many Chief Information Security Officers (CISOs) and cybersecurity practitioners to look for more effective approaches to manage cybersecurity risk for their organizations.

 One such approach, pioneered by Lockheed Martin Corporation, is described in [Intelligence-Driven Computer Network Defense Informed by Analysis of Adversary Campaigns and Intrusion Kill Chains](https://lockheedmartin.com/content/dam/lockheed-martin/rms/documents/cyber/LM-White-Paper-Intel-Driven-Defense.pdf).

 *Intelligence-driven computer network defense is a necessity in light of advanced persistent threats. As conventional, vulnerability-focused processes are insuﬃcient, understanding the threat itself, its intent, capability, doctrine, and patterns of operation is required to establish resilience. The intrusion kill chain provides a structure to analyze intrusions, extract indicators and drive defensive courses of actions. Furthermore, this model prioritizes investment for capability gaps, and serves as a framework to measure the eﬀectiveness of the defenders’ actions.*

**Note**
Hutchins EM, Cloppert MJ, Amin RM. Intelligence-driven computer network defense informed by analysis of adversary campaigns and intrusion kill chains. (Lockheed Martin, Bethesda, MD, 2011), 12.

 Since Lockheed Martin’s paper was published in 2011, many variations of this particular intrusion analysis approach have been developed in the cybersecurity industry, and many organizations have benefited from implementing this classic framework for intrusion analysis to guide mitigation and response strategy for their on-premises infrastructure.

 This whitepaper offers an assessment of the classic intrusion analysis framework from an AWS Cloud perspective; pointing out where it applies, where it may not, and describing AWS mechanisms to support and enhance any customers’ intrusion analysis approach.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
