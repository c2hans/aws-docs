---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/gen-ai-lifecycle-operational-excellence/dev-experimenting-prompt-lifecycle.html
---

# Managing the generative AI prompt lifecycle
<a name="dev-experimenting-prompt-lifecycle"></a>

As central components of a generative AI system, prompts cannot be treated as simple text files that are unplanned and unmanaged. They are critical software artifacts that demand a rigorous, disciplined lifecycle management process, similar to application code. Establishing a formal lifecycle drives quality, reproducibility, collaboration, and safe deployment of prompt changes.

Use the following mechanisms to properly manage your prompts throughout their lifecycle:
+ **Versioning** – Prompts must be versioned to track their evolution and enable rollbacks. Crucially, versioning a prompt goes beyond just tracking changes to the text. Each version's identity is defined by its performance. Therefore, a version number must be intrinsically linked to the comprehensive evaluation results it produced. This is described more in the following sections. For example, if the team discusses `customer-support-summarisation-v2.1.0`, they are referring to more than the template—they are also referring to its known set of performance metrics on a specific evaluation dataset.
+ **Prompt store and registry** – To enable independent iteration and management, prompts must be decoupled from the application code. They should be stored in a centralized prompt store or registry. This can range from a version-controlled Git repository that contains YAML or JSON configuration files to a dedicated prompt management tool, such as [Langfuse](https://langfuse.com/docs/prompt-management/get-started). This separation helps prompt engineers or even non-technical domain experts to update and experiment with prompts without requiring a full application redeployment.
+ **Smart labeling and documentation** – Each prompt version requires clear and consistent metadata.
  + **Labeling conventions** – Adopt a structured format, such as `<feature>-<purpose>-<version>` to make the purpose of each prompt immediately obvious.
  + **Structured documentation** – For each version, maintain documentation that tracks its purpose, the rationale for changes, expected output format, and key performance metrics from evaluations. This documentation is invaluable for debugging and onboarding new team members.
+ **Collaborative workflows** – Prompt development should be a collaborative process. It's a best practice to implementing a pull request (PR)-style workflow for prompt changes, especially in staging and production environments. This allows for peer review, discussion, and quality assurance before a change is merged. It also creates an audit trail of who changed what, when, and why.
+ **Environment promotion** – Just like application code, prompts must be managed across different environments. A typical promotion path is development to staging (or preproduction) to production:
  + **Development** – An environment for rapid iteration and experimentation.
  + **Staging** – A stable environment for rigorous testing and validation of prompt changes against a proven evaluation set before they are deployed to users.
  + **Production** – The live environment that serves users. Changes are promoted to production only after passing all tests in staging. This structured approach prevents experimental changes from accidentally impacting users and promotes a high-quality, reliable experience.

For more information about prompt management, see the following resources:
+ [Prompt versioning & management guide for building AI features](https://launchdarkly.com/blog/prompt-versioning-and-management/) (LaunchDarkly blog post)
+ [Prompt, agent, and model lifecycle management](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-serverless/prompt-agent-and-model.html) (AWS Prescriptive Guidance)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
