---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/azure-to-aws-platform-migration/targeted-business-outcomes.html
---

# Targeted Business Outcomes
<a name="targeted-business-outcomes"></a>

Data platform migration is a common enterprise initiative, typically taking one of the following forms:
+ Lift-and-shift or re-platforming
+ Re-engineering
+ Cross-cloud migration to Amazon Web Services (AWS)
+ Migration from third-party applications to AWS-native solutions

A recurring challenge across migration initiatives is the assessment of the current environment. Gaps in documentation, limited access to subject matter experts (SMEs), and incomplete inventories make it difficult to establish a clear picture of the existing state. This leads to:
+ Poor understanding of the current environment
+ Insufficient visibility into the inventories needed to form an accurate estimation basis

Together, these gaps contribute to schedule slippage, budget overruns, and unmet customer business outcomes.

During a large-scale data platform migration, the team introduced Generative AI (GenAI) to address these challenges and explore whether it could accelerate the assessment process and reduce the time required to produce implementation-ready documentation.

The initial results were promising but limited. Due to the non-deterministic nature of large language models (LLMs), prompt engineering alone proved insufficient — models cannot reliably infer knowledge of an existing system or generate migration documentation with actionable steps to the future state.

To address this, the team developed a context layer to ground the model in the customer's actual environment. This involved:
+ **Automated inventory collection** via custom scripts
+ **Requirement capture** from the Statement of Work (SoW), project specifications, and meeting transcripts — converted to plain text and provided as context to the model

With proper context in place, the model was able to map relationships among data lake components, identify infrastructure dependencies, populate inventory templates, complete assessment reports, and generate targeted questionnaires for customer SMEs.

This approach delivered several key outcomes:
+ **Reduced reliance on customer documentation — **consultants engaged customers to validate system understanding rather than gather baseline information
+ **Shorter requirement workshops** — customers spent less time in lengthy discovery sessions, and the risk of manual omissions due to knowledge gaps was reduced
+ **Faster assessment and planning** — during the referenced engagement, timelines were cut by approximately half compared to fully manual approaches, through AI-assisted inventory population, documentation generation, and cross-referencing
+ **Stronger estimation basis** — comprehensive inventory collection reduced the risk of schedule slippage and cost overruns during migration planning
+ **Traceable documentation** — every resource count, resource name, and architectural claim links back to source data
+ **Reusable knowledge repository** — all context layers (data, relationships, human knowledge) are preserved, enabling rapid regeneration of deliverables when stakeholder requirements or framing change
+ **Risk identification** — documented gaps in current customer processes surfaced risks and informed mitigation strategies

This guide presents a generic, portable, and reusable assessment approach that requires no specialized AI or agentic skills and adds no additional cost to the project beyond standard AI token expenses.
