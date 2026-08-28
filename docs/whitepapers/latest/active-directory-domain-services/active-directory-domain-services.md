---
source_url: https://docs.aws.amazon.com/whitepapers/latest/active-directory-domain-services/active-directory-domain-services.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Active Directory Domain Services on AWS
<a name="active-directory-domain-services"></a>

**Design and Planning Guide**

Publication date: **November 20, 2020** ([Document history](document-revisions.md))

 Cloud is now the center of most enterprise IT strategies. Many enterprises find that a well-planned move to the cloud results in an immediate business payoff. Active Directory is a foundation of the IT infrastructure for many large enterprises. This whitepaper covers best practices for designing Active Directory Domain Services (AD DS) architecture in Amazon Web Services (AWS), including AWS Managed Microsoft AD, Active Directory on Amazon Elastic Compute Cloud (Amazon EC2) instances, and hybrid scenarios.

## Importance of Active Directory in the cloud
<a name="importance-of-active-directory-in-the-cloud"></a>

 [Microsoft Active Directory](https://docs.microsoft.com/en-us/windows/desktop/ad/active-directory-domain-services) was introduced in 1999 and became *de facto* standard technology for centralized management of Microsoft Windows computers and user authentications. Active Directory serves as a distributed hierarchical data storage for information about corporate IT infrastructure, including Domain Name System (DNS) zones and records, devices and users, user credentials, and access rights based on groups membership.

 [Tens of thousands of enterprises use Active Directory](https://discovery.hgdata.com/product/microsoft-active-directory) for authentication. Successful adoption of cloud technology requires considering existing IT infrastructure and applications deployed on-premises. Reliable and secure Active Directory architecture is a critical IT infrastructure foundation for companies running Windows workloads.

## Are you Well-Architected?
<a name="are-you-well-architected"></a>

 The [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/) helps you understand the pros and cons of the decisions you make when building systems in the cloud. The six pillars of the Framework allow you to learn architectural best practices for designing and operating reliable, secure, efficient, cost-effective, and sustainable systems. Using the [AWS Well-Architected Tool](https://aws.amazon.com/well-architected-tool/), available at no charge in the [AWS Management Console](https://console.aws.amazon.com/wellarchitected), you can review your workloads against these best practices by answering a set of questions for each pillar.

 For more expert guidance and best practices for your cloud architecture—reference architecture deployments, diagrams, and whitepapers—refer to the [AWS Architecture Center](https://aws.amazon.com/architecture/).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
