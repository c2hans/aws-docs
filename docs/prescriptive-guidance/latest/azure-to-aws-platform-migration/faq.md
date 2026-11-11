---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/azure-to-aws-platform-migration/faq.html
---

# FAQ
<a name="faq"></a>

## Why AI-assisted instead of manual documentation?
<a name="why-ai-assisted-instead-of-manual-documentation-.ba3e0335-a245-566f-b482-e3cdb5b52a76"></a>

This methodology does not claim that AI is "as good as" manual documentation — rather, the combination of AI generation with deterministic validation produces documentation with higher accuracy and coverage than manual review alone. A consultant manually documenting 200\+ resources across 8 subscriptions will miss relationships, miscount environment breakdowns, and introduce inconsistencies between sections. AI reads every row in the context of every other row, and the validation pipeline catches every count mismatch deterministically. Manual review does not have that safety net.

The methodology also preserves all knowledge in a structured, queryable repository. When requirements change or a stakeholder asks a question six weeks later, AI can regenerate deliverables or answer from source data — not from someone's memory of what they wrote.

## How do I handle sensitive data in AI prompts?
<a name="how-do-i-handle-sensitive-data-in-ai-prompts-.9903d69f-bc48-53ce-a8bd-dcccb23b3d50"></a>

The AI prompts in this methodology reference source data files (CSVs, transcripts) rather than embedding sensitive data directly in prompts. AI reads the files at execution time. This means sensitive data flows through the AI's context but is not stored in the prompt templates themselves. For environments with strict data handling requirements, consider using AI that runs within your security boundary rather than cloud-hosted AI services.

## Can this methodology be applied to migrations other than Azure to AWS?
<a name="can-this-methodology-be-applied-to-migrations-other-than-azure-to-aws-.0f0e2e75-528a-50ed-bfc6-7432876273a2"></a>

Yes. The methodology is platform-agnostic in its structure. The extraction scripts are cloud-provider-specific, but the prompt architecture, validation pipeline, transcript indexing, and acceptance criteria patterns apply to any migration assessment. You would need to generate equivalent extraction scripts for the source platform (Phase 2's AI prompts handle this) and update the Phase 3 prompts to reference the appropriate source data formats.

## How many people does this methodology require?
<a name="how-many-people-does-this-methodology-require-.1ce5b5d0-3fe8-5654-93e9-0e10a0e44b19"></a>

We developed this methodology for a team of 2-3 consultants working on the multi-month engagement described in this guide. This accelerator does not replace team members however it reduces the project timeline by roughly 50%, resulting in reduced delivery costs. A data engineer still needs to understand the source environment and validate the output. An architect still needs to make design decisions; however, this accelerator handles the documentation effort that would otherwise consume 40-60% of the team's time, and—critically—it preserves all the knowledge in a structured repository so that when requirements change or new information emerges, the team can regenerate affected deliverables rather than rewriting them manually.

## What's in it for customers?
<a name="what-s-in-it-for-customers-.a0fe9e88-4bf7-53e6-9d0f-72204cf94199"></a>

During the engagement described in this guide, this methodology reduced required customer SME involvement by approximately 60–70% during the assessment and inventory collection phase. Rather than asking stakeholders to walk us through the environment from scratch, we derived system understanding directly from the inventories — mapping relationships and dependencies before the first meeting. Customer SMEs then validated and refined our understanding, rather than building it from the ground up.

Beyond time savings, this approach delivers measurable project outcomes:
+ **Reduced assessment effort and cost** by more than 50%
+ **Mitigated the risk of schedule slippage and cost overrun** by approximately 65%, through comprehensive inventory collection and a rigorous estimation basis
+ **Reduced source-to-destination (S2D) migration failures** by ensuring every architectural claim and resource dependency is traceable to validated source data before migration begins
