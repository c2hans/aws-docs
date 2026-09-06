---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/cyber-threat-intelligence-sharing/shared-responsibility-model.html
---

# CTI sharing model
<a name="shared-responsibility-model"></a>

The [AWS shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/) defines how you share responsibility with AWS for security and compliance in the cloud. AWS secures the infrastructure that runs all of the services offered in the AWS Cloud, known as *security of the cloud*. You are responsible for securing your use of those services, such as your data and applications. This is known as *security in the cloud*.

## Security of the cloud
<a name="security-of-the-cloud"></a>

Security is the top priority at AWS. We work hard to help prevent security issues from causing disruption to your organization. As we work to defend our infrastructure and your data, we use our global-scale insights to gather a high volume of security intelligence—at scale and in real time—to help automatically protect you. Whenever possible, AWS and its security systems disrupt threats where that action is most impactful. Often, this work happens behind the scenes.

Every day, across the AWS Cloud infrastructure, we detect and successfully thwart hundreds of cyberattacks that might otherwise be disruptive and costly. These important but mostly unseen victories are achieved with a global network of sensors and an associated set of disruption tools. Using these capabilities, we make it more difficult and expensive for cyberattacks to be carried out against our network and infrastructure.

AWS has the largest public network footprint of any cloud provider. This gives AWS unparalleled, real-time insight into certain activities on the internet. [MadPot](https://www.aboutamazon.com/news/aws/amazon-madpot-stops-cybersecurity-crime) is a globally distributed network of threat sensors (known as *honeypots*). MadPot helps AWS security teams understand attackers' tactics and techniques. Any time an attacker tries to target one of the threat sensors, AWS collects and analyzes the data.

Sonaris is another internal tool that AWS uses to analyze network traffic. It identifies and stops unauthorized attempts to access a large number of accounts and resources. Between May 2023 and April 2024, Sonaris denied over 24 billion attempts to scan customer data stored in Amazon Simple Storage Service (Amazon S3). It also prevented nearly 2.6 trillion attempts to discover vulnerable workloads running on Amazon Elastic Compute Cloud (Amazon EC2).

## Security in the cloud
<a name="security-in-the-cloud"></a>

This guidance focuses on best practices for cyber threat intelligence (CTI) in the AWS Cloud. You are responsible for generating localized and contextualized CTI. You control where your data is stored, how it is secured, and who has access to it. AWS does not have visibility into your logging, monitoring and audit data, which is essential for CTI-based security in the cloud.

[Structured Threat Information Expression (STIX)](https://docs.oasis-open.org/cti/stix/v2.1/csprd01/stix-v2.1-csprd01.html) is an open source language and serialization format that is used to exchange CTI. Indicators such as file hashes, domains, URLs, HTTP requests, and IP addresses are important outputs to share for threat blocking. However, effective action relies on additional intelligence, such as certainty ratings and intrusion set correlations. STIX 2.1 defines 18 [STIX Domain Objects](https://oasis-open.github.io/cti-documentation/stix/intro.html#stix-21-objects), including attack pattern, course of action, threat actor, geographic location, and malware information. It also introduces concepts, such as confidence ratings and relationships, that help entities determine signal from noise in the large volume of data that that the threat intelligence platform collects. You can detect, analyze, and share this level of detail about threats in your AWS environments. For more information, see [Automating preventative and detective security controls](architecture-automate-controls.md) in this guide.
