---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/data-lake-for-growth-scale/faq.html
---

# FAQ
<a name="faq"></a>

This section provides answers to commonly raised questions about designing a data lake for growth and scale on the AWS Cloud.

## Is this data lake reference architecture more applicable to enterprise organizations?
<a name="is-this-data-lake-reference-architecture-more-applicable-to-enterprise-organizations-.7260d7f6-288b-5223-82ba-da9a5f78f878"></a>

This guide's data lake reference architecture can be applied to data lakes belonging to organizations of any size. The reference architecture standardizes the data exchange interface, lowers the overhead and cost to maintain and grow the data lake, and can be applied to any scale that your organization's data lake grows to.

## Can I still use this reference architecture if my organization only has one data producer?
<a name="can-i-still-use-this-reference-architecture-if-my-organization-only-has-one-data-producer-.f1ba2201-1ac3-5d7f-b915-51b4ce06ec70"></a>

This guide's data lake reference architecture is still relevant and beneficial even if your organization only has one data producer. Without the centralized catalog, your data producer has to handle the growth of data consumers, which adds increasing complexity and overhead. Your data lake is also a long-term asset for your organization and typically organizations add more data producers. For example, you might need an additional data producer to store sensitive data for compliance reasons or because your organization acquires another business unit that has its own data producer.

## My data lake directly connects one data producer with multiple data consumers. Is this guide's data lake reference architecture still relevant?
<a name="my-data-lake-directly-connects-one-data-producer-with-multiple-data-consumers.-is-this-guide9999999999999999apos-s-data-lake-reference-architecture-still-relevant-.e01edefd-6793-58fa-aa64-2e76fde4d6b8"></a>

The data lake reference architecture would benefit your organization in the long term. You could use a two-step approach and begin by building the centralized catalog for new data consumers. You could then connect your existing data consumers to the centralized catalog.

## Should my organization follow the onboarding and access granting workflow without making changes to it?
<a name="should-my-organization-follow-the-onboarding-and-access-granting-workflow-without-making-changes-to-it-.2cf0f6f6-5b1b-5cb6-9115-11bb073691a8"></a>

No, the main purpose of that section is to illustrate the logical activity blocks required during the onboarding process. All organizations should customize the process and might even have multiple processes, depending on the sensitivity of their data.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
