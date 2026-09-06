---
source_url: https://docs.aws.amazon.com/solutions/latest/migration-assistant-for-amazon-opensearch-service/use-the-solution.html
---

# Configure and run workflows
<a name="use-the-solution"></a>

This section describes how to configure, pilot, and run a migration after you deploy Migration Assistant on Amazon EKS. The day-to-day operator interface is the **Workflow CLI**, which runs in the Migration Console pod (`migration-console-0`) on Amazon EKS. The supporting `console` CLI provides component-level inspection and ad-hoc operations during validation and troubleshooting.

## Getting started with the Workflow CLI
<a name="getting-started"></a>

This sequence is the shortest safe path to your first migration to Amazon OpenSearch Service or Amazon OpenSearch Serverless NextGen: load the right schema for your version, prove connectivity, run a small pilot, and only then run the full workflow.

### Before you start
<a name="before-you-start"></a>

Make sure all of the following are true:
+ Migration Assistant is deployed on Amazon EKS. See [Deploy the solution](deploy-the-solution.md).
+ The source cluster and the Amazon OpenSearch Service domain or Amazon OpenSearch Serverless NextGen collection are reachable from the Amazon EKS cluster.
+ Snapshot storage is ready in Amazon S3 if you plan to run backfill.
+ Any HTTP Basic credentials you need can be created as managed Kubernetes Secrets in the `ma` namespace.

### Step 1: Access the Migration Console
<a name="step-1-access-console"></a>

```
kubectl exec -it migration-console-0 -n ma -- /bin/bash
```

If you are accessing Amazon EKS from a new shell, refresh your kubeconfig first:

```
aws eks update-kubeconfig --region <REGION> --name migration-eks-cluster-<STAGE>-<REGION>
```

### Step 2: Confirm the installed version
<a name="step-2-confirm-version"></a>

```
console --version
```

This matters because the workflow schema can change by release.

### Step 3: Load the version-matched sample
<a name="step-3-load-sample"></a>

```
workflow configure sample --load
```

This gives you the safest starting point for your installed release.

### Step 4: Edit the workflow configuration
<a name="step-4-edit-config"></a>

```
workflow configure edit
```

Fill in the fields that describe your migration:
+ Source endpoint, version, and authentication.
+ Target endpoint and authentication. For Amazon OpenSearch Serverless NextGen, set `service: aoss` in the SigV4 `authConfig`. For Amazon OpenSearch Service, set `service: es`.
+ Snapshot repository details if you are running backfill.
+ The migration pattern: backfill only, capture and replay only, or both.

Use source version strings in `<ENGINE> <VERSION>` format. The workflow schema accepts `ES` for Elasticsearch 1.x, 2.x, and 5.x through 8.x; `OS` for OpenSearch 1.x through 3.x; and `SOLR` for Apache Solr 6.x through 9.x. Examples include `ES 7.10.2`, `OS 3.5.0`, and `SOLR 9.7.0`.

The keys under `sourceClusters` and `targetClusters` are workflow labels. Use a distinct label for every source and target; the same name cannot appear in both maps. `snapshotMigrationConfigs[].fromSource`, `snapshotMigrationConfigs[].toTarget`, `traffic.proxies.<name>.source`, and `traffic.replayers.<name>.toTarget` all reference those labels. In `perSnapshotConfig`, each key must match a snapshot declared under `sourceClusters.<source>.snapshotInfo.snapshots`, and optional migration `label` values must be unique within that snapshot group.

**Note**
Do not start by editing every possible field. Start with the minimum required fields for your path.

### Target configuration for Amazon OpenSearch Serverless NextGen
<a name="target-aoss-config"></a>

When the target is an Amazon OpenSearch Serverless NextGen collection, set the target cluster like this:

```
{
  "targetClusters": {
    "target": {
      "endpoint": "https://<collection-id>.<region>.aoss.amazonaws.com",
      "authConfig": {
        "sigv4": {
          "region": "<region>",
          "service": "aoss"
        }
      }
    }
  }
}
```

The migration IAM role created by the Amazon EKS deployment must also be added as a principal in your collection’s data access policy. The IAM role is named `<eks-cluster-name>-migrations-role`. Add it to the collection’s data access policy with both collection-level and index-level permissions before running the workflow.

### Target configuration for Amazon OpenSearch Service
<a name="target-aos-config"></a>

When the target is an Amazon OpenSearch Service domain:

```
{
  "targetClusters": {
    "target": {
      "endpoint": "https://<domain-endpoint>",
      "authConfig": {
        "sigv4": {
          "region": "<region>",
          "service": "es"
        }
      }
    }
  }
}
```

If your domain has fine-grained access control (FGAC) enabled, map the migration IAM role to a security role on the domain (typically `all_access` during migration, then scoped down). See [Troubleshooting](troubleshooting.md).

### Step 5: Create credentials if you use basic authentication
<a name="step-5-create-secrets"></a>

```
workflow configure credentials create source-credentials
workflow configure credentials create target-credentials
```

Reference those credential names in `authConfig.basic.secretName` in your workflow configuration. When you save configuration with `workflow configure edit`, the CLI detects missing HTTP Basic secrets and can prompt you to create them. Non-interactive submissions fail fast if a referenced secret is missing, so create or update credentials before you run `workflow submit`.

### Step 6: Verify connectivity before submitting a workflow
<a name="step-6-verify-connectivity"></a>

```
console clusters connection-check
```

The check runs against both source and target by default. To narrow it to one side:

```
console clusters connection-check --cluster source
console clusters connection-check --cluster target
```

For a direct API check:

```
console clusters curl source /
console clusters curl target /
```

If these checks fail, stop and fix connectivity or authentication first. Do not start a workflow yet.

### Step 7: Verify AWS identity if you use SigV4
<a name="step-7-verify-aws-identity"></a>

If your source or target uses Amazon OpenSearch Service or Amazon OpenSearch Serverless NextGen, verify pod identity is working from the Migration Console pod:

```
aws sts get-caller-identity
```

If `console clusters connection-check` works in the Migration Console but the workflow later fails with HTTP 401 or 403, verify that the Argo workflow executor pods are using the `argo-workflow-executor` service account with its EKS Pod Identity association. On Amazon EKS, both the Migration Console pod and the workflow executor pods get Pod Identity-backed AWS credentials automatically through the bootstrap script.

### Step 8: Run a pilot migration first
<a name="step-8-pilot"></a>

Use a small allowlist or a representative subset before you attempt the full migration. This is the easiest way to catch mapping issues, authentication issues, and throughput problems early.

```
workflow submit
workflow manage
```

Use `workflow manage` to watch the run and approve any gated steps.

### Step 9: Validate the pilot
<a name="step-9-validate"></a>

Check counts and basic behavior on the Amazon OpenSearch Service domain or Amazon OpenSearch Serverless NextGen collection before you expand scope:

```
console clusters cat-indices
console clusters curl target /<index>/_count
console clusters curl target /<index>/_search?size=5&pretty
```

If you are migrating applications with live traffic, also validate representative queries against the target.

### Step 10: Run the real migration
<a name="step-10-real-migration"></a>

After the pilot succeeds, widen the configuration to the full index set and submit again:

```
workflow configure edit
workflow submit
workflow manage
```

### Step 11: Use logs if anything fails
<a name="step-11-logs"></a>

```
workflow status
workflow log all
workflow log all -f
workflow log resource --list
workflow log resource snapshotmigration.<NAME> -- --tail=100
```

 `workflow submit` automatically stops and replaces an existing workflow with the same name, so you do not need to manually clean up between runs. If a previous run left orphaned migration custom resources, use `workflow reset` instead of deleting Argo workflows directly:

```
workflow reset                # lists migration custom resources
workflow reset --list         # lists migration custom resources and exits
workflow reset migration-foo  # delete a specific resource by name
workflow reset --all          # delete everything (capture proxies are protected)
workflow reset --all --include-proxies --delete-storage  # also remove capture proxies and Apache Kafka PVCs
```

## Core commands
<a name="core-commands"></a>

The `workflow` CLI orchestrates a full migration; the `console` CLI inspects or manually drives a single component during validation and troubleshooting.

### Workflow commands
<a name="workflow-commands"></a>

| Command | Why you use it |
| --- | --- |
|  `workflow configure sample`  | Shows the sample schema for your installed version |
|  `workflow configure sample --load`  | Loads that sample as your starting point |
|  `workflow configure edit`  | Opens the workflow config in your editor (`$EDITOR`, defaults to `vi`). Use `--stdin` to pipe configuration from stdin instead of launching an editor |
|  `workflow configure view`  | Prints the current config |
|  `workflow configure clear`  | Clears the current config and lets you start over. Use `--confirm` to skip the confirmation prompt |
|  `workflow submit`  | Starts the migration workflow (auto-stops and replaces an existing one with the same name) |
|  `workflow submit --wait --timeout 300`  | Submits and blocks until the workflow completes or the timeout is reached |
|  `workflow manage`  | Primary day-to-day interface for monitoring, approvals, and logs (interactive TUI) |
|  `workflow status`  | Shows the current workflow tree in a non-interactive form |
|  `workflow status --all`  | Shows running and completed workflows |
|  `workflow status --resource-view`  | Shows migration resources grouped by role instead of only the current Argo workflow step tree |
|  `workflow log all`  | Shows logs across workflow pods |
|  `workflow log all -f`  | Streams logs live |
|  `workflow log resource <RESOURCE>`  | Shows logs for one migration resource, such as `snapshotmigration.<NAME>` or `captureproxy.<NAME>`  |
|  `workflow log filter --list`  | Lists pod label selectors available for filtered logs |
|  `workflow show --list`  | Lists migration resources that have managed output artifacts, such as metadata evaluation and migration reports |
|  `workflow show snapshotmigration.<NAME> evaluatemetadata`  | Prints the latest metadata evaluation report for a snapshot migration. Use `migratemetadata` for the metadata migration report |
|  `workflow show --all`  | Prints the latest managed output artifacts for all current migration resources |
|  `workflow approve step <PATTERN>`  | Approves pending step gates that match exact names or globs |
|  `workflow approve --list`  | Lists available approval gates across step, change, and retry categories |
|  `workflow reset`  | Lists migration custom resources; pass a resource name or `--all` to delete them safely |

### Workflow command flags
<a name="workflow-flag-reference"></a>

The tables below cover the workflow subcommands and the advanced flags that matter for migration operations and automation. Global flags (`-v`/`--verbose`) can be placed before any subcommand to increase logging.

 **workflow configure**

| Command or flag | Purpose |
| --- | --- |
|  `workflow configure view`  | Print the current workflow configuration |
|  `workflow configure edit`  | Open the current configuration in `$EDITOR` (defaults to `vi`) and save it after validation |
|  `workflow configure edit --stdin`  | Read configuration from stdin, save it, and report validation errors without launching an editor |
|  `workflow configure sample`  | Print the installed version’s sample configuration |
|  `workflow configure sample --load`  | Load the installed version’s sample configuration into the current session |
|  `workflow configure clear`  | Clear the current workflow configuration after a confirmation prompt |
|  `workflow configure clear --confirm`  | Clear the current workflow configuration without prompting |
|  `workflow configure credentials list`  | List managed HTTP Basic credential secrets |
|  `workflow configure credentials create <NAME>`  | Create managed HTTP Basic credentials, prompting for username and password |
|  `workflow configure credentials create --show-missing` or `--list`  | List configured HTTP Basic credential names that have not been created yet |
|  `workflow configure credentials create <NAME> --stdin`  | Read one `USERNAME:PASSWORD` line from stdin and create the managed credentials secret |
|  `workflow configure credentials create <NAME> --stdin --silent`  | Disable terminal echo while reading credentials from stdin |
|  `workflow configure credentials update <NAME>`  | Update an existing managed HTTP Basic credential secret |
|  `workflow configure credentials update --list`  | List managed HTTP Basic credential secrets |
|  `workflow configure credentials update <NAME> --stdin`  | Read one `USERNAME:PASSWORD` line from stdin and update the managed credentials secret |
|  `workflow configure credentials update <NAME> --stdin --silent`  | Disable terminal echo while reading credentials from stdin |
|  `workflow configure credentials delete <NAME>`  | Delete a managed HTTP Basic credential secret after a confirmation prompt |
|  `workflow configure credentials delete --list`  | List managed HTTP Basic credential secrets |
|  `workflow configure credentials delete <NAME> -y` or `--yes`  | Delete a managed HTTP Basic credential secret without prompting |

 **workflow submit**

| Flag | Purpose |
| --- | --- |
|  `--wait`  | Block until the workflow completes or times out (default: return immediately) |
|  `--timeout <seconds>`  | Timeout when using `--wait` (default: 120) |
|  `--wait-interval <seconds>`  | Polling interval between status checks when using `--wait` (default: 2) |
|  `--session <name>`  | Configuration session name to load parameters from (default: `default`) |
|  `--workflow-name <name>`  | Name of the workflow to replace if one already exists (default: `migration-workflow`) |
|  `--unique-run-nonce <value>`  | Advanced: override the generated run nonce that is passed to downstream resources and names such as snapshots (default: current timestamp) |
|  `--namespace <ns>`  | Kubernetes namespace (default: `ma`) |

 **workflow status**

| Flag | Purpose |
| --- | --- |
|  `--all`  | Show all workflows including completed ones (default: only running) |
|  `--all-workflows`  | Show status for all workflows regardless of name (mutually exclusive with `--workflow-name`) |
|  `--workflow-name <name>`  | Show status for a specific workflow (default: `migration-workflow`) |
|  `--live-status` / `--no-live-status`  | Run or skip current status checks for each snapshot and backfill still in progress (default: `--live-status`) |
|  `--resource-view` / `--step-view`  | Show the resource-centric view or the current Argo Workflow step tree (default: `--step-view`) |
|  `--argo-server <url>`  | Argo Server URL (default: auto-detected from environment) |
|  `--namespace <ns>`  | Kubernetes namespace (default: `ma`) |
|  `--insecure`  | Skip TLS certificate verification (default: true) |
|  `--token <token>`  | Bearer token for Argo Server authentication |

 **workflow log**

| Flag | Purpose |
| --- | --- |
|  `--follow` / `-f`  | Stream logs live using `stern` (default: show historical logs) |
|  `--timestamps`  | Include RFC 3339 timestamps in log output |
|  `workflow log resource <RESOURCE>`  | Show logs for pods associated with one migration resource. Use typed names such as `snapshotmigration.<NAME>` when names overlap. |
|  `workflow log resource --list`  | List migration resources that can be used with `workflow log resource`  |
|  `workflow log filter --list`  | List available label selectors for `workflow log filter`  |
|  `--all-workflows`  | Show output for all workflows (mutually exclusive with `--workflow-name`) |
|  `--workflow-name <name>`  | Filter logs to a specific workflow (default: `migration-workflow`) |
|  `--source` / `--target` / `--snapshot` / `--task` / `--from-snapshot-migration <value>`  | Filter pods by the corresponding migration label (available on `workflow log filter`) |
|  `--label <key=value>`  | Additional raw label selector to filter pods, repeatable (e.g. `--label source=a --label target=b`); available on `workflow log filter`  |
|  `--prefix <prefix>`  | Label prefix for unqualified filter keys (default: `migrations.opensearch.org/`) |
|  `-- <kubectl-or-stern-args>`  | Forward extra arguments to `kubectl logs` for historical logs or `stern` when using `--follow`  |
|  `--namespace <ns>`  | Kubernetes namespace (default: `ma`) |
|  `--argo-server <url>`  | Argo Server URL |
|  `--insecure`  | Skip TLS certificate verification (default: true) |
|  `--token <token>`  | Bearer token for authentication |

 **workflow show**

| Flag | Purpose |
| --- | --- |
|  `<RESOURCE> [TASK]`  | Show the latest managed output artifact for a resource and optional task, such as `workflow show snapshotmigration.<NAME> evaluatemetadata`  |
|  `<TASK> [RESOURCE-FILTER]`  | Show latest output for a managed task across matching resources. Supported tasks are `evaluatemetadata` and `migratemetadata`; `metadataevaluate` and `metadatamigrate` are accepted as aliases. |
|  `evaluatemetadata.<NAME>` or `migratemetadata.<NAME>`  | Show metadata output using the approval-gate style name; the command maps it to the matching `snapshotmigration.<NAME>` output |
|  `--list`  | List resources and tasks that have managed output artifacts |
|  `--all`  | Show the latest managed output artifacts for all current resources |
|  `--history`  | List retained output artifacts for the selected resource UID instead of printing the latest output |
|  `--run <index-or-timestamp>`  | Show one retained artifact selected from `--history` by index or ISO timestamp |
|  `--clean`  | Print only the artifact content, without section headers |
|  `--namespace <ns>`  | Kubernetes namespace (default: `ma`) |

 **workflow manage**

| Flag | Purpose |
| --- | --- |
|  `--workflow-name <name>`  | Workflow to manage (default: `migration-workflow`) |
|  `--argo-server <url>`  | Argo Server URL (default: auto-detected from environment) |
|  `--namespace <ns>`  | Kubernetes namespace (default: `ma`) |
|  `--insecure`  | Skip TLS certificate verification (default: true) |
|  `--token <token>`  | Bearer token for authentication |
|  `--resource-view` / `--step-view`  | Open the resource-centric view or the current Argo Workflow step tree (default: `--step-view`) |

 **workflow reset**

| Flag | Purpose |
| --- | --- |
|  `<NAME>…​`  | One or more resource names or glob patterns to delete (e.g. `migration-foo`, `kafka-*`) |
|  `--list`  | List migration resources and exit without deleting anything |
|  `--all`  | Delete all migration custom resources |
|  `--cascade`  | Also delete resources that depend on the targeted resource |
|  `--include-proxies`  | Include capture proxies in deletion (they are protected by default) |
|  `--delete-storage`  | Delete Kafka PVCs and orphaned PVs during reset |
|  `--keep-output-artifacts`  | Keep retained workflow output artifacts and print their S3 prefix instead of deleting the artifact prefix with the resource |
|  `--namespace <ns>`  | Kubernetes namespace (default: `ma`) |

 **workflow approve**

| Flag | Purpose |
| --- | --- |
|  `<NAMES>` (one or more, supplied to a subcommand such as `step`, `change`, or `retry`) | Exact names or glob patterns of pending approval gates to approve (e.g. `workflow approve step 'evaluatemetadata.*'`) |
|  `--list`  | List gates instead of approving them. Use `workflow approve --list` for all categories or `workflow approve step --list`, `change --list`, or `retry --list` for one category. |
|  `--all`  | Approve every matching gate for the selected subcommand. For retry gates, the command blocks approval until required reset prerequisites are complete. |
|  `--pre-approve`  | For `step` and `change`, include pending gates the workflow has not reached yet. Retry gates do not support pre-approval. |
|  `--workflow-name <name>`  | Workflow containing the gates (default: `migration-workflow`) |
|  `--argo-server <url>`  | Argo Server URL (default: auto-detected from environment) |
|  `--namespace <ns>`  | Kubernetes namespace (default: `ma`) |
|  `--insecure`  | Skip TLS certificate verification (default: true) |
|  `--token <token>`  | Bearer token for authentication |

### Console commands
<a name="console-commands"></a>

The `console` CLI groups operations by component:

| Command | Why you use it |
| --- | --- |
|  `console --version`  | Confirms which schema and behavior your Migration Console is running |
|  `console clusters connection-check`  | Verifies the Migration Console can reach and authenticate to source and target |
|  `console clusters cat-indices [--cluster source\|target\|proxy]`  | Lists indexes on one or both clusters |
|  `console clusters curl source /_cat/indices?v`  | Issues a direct API request against the named cluster |
|  `console clusters clear-indices --cluster target --acknowledge-risk`  |  **Destructive** — deletes all indexes on the named cluster |
|  `console snapshot {create\|status\|delete\|unregister-repo}`  | Legacy/direct snapshot operations. In workflow-managed runs, snapshots are created and monitored by the workflow |
|  `console metadata {migrate\|evaluate}`  | Run or preview metadata migration outside the workflow |
|  `console backfill {describe\|start\|pause\|stop\|scale\|status}`  | Legacy/direct RFS backfill control. In workflow-managed runs, configure `documentBackfillConfig` and monitor `SnapshotMigration` resources with workflow commands |
|  `console replay {describe\|start\|stop\|scale\|status}`  | Legacy/direct component control for Traffic Replayer. In workflow-managed runs, use `workflow submit`, `workflow manage`, `workflow status --resource-view`, and `workflow log resource` instead |
|  `console metrics {list\|get-data}`  | Inspect Migration Assistant metrics |
|  `console kafka {create-topic\|list-topics\|delete-topic\|…​}`  | Inspect Strimzi-managed Apache Kafka used by capture and replay |
|  `console tuples`  | Inspect captured request/response tuples for replay validation |

**Note**
The workflow path drives `metadata`, `backfill`, and `replay` automatically. Reach for an equivalent `console` command only when the command is wired for the resource you are inspecting or when you are working around a specific direct-component failure. For workflow-managed runs, prefer `workflow manage`, `workflow status --resource-view`, `workflow log resource`, and `workflow show`.

## Approval gates
<a name="approval-gates"></a>

Not every migration step should run without human review. Approval gates let the workflow stop at meaningful checkpoints — typically transitions after metadata work, backfill milestones, and cutover-sensitive steps — so you can validate before continuing.

```
workflow manage
workflow approve step <STEP_NAME>
```

Approval behavior can also be controlled in the workflow configuration:
+  `skipApprovals` - top-level flag that skips all manual approval gates in the workflow.
+  `metadataMigrationConfig.skipEvaluateApproval` - skips the gate after metadata evaluation.
+  `metadataMigrationConfig.skipMigrateApproval` - skips the gate after metadata migration applies changes.
+  `documentBackfillConfig.skipApproval` - skips the gate after document backfill completes.

Use these flags only when validation, alerting, and rollback decisions are already automated. For first runs and pilots, leave approvals enabled so you can inspect metadata evaluation output, backfill status, and cutover-sensitive steps before continuing.

When a metadata gate is waiting, inspect the managed output before approving it. In `workflow manage`, select the metadata output step and use **Show Output**. For a non-interactive view, run `workflow show --list` to find the `snapshotmigration.<NAME>` resource, then run `workflow show snapshotmigration.<NAME> evaluatemetadata` or `workflow show snapshotmigration.<NAME> migratemetadata`. The workflow records the output artifact location on the `SnapshotMigration` resource, so `workflow show --history` can list retained reports for that resource.

## Status symbols
<a name="status-symbols"></a>

| Symbol | Meaning |
| --- | --- |
|  `✓`  | Succeeded |
|  `▶`  | Running |
|  `○`  | Pending |
|  `✗`  | Failed |
|  `⟳`  | Waiting for approval |

## Migration scenarios
<a name="migration-scenarios"></a>

Migration Assistant supports three migration patterns. Pick the one that matches your downtime tolerance.

### Scenario 1: Backfill only
<a name="scenario-backfill"></a>

Best when you can tolerate a brief write freeze, or when writes can be paused and replayed from an external queue.

```
Snapshot source → Migrate metadata → Backfill documents → Verify → Switch traffic
```

### Scenario 2: Capture and Replay only
<a name="scenario-replay"></a>

Best when the data is small enough that live replay alone can synchronize the target on Amazon OpenSearch Service or Amazon OpenSearch Serverless NextGen, or when you want to replay traffic against multiple targets to compare results.

```
Reroute traffic to capture proxy → Migrate metadata → Replay traffic → Verify → Switch traffic to target
```

### Scenario 3: Backfill \+ Capture and Replay (zero-downtime)
<a name="scenario-zero-downtime"></a>

The most comprehensive approach. Capture begins first so no writes are lost, then backfill brings over historical data, then replay catches the target up to real-time.

```
Reroute traffic to capture proxy → Snapshot source → Migrate metadata → Backfill documents → Replay captured traffic → Verify → Switch traffic to target
```

## Assessment and breaking changes
<a name="assessment-and-breaking-changes"></a>

Before running a migration, review breaking changes between your source and target versions. Breaking changes may require modifications to your client applications after the migration completes.

### Understanding breaking changes
<a name="understanding-breaking-changes"></a>

Between major versions of Elasticsearch and OpenSearch, features may be deprecated or removed. Common breaking changes include:
+ Removal of mapping types (Elasticsearch 6.x to 7.x and later)
+ Changes to field types (for example, `string` replaced by `text` and `keyword`)
+ Query DSL syntax changes
+ REST API endpoint changes
+ Plugin compatibility differences

For a complete list of breaking changes for your migration path, see the [Migration Assistant documentation](https://docs.aws.amazon.com/solutions/migration-assistant-for-amazon-opensearch-service/).

### Impact of data transformations
<a name="data-transformation-impact"></a>

Any time you apply a transformation to your data — such as changing index names, modifying field mappings, or splitting indexes with type mappings — these changes may need to be reflected in your client configurations. Run production-like queries against the Amazon OpenSearch Service domain or Amazon OpenSearch Serverless NextGen collection before switching over actual production traffic. This verifies that clients can communicate with the target, locate the necessary indexes and fields, and retrieve expected results.

For complex migrations involving multiple transformations, perform a trial migration with representative non-production data to fully test client compatibility.
