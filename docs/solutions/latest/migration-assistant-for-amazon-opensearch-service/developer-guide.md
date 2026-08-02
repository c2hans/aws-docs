---
source_url: https://docs.aws.amazon.com/solutions/latest/migration-assistant-for-amazon-opensearch-service/developer-guide.html
---

# Developer guide
<a name="developer-guide"></a>

This section provides the source code for the solution.

## Source code
<a name="source-code"></a>

The solution source code includes the Migration Assistant Helm chart, the Workflow CLI, the bootstrap script, the Reindex-from-Snapshot engine, the Capture Proxy, the Traffic Replayer, and supporting tooling.

The Amazon EKS deployment is bootstrapped by `aws-bootstrap.sh`, which deploys an AWS CloudFormation stack and installs the Migration Assistant Helm chart. The AWS CloudFormation stacks deployed by the bootstrap script are generated from AWS Cloud Development Kit (AWS CDK) constructs.

For Migration Assistant releases, see [Revisions](revisions.md). Pinning to a specific release tag using the `--version <tag>` flag of the bootstrap script is recommended for reproducible deployments.

## Using AI agents for migration
<a name="agent-assisted-migrations"></a>

Migration Assistant includes an AI agent mode that allows you to run migrations conversationally. Instead of manually constructing workflow JSON, running CLI commands, and troubleshooting issues step by step, you describe your migration goals in plain language and the agent handles the execution.

The agent can:
+  **Deploy infrastructure** — Run the full Migration Assistant deploy pipeline (CloudFormation → Amazon EKS → image mirroring → Helm install) with automatic error recovery.
+  **Generate configuration** — Build workflow JSON from your description of source cluster, target cluster, collections, and authentication requirements.
+  **Operate the migration** — Submit workflows, monitor progress, handle approval gates, and troubleshoot failures in real time.
+  **Validate results** — Check document counts, verify schema translation, confirm traffic replay, and report discrepancies.
+  **Troubleshoot automatically** — Recognize common failure patterns and apply fixes without manual intervention.

### Prerequisites
<a name="agent-prerequisites"></a>
+ Migration Assistant CLI installed (`migration-assistant` binary on your PATH).
+ A supported AI coding agent configured:
  +  [Kiro CLI](https://kiro.dev/docs/cli/) (recommended for AWS environments)
  +  [Kiro IDE](https://kiro.dev/docs/getting-started/installation/)
  +  [Claude Code](https://code.claude.com/docs/en/quickstart)
  +  [Codex](https://developers.openai.com/codex/cli)
  +  [Cursor](https://cursor.com/docs)
+ AWS credentials with sufficient permissions for Amazon EKS, AWS CloudFormation, Amazon ECR, and Amazon S3.

### Getting started
<a name="agent-getting-started"></a>

Install the Migration Assistant CLI, then launch an interactive agent session:

```
migration-assistant
```

The CLI automatically detects which agents are installed on your system. It sets up a workspace with skills (domain knowledge for deploying, operating, and troubleshooting migrations), then hands off to your chosen agent. Terminal agents (Kiro CLI, Claude Code, Codex) run in your current terminal. IDE agents (Kiro IDE, Cursor) open a workspace — you drive the migration from the in-IDE chat panel.

### Agent capabilities
<a name="agent-capabilities"></a>

| Capability | Description |
| --- | --- |
| Infrastructure deployment | Deploys the full Amazon EKS stack, installs required addons (Pod Identity Agent), creates Pod Identity associations, and handles Helm chart installation. |
| VPC and networking | Detects VPC limits, offers to use existing VPCs, tags subnets for load balancer provisioning, and configures security groups for connectivity. |
| Image management | Mirrors container images to Amazon ECR, retries on rate-limiting failures, and verifies correct image tags for Solr transform support. |
| Kafka cluster management | Manages Strimzi Kafka lifecycle, resets CrashLooping operators, and validates topic provisioning. |
| Schema extraction | Retrieves schema files from ZooKeeper (for Solr sources) using the correct method, creates Kubernetes ConfigMaps. |
| Workflow configuration | Generates complete workflow JSON from conversational inputs, sets `targetType` correctly for Serverless targets, configures transform providers. |
| Monitoring and validation | Tracks workflow progress, checks document counts, verifies schema translation, confirms replayed traffic appears in the target. |
| Credential management | Detects credential expiry mid-operation, prompts for refresh, and resumes where it left off. |

### Security and control
<a name="agent-security"></a>
+  **Your credentials** — The agent uses your existing AWS credentials and `kubectl` context. It does not store or transmit credentials.
+  **Approval gates** — Workflow configurations include approval gates at key checkpoints (after metadata migration, after backfill). The agent pauses and asks for your confirmation at these points unless you explicitly choose to skip approvals.
+  **Destructive actions** — The agent asks for explicit confirmation before operations like deleting VPCs, removing existing workflow resources, or modifying production clusters.
+  **Auditability** — All commands the agent runs are visible in the session transcript. You can review exactly what was executed.
