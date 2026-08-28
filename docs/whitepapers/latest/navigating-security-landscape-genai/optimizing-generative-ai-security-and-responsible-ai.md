---
source_url: https://docs.aws.amazon.com/whitepapers/latest/navigating-security-landscape-genai/optimizing-generative-ai-security-and-responsible-ai.html
---

# Optimizing generative AI security and responsible AI
<a name="optimizing-generative-ai-security-and-responsible-ai"></a>

 Understanding the distinct yet complementary roles of generative AI security and [responsible AI](https://aws.amazon.com/ai/responsible-ai/) is essential for comprehensive risk management. While security safeguards systems and data assets, responsible AI addresses broader safety imperatives including bias prevention, output reliability, and ethical considerations. Both security and responsible AI controls must be integrated throughout the entire AI system lifecycle within an organization.

 Traditional security controls focused on perimeter protection and data access are necessary but insufficient for generative AI systems, which face unique threat vectors such as prompt injection, model poisoning, and adversarial exploits. This new landscape requires innovative security approaches specifically designed for AI architectures.

 Calibrate your risk strategy based on deployment context and user exposure. For example, internal enterprise applications warrant different controls compared to public-facing AI systems. Define specific thresholds for both security risks (such as data exposure) and AI safety risks (including bias, harmful content generation, and hallucinations). Given the probabilistic nature of generative AI outputs and associated risks, safety controls might need more stringent thresholds than traditional security measures. Align your risk framework with established standards like the [NIST AI Risk Management Framework (RMF)](https://www.nist.gov/itl/ai-risk-management-framework) while adapting controls for AI-specific challenges.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
