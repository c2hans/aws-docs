---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/llm-prompt-engineering-best-practices/introduction.html
---

# Prompt engineering best practices to avoid prompt injection attacks on modern LLMs
<a name="introduction"></a>

*Ivan Cui, Andrei Ivanovic, and Samantha Stuart, Amazon Web Services*

The proliferation of large language models (LLMs) in enterprise IT environments presents new challenges and opportunities in security, responsible artificial intelligence (AI), privacy, and prompt engineering. The risks associated with LLM use, such as biased outputs, privacy breaches, and security vulnerabilities, must be mitigated. To address these challenges, organizations must proactively ensure that their use of LLMs aligns with the broader principles of responsible AI and that they prioritize security and privacy.

When organizations work with LLMs, they should define objectives and implement measures to enhance the security of their LLM deployments, as they do with applicable regulatory compliance. This involves deploying robust authentication mechanisms, encryption protocols, and optimized prompt designs to identify and counteract prompt injection attempts, which helps increase the reliability of AI-generated outputs as it pertains to security.

Central to responsible LLM usage is prompt engineering and the mitigation of prompt injection attacks, which play critical roles in maintaining security, privacy, and ethical AI practices. Prompt injection attacks involve manipulating prompts to influence LLM outputs, with the intent to introduce biases or harmful outcomes. In addition to securing LLM deployments, organizations must integrate prompt engineering principles into AI development processes to mitigate prompt injection vulnerabilities.

This guide outlines security guardrails for mitigating prompt engineering and prompt injection attacks. These guardrails are compatible with various model providers and prompt templates, but require additional customization for specific models.

## Targeted business outcomes
<a name="targeted-business-outcomes"></a>
+ Significantly improve the prompt-level security of LLM-powered retrieval-augmented generation (RAG) applications against a variety of common attack patterns while maintaining high accuracy for non-malicious queries.
+ Mitigate the cost of inference by employing a small number of brief but effective guardrails in the prompt template. These guardrails are compatible with various model providers and prompt templates, but require additional model-specific tailoring.
+ Instill higher trust and credibility in the use of generative AI-based solutions.
+ Help maintain uninterrupted system operations, and reduce the risk of downtime caused by security events.
+ Help enable in-house data scientists and prompt engineers to maintain responsible AI practices.
