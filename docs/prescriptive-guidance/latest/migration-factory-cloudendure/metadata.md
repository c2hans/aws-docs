---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-factory-cloudendure/metadata.html
---

# The migration metadata pipeline tool
<a name="metadata"></a>

Cloud Migration Factory includes a migration metadata pipeline tool and automation scripts. The metadata pipeline tool integrates with other migration tools and scripts through Representational State Transfer (REST) APIs, as shown in the following diagram. This enables migration metadata to flow from one tool to another to support end-to-end automation. Currently, Cloud Migration Factory is natively integrated with the AWS Managed Services (AMS) workload ingest process. By integrating this process, Cloud Migration Factory can automate migration tasks across multiple tools.

![The Cloud Migration Factory metadata pipeline tool](http://docs.aws.amazon.com/prescriptive-guidance/latest/migration-factory-cloudendure/images/guide-img/3ff8a3b6-fa4d-412f-ba5f-3d8aad3942a7/images/f9406870-38c3-479c-8ef7-2e1606b4177f.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
