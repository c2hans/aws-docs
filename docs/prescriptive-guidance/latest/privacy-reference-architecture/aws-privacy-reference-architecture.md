---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/privacy-reference-architecture/aws-privacy-reference-architecture.html
---

# The AWS Privacy Reference Architecture
<a name="aws-privacy-reference-architecture"></a>

**Note**
We would love to hear from you. Please provide feedback on the AWS PRA by taking a [short survey](https://amazonmr.au1.qualtrics.com/jfe/form/SV_cMxJ0MG3jU91Fk2).

The following diagram illustrates the AWS Privacy Reference Architecture (AWS PRA). This is an example of an architecture that connects many privacy-related AWS services and features. This architecture is built on a landing zone that is governed by AWS Control Tower.

![Diagram of the AWS services deployed in the AWS Privacy Reference Architecture](http://docs.aws.amazon.com/prescriptive-guidance/latest/privacy-reference-architecture/images/guide-img/a4379862-3434-48e4-8691-64db36363b08/images/e9c228f3-b7bb-4ee9-b4f6-90c0c6f5423d.png)

The AWS PRA includes a serverless web architecture that is hosted in the Personal Data (PD) Application account. The architecture in this account is an example workload that collects personal data directly from consumers. In this workload, users connect through a web tier. The web tier interacts with the application tier. This tier receives inputs from the web tier, processes and stores the data, allows authorized internal teams and third parties to access the data, and eventually archives and deletes the data when it's no longer required. The architecture is purposefully modular and event-driven in order to demonstrate many of the foundational privacy engineering techniques without delving into specific use cases, such as data lakes, containers, compute, or Internet of Things (IoT).

Next, this guide describes each account in the organization in detail. It discusses the privacy-related services and features, considerations and recommendations, and diagrams for each of the following accounts:
+ [Org Management account](org-management-account.md)
+ [Security OU – Security Tooling account](security-tooling-account.md)
+ [Security OU – Log Archive account](log-archive-account.md)
+ [Infrastructure OU – Network account](network-account.md)
+ [Personal Data OU – PD Application account](personal-data-account.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
