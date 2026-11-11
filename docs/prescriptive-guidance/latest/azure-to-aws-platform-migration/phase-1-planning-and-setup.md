---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/azure-to-aws-platform-migration/phase-1-planning-and-setup.html
---

# Phase 1 - Planning and Setup
<a name="phase-1-planning-and-setup"></a>

## Prerequisites
<a name="prerequisites.3eed6656-524d-5a2f-b1a8-154bda4f5ee3"></a>

Scope the engagement before using AI to generate a work breakdown. At minimum, the following inputs are required:
+ A scoping document that defines the body of work — a statement of work (SOW), level of effort (LOE) estimate, or engagement proposal that identifies which workloads to migrate, what deliverables you expect, and the engagement timeline
+ A platform overview or architecture brief from the customer that describes the source environment — even a rough one is sufficient for AI to identify the major components, business domains, and workload boundaries
+ Knowledge of the source and target cloud platforms (e.g., Azure to AWS)

### Create Epics, User Stories, and Acceptance Criteria
<a name="ai-prompt-create-epics-user-stories-and-acceptance-criteria"></a>

**Epics** ensure that every piece of work ties back to a meaningful business objective, giving teams and stakeholders a shared understanding of *why* the work matters. **User stories** break that vision into small, customer-focused increments that describe *who* benefits and *what* they need, keeping delivery human-centered and manageable. **Acceptance criteria** define exactly what "done" looks like for each story, eliminating ambiguity and preventing costly rework. AI performs best when you provide clear, scoped, and unambiguous context, which is exactly what you provide when you generate these against the prerequisite documents.

#### AI prompt:
<a name="ai-prompt-.769151a5-09a2-52b9-9786-6107e0a7dc5e"></a>

```
Create the epic and user story structure for a data platform migration
assessment from [SOURCE CLOUD] to [TARGET CLOUD].

CONTEXT:
- Scoping Document: [path to SOW, LOE, or engagement proposal in sources/provided-docs/]
- Platform Overview: [path to customer-provided platform overview in sources/provided-docs/]
- Domain Definitions: sources/domains.csv
- Key Workloads: [Databricks, data lake, orchestration, BI tools, ML/AI, etc.]

Read the scoping document to understand which deliverables are expected and what
workloads are in scope. Create work-breakdown/epics.md with epics and user stories
tailored to the engagement scope — skip epics or user stories that don't apply.

For each user story, create:
- A user story file (us-NNN-name.md) containing the user story statement
  (As a / I want / So that), a list of acceptance criteria, and context.
- An AC file (ac-NN-name.md) for each acceptance criterion, with pre-generated
  section structures: headings, tables with placeholder rows (___), and
  descriptions of what content each section should contain. The sections should
  reflect the scope of that acceptance criterion — e.g., an inventory AC gets
  resource type tables, a cost AC gets spend breakdown tables, a security AC
  gets compliance control tables.

For mixed epics (containing both current-state and target-state work), use
current-state/ and target-state/ subfolders.

RULES:
- Read the scoping document and platform overview FIRST to understand scope
- Tailor user stories to the specific engagement — skip irrelevant ACs
- AC files should have enough section structure to define scope but not so
  much detail that they constrain AI in later phases
```

Each user story file lists its acceptance criteria as bullet points. You convert each bullet into a separate acceptance criteria file with scaffolded sections — headings, tables, and placeholders that define the scope of what to document. This scaffolding gives AI a clear structure to fill in during later phases without inventing its own organization.

This structure serves three purposes:
+ Each acceptance criterion becomes a discrete task AI can complete — natural work boundaries that map to prompts
+ Team members and AI can work in parallel across different acceptance criteria
+ You can track progress at the acceptance criterion level

##### Recommended epic structure
<a name="recommended-epic-structure.bfea420a-4479-520a-9946-4b6c58f2c57d"></a>

|
|
| Epic | Focus Area |
| --- |--- |
| Current State Assessment and Analysis | Source environment inventory, data asset cataloging, performance analysis, data science assets |
| Migration Strategy Development | Target architecture design, migration approach, risk assessment, implementation roadmap |
| Integration with Third-Party Applications | System integration inventory, tool migration planning, licensing assessment |
| Operations and Cost Analysis | Operations documentation, cost modeling, HA/DR assessment, CI/CD pipeline inventory |
| Data Validation Approach | Testing strategy, data classification validation, migration validation methodology |
| Security and Compliance Assessment | Security monitoring, compliance validation, data classification, incident response |

Each epic contains 3-5 user stories, and each user story contains 2-6 acceptance criteria documents. The acceptance criteria are the actual deliverables — the documents that you convert to Word and deliver to the customer.

### Create Repository Structure
<a name="ai-prompt-create-repository-structure"></a>

#### AI prompt:
<a name="ai-prompt-.d83d731b-a1a1-5ea6-a4e8-f4a50d755332"></a>

```
Create the repository directory structure for a data platform migration
assessment from [SOURCE CLOUD] to [TARGET CLOUD].

Create:
  sources/ (current-state-inventory/, meeting-transcripts/, provided-docs/, domains.csv)
  work-breakdown/ (epics.md)
  deliverables/
  collaboration/ (download/, markdown-converted/, upload/)
```

The repository has three layers that serve different purposes:

```
project-root/
├── sources/                             # Source data + AI-generated context
│   ├── current-state-inventory/         # Extraction outputs + AI relationship docs
│   │   ├── [cloud]/                     # e.g., azure/
│   │   │   ├── cloud-envs/             # Per-subscription: csv-data/ + resource-summary.md
│   │   │   │   ├── subscription-mapping.csv
│   │   │   │   ├── resource-relationships.md    # AI-generated cross-subscription view
│   │   │   │   └── sub-analytics-prd/
│   │   │   │       ├── csv-data/                # Script-extracted CSVs
│   │   │   │       └── resource-summary.md      # AI-generated (next to the data it describes)
│   │   │   └── devops-envs/            # Per-project: csv-data/ + pipeline-relationships.md
│   │   │       ├── pipeline-relationships.md    # AI-generated cross-project view
│   │   │       └── AnalyticsPlatform/
│   │   │           └── csv-data/                # Script-extracted CSVs
│   ├── meeting-transcripts/             # Raw transcripts + companion indexes
│   │   ├── README.md                    # Root index (topic → session)
│   │   ├── session-1.md                 # Raw transcript
│   │   └── session-1.companion.md       # Companion index (topics, decisions, facts)
│   ├── provided-docs/                   # Scoping docs, platform overview, architecture briefs
│   └── domains.csv                      # Business domain definitions
│
├── work-breakdown/                      # Epics/user stories/ACs — where AI writes
│   ├── epics.md
│   ├── epic-1-current-state-assessment/
│   │   └── us-001-environment-assessment/
│   │       ├── us-001-environment-assessment.md  # User story with AC list
│   │       ├── ac-01-resource-inventory.md       # AC with scaffolded sections
│   │       ├── ac-02-architecture-patterns.md
│   │       └── excel-template/
│   ├── epic-4-operations-and-cost/
│   │   ├── current-state/
│   │   │   ├── us-011-operations-documentation/
│   │   │   └── us-012-devops-pipelines/
│   │   └── target-state/
│   │       ├── us-015-aws-cost-strategy/
│   │       └── us-018-aws-devops-strategy/
│   └── ...
│
├── deliverables/                        # Final assembled documents
│   ├── Current_State_Assessment_v1.0.md
│   ├── Migration_Strategy_v1.0.md
│   └── Risk_Register_v1.0.md
│
├── collaboration/                       # Document lifecycle round-trip
│   ├── download/
│   ├── markdown-converted/
│   └── upload/
│
└── scripts/
```

The key structural decisions:
+ `sources/`** holds all source data with AI-generated context embedded alongside it.** Scoping documents and platform overviews go in `provided-docs/`. Script-extracted CSVs live in `csv-data/` folders under `current-state-inventory/`. AI-generated relationship docs and resource summaries sit next to the data they describe. Meeting transcripts and companion indexes live in `meeting-transcripts/`.
+ `work-breakdown/`** holds the epic/user story structure.** This is where AI does the actual writing, one acceptance criterion at a time. Some epics are purely current-state (Epic 1), some are purely target-state (Epic 2), and some have both (Epics 3, 4, 6). Mixed epics use `current-state/` and `target-state/` subfolders to separate the two workflows. Current-state acceptance criteria get filled first. Target-state acceptance criteria follow the same process but with the additional context of the completed Current State Assessment, meeting transcripts, and ancillary context.
+ `deliverables/`** holds the final assembled documents.** A roll-up script (see Phase 4) walks the `work-breakdown/` directory tree, combines acceptance criteria files from each user story, and produces the final deliverable markdown files.
