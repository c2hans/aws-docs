---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/azure-to-aws-platform-migration/ai-driven-assessment-methodology.html
---

# AI Driven Assessment Phases
<a name="ai-driven-assessment-methodology"></a>

## Assessment Phases
<a name="assessment-phases.a20b8f33-eb45-5c96-841c-7e34e2519460"></a>

**Phase 1 - Work Decomposition and Environment Setup — **Structure project planning to enable AI tools to operate on discrete, actionable content. This phase produces epics and user stories with detailed acceptance criteria.

**Phase 2 - Source Environment Discovery** — An AI assistant generates extraction scripts that collect raw inventory data from the source environment in CSV format. Environment owners validate the resulting CSVs to finalize the current-state inventory assessment.

**Phase 3 - Current State Documentation** — An AI assistant classifies and contextualizes inventory data to build knowledge of the current environment and prepares current-state assessment documentation.

**Phase 4 - Stakeholder Collaboration and Knowledge Capture** — Environment SMEs contribute process knowledge, decisions, and migration intent. Consultants capture and organize this information to provide the AI assistant with meaningful environment context.

**Phase 5 - Target State Design and Migration Strategy** — The AI assistant generates target-state documentation and refines it based on future-state requirements and the knowledge accumulated across previous phases.

## How AI Fits in This Workflow
<a name="how-ai-fits-in-this-workflow.9941449a-efa2-5cfb-be29-dd7725bfb134"></a>

AI's role shifts as available context grows.

In Phase 2, AI acts as a ***toolmaker****:* it generates the extraction scripts that you manually execute to pull structured data from the source environment. Deterministic scripts collect the raw inventory data.

In Phase 3, AI acts as an ***analyst****:* it reads across hundreds of CSVs to classify resources into business domains, identify relationships between components, and write contextual descriptions for each inventory row. Work that typically takes days or weeks — reading every row in the context of every other row — completes in hours. Deterministic scripts pre-compute all totals; AI uses those numbers verbatim.

In Phase 4, AI acts as a ***knowledge consumer****:* meeting transcripts, architecture documents, and stakeholder feedback contain the process knowledge, decisions, and intent that do not exist in inventories. Consultants organize this knowledge into indexed, structured markdown so AI can find and reference specific discussions without loading entire transcripts into context.

In Phase 5, AI acts as a ***synthesizer****:* with all four layers assembled, it generates target-state migration document. When requirements change or stakeholders want different views of the same information, AI regenerates documentation on demand using the underlying repository as context.

The validation pattern is consistent throughout: ***AI generates, scripts validate, consultants approve.*** This loop typically runs 2-3 iterations per deliverable before all counts, references, and stakeholders align.

## Context
<a name="context.bc1689eb-bce8-5345-8eb1-c8b684a0a485"></a>

AI's effectiveness depends on the context it can access. A migration assessment requires four distinct layers of knowledge, each building on the previous:

1. **Raw inventory data** — structured CSV exports from the source environment

1. **Relationships between components** — which resources connect to which, which pipelines deploy what

1. **Stakeholder process knowledge** — decisions, intent, and operational context from meetings and stakeholder input

1. **Synthesized current-state understanding** — the documentation that combines all three layers above

The methodology progressively builds these layers so that by the final phase, AI has sufficient context to generate target-state deliverables rapidly and regenerate them when requirements change.

## Prerequisite for AI Assistance
<a name="prerequisite-for-ai-assistance.7162dc10-65c1-554c-9257-049372acc5c9"></a>

At minimum, the AI assistant must be able to:
+ Read files in a repository (CSVs, markdown, transcripts, configuration files)
+ Create new files and write structured content (markdown, CSV)
+ Update existing files without corrupting adjacent content
+ Process structured prompts that reference multiple input files
+ Generate Mermaid diagrams from relationship data

Kiro (AWS agentic coding service) — the AI tool that the referenced engagement used — has these capabilities built in. The reference implementation uses an AI assistant that embeds in an IDE, though a CLI-based assistant works equally well.
