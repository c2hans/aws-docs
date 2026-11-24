---
source_url: https://docs.aws.amazon.com/eks/latest/userguide/agents-memory.html
---

 **Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Choose an agent’s memory components

A model keeps no state between calls. Anything an agent remembers, from the previous turn to a preference a user stated last month, is stored outside the model and loaded back into its context. These stores hold what people told your agents, so they need the same retention, access control, and isolation as any other store of user data.

Agents typically need these capabilities in order as the workload grows more complex. Most agents with more than one turn need session state, and many also need durable checkpoints so that a conversation or a task survives a pod restart. Fewer need semantic recall, and only agents that personalize across sessions need consolidation. Each capability adds a component to operate and secure, so turn on only the ones your agent needs.

| Capability | Agent gains | You take on |
| --- | --- | --- |
| Session state | Continuity between turns, and replicas that can serve any turn | A key-value store |
| Durable checkpoints | State and conversations that survive the pod | An Amazon S3 bucket |
| Semantic recall | Retrieval by meaning over a corpus or past interactions | A vector index tied to one embedding model |
| Consolidation | Facts selected and reconciled across sessions, scoped per user | A consolidation layer, plus model calls to extract what to keep |

The following diagrams show each path.

------
#### [ Open source ]

The following diagram shows the open source path. Consolidation runs as the Mem0 library inside the agent and stores memories in pgvector on CloudNativePG in the cluster. Consolidation requires semantic recall and the gateway.

![Inside the agent’s Nitro Sandbox pod, the Mem0 library consolidates memories and stores them in pgvector on CloudNativePG, which provides semantic recall.](https://docs.aws.amazon.com/eks/latest/userguide/images/agents-memory-open-source.png)

------
#### [  AWS services ]

The following diagram shows the AWS services path. Semantic recall uses Amazon S3 Vectors, and consolidation uses AgentCore memory. The stack grants the agent access and passes it the resource names. The agent’s code makes the calls.

![The agent puts and queries vectors in Amazon S3 Vectors for semantic recall, and writes events to AgentCore memory, which consolidates them into scoped records.](https://docs.aws.amazon.com/eks/latest/userguide/images/agents-memory-aws-services.png)

------

## Open source and AWS services paths
<a name="agents-memory-paths"></a>

The following table compares how each path provides each memory capability.

| Aspect | Open source |  AWS services |
| --- | --- | --- |
| Session state | Valkey in the cluster | Amazon ElastiCache Serverless |
| Durable checkpoints | A versioned Amazon S3 bucket with one prefix per agent | A versioned Amazon S3 bucket with one prefix per agent |
| Semantic recall | pgvector on Postgres, run in the cluster by the CloudNativePG operator | Amazon S3 Vectors, in a shared vector bucket |
| Consolidation | The Mem0 library inside the agent, storing records in the semantic recall tier | AgentCore memory, a managed service with its own record store |
| Consolidation requires | Semantic recall, the gateway, and `platform-secrets`  | No other memory capability |
| Separation between agents | One Postgres table per agent for Mem0 records | Namespaces in one shared memory, and one vector bucket that every agent’s grant covers |
| Who operates the stores | You operate Valkey and Postgres, including backups, upgrades, and capacity | The managed services, with no tier to operate |

## Choose memory capabilities
<a name="agents-memory-decide"></a>

An agent whose work ends within one task, such as a coding agent or a build-and-test agent, needs none of these. Its state is ephemeral, and its execution tier exchanges files through a workspace volume. For other agents, use the following:
+  **The agent has more than one turn:** session state. Turn it on before you run more than one replica.
+  **A conversation or a task must survive a pod restart, or the execution tier returns files:** durable checkpoints.
+  **The agent answers questions over a corpus:** semantic recall.
+  **The agent personalizes across sessions, or several agents share one model of the same user:** consolidation.

The capabilities you need don’t depend on the path you chose. Each has an open source and a managed option.

## Session state
<a name="agents-memory-session"></a>

Most agents have more than one turn, and between turns they hold the conversation so far, intermediate results, and tool outputs. Kept in the pod, that state ties a session to one replica and disappears when the pod restarts. Kept in a key-value store, it lets any replica serve the next turn and survives a restart. A key-value store is enough, because the agent reads and writes this state by session ID and doesn’t search it.

The open source option is Valkey in the cluster. The managed option is Amazon ElastiCache Serverless for Valkey, or Amazon MemoryDB when the state must also survive a cache failure. Store structured facts that an agent writes and reads back in a relational database you already operate.

The cache is shared, so isolating one agent’s sessions from another’s is a design decision. See [Store agent session state](agents-session-state.md).

## Durable checkpoints
<a name="agents-memory-durable"></a>

Durable checkpoints hold state that must outlive the pod, such as a checkpoint an agent resumes from, the record of its actions, and files returned by the execution tier. Both paths use a versioned Amazon S3 bucket with one prefix per agent, enforced in each agent’s IAM policy. The reference agent saves its conversation there. If you split an agent into two tiers, the execution tier can exchange data only through a volume and this bucket. See [Durable state in Amazon S3](agents-session-state.md#agents-session-state-durable) and [Save the conversation between turns](agents-session-state.md#agents-session-state-conversation).

## Semantic recall
<a name="agents-memory-recall"></a>

Semantic recall lets an agent find stored text by meaning instead of by key. An embedding model turns each piece of text into a vector, and a vector index returns the stored vectors closest to the vector of a query. An agent that answers questions over a corpus needs semantic recall, and an agent that needs only retrieval needs nothing more.

An index is bound to the embedding model that fills it. The vector length is fixed when the index is created, and so is the distance metric that ranks matches, so changing the embedding model means building a new index. Cosine distance suits most text embeddings.

The two options trade operating effort for control:
+  **pgvector** adds a vector index to Postgres. If you already operate Postgres, add the index there instead of running a second database for one index. You own backups, upgrades, and capacity. The sample includes a Postgres tier, run by the CloudNativePG operator, for clusters without one.
+  **Amazon S3 Vectors** is managed, with no tier to operate. Vectors live in a vector bucket that holds one or more indexes. A dimension mismatch isn’t detected until the first write, so confirm your embedding model’s vector length before you create an index.

Isolation between agents works the same way as for any shared store. In the sample, every agent’s IAM grant covers the whole shared vector bucket, so one agent can query another’s vectors unless you separate them. Give each agent its own index and scope its grant to that index, or keep vectors that must stay private in a store only that agent can reach.

## Consolidation
<a name="agents-memory-consolidation"></a>

Retrieval returns whatever was stored, including statements that are no longer true. Consolidation sits above the stores and decides what to keep. It extracts facts from conversations, reconciles a new statement with a stored one so that a changed preference replaces the old one, and scopes each record to a user and an agent. An agent that personalizes across sessions, or several agents that share one model of the same user, need consolidation. Most agents don’t, and it adds a stateful tier and the model calls that do the extraction.

Scoping is the security property of consolidation. A consolidated store holds facts about many people. If records aren’t scoped per user, an agent can return one person’s context in another person’s session. Both options scope by namespace, a path filled in from the user and session IDs on each event, such as `/agents/{actorId}/{sessionId}`. A strategy that defines no namespace pools every user’s records.

The two options differ in where consolidation runs:
+  **Mem0** runs as a library inside the agent and stores records in the semantic recall tier. Its extraction and embedding calls are model calls the agent makes through the gateway with its own token, so they count against the agent’s budget and appear in its audit trail. The agent image must include Mem0. The reference sample’s reference image does.
+  **AgentCore memory**, a capability of Amazon Bedrock AgentCore, runs consolidation as a managed service with its own record store. A strategy tells it what to extract, such as user preferences, and its namespaces say where each record goes. In the sample, the stack has one memory and every agent’s grant covers all of it, because AgentCore memory has no ACK controller to create one per agent. The namespaces are then the only separation between agents.

Set how long records are kept from your organization’s data retention policy, because the store holds what people told your agents.

## Memory in the reference sample
<a name="agents-memory-settings"></a>

The base setup in the reference sample turns off all four. Each is a Terraform variable on both paths. `enable_session_state` turns on session state, `enable_checkpoints` durable checkpoints, `enable_semantic_recall` semantic recall, and `enable_consolidation` consolidation. Session state and durable checkpoints are set up in [Store agent session state](agents-session-state.md), and this page sets up the other two. Consolidation’s requirements differ by path:
+  **Open source path.** Consolidation also requires semantic recall, the gateway, and `platform-secrets`.
+  ** AWS services path.** Consolidation doesn’t require semantic recall, because AgentCore Memory stores its own records.

## Prerequisites
<a name="agents-memory-prereqs"></a>
+ The base setup from [Set up an Amazon EKS cluster for agent workloads](agents-cluster-setup.md), applied, and the in-cluster components from [Set up EKS Capabilities and in-cluster components for agents](agents-capabilities-setup.md), synced.
+ For consolidation on the open source path: the gateway from [Route agent egress through a gateway](agents-gateway.md), semantic recall, `platform-secrets`, and an agent image that includes Mem0, such as the sample’s reference image.
+  `PAVED_PATH` set to `open-source` or `aws-services`, such as with `export PAVED_PATH=open-source`.
+ A shell with `kubectl` access to the cluster, on the bastion or your workstation, and an agent deployed as in [Deploy an agent on Amazon EKS](agents-application-setup.md). The commands use the reference agent `research` in namespace `agents`.

## Step 1: Turn on semantic recall and consolidation
<a name="agents-memory-step1"></a>

This step turns on the capabilities your agents need. Outside these templates, create the same stores, grant each agent’s role access, and pass the resource names to the agent as environment variables.

------
#### [ Open source ]

Set the variables. Each capability is one variable:

```hcl
enable_semantic_recall = true
enable_consolidation   = true
```

Apply and sync:

```bash
./scripts/apply.sh --root terraform/open-source -var-file=my.tfvars
./scripts/run-stack.sh --root terraform/open-source -- ./scripts/bootstrap-gitops.sh --path open-source --sync --roll-agents
```

 `enable_semantic_recall` deploys the CloudNativePG operator and a Postgres cluster with pgvector in namespace `agent-memory`, and `enable_consolidation` passes the agent the database host in `AGENT_CONSOLIDATION_DB_HOST` and the credential’s secret ARN in `AGENT_CONSOLIDATION_DB_SECRET_ARN`.

The reference agent builds Mem0 from those variables when consolidation is on. It reads the database login from Secrets Manager with its own role, and sends both of Mem0’s model calls, extraction and embedding, through the gateway’s OpenAI-compatible endpoint with its gateway token. Those calls count against the agent’s token budget and appear in its audit trail like any other model call. The following excerpt is the Mem0 configuration the agent passes to `Memory.from_config`:

```python
{
    "vector_store": {
        "provider": "pgvector",
        "config": {
            "host": os.environ["AGENT_CONSOLIDATION_DB_HOST"],
            "port": 5432,
            "dbname": "agentmemory",
            "user": login["user"],                 # from AGENT_CONSOLIDATION_DB_SECRET_ARN
            "password": login["password"],
            "collection_name": "mem0_research",    # one table per agent
            "embedding_model_dims": 1024,
        },
    },
    "llm": {
        "provider": "openai",                      # the gateway speaks the OpenAI API
        "config": {"model": os.environ["AGENT_MODEL"], "openai_base_url": gateway_url, "api_key": token},
    },
    "embedder": {
        "provider": "openai",
        "config": {"model": "amazon.titan-embed-text-v2:0", "openai_base_url": gateway_url,
                   "api_key": token, "embedding_dims": 1024},
    },
}
```

One table per agent keeps each agent’s memories separate in the shared Postgres cluster. The embedding dimension must match the model, and 1024 matches Amazon Titan Text Embeddings V2.

------
#### [  AWS services ]

Set the variables. The following example turns on both. Address an index as `bucket-arn/index/index-name`. A dimension of 1024 matches Amazon Titan Text Embeddings V2. Built-in strategies such as `USER_PREFERENCE` need no model grant, because AgentCore manages their models. A custom strategy extracts with a model you choose, so list that model in `consolidation_model_arns`, which the memory’s execution role is allowed to invoke.

```hcl
enable_semantic_recall  = true
semantic_recall_indexes = {
  recall = { dimension = 1024, distance_metric = "cosine" }
}

enable_consolidation     = true
consolidation_strategies = {
  preferences = { type = "USER_PREFERENCE", namespaces = ["/agents/{actorId}/{sessionId}"] }
}
```

Apply and sync:

```bash
./scripts/apply.sh --root terraform/aws-services -var-file=my.tfvars
./scripts/run-stack.sh --root terraform/aws-services -- ./scripts/bootstrap-gitops.sh --path aws-services --sync --roll-agents
```

 `enable_semantic_recall` creates the shared vector bucket and the indexes you declare in `semantic_recall_indexes`, and gives each agent the bucket ARN in `AGENT_VECTOR_BUCKET_ARN`, an IAM grant to read, write, and query vectors, and an egress rule to the Amazon S3 Vectors endpoint. `enable_consolidation` creates one AgentCore memory with the strategies in `consolidation_strategies`, and gives each agent the memory ID in `AGENT_MEMORY_ID`, a grant for events and memory records, and an egress rule to the AgentCore data plane.

------

The bootstrap script applies the rendered root Application, refreshes and syncs it, and waits for the Applications to converge. With `--roll-agents`, it then recreates each agent pod whose `Sandbox` changed, and prints a line for each agent, such as `agents/research: recreating (env AGENT_MEMORY_ID added)`, or `current` for an agent that didn’t change.

Every Application reports `Synced` and `Healthy`. If one stays `Progressing` after its objects are ready, run the bootstrap script again, because Argo CD can keep the health it computed while they were starting. See [Turn on a component later](agents-capabilities-setup.md#agents-capabilities-later).

**Important**
A `Sandbox` doesn’t replace its running pod when its spec changes, so without `--roll-agents` a sandboxed agent keeps running without the new variable. The `--roll-agents` on the sync recreates the pod. To confirm that the agent’s `Sandbox` has the new variable, run the following. The variable depends on the path:
 **Open source path.** `AGENT_CONSOLIDATION_DB_HOST`.
 ** AWS services path.** `AGENT_VECTOR_BUCKET_ARN` or `AGENT_MEMORY_ID`.

```bash
./scripts/run-stack.sh --root terraform/$PAVED_PATH -- bash -c "kubectl -n agents get sandbox research -o yaml | grep -A1 -E 'AGENT_CONSOLIDATION_DB_HOST|AGENT_VECTOR_BUCKET_ARN|AGENT_MEMORY_ID'"
```
An agent with `runtime: deployment` rolls automatically.

## Step 2: Verify each capability as the agent
<a name="agents-memory-verify"></a>

This step confirms each capability works with the agent’s own identity.

------
#### [ Open source ]

After Step 1, the agent’s pod has `AGENT_CONSOLIDATION_DB_HOST` and `AGENT_CONSOLIDATION_DB_SECRET_ARN`.

Confirm the pgvector tier is healthy, then run the `memory` phase of the sample’s `exercise.sh`. It confirms that a fact from one session is extracted and stored, is recalled in a new session for the same user, and is not recalled for another user:

```bash
kubectl get clusters.postgresql.cnpg.io -n agent-memory    # STATUS: Cluster in healthy state
./scripts/exercise.sh --path open-source memory
```

------
#### [  AWS services ]

After Step 1, the agent’s pod has `AGENT_VECTOR_BUCKET_ARN` and `AGENT_VECTOR_INDEXES` for semantic recall, and `AGENT_MEMORY_ID` and `AGENT_MEMORY_NAMESPACES` for consolidation.

Run the `memory` phase of the sample’s `exercise.sh`. It runs from a short-lived AWS CLI pod with the agent’s service account, its `eks-agents/agent` label, and its sandbox, so it tests the agent’s own permissions without a model call. That pod can do exactly what the agent can.
+  **Semantic recall.** It writes a vector to the first index in `AGENT_VECTOR_INDEXES` and queries it back, and confirms that the agent’s role cannot list the bucket’s indexes.
+  **Consolidation.** It writes a conversational event, then waits for the record the strategy extracts, in the namespace from `AGENT_MEMORY_NAMESPACES` with the actor and session IDs filled in. The strategy extracts the record asynchronously, so the record appears some time after its event.

```bash
./scripts/exercise.sh --path aws-services memory
```

An agent makes the same calls with its AWS SDK, using its own role. The following commands show them with the CLI. `EMBEDDING` stands for a 1024-dimension vector from your embedding model, and the index and memory names come from the agent’s environment:

```bash
# Semantic recall: store a vector and query by similarity.
aws s3vectors put-vectors --vector-bucket-name my-agents-agent-vectors-111122223333 --index-name recall \
  --vectors '[{"key":"note-1","data":{"float32":EMBEDDING}}]'
aws s3vectors query-vectors --vector-bucket-name my-agents-agent-vectors-111122223333 --index-name recall \
  --top-k 1 --query-vector '{"float32":EMBEDDING}' --return-distance

# Consolidation: record a conversation, then read what the strategy extracted.
aws bedrock-agentcore create-event --memory-id {{memory-id}} --actor-id user-1 --session-id s1 \
  --event-timestamp "$(date +%s)" \
  --payload '[{"conversational":{"role":"USER","content":{"text":"I want answers in metric units."}}}]'
aws bedrock-agentcore list-memory-records --memory-id {{memory-id}} --namespace /agents/user-1/s1
```

The namespace in `list-memory-records` is the strategy’s namespace template, `/agents/{actorId}/{sessionId}`, with the actor and session IDs filled in. Scoping records to the actor is what keeps one user’s memories out of another user’s recall.

With consolidation on, the reference agent makes these calls itself. After each turn it writes the person’s message and its reply as one conversational event. The actor ID is derived from the verified caller and, beneath it, the person a front end names, so each person has their own records. To recall, it searches under the person’s part of each namespace template with `namespacePath`, which returns records from every earlier session, not only the current one:

```bash
aws bedrock-agentcore retrieve-memory-records --memory-id {{memory-id}} \
  --namespace-path /agents/user-1/ --search-criteria '{"searchQuery":"units","topK":3}'
```

Include `{actorId}` in every namespace template. A template without it pools every person’s records, and the reference agent doesn’t search it on a person’s behalf. To confirm that two people stay apart end to end, through the chat interface, run the `people` phase. See [Keep people apart behind a shared agent](agents-identity-acting-for.md#agents-identity-acting-for-try).

------

## Clean up
<a name="agents-memory-cleanup"></a>

To remove semantic recall and consolidation, turn it off as described in [Turn on a component later](agents-capabilities-setup.md#agents-capabilities-later). Set the variable to `false`, apply with `scripts/apply.sh`, and run the bootstrap script with `--sync --prune`. Set `enable_consolidation` to `false` first, then `enable_semantic_recall`, because consolidation on the open source path stores its records in the semantic recall tier.

------
#### [ Open source ]

**Important**
These stores hold what people told your agents. Move any data you need before you delete them.
Turning `enable_semantic_recall` off doesn’t delete the pgvector database. Both of its Argo CD Applications, `cloudnative-pg` and `agent-semantic-recall`, are marked `Prune=false`, so the prune leaves the database running. Consolidation adds no store of its own, because Mem0 runs inside the agent and writes to the same database.

1. After you move the data, delete the two Applications to remove the database and the operator. Delete the database first, so the operator can process its finalizers:

   ```bash
   ./scripts/run-stack.sh --root terraform/open-source -- \
     kubectl -n argocd delete applications.argoproj.io agent-semantic-recall
   ./scripts/run-stack.sh --root terraform/open-source -- \
     kubectl -n argocd delete applications.argoproj.io cloudnative-pg
   ```

1. Delete the database’s volume claims, which keep billing after the database is gone, and confirm that none are left. Deleting a claim deletes its volume:

   ```bash
   ./scripts/run-stack.sh --root terraform/open-source -- \
     kubectl -n agent-memory delete pvc -l cnpg.io/cluster
   ./scripts/run-stack.sh --root terraform/open-source -- \
     kubectl -n agent-memory get pvc -l cnpg.io/cluster
   ```

   The second command returns no claims.

1. Recreate each agent’s pod, so it starts without the memory variables. See [Turn on a component later](agents-capabilities-setup.md#agents-capabilities-later).

------
#### [  AWS services ]

**Important**
These stores hold what people told your agents. Move any data you need before you delete them.
Turning `enable_semantic_recall` off deletes the vector bucket and its indexes. Turning `enable_consolidation` off deletes the AgentCore memory and every record in it.

1. Recreate each agent’s pod, so it starts without the memory variables. See [Turn on a component later](agents-capabilities-setup.md#agents-capabilities-later).

------

## Next steps
<a name="agents-memory-next"></a>

 [Evaluate agent output on Amazon EKS](agents-evaluations.md) for grading what the agent does with its memory.
