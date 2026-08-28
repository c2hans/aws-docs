---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-retiring-applications/faq.html
---

# FAQ
<a name="faq"></a>

This section provides answers to commonly raised questions about retiring applications.

## My applications are containerized. Can I still adopt a data-driven approach to migration?
<a name="q1"></a>

Yes, by using the port and IP address to distinguish between different containers.

## How long should I run discovery tooling?
<a name="q2"></a>

The duration depends on an individual application. Four weeks should be enough. However, for batch applications that run only once a quarter, you'll need to plan accordingly.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
