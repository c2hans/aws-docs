---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/azure-to-aws-platform-migration/phase-3-ai-assisted-current-state-documentation.html
---

# Phase 3 AI-Assisted Current State Documentation
<a name="phase-3-ai-assisted-current-state-documentation"></a>

## AI-assisted resource mapping
<a name="ai-assisted-resource-mapping.e6f62b02-2013-5238-bffa-79320f6cec56"></a>

This phase transforms the flat CSV data from Phase 2 into a connected knowledge layer. AI reads across hundreds of CSVs in `sources/current-state-inventory/` simultaneously to classify resources into business domains, identify relationships between components, and write architectural descriptions — work that would otherwise require days or weeks of manual effort.

The output of this phase is not the deliverable itself — it is the relationship and context layer that AI and consultants will use in Phase 4 to fill out the actual acceptance criteria documents. AI-generated context (resource summaries, relationship docs, Mermaid diagrams) is written back into `sources/current-state-inventory/` next to the data it describes. Enriched inventory CSVs go into the `excel-template/` folders under each user story.

AI analyzes DevOps pipelines first because the cloud resource enrichment needs to cross-reference which pipeline deploys each resource.

### Define Business Domains
<a name="ai-prompt-define-business-domains"></a>

After Phase 2 provides the raw inventory CSVs, AI can identify the actual business domains from resource names, tags, and naming patterns.

#### AI prompt:
<a name="ai-prompt-.20217153-b943-5a3c-8685-eb37a7d07551"></a>

```
Read the raw inventory CSVs and platform overview to define business domains.

CONTEXT:
- Platform Overview: sources/provided-docs/platform-overview.md
- Raw Inventories: sources/current-state-inventory/[cloud]/cloud-envs/*/csv-data/
  (specifically: all-resources.csv, resource-tags.csv from each subscription)

Create sources/domains.csv with columns:
  Domain, Covers, Resource Patterns, Pipeline Patterns.

Identify major business domains by analyzing resource names, tags, and resource
group naming patterns across all subscriptions. Common domains for data platform
migrations: Data Engineering, Data Science, Data Analytics, Platform Operations,
plus customer-specific business domains.

For each domain, list:
- What it covers (brief description)
- Resource naming patterns (regex patterns that identify resources in this domain)
- Pipeline patterns (DevOps folder paths associated with this domain)
```

Output:

```
sources/domains.csv
```

### DevOps Pipeline Analysis
<a name="ai-prompt-dev-ops-pipeline-analysis"></a>

Run this before cloud resource analysis. First, enrich the pipeline inventories with Domain, Purpose, and Deploys To so that the cloud resource enrichment can cross-reference which pipeline deploys each resource.

#### AI prompt:
<a name="ai-prompt-.af6d6062-5d82-5596-8d46-be7fda85137c"></a>

```
Analyze DevOps pipeline data, create distilled inventory CSVs, and enrich
each pipeline with Domain, Purpose, and deployment target.

CONTEXT:
- Raw Data: sources/current-state-inventory/[cloud]/devops-envs/[project]/csv-data/
- Platform Overview: sources/provided-docs/platform-overview.md
- Domain Definitions: sources/domains.csv

STEP 1: CREATE DISTILLED INVENTORY CSVs
Read source pipeline CSVs. Create distilled inventories with enriched columns:
- inventory-01-build-pipelines.csv
  Columns: Name, AzureDevOpsProject, Environment, Domain, Purpose, Deploys To,
  Build Pattern, Repository, Id, Folder, Revision, Component, raw_scrape_origin
- inventory-02-pipeline-details.csv (PipelineName, Repo, YamlPath, ConfigType)
- inventory-03-build-definitions.csv (Name, Path, Type, Repo, Environment, TaskCount)
- inventory-04-repositories.csv (Name, DefaultBranch, Size, PipelineCount)
Plus trigger, task, variable, release, and integration inventories.

For each pipeline row, determine:
- Environment: extract from pipeline name (Dev, NonProd, PreProd, Prod, Other)
- Domain: assign using patterns from sources/domains.csv
- Purpose: specific description of what this pipeline does
- Deploys To: which cloud resources this pipeline deploys
- Build Pattern: the build/deploy pattern (e.g., Terraform IaC, Node.js Build, Databricks Artifact)
- Component: logical component folder grouping
- raw_scrape_origin: trace back to source CSV and row number

STEP 2: CREATE PIPELINE RELATIONSHIP DOCS
Create pipeline-relationships.md containing:
- Component → resource mapping (which pipelines deploy which resources)
- Architecture layer assignments
- Domain groupings
- Pipeline pattern analysis (common task sequences, build patterns)
- Component summary (folder groupings, pipeline counts, environments)

RULES:
- Distill, don't copy — inventory CSVs are summaries, not raw dumps
- No migration planning or recommendations — document what exists
```

Output:

```
sources/current-state-inventory/[cloud]/devops-envs/
  pipeline-relationships.md                          # Patterns, component summary, resource mapping
work-breakdown/[epic]/[devops-user-story]/excel-template/
  inventory-01-build-pipelines.csv                   # Enriched: Environment, Domain, Purpose, Deploys To, Build Pattern, raw_scrape_origin
  inventory-02-pipeline-details.csv
  inventory-03-build-definitions.csv
  inventory-04-repositories.csv
  inventory-05-build-triggers.csv
  ...
```

### Cloud Resource Analysis
<a name="ai-prompt-cloud-resource-analysis"></a>

After you enrich pipeline inventories, AI can analyze cloud resources and cross-reference which pipeline deploys each resource.

#### AI prompt:
<a name="ai-prompt-.2070488e-311f-5933-a71d-87f92b26d955"></a>

```
Analyze cloud subscriptions to identify data platform resources, document
relationships, populate inventory templates, and enrich each resource with
Domain, Purpose, Environment, and Deployed By.

CONTEXT:
- Platform Overview: sources/provided-docs/platform-overview.md
- Domain Definitions: sources/domains.csv
- Cloud Subscriptions: sources/current-state-inventory/[cloud]/cloud-envs/
- Subscription Mapping: sources/current-state-inventory/[cloud]/cloud-envs/subscription-mapping.csv
- Pipeline Inventories: work-breakdown/[epic]/[devops-user-story]/excel-template/inventory-01-build-pipelines.csv
- Pipeline Relationships: sources/current-state-inventory/[cloud]/devops-envs/pipeline-relationships.md

STEP 1: IDENTIFY RELEVANT SUBSCRIPTIONS
For each subscription: read resource-tags.csv for platform-specific tags, then
all-resources.csv for naming patterns. Track which subscriptions have platform
resources and which don't.

STEP 2: DOCUMENT SUBSCRIPTION RELATIONSHIPS
For each relevant subscription, create resource-summary.md (in the subscription
folder, next to csv-data/) containing: overview, resource inventory grouped by
type, Mermaid relationship diagram from dependency data, architecture layer
mapping, and key observations.

STEP 3: POPULATE AND ENRICH INVENTORY CSVs
From each relevant subscription, populate inventory CSVs. For each resource row:
- Environment: determine from subscription name or resource naming pattern
- Domain: assign using patterns from sources/domains.csv
- Purpose: specific description including function and connections
  (e.g., "Portal UI (Node.js 18) - production web interface
  for data source registration" not "application service")
- Deployed By: cross-reference pipeline-relationships.md and
  inventory-01-build-pipelines.csv to find which pipeline deploys this resource.
  Format: pipeline-name | [DevOps](url) | [inventory-01-build-pipelines.csv, row N](path)
- raw_scrape_origin: trace back to source CSV and row number

For data-layer resources (data lakes, databases, ETL services like ADF /
Databricks / Airflow, BI sources), additionally enrich with:
- Reads From: upstream data sources this resource consumes (other tables,
  storage paths, external APIs). Source from repository contents and IaC
  captured in DevOps extraction CSVs, plus dependencies.csv.
- Writes To: downstream targets this resource produces (tables, storage
  paths, reports). Same sources as Reads From.
- Schedule: cron expression, trigger type, or event-based trigger that
  invokes this resource. Source from build-definition-triggers.csv,
  release-triggers.csv, Databricks job definitions, or DAG schedules in
  repository source.
- Owner: responsible team or individual. Source from rbac-assignments.csv,
  resource tags, or repository CODEOWNERS.

When the source data does not contain enough detail to populate one of these
columns, leave it blank rather than inferring — sub-resource depth is added
later via on-demand extraction (see Phase 2 "On-Demand Sub-Resource Extraction").

RULES:
- Analyze subscriptions ONE AT A TIME
- Complete each step before starting the next
- Every resource name must exist in the corresponding source CSV
- Purpose must be specific — include the technology, version, and function
```

Output:

```
sources/current-state-inventory/[cloud]/cloud-envs/
  resource-relationships.md                          # Cross-subscription relationship view
  [sub-name]/resource-summary.md                     # Per-subscription: inventory, Mermaid diagram, architecture mapping
work-breakdown/[epic]/[resource-user-story]/excel-template/
  inventory-01-app-services.csv                      # Enriched: Environment, Domain, Purpose, Deployed By, raw_scrape_origin
  inventory-02-storage-accounts.csv
  inventory-03-key-vaults.csv
  inventory-04-certificates.csv
  inventory-05-log-analytics-workspaces.csv
  inventory-06-metric-alerts.csv
  inventory-07-service-principals.csv
  ...
```

At this point, AI has built a rich understanding of *what* exists and *how* components relate. But it is missing *why* things are the way they are, *how* teams actually operate, and *what decisions teams made.* That knowledge lives in people's heads and meeting recordings. Phase 4 makes it accessible to AI — and then uses all of it to fill out the actual deliverable documents.
