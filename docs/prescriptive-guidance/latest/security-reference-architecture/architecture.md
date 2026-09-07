---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/architecture.html
---

# The AWS Security Reference Architecture
<a name="architecture"></a>

The following diagram illustrates the AWS SRA. This architectural diagram brings together all the AWS security-related services. It is built around a simple, three-tier web architecture that can fit on a single page. In such a workload, there is a *web tier* through which users connect and interact with the *application tier,* which handles the actual business logic of the application: taking inputs from the user, doing some computation, and generating outputs. The application tier stores and retrieves information from the *data tier*. The architecture is purposefully modular and provides high-level abstraction for many modern web applications.

**Note**
To customize the reference architecture diagrams in this guide based on your business needs, you can download the .zip file from the *Attachments* section of the *Introduction *chapter.

![AWS Security Reference Architecture diagram.](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/images/guide-img/91d313fc-d5f1-45a8-a5a6-2f4fc7abc93a/images/a4175a63-9c19-4ca2-9860-d3f983993e81.png)

For this reference architecture, the actual web application and data tier are deliberately represented as simply as possible, through Amazon EC2 instances and an Amazon Aurora database, respectively. Most architecture diagrams focus and dive deep on the web, application, and data tiers. For readability, they often omit the security controls. This diagram flips that emphasis to show security wherever possible, and keeps the application and data tiers as simple as necessary to show security features meaningfully.

The AWS SRA contains all AWS security-related services available at the time of publication. (See [document history](doc-history.md).) However, not every workload or environment, based on its unique threat exposure, has to deploy every security service. Our goal is to provide a reference for a range of options, including descriptions of how these services fit together architecturally, so that your business can make decisions that are most appropriate for your infrastructure, workload, and security needs, based on risk.

The following sections walk through each OU and account to understand its objectives and the individual AWS security services associated with it. For each element (typically an AWS service), this document provides the following information:
+ Brief overview of the element and its security purpose in the AWS SRA. For more detailed descriptions and technical information about individual services, see [the appendix](appendix.md).
+ Recommended placement to most effectively enable and manage the service. This is captured in the individual architecture diagrams for each account and OU.
+ Configuration, management, and data sharing links to other security services. How does this service rely on, or support, other security services?
+ Design considerations. First, the document highlights *optional* features or configurations that have important security implications. Second, where our teams' experience includes common variations in the recommendations we make—typically as a result of alternate requirements or constraints—the document describes those options.

**OUs and accounts**
+ [Org Management account](org-management.md)
+ [Security OU – Security Tooling account](security-tooling.md)
+ [Security OU – Log Archive account](log-archive.md)
+ [Infrastructure OU – Network account](network.md)
+ [Infrastructure OU – Shared Services account](shared-services.md)
+ [Workloads OU – Application account](application.md)
