---
source_url: https://docs.aws.amazon.com/whitepapers/latest/navigating-security-landscape-genai/scoping-generative-ai-use-cases.html
---

# Scoping generative AI use cases
<a name="scoping-generative-ai-use-cases"></a>

The first step in developing a robust security strategy for generative AI is to properly scope its use within your organization. See the [AWS Generative AI Security Scoping Matrix](https://aws.amazon.com/ai/generative-ai/security/scoping-matrix/) (shown in the following figure) to categorize your use cases.

![Generative AI Security Scoping Matrix, a mental model to classify use cases.](http://docs.aws.amazon.com/whitepapers/latest/navigating-security-landscape-genai/images/gen-ai-security-scoping-matrix.png)

 The scoping matrix includes five scopes. For Scope 1 or Scope 2 applications, which typically involve off-the-shelf AI solutions, adopt a buyer's perspective. Focus on risk management through data governance and carefully review enterprise agreements. It's crucial to clearly understand which data is authorized for sharing and under what circumstances. While Scope 2 applications would typically be built to support enterprise data security and compliance needs, Scope 1 applications most often are not.

 For Scope 3, 4, or 5 applications, which involve more customized or internally developed AI solutions, adopt a builder's perspective. Determine what data is in scope for the application and conduct thorough threat modeling (detailed in [Threat modeling for generative AI applications](https://aws.amazon.com/blogs/security/threat-modeling-your-generative-ai-workload-to-evaluate-security-risk/)). In these three scopes, while you generally have more control over your data, you also have more responsibility in protecting it. Be aware that the complexities for managing both the model and data components progressively increase as you move from Scope 3 through Scope 5, requiring increasingly rigorous security considerations at each level.

 For all scopes, the way you approach governance and compliance, legal and privacy, risk management, controls, and resilience requirements will vary. However, by understanding the scopes that align to your use cases, you can quickly narrow down how you will address the requirements that align to these different security dimensions.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
