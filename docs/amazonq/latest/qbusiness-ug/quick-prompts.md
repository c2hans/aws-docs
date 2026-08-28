---
source_url: https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/quick-prompts.html
---

Amazon Q Business is no longer open to new customers. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

# Quick prompts in Amazon Q Business
<a name="quick-prompts"></a>

The Amazon Q Business web experience welcome page provides sample prompts to help your end users understand the types of questions and tasks that they can ask. Sample prompts are not enabled by default.

If you're an AWS Management Console customer who needs to configure the web experience for your end users, you can enable the sample prompts feature when you preview the web experience. For more information, see [Customizing a web experience (IAM Identity Center)](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/customizing-web-experience.html) or [Customizing a web experience (IAM)](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/customizing-web-experience.html).

**Important**
Before you enable sample prompts, make sure that the **Only produce responses from retrieval augmented generation (RAG)** check box for **Application guardrails** is not selected. For more information, see [Customizing global controls](guardrails-global-controls.md#guardrails-global-controls-customizing).
You can't create your own prompts or edit the provided sample prompts.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Q. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazonq` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
