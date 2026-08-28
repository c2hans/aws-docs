---
source_url: https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-trusted-identity-emr-studio.html
---

# Using EMR Studio with Trusted Identity Propagation on Amazon EMR on EC2
<a name="emr-trusted-identity-emr-studio"></a>

This section covers how to set up and use trusted identity propagation with Amazon EMR on EC2 clusters through EMR Studio. It includes the prerequisites, identity-based authorization with open table formats, and cross-account access.

This section covers the following:
+ **Prerequisites** — Configure IAM Identity Center, Lake Formation, and the Amazon EMR security configuration.
+ **Identity-based authorization** — Query open table formats (Parquet, Iceberg, and Delta Lake) with propagated identities.
+ **Cross-account access** — Access data governed by Lake Formation in a different AWS account.

**Topics**
+ [Prerequisites to configure Trusted Identity Propagation with EMR on EC2](emr-trusted-identity-prerequisites.md)
+ [Using identity based authorization with OTFs](emr-trusted-identity-auth.md)
+ [Cross account setup with trusted identity propagation](emr-trusted-identity-cross-account.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EMR Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query emr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
