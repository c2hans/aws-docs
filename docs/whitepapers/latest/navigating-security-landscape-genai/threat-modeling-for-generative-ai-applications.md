---
source_url: https://docs.aws.amazon.com/whitepapers/latest/navigating-security-landscape-genai/threat-modeling-for-generative-ai-applications.html
---

# Threat modeling for generative AI applications
<a name="threat-modeling-for-generative-ai-applications"></a>

 Threats on AI and machine learning (AI/ML) systems are becoming more frequent, moving beyond controlled environments to real-world production deployments. These threats target vulnerabilities such as exposure to personally identifiable information (PII), lack of oversight in decision-making, and insufficient logging and monitoring.

 Conducting a thorough threat model for your generative AI application is essential. Begin by defining the level of agency that you will provide to the LLM and any AI agents that you might use. This involves determining the extent of autonomy and decision-making power the AI system will have.

 Next, clearly define where authentication and authorization should be performed. For guidance on this, see [this blog post](https://aws.amazon.com/blogs/security/implement-effective-data-authorization-mechanisms-to-secure-your-data-used-in-generative-ai-applications/). Align your threat modeling process with established web security and generative AI frameworks such as [MITRE ATLAS](https://atlas.mitre.org/) and [OWASP Top 10 for LLMs](https://owasp.org/www-project-top-10-for-large-language-model-applications/). These frameworks provide comprehensive guidance on potential threats and mitigation strategies specific to AI systems.

 Implement applicable traditional security controls for data security and deploy AI-specific mitigations for AI safety risks. For example, consider implementing controls such as [Amazon Bedrock Guardrails](https://aws.amazon.com/bedrock/guardrails/) to minimize the possibility of your AI-based application generating harmful or biased content. However, it's important to note that traditional controls like perimeter protection don't extend to cover many of the new threat vectors such as model-specific protections (see [Traditional Cybersecurity Controls DO NOT STOP Attacks Against AI](https://www.rsaconference.com/library/blog/traditional-cybersecurity-controls-do-not-stop-attacks-against-ai)). Make sure that you layer traditional controls with emerging controls and capabilities that are designed to address the unique requirements for LLMs and the systems built around them.

 Carefully consider the pros and cons of logging in generative AI systems and determine the appropriate level of logging for your application. This decision will directly impact your ability to monitor, audit, and respond to incidents.

 Finally, establish incident response plans that align with your logging capabilities and the specific risks associated with your generative AI application.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
