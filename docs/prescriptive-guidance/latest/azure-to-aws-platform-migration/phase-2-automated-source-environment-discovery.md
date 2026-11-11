---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/azure-to-aws-platform-migration/phase-2-automated-source-environment-discovery.html
---

# Phase 2 - Automated Source Environment Discovery
<a name="phase-2-automated-source-environment-discovery"></a>

## Building AI's Ground Truth Layer
<a name="building-ai-s-ground-truth-layer.f8c3ed15-40a6-546d-9a9a-91573a603eb4"></a>

Your AI coding assistant (such as Kiro) generates the extraction scripts. Writing PowerShell or Python that lists cloud resources across dozens of API categories is structured, repetitive work, which is where the AI assistant saves the most time. The AI assistant doesn't run the scripts or interpret the results. You run the scripts against the live environment with read-only credentials that the customer approves, and they export everything to CSV files. Those exports become the single source of truth for the engagement. Every AI-generated claim in later phases traces back to a specific CSV row.

### Subscription mapping (optional)
<a name="subscription-mapping--optional-.9b6ec510-0c3f-542f-9a87-a98e0e7e34db"></a>

By default, the extraction scripts discover every subscription that your credentials can access. Filter subscriptions before extraction when some of them are outside the engagement scope, belong to a different business unit, hold sensitive or regulated data the customer hasn't approved for assessment, or would add extraction time without adding useful information. To filter, create a subscription mapping that records each subscription's name, ID, environment, Region, and main purpose, and whether it's in scope. The extraction scripts then run only against the in-scope subscriptions.

If you don't need to filter, the extraction scripts build the subscription mapping automatically from the subscriptions they discover.

#### Cloud Resource Extraction
<a name="what-to-extract"></a>

**Why this step matters**

A migration estimate is only as good as its inventory. If a resource is missing from the inventory, it's missing from the estimate, the target design, and the migration plan. This step gives you a full, repeatable snapshot of every resource in the source environment, so later the AI assitant analysis works from facts instead of assumptions.

**What the extraction does**

The extraction goes through each subscription you can access (or a list you specify) and exports one CSV file for each resource category. A generic resource listing gives you a flat inventory, but it leaves out deeper properties such as VM size, storage tier, hierarchical namespace, or subnet security groups. So the extraction calls a separate, category-specific query for each resource type that needs that detail.

**Logic**

`FOR each subscription in scope: switch context to the subscription create an output folder named after the subscription export a flat inventory of all resources (name, type, group, region, SKU, tags) FOR each resource category (resource groups, VMs, storage, RBAC, logging, networking, key vaults, databases, Databricks, ...): query the category-specific API keep the properties that drive sizing and service mapping flatten nested values (tags, subnets) into columns write one CSV per category log completion and row counts for human verification`

##### AI prompt
<a name="ai-prompt.4bf39341-e163-5201-92ba-26b99a433b70"></a>

```
Generate an extraction script that pulls comprehensive resource inventory data
from our source cloud environment.

CONTEXT:
- Source Cloud: [Azure / GCP / other]
- Subscription Mapping: sources/current-state-inventory/[cloud]/cloud-envs/subscription-mapping.csv
- Output Directory: sources/current-state-inventory/[cloud]/cloud-envs/[sub-name]/csv-data/

SUBSCRIPTION FILTERING:
The script should accept a subscription mapping CSV and filter to relevant
subscriptions only. Identify relevant subscriptions by checking resource tags
(e.g., AppName: DataPlatform, TechnologyDomain: Analytics) and resource naming
patterns. Document which subscriptions are in scope and which are excluded.

Generate a script that authenticates and iterates through each relevant
subscription. For each subscription, produce one CSV per cloud service type.

Each CSV must be packed with every available metadata property for that
service — not just name and location, but configuration details like SKU,
replication settings, TLS version, access tiers, runtime versions, scaling
config, network rules, certificate expiration dates, etc. The more metadata
per row, the more context the AI assistant has in later phases to classify resources,
identify relationships, and write accurate descriptions.

Also generate a separate script using the Databricks REST API for
workspace-internal data not available through cloud provider APIs:
cluster-policies, cluster-configs, job-definitions.

RULES:
- AI assistant generates scripts but does NOT run them
- Scripts must be idempotent and handle missing resources gracefully
- CSV output must use consistent UTF-8 encoding
- Include row counts in progress output for human verification
- Flag secrets (mark as "***", don't export values)
```

Output per subscription in `sources/current-state-inventory/[cloud]/cloud-envs/[sub-name]/csv-data/`:

The extraction produces one CSV per resource category, for example a complete resource list with tags, resource groups, storage accounts, virtual machines, key vaults, app services, networks and security rules, role assignments, service principals, monitoring and alerts, databases, Databricks workspaces, and storage capacity metrics. Add categories to match your platform.

**Inputs and outputs**

|
|
| Item | Description |
| --- |--- |
| Input | Read-only credentials for the source cloud, optional subscription filter |
| Output | One folder per subscription with one CSV per resource category |
| Key properties | Identity (name, group, region), sizing (SKU, tier, size), security (RBAC, network rules), and tags |

**Design principles**

**Read-only.** The extraction never changes the source environment.

**Idempotent.** Running it again overwrites the output with a fresh snapshot.

**Fault tolerant.** If a category is missing or access is denied, the extraction records that and keeps going.

**AI assitant writes it, people run it.** The AI assistant generates the script from this specification. A consultant reviews it and runs it with the customer's approved credentials.

**Note**
If your source is a different cloud or on-premises environment, the logic stays the same. Only the API calls change.

#### DevOps Pipeline Extraction
<a name="ai-prompt-dev-ops-pipeline-extraction"></a>

**Why this step matters**

Infrastructure inventories show *what* exists. CI/CD pipelines show *how it gets there*: which pipelines deploy which resources, which scripts transform data, and which approvals gate production. That information is how you tie resources to business workloads, and it usually isn't written down anywhere else.

**What the extraction does**

The extraction authenticates to the DevOps platform's REST API with a personal access token (PAT), goes through every project, and exports one CSV for each pipeline artifact type. It records the full sequence of tasks, not just pipeline names, so later analysis can see what each pipeline actually runs.

**Logic**

`authenticate to the DevOps REST API with a token from a secure environment variable list projects (optionally filtered by name) FOR each project: export repositories (name, default branch, size, URL) export YAML pipelines (name, folder, definition path, linked repository) FOR each classic build definition: export the definition metadata FOR each step: record order, task name, enabled flag, inline script or script path export triggers and branch filters export variables: names only, with a secret flag (never values) FOR each release definition: FOR each stage: record name and order FOR each deployment task: record order, task name, enabled flag export variable groups (name, type, variable count) export service connections (name, type, endpoint, readiness) log completion and row counts`

##### AI prompt:
<a name="ai-prompt-.4d75cc80-d987-59fa-9ec7-c22eac3d3449"></a>

```
Generate an extraction script that pulls comprehensive CI/CD pipeline data
from our DevOps platform.

CONTEXT:
- DevOps Platform: [Azure DevOps / GitHub / GitLab]
- Output Directory: sources/current-state-inventory/[cloud]/devops-envs/[project-name]/csv-data/

Generate a script that authenticates via PAT, iterates through projects, and
produces one CSV per pipeline artifact type.

Pack each CSV with full metadata — not just pipeline names, but task sequences,
trigger configurations, variable names (flag secrets; never export values), branch filters,
deployment stages, approval gates, and service connections.

RULES:
- The AI generates scripts but does NOT run them
- Ensure scripts are idempotent and handle missing resources gracefully
- Use consistent UTF-8 encoding for CSV output
- Include row counts in progress output for human verification
- Mark secrets as "***" and do not export their values
```

Output per project in `sources/current-state-inventory/[cloud]/devops-envs/[project-name]/csv-data/`:

The extraction produces one CSV per pipeline artifact type: repositories, YAML pipelines, classic build definitions with their tasks, triggers, and variables, release pipelines with their stages, tasks, and triggers, variable groups, and service connections.

**Inputs and outputs**

|
|
| Item | Description |
| --- |--- |
| Input | Organization name, a read-scoped PAT supplied through an environment variable, optional project filter |
| Output | One folder per project containing repositories, build and release pipelines, tasks, triggers, variables, variable groups, and service connections as separate CSVs |

**Security requirements**

Read the token from an environment variable or secrets store. Never hardcode it or write it to logs.

Export variable **names and secret flags only**. Mask secret values as \*\*\*.

Use a token with the narrowest read-only scope the platform allows.

**Note**
The same logic works for GitHub Actions or GitLab CI. Swap in the matching REST endpoints for projects, workflows, runs, and secrets metadata.

#### Data Asset Discovery
<a name="data-asset-discovery"></a>

The cloud resource extraction and the DevOps pipeline extraction give you three complementary views: every cloud resource in the environment, every CI/CD pipeline that builds or deploys to those resources, and the source code and infrastructure as code (IaC) that defines them. Together, these views identify the data-layer entities a migration assessment needs, without listing every table, file, or directed acyclic graph (DAG) in the first pass.

##### Where Data-Layer Entities Surface
<a name="where-data-layer-entities-surface.3fdc283d-f907-59d7-b947-443d2590ab48"></a>

|
|
| Entity | Where it surfaces in Phase 2 outputs |
| --- |--- |
| **Data Sources** (Databases, data lakes, streaming, SaaS connections) | `all-resources.csv`, `sql-databases.csv`, `storage-accounts.csv`, `databricks.csv`, `dependencies.csv` |
| **Source Details** (tables/views, file paths, datasets) | Repository contents (via `repositories.csv` \+ cloned source) and IaC inside `build-definition-tasks.csv` / `release-tasks.csv` |
| **ETL / ELT Definitions** (Azure Data Factory (ADF) pipelines, Databricks jobs, Airflow DAGs, dbt models) | Repository source \+ Infrastructure as code (IaC) tasks; Databricks REST API output for cluster-policies, cluster-configs, job-definitions |
| **Schedules / Triggers** | `build-definition-triggers.csv`, `release-triggers.csv`, plus Databricks job schedules and Airflow DAG schedules in repository source |
| **Data Volumes** | `storage-capacity-metrics.csv`, `sql-databases.csv` (max size), `vms.csv` (disk count) |
| **Owners / Role Based Access Control (RBAC)** | `rbac-assignments.csv`, `service-principals.csv`, resource tags in `resource-tags.csv` |

This means a Phase 3 prompt asking "which Databricks job reads from which Azure Data Lake Storage (ADLS) path and writes where" can be answered from the repository source captured in DevOps extraction plus the resource inventory — without a separate data-asset extraction pass.

##### On-Demand Sub-Resource Extraction
<a name="on-demand-sub-resource-extraction.594be94e-d1eb-5838-8c44-b0053ef9afc4"></a>

For cases where the initial sweep does not provide enough detail — table schemas inside a SQL database, Azure Data Factory (ADF) dataset definitions inside a factory, directed acyclic graph (DAG) bodies inside an Airflow instance, query history from a warehouse —generate a targeted extraction script using the same prompt pattern as the extraction prompts earlier in this phase. The Phase 2 outputs identify *what* to extract from; the targeted script extracts the *contents*. **AI prompt:**

```
Generate a targeted extraction script for sub-resource data asset details.

CONTEXT:
- Phase 2 Outputs: sources/current-state-inventory/[cloud]/cloud-envs/*/csv-data/
- Target Resources: [list of resource names from Phase 2 inventories — e.g.,
  specific SQL databases, storage accounts, ADF factories, Databricks workspaces]
- Output Directory: sources/current-state-inventory/[cloud]/data-assets/[resource-name]/

Extract the next layer of detail for the listed resources. Examples:
- For SQL databases: query INFORMATION_SCHEMA for tables, views, columns,
  row counts, last updated timestamps. Output: tables.csv, views.csv, columns.csv.
- For ADLS / storage accounts: list containers and prefixes, capture file
  format, partitioning pattern, and approximate size per prefix.
  Output: data-lake-paths.csv.
- For ADF factories: enumerate pipelines, datasets, linked services, and
  triggers. Output: adf-pipelines.csv, adf-datasets.csv, adf-triggers.csv.
- For Airflow: enumerate DAGs, schedules, task graph edges (source → sink).
  Output: airflow-dags.csv, airflow-tasks.csv.
- For Databricks: cluster-configs, job-definitions, notebook references.
  Output: databricks-jobs.csv, databricks-clusters.csv.

RULES:
- AI assistant generates scripts but does NOT run them
- Scripts must be idempotent and handle missing resources gracefully
- CSV output must use consistent UTF-8 encoding
- Flag secrets (mark as "***", don't export values)
- Each row must include a raw_scrape_origin column tying it back to the
  parent resource and source API call
```

This keeps the first extraction fast and broad. Add depth one data domain at a time, based on what the Phase 3 analysis shows about which resources are in scope and which need closer inspection.

At this point, the AI assistant has the raw facts — comprehensive, structured, and complete. But the data is flat. A storage account CSV row does not know it is the primary data lake for the production ingestion framework. Phase 3 is where the AI assistant builds that understanding.
