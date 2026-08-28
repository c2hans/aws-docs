---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/cyber-threat-intelligence-sharing/introduction.html
---

# Cyber threat intelligence sharing on AWS
<a name="introduction"></a>

*Jess Modini, Alexa Donovan, and Byron Pogson, Amazon Web Services*

As new risks emerge, the best practices for protecting critical cloud workloads continuously evolve. As the number of internet-connected assets that require protection increases, so does the risk of a security event associated with threat actors. *Cyber threat intelligence (CTI)* is the collection and analysis of data that indicates a threat actor's intent, opportunity, and capability. It is evidence-based and actionable, and it informs cyber defense activities. It often includes information pertaining to actor attribution, tactics techniques and procedures, motives, or targets.

CTI can be shared within an organization, between organizations in a trust community, with Information Sharing and Analysis Centers (ISACs), or with other entities, such as government authorities. Examples of government authorities include the [Australian Cyber Security Centre (ACSC)](https://www.cyber.gov.au/) and the American [Cybersecurity and Infrastructure Security Agency (CISA)](https://www.cisa.gov/).

Like all forms of intelligence, threat context is critical. CTI sharing informs dynamic cybersecurity risk management. It is essential for timely cybersecurity defense, response, and recovery. This increases the efficiency and effectiveness of cybersecurity capabilities. Threat context is also essential to distinguish between CTI capability requirements relating to different targets. For example, sophisticated actors might target specific enterprises or governments whereas commodity actors use readily available tools and techniques to broadly attack individuals and organizations.

Security planning, observability, threat intelligence analysis, security control automation, and sharing within a trust community are key parts of the threat intelligence lifecycle. AWS helps you automate manual security tasks to detect threats with higher accuracy, respond faster, and generate high-quality threat intelligence that you can share. You can discover a new cyberattack, analyzed it, generate a CTI, share it, and apply it—all at speeds designed to prevent a second attack from occurring.

This guide describes how to deploy a threat intelligence platform on AWS. Trust communities provide CTI, and the platform ingests it to identify actionable intelligence and automate protective and detective controls in the AWS environment. The following image shows the threat intelligence lifecycle. The CTI arrives from its source, and then the threat intelligence platform processes it. By using [Trusted Automated Exchange of Intelligence Information (TAXII)](https://oasis-open.github.io/cti-documentation/taxii/intro.html) protocol or the [Malware Information Sharing Platform (MISP)](https://www.misp-project.org/), the CTI is shared with the trust community for action.

![The threat intelligence lifecycle that flows from the source back to the trust community.](http://docs.aws.amazon.com/prescriptive-guidance/latest/cyber-threat-intelligence-sharing/images/guide-img/65270b8a-43a4-49d2-8123-9467febf488a/images/03ce9b46-ffd5-4d01-bf23-875e0e7128c9.png)

The threat intelligence platform uses the CTI to automatically implement security controls in your AWS environment or to notify your security team if manual action is required. A *preventative control *is a security control that is designed to prevent an event from occurring. Examples include automation of blocking lists of known bad IP addresses or domain names by using network firewalls, DNS resolvers, and other intrusion prevention systems (IPSs). A *detective control* is a security control that is designed to detect, log, and alert after an event has occurred. Examples include continuous monitoring for malicious activity and searching logs for evidence of issues or events.

You can aggregate any findings in a centralized security observability tool, such as [AWS Security Hub CSPM](https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub.html). Then, you can share the findings with a trust community to collaboratively build a comprehensive threat picture.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
