---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/tagging-best-practices/faq.html
---

# FAQ
<a name="faq"></a>

The following are frequently raised questions about tagging on AWS.

## Can you enforce creation of tags when any infrastructure is deployed?
<a name="q-1"></a>

Yes, you can enforce tag creation by using [service control policies](https://aws.amazon.com/blogs/mt/implement-aws-resource-tagging-strategy-using-aws-tag-policies-and-service-control-policies-scps/).

## Is tagging infrastructure enough?
<a name="q-2"></a>

Typically, tagging only infrastructure isn't enough. To get accurate numbers in dashboards, you must tag all resources and data files that are stored or processed on AWS.

## What are the next steps?
<a name="q-3"></a>

Reevaluate your project. Apply tags to all data and infrastructure, and set up dashboards. Even if there is no current need for such dashboards, tagging resources now will make dashboard setup much faster if you determine a need for separated-cost understanding.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
