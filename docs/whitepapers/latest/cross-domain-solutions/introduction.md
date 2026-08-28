---
source_url: https://docs.aws.amazon.com/whitepapers/latest/cross-domain-solutions/introduction.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Introduction
<a name="introduction"></a>

 To control access across security domains, it’s common to employ a specialized hardware solution such as a cross-domain system (CDS) to manage and control the interactions between two security boundaries. When security domains extend across data centers or expand into the cloud, you can encounter additional challenges when including the hardware solution you want in your architecture.

 You are not limited to any vendor solution to deploy a CDS on the AWS Cloud. However, one challenge is that you cannot place your own hardware within an AWS data center. This requirement is part of the AWS commitment to maintain security within AWS data centers. As part of the growing need to move data within cloud-based security domains, AWS provides an AWS Service to allow moving data within security domains.

 This whitepaper provides best practices for designing hybrid architectures where AWS services are incorporated into one or more security domains within a multidomain environment and to describe a best practice of using a cloud-based CDS service.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
