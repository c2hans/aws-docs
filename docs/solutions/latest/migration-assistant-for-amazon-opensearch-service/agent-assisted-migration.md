---
source_url: https://docs.aws.amazon.com/solutions/latest/migration-assistant-for-amazon-opensearch-service/agent-assisted-migration.html
---

# AI-assisted migration
<a name="agent-assisted-migration"></a>

Instead of manually constructing workflow JSON, running CLI commands, and troubleshooting issues step by step, you describe your migration goals in plain language and the agent handles the execution.

## Prerequisites
<a name="agent-prerequisites"></a>

Before starting, ensure you have the following:
+  **AWS credentials** configured for the target account (IAM Identity Center, temporary credentials, or an IAM role with sufficient permissions).
+  **AWS CLI v2** installed and configured.
+  **kubectl** installed — used to interact with the EKS-based Migration Assistant infrastructure.
+  **Helm 3** installed — used to install the Migration Assistant Helm chart.
+  **Network access** from your workstation to AWS APIs and, optionally, to the source cluster for assessment.
+  **Source cluster details** — endpoint, version, and authentication method for your Elasticsearch, OpenSearch, or Solr cluster.
+ A supported AI coding agent:
  + Kiro CLI or IDE
  + Claude Code
  + Codex
  + Cursor
  + Any other coding agent

**Note**
The Migration Assistant CLI is installed as part of the setup process below. Your AI coding tool may also guide you if any prerequisites are missing.

## Launch agent mode
<a name="agent-launch"></a>

Install the Migration Assistant CLI using the same installer as the manual workflow:

```
curl -fsSL https://solutions-reference.s3.amazonaws.com/migration-assistant-for-amazon-opensearch-service/latest/install.sh | bash
```

When prompted, choose **Agent mode** for an AI-guided experience, or **Manual** to configure the infrastructure yourself. Once installed, you can launch agent mode directly at any time:

```
migration-assistant agent
```

## What the agent does
<a name="agent-capabilities"></a>

The agent handles the operational complexity of the migration:

1.  **Discovers your environment** — identifies source clusters, validates connectivity, and checks prerequisites.

1.  **Proposes a plan** — recommends the migration path (historical data migration, live traffic migration, or both) based on your requirements.

1.  **Deploys infrastructure** — provisions the EKS cluster, networking, Kafka, and supporting services.

1.  **Configures the workflow** — builds the workflow configuration (source, target, snapshot settings, transform providers) and presents it for your review.

1.  **Runs the migration** — submits the workflow, monitors progress, and surfaces approval gates for you to review before proceeding.

1.  **Validates results** — compares document counts, verifies schema translation, and checks replayer health.

The following table describes the agent’s specific capabilities:

| Capability | Description |
| --- | --- |
| Infrastructure deployment | Deploys the full EKS stack, installs required add-ons (Pod Identity Agent), creates Pod Identity associations, and handles Helm chart installation. |
| VPC and networking | Detects VPC limits, offers to use existing VPCs, tags subnets for load balancer provisioning, and configures security groups for connectivity. |
| Image management | Mirrors container images to ECR, retries on rate-limiting failures, and verifies correct image tags (for Solr transform support). |
| Kafka cluster management | Manages Strimzi Kafka lifecycle, resets CrashLooping operators, and validates topic provisioning. |
| Schema extraction | Retrieves schema files from ZooKeeper (for Solr sources), creates ConfigMaps. |
| Workflow configuration | Generates complete workflow JSON from conversational inputs, sets `targetType` correctly for Serverless NextGen targets, and configures transform providers. |
| Monitoring and validation | Tracks workflow progress, checks document counts, verifies schema translation, and confirms replayed traffic appears in the target. |
| Credential management | Detects credential expiry mid-operation, prompts for refresh, and resumes where it left off. |

## Starting a session
<a name="agent-session"></a>

The agent greets you and asks what you’d like to accomplish. You can request:
+  **An assessment** — The agent connects to your source cluster (read-only), analyzes the schema, identifies compatibility gaps, and produces a migration assessment report. If you cannot connect to your cluster, the agent asks you for the required information to generate the assessment.
+  **A deployment** — The agent deploys the Migration Assistant infrastructure (CloudFormation stack \+ EKS cluster \+ Helm chart) into your AWS account. Standard AWS pricing applies.
+  **A migration** — The agent configures and runs the end-to-end migration workflow, including historical data backfill and optional live traffic capture and replay.

Describe your goal in plain language. For example:

"I want to migrate my Solr 8.11 cluster to OpenSearch Serverless NextGen."

"Deploy Migration Assistant in us-west-2 so I can start testing."

"Run the historical data migration for my Elasticsearch 7.10 cluster."

## Working with the agent
<a name="agent-working"></a>

### Confirm before you begin
<a name="agent-confirm"></a>

The agent asks you to confirm three things before touching any infrastructure:
+  **AWS account** — The agent runs `aws sts get-caller-identity` and shows you the account and role. Confirm it is correct.
+  **AWS region** — The agent asks which region to operate in. Do not assume it uses your CLI default.
+  **Stage name** — This becomes the Kubernetes namespace, Helm release, and CloudFormation stack suffix.

### Approval gates
<a name="agent-approval-gates"></a>

The migration workflow includes approval gates at key checkpoints. When the workflow pauses for approval, the agent shows you what was evaluated (for example, the schema translation results) and asks whether to proceed. Review the output before approving.

You can also give the agent explicit guardrails for your session. For example:
+  *"Always ask me before running any `kubectl delete` or `helm uninstall` command."*
+  *"Do not modify my source cluster in any way."*
+  *"Do not skip approval gates — I want to review each step."*

The agent respects these instructions for the duration of the session.

## Security and control
<a name="agent-safety"></a>
+  **Your credentials** — The agent uses your existing AWS credentials and `kubectl` context. It does not store or transmit credentials.
+  **Destructive actions** — The agent asks for explicit confirmation before operations such as deleting VPCs, removing existing workflow resources, or modifying production clusters.
+  **Auditability** — All commands the agent runs are visible in the session transcript. You can review exactly what was executed.

The following safety behaviors are active by default:

| Behavior | Description |
| --- | --- |
| Show before running | Any command that modifies AWS, Kubernetes, or cluster state is shown to you for confirmation before execution. |
| Stop on failure | When something fails, the agent stops, describes the problem, and presents options rather than attempting automatic fixes. |
| Read-only source access | The agent never modifies your source cluster (no config changes, no synthetic writes, no collection creation) without your explicit instruction. |
| No credential storage | The agent never writes passwords, tokens, or secrets to files. |
| Approval gates preserved | The agent does not skip workflow approval gates unless you specifically request it. |

## Important guidance for working with AI agents
<a name="agent-ai-guidance"></a>

AI agents are powerful assistants, but they require your oversight.
+  **AI models can produce incorrect output.** If a root cause analysis or recommendation does not align with what you are observing, probe further. Ask the agent to show the raw logs, re-examine the evidence, or consider alternative explanations.
+  **Cross-check recommendations** against the [AWS documentation](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/) and your own operational knowledge.
+  **Review execution steps before approving.** The agent shows commands before running them. Ensure the region, account, endpoint, and parameters match your expectations.

### When something goes wrong
<a name="agent-failures"></a>

If the agent encounters an error during deployment or migration:

1. It collects diagnostics (pod status, logs, events) using read-only commands.

1. It describes the problem with the exact error message.

1. It presents options — typically: fix in-place, tear down and redeploy, or investigate further.

1. It waits for your choice before proceeding.

If the agent’s diagnosis does not make sense to you, ask it to gather more evidence or try a different angle:

"I don’t think that’s the root cause. Can you check the pod logs for the last 5 minutes instead?"

## Example session
<a name="agent-example"></a>

```
$ migration-assistant agent

Welcome to Migration Assistant for Amazon OpenSearch Service.

I can help you:

  [1] Assess or plan a migration
  [2] Deploy migration infrastructure into my AWS account
  [3] Run a migration

What are you trying to accomplish today?

> I want to migrate my Elasticsearch 7.10 cluster to Amazon OpenSearch Service.
  It's running on EC2 in us-east-1. I need zero downtime.

Let me start by confirming your AWS identity...
```

From here, the agent walks you through discovery, deployment, configuration, and execution — one step at a time, with your approval at each checkpoint.

## Next steps
<a name="agent-next-steps"></a>

For the manual CLI workflow, see [Configure and run workflows](use-the-solution.md).

For full reference documentation, see [Migration Assistant for Amazon OpenSearch Service documentation](https://docs.aws.amazon.com/solutions/migration-assistant-for-amazon-opensearch-service/).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Migration Assistant for Amazon OpenSearch Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
