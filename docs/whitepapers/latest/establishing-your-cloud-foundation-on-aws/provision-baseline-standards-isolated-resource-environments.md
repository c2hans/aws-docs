---
source_url: https://docs.aws.amazon.com/whitepapers/latest/establishing-your-cloud-foundation-on-aws/provision-baseline-standards-isolated-resource-environments.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Provision baseline standards to isolated resource environments
<a name="provision-baseline-standards-isolated-resource-environments"></a>

In addition to provisioning guardrails to isolated resource environments, it is also necessary to provision other baseline requirements within the environment. This can include roles, network components and connectivity, and security applications or services.

In order to maintain consistency in configuration across different resource environments, the baseline configuration should be deployed in an automated fashion in existing or newly created isolated resource environments. This can include roles, network connectivity, or operational or security services. It is often helpful to be able to apply baseline configurations globally (to all isolated resource environments) or to logical groupings of the isolated resource environments. Global baselines will apply to all isolated resource environments and therefore should be considered carefully. Isolated resource environments should be grouped and organized in a way that allows baseline configurations to be applied to the logical grouping of environments. For example, it is common to apply stricter controls on production environments than in development environments. Therefore, production environments should be grouped in a way that allows for different baseline configurations to be applied to production environments and development environments.

Once the different stakeholders are identified, we recommend you align them to the [Shared Responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/). This will enable you to define a cloud operating model for your environment, where all the different teams involved in creating or enhancing your environment are aware of what needs to be done to move forward. Processes and standards are easier to manage, and they are visible across your organization.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
