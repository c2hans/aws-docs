---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-multicloud-fsi/saas.html
---

# Accelerate and optimize operations with SaaS applications
<a name="saas"></a>

Most FIs have adopted software as as service (SaaS) applications for key parts of their business. Common SaaS applications include productivity applications such as word processing and email. SaaS options also exist for many mission-critical workloads, including payments processing, treasury, trading, anti-money laundering (AML), know your customer (KYC), learning management systems (LMS), and customer relationship management (CRM) workloads. When your FI adopts a SaaS offering, your IT team doesn't have to maintain the service or manage the infrastructure―your users consume the service without any IT involvement. Even if you have the resources to host the application yourself, it might be more cost-effective to adopt a SaaS solution and invest in other projects instead.

Knowing how and where your SaaS application is hosted, or choosing the right hosting environment, leads to lower data transfer costs, better integration, lower latency, and native backups. For example, Genesys is a call center application built on AWS. Integrating with this SaaS solution and using custom-built modules on AWS gives you the flexibility to define your users' experience on this application and to speed up implementation by taking advantage of the services and integrations offered by AWS.

As another example, services such as [AWS Glue](https://aws.amazon.com/glue/) provide seamless, bidirectional data movement for Salesforce, and integrating AWS generative AI services complements the strengths of Salesforce. Consolidate and converge your SaaS landscape and understand how you will integrate with SaaS solutions to get the best experience for your users.

Many SaaS providers offer services that are hosted on another CSP's infrastructure. When you're deciding on workload placement, consider the latency and availability of these services and your access pattern. Some questions you should consider in this context include:
+ Do I access these services asynchronously or through batch processing?
+ Is near real-time, on-demand access a requirement?
+ How latency-sensitive are my workload's requirements?
+ Are my customers or internal users sensitive to whether my systems are colocated near our SaaS partners?

Align your SaaS providers and CSPs with your requirements. Your SaaS products should both speed up your business outcomes and reduce operational impact through cloud-native colocation where appropriate.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
