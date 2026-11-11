---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/azure-to-aws-platform-migration/phase-4-knowledge-capture.html
---

# Phase 4 - Knowledge Capture
<a name="phase-4-knowledge-capture"></a>

This phase has three parts: organizing human knowledge so that the AI assistant can use it, filling out the acceptance criteria documents with all available context, and validating the result before producing deliverables.

## Getting Transcripts Into the Repository
<a name="getting-transcripts-into-the-repository"></a>

Convert meeting recordings (from Zoom, Microsoft Teams, or similar platforms) to Markdown and store them in a dedicated transcripts folder in the repository. Most platforms export transcripts as plain text or Web Video Text Tracks (VTT) files, which you can clean up and save as Markdown. You can organize transcripts into subfolders by topic, team, or event. For example, an onsite workshop can have its own subfolder. Keep every transcript under one root folder so that a single root index can cover all of them. Each transcript gets its own companion index stored next to it.

## Meeting Transcript Indexing
<a name="meeting-transcript-indexing"></a>

Meeting transcripts contain the *why* and *how* that no extraction script can capture: architectural intent, operational constraints, and migration decisions. A 3-hour meeting produces more than 30,000 words, and an engagement can build up dozens of sessions. Loading every transcript into each the AI assistant request increases cost and response time, and important details are more likely to get lost in unrelated discussion. A tree-structured index lets the AI assistant go straight to the knowledge it needs.

The index has three levels: a root index that maps topics to sessions across all subfolders, a companion index for each session that maps topics to timestamps, and the raw transcripts. The AI assistant works down the tree, from root index to companion index to the relevant transcript section.

After each meeting, use the following prompt to create a companion index for that transcript.

### AI prompt:
<a name="ai-prompt-.7292c5e6-489f-512d-a69c-cdf811695588"></a>

```
Create a companion index for this meeting transcript.

CONTEXT:
- Raw Transcript: sources/meeting-transcripts/[subfolder/][session-name].md
- Epics and User Stories: work-breakdown/epics.md
- Domain Definitions: sources/domains.csv

Create [session-name].companion.md containing:
- Topic Index: timestamp ranges with specific topics and key details
- Key Decisions: numbered list of actual decisions (not discussion points)
- Key Facts: specific quantitative facts (counts, configs, costs, timelines)
- Action Items: owner + description + timeline

RULES:
- Be specific in topic indexes — include actual numbers and details
- Key facts must be verifiable — actual numbers, not "several" or "many"
- Decisions must be clear and actionable — "Unity Catalog migration before
  workspace migration" not "discussed Unity Catalog"
```

Once all companion indexes are created, use this prompt to build the root index:

### AI prompt:
<a name="ai-prompt-.47cd9361-31e6-5a27-8f36-7f9808415b9c"></a>

```
Build the root index from all companion indexes.

CONTEXT:
- Companion Indexes: sources/meeting-transcripts/**/*.companion.md (all subfolders)
- Epics and User Stories: work-breakdown/epics.md

Create/update sources/meeting-transcripts/README.md mapping topics to sessions
across all companion indexes. Organize by deliverable category: Architecture,
Data Assets, Operations, Migration Strategy, Risk, Integrations, Testing.

Also identify gaps: compare transcript coverage against user stories. Output
which user stories have no coverage, partial coverage, and which topics
discussed don't map to any user story.

RULES:
- Read ALL companion indexes before building the root index
- Every topic should reference at least one session
- Topics that span multiple sessions should list all relevant sessions
```

### Example companion index:
<a name="example-companion-index-.9592e25a-0051-5cab-a1f5-26b26753f9ec"></a>

```
# Meeting Companion: Architecture Review

## Topic Index
| Time Range | Topic | Key Points |
|---|---|---|
| 0:00-0:15 | Introductions and scope | Confirmed 4 environments in scope |
| 0:15-0:45 | Storage architecture | 6 data zones, ~450TB total, ADLS Gen2 |
| 0:45-1:10 | Compute architecture | 3 Databricks workspaces, Unity Catalog planned |
| 1:10-1:30 | Orchestration | Airflow on VMs, Python wrapper pattern |

## Key Decisions
1. Unity Catalog migration will happen before workspace migration
2. Dual ingestion during transition (not data sync)
3. DR site is cold standby, not active-active

## Key Facts
- Total storage: ~450TB across 6 zones
- Databricks clusters: 14 production, 8 non-production
- Daily ingestion volume: ~2.5TB
- Orchestration: 350+ Airflow DAGs

## Action Items
- [Architect] Document storage zone mapping to S3 bucket structure
- [Data Engineer] Export Databricks cluster configurations
- [Operations] Provide patching schedule and maintenance windows
```

The AI assistant reads the root index, identifies which session covers the topic it needs, reads that session's companion index for the specific timestamp range, and only then reads the relevant section of the raw transcript if needed.

## Filling Out Acceptance Criteria Documents
<a name="filling-out-acceptance-criteria-documents"></a>

The AI assistant uses all four knowledge layers (raw inventories, AI-generated relationships, enriched inventory CSVs, and indexed meeting transcripts) to complete the acceptance criterion documents one at a time.

Each acceptance criterion file already has pre-generated section structures and placeholders from Phase 1. The AI assistant reads the acceptance criterion file, the relevant inventory CSVs, the relationship docs, and the transcript index, then fills in the placeholders with real data. The consultant reviews, requests changes through chat, and iterates until the acceptance criterion is accurate.

This is where the small-context advantage of separate acceptance criterion files pays off. The AI assistant works on one document at a time with only the relevant inventory CSVs, relationship documents, and transcript index entries, rather than trying to hold an entire deliverable in context.

### AI prompt:
<a name="ai-prompt-.ce8d4542-c5a2-507f-a5d7-f7eb997491d7"></a>

```
Fill out this acceptance criteria document using the inventory data,
relationship docs, and meeting transcripts.

CONTEXT:
- AC Document: work-breakdown/[epic]/[user-story]/ac-NN-name.md
- Raw Inventories: sources/current-state-inventory/[cloud]/cloud-envs/*/csv-data/
- Enriched Inventories: work-breakdown/*/excel-template/inventory-*.csv
- Resource Relationships: sources/current-state-inventory/[cloud]/cloud-envs/resource-relationships.md
- Pipeline Relationships: sources/current-state-inventory/[cloud]/devops-envs/pipeline-relationships.md
- Per-subscription Summaries: sources/current-state-inventory/[cloud]/cloud-envs/*/resource-summary.md
- Meeting Transcripts: sources/meeting-transcripts/ (read README.md index first)
- Domain Definitions: sources/domains.csv

Fill in the placeholder sections in the AC document with real data. The
document structure is dictated by the acceptance criteria — follow the
headings and sections already scaffolded in the AC file.

When the AC references inventory items (e.g., listing resources per
environment), present them as nested lists with a consistent grouping.
The default grouping is by business domain (from sources/domains.csv),
but the grouping can be anything specified in the prompt — by environment,
by resource type, by architecture layer, etc.

INVENTORY LIST STRUCTURE (when referencing inventory items):
- **[Group]**: N [Resource Type]
  - **[Sub-group]** (count)
    - resource-name - purpose (deployed by: pipeline) ([inventory CSV, row N])

ROW REFERENCES: [inventory-XX-name.csv, row N](./excel-template/inventory-XX-name.csv)
CROSS-REFERENCES: pipeline-name | [DevOps](url) | [inventory-01.csv, row N](path)

RULES:
- All counts, resource names, and row references must come from inventory CSVs
- ac-01 is the source of truth — ac-02/03/04 must match its counts and names
- Every resource name must exist in the corresponding CSV
- Do NOT count resources yourself — use pre-computed counts from resource-counts.md
- Do NOT generate summary totals — use validation script output
- Incorporate relevant context from meeting transcripts (decisions, constraints,
  operational details) where the AC sections call for it
```

## Generate Validation Script
<a name="ai-prompt-generate-validation-script"></a>

**Why this step matters**

Large language models (LLMs) can write fluent, convincing text that still contains wrong counts or resource names that don't exist. In a migration assessment, a single wrong number can carry into the effort estimate, the staffing plan, and the cost model. After you fill and refine the acceptance criterion documents, run a validation script to confirm that every count, resource name, and summary table matches the inventories. This deterministic check stops the AI assistant errors before they reach customer deliverables. Scripts count, AI assistant writes, and consultants approve.

The validation script is specific to each engagement because inventory file names, document paths, and the way counts are written all vary. Use the following prompt to have your AI coding assistant generate a script for your engagement, then review the script before you run it.

### AI prompt:
<a name="ai-prompt-.ba156c8b-8cdc-5eda-8740-6c2819db0374"></a>

```
Generate a Python validation script that verifies count parity between
inventory CSVs and acceptance criteria documents.

CONTEXT:
- Inventory CSVs: work-breakdown/*/excel-template/inventory-*.csv
- AC Documents: work-breakdown/*/ac-*.md
- Raw Source CSVs: sources/current-state-inventory/[cloud]/cloud-envs/*/csv-data/

The script should:

1. COUNT ROWS in each inventory CSV (excluding header). These are the
   authoritative counts.

2. PARSE AC DOCUMENTS for stated counts. Look for patterns like:
   "**Resource Inventory**: N [Resource Type]" and summary tables with
   totals. Map each stated count to its corresponding inventory CSV.

3. COMPARE inventory CSV row counts against AC document stated counts.
   Flag mismatches as errors.

4. OPTIONALLY compare inventory CSV row counts against raw source CSV
   row counts. Source > Inventory is expected (source includes out-of-scope
   resources). This comparison is informational, not an error.

5. OUTPUT two files:
   - resource-counts.md: pre-computed totals and per-environment breakdowns
     from inventory CSVs. AI reads this file and uses its numbers verbatim
     when writing or updating AC documents. Do NOT count yourself.
   - validation-report.txt: source vs inventory vs AC comparison with
     mismatches flagged. For human review.

6. CHECK PROVENANCE: verify that inventory CSV rows with empty
   raw_scrape_origin are flagged as potentially hallucinated.

7. For target-state documents: cross-check that every resource count
   referenced in the target state matches the current state assessment.
   Verify internal consistency (do sub-counts add up to stated totals?).

The script should exit with a non-zero code if any inventory-vs-AC
mismatches are found.
```

Expected output:

```
resource-counts.md (for AI consumption):
| Inventory CSV                     | Total Rows | Breakdown by Environment      |
|-----------------------------------|------------|-------------------------------|
| inventory-01-app-services.csv     | 12         | DEV: 4, Non-PRD: 4, PRD: 4   |
| inventory-02-storage-accounts.csv | 28         | DEV: 8, Non-PRD: 8, PRD: 12  |

validation-report.txt (for human review):
| Resource Type    | Source | Inventory | AC Doc | Status   |
|------------------|--------|-----------|--------|----------|
| app-services     | 45     | 12        | 12     | OK       |
| storage-accounts | 92     | 28        | 28     | OK       |
| key-vaults       | 38     | 15        | 14     | MISMATCH |
```

Source → Inventory variance is expected — source counts include all resources in the subscription, while inventory counts contain only in-scope resources filtered by domain, naming patterns, and other criteria. The critical check is Inventory vs. acceptance criterion document: if those don't match, the AI assistant stated a wrong count.

The validation loop runs: AI assistant writes → script validates → you apply corrections → AI assistant rewrites → script validates again. In the engagement described in this guide, deliverables typically aligned after two to three iterations.

## Rollup (optional)
<a name="rollup-optional"></a>

At any point during this phase, you can roll up the individual acceptance criterion documents into one Markdown document per user story for stakeholder review. Small, separate documents keep each AI assistant task focused and reduce errors, but stakeholders usually prefer one consolidated document. The rollup gives them that without changing how you work.

The rollup goes through each user story folder, combines its acceptance criterion documents in numeric order, skips any marked as not included, and writes one deliverable per user story. If you don't have a rollup script, ask your AI coding assistant to generate one from this description.

The rollup is optional and isn't required for Phase 5. The individual acceptance criterion documents stay the source of truth, so keep editing those and run the rollup again whenever you need a fresh review copy.

With the current-state acceptance criteria accurate and validated, Phase 5 uses all of this context to build the target state.
