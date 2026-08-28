---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/gen-ai-lifecycle-operational-excellence/dev-experimenting-model-selection.html
---

# Choosing models for generative AI applications
<a name="dev-experimenting-model-selection"></a>

Every generative AI PoC begins with a fundamental question: which model should I use? This isn't about finding the best model in absolute terms, but rather identifying the right starting point for your specific use case and constraints. The model you choose becomes the engine that powers all subsequent experimentation. This decision is foundational to development velocity and cost efficiency.

Start by mapping your use case requirements to model capabilities across multiple dimensions:
+ **Functional requirements mapping** – Identify non-negotiable capabilities upfront. If your PoC requires analyzing images of documents, you need multi-modal support. If it involves orchestrating multiple API calls, function-calling capability is essential. For specialized domains (such as medical, legal, or non-English markets), consider models that have been pretrained on relevant datasets to reduce the prompt engineering overhead. These requirements can immediately narrow the field of viable models.
+ **Performance and cost trade-offs** – Balance model intelligence against operational costs from day one. Although starting with a capable model helps establish quality baselines, simultaneously test smaller variants to understand the quality degradation curve. A customer support bot might achieve 95% accuracy with a large model at $0.50 per conversation, but some business might prefer 90% accuracy with a smaller model at $0.05 per conversation.
+ **Latency considerations** – Different use cases have vastly different response time tolerances. Real-time applications (such as autocomplete functions or voice interactions) require sub-second responses. Analytical tasks (such as report generation and research) can accommodate multi-second latencies or longer. Test response times early, including network overhead and any pre or post-processing, to make sure that your chosen model can meet user experience requirements. Sometimes a smaller, faster model provides better overall user experience than a more capable but slower alternative.

We recommend the following to help you avoid common pitfalls when selecting a model:
+ **Don't over-optimize prematurely** – The PoC phase is about proving feasibility, not achieving perfect optimization.
+ **Don't ignore specialized models** – If you're working in a specific domain, test domain-specific models early.
+ **Don't assume bigger is better** – Sometimes a smaller, faster model with well-crafted prompts can outperform a larger model for specific tasks.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
