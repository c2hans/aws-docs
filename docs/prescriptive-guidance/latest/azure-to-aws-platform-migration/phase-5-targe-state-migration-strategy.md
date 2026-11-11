---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/azure-to-aws-platform-migration/phase-5-targe-state-migration-strategy.html
---

# Phase 5 - Target State Design and Migration Strategy
<a name="phase-5-targe-state-migration-strategy"></a>

After you validate and assemble all current-state context — raw inventories, AI-generated relationships, enriched inventory CSVs, meeting transcripts with indexes, and accurate acceptance criteria documents — the AI assistant generates target-state migration documents.

Target-state design also draws on future-state requirements that the current environment doesn't reflect: the customer's preferred AWS services and patterns, security and compliance controls, performance and availability targets, cost constraints, and any modernization goals beyond a like-for-like migration. Capture these requirements in meeting transcripts or scoping documents so that the AI assistant can apply them.

This phase includes two stages. First, AI assistant generates a high-level target state architecture that maps every current-state component to its target equivalent and establishes the major architectural decisions. Architects review and approve this document before detailed work begins. Second, AI assistant fills the target-state acceptance criteria one at a time, using the approved architecture as the guiding constraint.

This two-stage approach prevents the AI assistant from making independent architectural decisions in each acceptance criterion that might contradict each other. The high-level document is the contract between architects and the AI assistant — every detailed acceptance criterion must comply with it.

## High-Level Target State Architecture
<a name="high-level-target-state-architecture"></a>

The high-level architecture document is the 10,000-foot view. It maps current-state components to target services, captures the major architectural decisions from transcripts, and establishes the patterns that all detailed acceptance criteria must follow.

### AI prompt:
<a name="ai-prompt-.13f2fe1d-5875-5839-8279-8425a004f316"></a>

```
Generate a high-level target state architecture document that maps every
current-state component to its target equivalent.

CONTEXT:
- Current State ACs: work-breakdown/ (all filled current-state AC files)
- Enriched Inventories: work-breakdown/*/excel-template/inventory-*.csv
- Meeting Transcripts: sources/meeting-transcripts/ (read README.md index first)
- Domain Definitions: sources/domains.csv
- Resource Relationships: sources/current-state-inventory/[cloud]/cloud-envs/resource-relationships.md
- Pipeline Relationships: sources/current-state-inventory/[cloud]/devops-envs/pipeline-relationships.md

Generate a document covering:

1. SOURCE-TO-TARGET SERVICE MAPPING
   For every resource type in the current-state inventory, map to the AWS
   equivalent. Include current count, target service, and migration notes.
   Every raw inventory item must be accounted for.

2. ARCHITECTURAL DECISIONS
   Reference specific meeting sessions where decisions were made. For each:
   - What was decided (e.g., "dual ingestion during transition, not data sync")
   - Why (rationale from the transcript)
   - Impact on target architecture
   Flag undecided items as "[ARCHITECT DECISION NEEDED]".

3. MIGRATION PATTERNS
   Establish the repeatable patterns:
   - Storage migration pattern (zone mapping, replication strategy)
   - Compute migration pattern (workspace structure, cluster policies)
   - Pipeline migration pattern (CI/CD tool mapping, trigger conversion)
   - Monitoring migration pattern (alert mapping, dashboard recreation)

4. MIGRATION SEQUENCING
   High-level wave structure based on dependency analysis from
   resource-relationships.md and pipeline-relationships.md.

5. RISK PROFILE
   Top risks from technical complexity, operational gaps, and integration
   dependencies identified in the current-state assessment.

RULES:
- Ground every mapping in specific current-state resource names and counts
- Reference specific meeting sessions for every architectural decision
- Flag anything not yet decided as "[ARCHITECT DECISION NEEDED]"
- This document will be reviewed by architects before detailed ACs are filled
```

The AI assistant produces a draft target-state architecture document. Architects review it and then approve the decisions, change them, or flag the ones that need more discussion. Start the detailed acceptance criteria only after architects approve the high-level architecture.

## Filling Target-State Acceptance Criteria
<a name="filling-target-state-acceptance-criteria"></a>

With the approved high-level architecture as the guiding constraint, AI assistant fills the target-state acceptance criteria one at a time — the same process as current-state acceptance criteria in Phase 4. Each acceptance criterion covers its specific area in depth and complies with the decisions in the approved architecture document.

### AI prompt:
<a name="ai-prompt-.45dd5bde-3d88-59a7-9a89-a7c3d1df66d0"></a>

```
Fill out this target-state acceptance criteria document using the approved
high-level architecture, current-state assessment, and meeting transcripts.

CONTEXT:
- Approved Architecture: deliverables/[name]_Target_State_Architecture_v0.1.md
- Current State ACs: work-breakdown/ (all filled current-state AC files)
- Enriched Inventories: work-breakdown/*/excel-template/inventory-*.csv
- Meeting Transcripts: sources/meeting-transcripts/ (read README.md index first)
- Domain Definitions: sources/domains.csv
- Target-State AC: work-breakdown/[epic]/target-state/[user-story]/ac-NN-name.md

Fill in the placeholder sections in the AC document. This AC must comply
with the architectural decisions in the approved architecture document.

For each component covered by this AC:
- Reference the specific current-state resource by name and count
- Map to the target service per the approved architecture
- Include migration approach, validation criteria, and rollback method
- Reference meeting sessions where relevant decisions were made

RULES:
- Every claim must be grounded in source data with specific names and counts
- Every architectural decision must match the approved architecture document
- Flag anything that contradicts or extends the approved architecture as
  "[ARCHITECT REVIEW NEEDED]"
- Do NOT count or summarize yourself — use validation script output
- Do NOT make architectural decisions — reference the approved document
```

The consultant reviews each acceptance criterion through iterative chat, then runs the validation script (see Phase 4) to confirm the counts match. The same validation loop applies: AI assistant writes → script validates → you apply corrections.

## Delivering Final Documents
<a name="delivering-final-documents"></a>

The final step is converting the validated markdown deliverables to the formats stakeholders expect.

### Producing Final Deliverables
<a name="producing-final-deliverables.78fb6e3f-f183-5113-b023-868971183a99"></a>

After you fill and validate all target-state acceptance criteria, roll them up into one deliverable per user story by using the approach described in Phase 4. If you don't have a rollup script, ask your AI coding assistant to generate one from that description.

### Converting Markdown To Word and Excel
<a name="converting-markdown-to-word-and-excel.9138bbbd-575e-55c9-ba19-6dd2730b9beb"></a>

Stakeholders usually expect Word and Excel documents. AI assistants with document-generation capabilities can convert the rolled-up Markdown deliverables to Word (.docx) and Excel (.xlsx) files, including tables of contents, numbered headings, and consistent styling. For production use, you can access foundation models through [Amazon Bedrock](https://aws.amazon.com/bedrock/), which provides managed security and compliance capabilities. If your AI assistant can't generate documents, open-source libraries such as python-docx and openpyxl, or a converter such as Pandoc, can turn Markdown into Word files based on a template.

### Incorporating Stakeholder Feedback
<a name="incorporating-stakeholder-feedback.ba5557eb-5740-5a74-9fc4-7e8a36c41df8"></a>

Keep the Markdown files as the source of truth, even after stakeholders start editing Word copies. When stakeholders return edited Word documents, convert them back to Markdown and use the AI assistant to merge the feedback into the source files. Then run the validation script again to confirm the counts still match, and regenerate the Word documents for the next review. This round trip keeps the validation checks working while stakeholders still work in familiar tools.

### Additional Deliverables
<a name="additional-deliverables.8963795e-fcb1-5f49-a7f2-cf9986f6bfd1"></a>

With all current-state and target-state context assembled in the repository, AI assistant can generate additional deliverables beyond the core assessment documents. Because the repository preserves all knowledge layers, the AI assistant can also regenerate any deliverable when requirements change.
+ Risk registers with severity ratings, mitigation strategies, and owners
+ Training and upskilling plans tailored to each business domain's migration path
+ Preliminary work breakdown structures with hour estimates per migration wave
+ Gantt charts or timeline visualizations for migration sequencing
+ Runbooks for disaster recovery (DR), failover, and operational procedures on the target platform
+ Cost comparison models mapping current spend to projected target costs
+ Data lineage diagrams per business domain, built from enriched data-asset rows (`Reads From` / `Writes To` / `Schedule`)
+ Data quality rule extraction from existing tooling (Great Expectations, Soda, dbt tests) — captured as a portable rule inventory for re-implementation on the target platform
+ Deeper extraction of third-party data tooling (Informatica, Talend, dbt, Collibra) using the same Phase 2 AI-prompt pattern applied to each tool's API
+ Ad-hoc query log analysis from the warehouse query history — usage hotspots, unused tables, top consumers, and peak concurrency patterns to inform target sizing

Each of these draws from the same knowledge layers — raw inventories, relationships, transcripts, and validated acceptance criteria — so AI assistant can produce them rapidly and ground every claim in source data.

### Queryable Knowledge Repository
<a name="queryable-knowledge-repository.e9037726-d679-56b4-b543-1f0f7952766a"></a>

Beyond generating documents, the assembled repository becomes a queryable knowledge repository for the engagement. When a stakeholder asks why a particular architectural decision was made, the AI assistant searches the transcript root index, finds the session where that decision was discussed, and provides the exact rationale with a reference to the timestamp. When someone asks how many resources of a given type exist in production and what their configurations are, the AI assistant reads the enriched inventory CSV and answers with specific names, counts, and configurations — not approximations.

This turns the repository into a living reference that supports fast, accurate responses to stakeholder questions throughout the engagement and beyond.
