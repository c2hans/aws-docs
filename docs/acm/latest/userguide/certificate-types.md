---
source_url: https://docs.aws.amazon.com/acm/latest/userguide/certificate-types.html
---

# Types of certificates in AWS Certificate Manager
<a name="certificate-types"></a>

AWS Certificate Manager (ACM) supports three types of certificates. Each type serves different use cases depending on your security requirements and infrastructure needs.

Public certificates
Publicly trusted across the internet. Public certificates issued by ACM are trusted by all major browsers and operating systems, making them suitable for securing public-facing websites and applications.

Private certificates
Not publicly trusted. Private certificates are primarily used internal to an organization, such as for encrypting internal traffic, authenticating services, or implementing mutual TLS (mTLS) between microservices.

Imported certificates
Customer-owned certificates imported into ACM. You can import certificates obtained from third-party certificate authorities for use with ACM integrated services or for export.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Certificate Manager (ACM). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query acm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
