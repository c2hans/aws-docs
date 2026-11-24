---
source_url: https://docs.aws.amazon.com/eks/latest/userguide/agents.html
---

 **Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Overview of AI agents on Amazon EKS

An AI agent is a workload that decides its own next step at runtime. It calls a model, chooses a tool, acts on the result, and repeats until the task is done. Because a prompt or model output can steer what the agent does, you can’t predict its behavior the way you can for a conventional Kubernetes application.

Running agents in production therefore needs least privilege for each agent on its host, on the network, and in the credentials it holds. This section shows how to build those controls on Amazon EKS.

This section covers two deployment paths that build the same base, an EKS Auto Mode cluster where every agent runs in its own Nitro Sandbox with its own IAM role and an egress boundary it can’t change. The paths differ only in whether the layers around the agents, the egress gateway, memory, observability, and evaluation, run in the cluster or as AWS managed services. Which one fits depends on your platform. In your own platform you can combine components from both. The procedures in this section use [AI agents on Amazon EKS: reference sample](https://github.com/aws-samples/sample-eks-docs) on GitHub, called the reference sample on these pages, which implements each path as one configuration.
+  **Open source path.** The layers run in the cluster as open source components. [AgentGateway](https://github.com/agentgateway/agentgateway) is an open source gateway for model and tool calls. Valkey is a key-value store for session state, pgvector adds a vector index to Postgres, and Mem0 is a library that consolidates what to remember about each user. Prometheus and Grafana show metrics, and Langfuse stores traces and evaluation grades.
+  ** AWS services path.** AWS runs the layers as managed services. [AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html) is the managed gateway in Amazon Bedrock AgentCore, and Amazon ElastiCache, AgentCore Memory, Amazon CloudWatch, and AgentCore Evaluations provide session state, memory, observability, and evaluation. The ADOT collector, the AWS Distro for OpenTelemetry, sends the agents' telemetry to CloudWatch.

To start, create the base cluster in [Set up an Amazon EKS cluster for agent workloads](agents-cluster-setup.md).

Several names in this section contain the word sandbox. Nitro Sandboxes are the EC2 isolation that runs each pod in its own lightweight virtual machine, with its own guest kernel. A pod requests one with the `isolated-sandbox` runtime class. Agent Sandbox is a Kubernetes SIG project whose `Sandbox` object runs one long-lived agent pod and adds warm pools, suspend and resume, and scheduled deletion.

## Why run agents on Amazon EKS
<a name="agents-why-eks"></a>
+  **Use your existing platform.** An agent is a Kubernetes workload, so it shares clusters, pipelines, and on-call with the services it calls. Your platform team keeps using GitOps, admission policy, network policy, IAM, and its existing observability and security tools, and applies them per agent. The team that governs infrastructure lifecycle, security, and cost for your organization keeps that role for agents.
+  **Choose open source or AWS services per layer.** For each layer, Amazon EKS integrates with both. The gateway can be [AgentGateway](https://github.com/agentgateway/agentgateway) in your cluster or [AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html). Session state can be Valkey or Amazon ElastiCache Serverless for Valkey. Semantic recall can be pgvector or Amazon S3 Vectors. Observability can be Prometheus and Grafana or Amazon CloudWatch. Evaluation results can be Langfuse or AgentCore Evaluations.
+  **Enforce containment with cluster primitives.** An agent that runs model-generated code needs kernel-level isolation per workload, an egress boundary it can’t change, and credentials it can’t read. On Amazon EKS, those are the runtime class, network policy, and EKS Pod Identity, applied per agent. When you run the agent’s tools, cache, and vector index in the cluster, those calls stay on a network you control, under policies you manage as Kubernetes objects.

This section assumes your agents call a model you don’t host on Amazon EKS. For model serving and training, see [Overview of Artificial Intelligence and Machine Learning on Amazon EKS](ml-on-eks.md).

## EKS foundation for agents
<a name="agents-primitives"></a>

The following table lists the building blocks that every agent in this section runs on. What an agent adds on top depends on what it does. See [Agent archetypes](#agents-archetypes).

| Building block | EKS feature | What it gives an agent |
| --- | --- | --- |
| Isolation | Nitro Sandbox, `isolated-sandbox` runtime class | A separate guest kernel per pod, so code that escapes the container can’t reach the node or other agents. |
| Identity | EKS Pod Identity, an IAM role per agent |  AWS access that’s authorized, attributed, and revoked per agent. |
| Egress boundary | Network policy, enforced by EKS Auto Mode | Egress only to DNS and the agent’s approved destinations, which the agent can’t change. |
| Agent definition | An `Agent` resource, composed by the kro and ACK EKS Capabilities | One reviewable object that creates the agent’s identity, network policy, and workload. |
| Delivery | The Argo CD EKS Capability | The in-cluster components and each agent reconciled from Git. |

kro, Kube Resource Orchestrator, composes one custom resource into the Kubernetes objects it describes. ACK, AWS Controllers for Kubernetes, creates AWS resources, such as IAM roles, from Kubernetes objects. Both run as EKS Capabilities outside the cluster. Agents call models in Amazon Bedrock, and their images come from Amazon ECR.

## Deployment paths
<a name="agents-two-paths"></a>

Both paths share EKS Auto Mode, Amazon ECR, the Strands Agents SDK reference agent, Nitro Sandbox isolation, sandbox lifecycle, IAM roles with EKS Pod Identity, network policy, the Application Load Balancer with user authentication through an Amazon Cognito user pool or your OIDC provider, Amazon Bedrock for inference, and Amazon S3 for durable state.

They differ in whether the gateway, memory, evaluation, and observability run in the cluster or as AWS managed services. The reference sample implements each path as a separate configuration. The following table lists the component for each layer.

| Layer | Open source |  AWS services |
| --- | --- | --- |
| Egress gateway | AgentGateway | AgentCore Gateway |
| Gateway policy | AgentGateway policies | Policy in Amazon Bedrock AgentCore |
| Third-party credentials |  AWS Secrets Manager, synced to AgentGateway | AgentCore Identity |
| Observability | Prometheus, Grafana, and Langfuse | Amazon CloudWatch and AWS X-Ray, through the ADOT collector |
| Session state | Valkey | Amazon ElastiCache Serverless for Valkey |
| Semantic recall | pgvector | Amazon S3 Vectors |
| Consolidation | Mem0 | AgentCore Memory |
| Evaluations | Strands Evals, with grades in Langfuse | Strands Evals for release gates, AgentCore Evaluations |
| Service mesh | Istio in ambient mode, off by default | Istio in ambient mode, off by default |

**Sample templates and directional guidance**
The Amazon EKS service team doesn’t support the Terraform and GitOps templates or many of the open source components in this section. They’re sample code that shows one way to run agents on Amazon EKS, not a production-ready deployment. Adapt them to your architecture, security requirements, and deployment process, and review and test anything you adopt before you run it in production.
The Amazon EKS features the templates use, such as EKS Auto Mode, EKS Capabilities, EKS Pod Identity, and Nitro Sandboxes, are supported.

The following diagrams show each path.

------
#### [ Open source ]

The following diagram shows the open source path, where the platform team runs every component in the request path. The base setup is the cluster, network policy, and sandboxes, with agents calling Amazon Bedrock directly. Every other layer is off by default.

![The open source path. A caller reaches the agent in a Nitro Sandbox pod through an authenticating load balancer. The agent calls models and tools through AgentGateway. Valkey, pgvector, Prometheus, and Langfuse run in the cluster.](https://docs.aws.amazon.com/eks/latest/userguide/images/agents-open-source-path.png)

------
#### [  AWS services ]

The following diagram shows the AWS services path. It has the same controls, with managed services for the gateway, memory, evaluation, and observability. The base setup calls Amazon Bedrock directly, and every other layer is off by default.

![The managed services path. A caller reaches the agent in a Nitro Sandbox pod through an authenticating load balancer. The agent calls models and tools through AgentCore Gateway, with ElastiCache, AgentCore, and CloudWatch as managed services.](https://docs.aws.amazon.com/eks/latest/userguide/images/agents-aws-services-path.png)

------

## Agent workload characteristics
<a name="agents-what-is-different"></a>

The following table lists the agent characteristics that conventional application platforms don’t handle, and that the controls in this section address.

| Property | What it means |
| --- | --- |
| Untrusted code | The agent runs model-written code. A malicious prompt can make that code reach the network or read credentials. |
| High idle ratio | An interactive agent holds compute while it waits for a person. An idle pod per session doesn’t scale. |
| Rapid churn | Sessions start and stop in bursts, and users wait through every cold start. |
| Per-agent authority | Authorize and attribute each agent’s calls, and revoke one agent without affecting another. |
| Per-user authority | When an agent acts for a person, the systems it calls decide with that person’s permissions, so a request can’t reach another person’s data. |
| Unpredictable egress | An agent decides at runtime which hosts to call, so you can’t predict its destinations. |
| Policy at every layer | The sandbox, network policy, IAM, the gateway, and the mesh each enforce their own policy. |
| Cost per agent | Compute plus model tokens, reported by different systems. |

## Agent archetypes
<a name="agents-archetypes"></a>

Most agents fit one of a few archetypes. Every archetype runs on the building blocks in [EKS foundation for agents](#agents-primitives). Each of the following describes an archetype and lists the features it needs beyond those building blocks.

 **Request and response agent**
A stateless agent behind a Service that answers each request with a model call and tools.
+ An egress gateway, for per-agent token budgets and tool policy

 **Code-executing agent**
A software delivery agent that writes and runs code for the tasks you hand it.
+ An execution tier with no network device for model-written code
+ Credentials held by the gateway for the source repository
+ On-behalf-of authorization, only if each developer’s own repository access should bound the agent

 **Stateful interactive agent**
A chat or coding assistant that holds a session for days, with long idle gaps.
+ Session state outside the pod
+ A sandbox lifecycle that suspends idle sessions
+ User sign-in at ingress
+ Long-term memory
+ Evaluation of its responses

 **Agent acting for a person**
A customer-facing agent that issues a refund or unlocks an account.
+ User sign-in at ingress
+ On-behalf-of authorization, so the service decides with that person’s permissions rather than the agent’s

 **Operations agent**
An agent that inspects or changes infrastructure through `kubectl` or MCP tools.
+ Kubernetes API access with `needsClusterApi`, scoped by RBAC
+ Tools and tool policy at the gateway
+ Control plane audit logs, as a record the agent can’t alter

 **Retrieval agent**
An agent that answers questions over a document corpus.
+ A vector index for semantic recall

 **Background or scheduled agent**
An agent triggered by a schedule, a queue, or an event, with no person present.
+ A task runtime that runs work from a queue
+ Third-party credentials, with consent collected ahead of time

 **Multi-agent system**
An orchestrator that delegates to specialist agents.
+ A verifiable identity for each agent
+ A check of the caller at each specialist

Every archetype gains from observability, which attributes tokens, latency, errors, and refusals to each agent ([Observe agent workloads on Amazon EKS](agents-observability.md)).

## How this guide is organized
<a name="agents-structure"></a>

The pages are in deployment order. Deploy the base setup first, then add optional components.

## Base setup
<a name="agents-structure-base"></a>

In the base setup, every agent runs in a Nitro Sandbox, authenticates to AWS with its own IAM role, and can reach only DNS and its approved destinations. Agent namespaces reject pods without a sandbox runtime class and enforce network policy in strict mode.
+  [Set up an Amazon EKS cluster for agent workloads](agents-cluster-setup.md): The EKS Auto Mode cluster with network policy enforced, the container registry for the agent application code, and the permissions boundary, deployed with Terraform.
+  [Set up EKS Capabilities and in-cluster components for agents](agents-capabilities-setup.md): The EKS Capabilities that reconcile per-agent infrastructure, in-cluster components, and agentic applications.
+  [Deploy an agent on Amazon EKS](agents-application-setup.md): The `Agent` custom resource and the objects it creates.

The following pages explain the base runtime, identity, and networking controls.
+  [Isolate agent workloads on Amazon EKS](agents-isolation.md): The reasoning tier, the agent pod that calls the model, and the execution tier, a separate pod with no network device that runs model-generated code, and how Nitro Sandboxes apply to each.
+  [Give each agent its own identity with EKS Pod Identity](agents-identity-agent.md): Per-agent IAM roles, EKS Pod Identity session tags, and the tokens an agent presents.
+  [Restrict agent egress with network policy](agents-network-policies.md): The three policy tiers, and strict enforcement mode, which blocks traffic from a new pod until its policies are programmed.

The base setup also installs the Agent Sandbox controller. It stores no state; the session cache and durable storage are optional components. Without a gateway, agents call Amazon Bedrock directly with their own IAM role, and network policy permits the Amazon Bedrock runtime endpoint.

## Optional components
<a name="agents-structure-add-ons"></a>

Each of these components is off by default. Turn on only the ones your agents need.
+  [Route agent egress through a gateway](agents-gateway.md): Without a gateway, nothing limits how many tokens an agent spends or which tools it calls, and any credential an agent uses has to be in its pod. An egress gateway carries the agent’s model, tool, and third-party API calls, and applies per-agent model budgets, tool policy, and credentials held outside the pod to each one. AgentGateway runs in the cluster on the open source path, and AgentCore Gateway is managed on the AWS services path.
+  [Choose a service mesh mode for agents](agents-mesh.md): Network policy decides where a pod can connect, but not which workload is calling. A service mesh adds a verified caller identity, mTLS, and a record of each connection between unsandboxed workloads that run beside the agents, such as MCP and tool servers, and on the open source path it can route their calls through the gateway. It doesn’t capture a Nitro Sandbox pod’s traffic.
+  [Expose an agent through an authenticated Application Load Balancer](agents-ingress.md): Agents can’t be reached from outside the cluster by default. Ingress lets a person or an external application call an agent through an internal Application Load Balancer that authenticates the caller first.
+  [Act on behalf of a user with an agent on Amazon EKS](agents-identity-acting-for.md): By default, an agent acts with its own permissions whoever asked it. On-behalf-of authorization carries a person’s own permissions through the agent’s actions, so a tool or AWS refuses a request for data that person can’t reach, whatever the agent was asked to do. It requires ingress. On the open source path, AgentGateway signs the agent’s AWS calls for the person by default.
+  [Call third-party APIs from agents without giving them credentials](agents-third-party-credentials.md): An agent that calls a third-party API, such as GitHub, would otherwise hold that API’s token in its pod. The stack stores the token, collecting OAuth consent once where the API needs it, and the gateway attaches it to calls from the agent it belongs to.
+  [Manage the agent session lifecycle on Amazon EKS](agents-lifecycle.md): Agents sit idle most of the time and then start many sessions at once. The lifecycle choice decides what an idle agent costs and how isolated sessions are from each other, from a long-lived sandbox per agent (the default) to Deployment replicas to a sandbox per session with warm pools, suspend and resume, and scheduled deletion.
+  [Store agent session state](agents-session-state.md): An agent that keeps state in its pod loses the conversation when the pod restarts. Checkpoints in Amazon S3 let a restarted pod or another replica continue a session, and a session cache holds state that changes within a turn.
+  [Choose an agent’s memory components](agents-memory.md): Session state remembers one conversation. A vector index adds retrieval by meaning across conversations, and consolidation selects what to keep per user.
+  [Observe agent workloads on Amazon EKS](agents-observability.md): Pod metrics can’t show which agent spent tokens or called which tool. OpenTelemetry GenAI telemetry, a collector, dashboards, and per-agent cost attribution can, with a trace backend on the open source path. A policy decisions view shows what each control refused.
+  [Evaluate agent output on Amazon EKS](agents-evaluations.md): Agent output isn’t deterministic, so passing tests don’t prove the next release behaves. Evaluation grades agent output before a release and on live traffic. Both require observability, and the release gate also requires the gateway.

The following pages cover additional patterns:
+  [Use Amazon Bedrock or self-hosted inference for agents on Amazon EKS](agents-inference.md): Calling Amazon Bedrock, and when to serve a model on the EKS cluster instead.
+  [Give an agent tools with MCP](agents-mcp.md): Running and reaching Model Context Protocol tool servers.
