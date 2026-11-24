---
source_url: https://docs.aws.amazon.com/eks/latest/userguide/agents-inference.html
---

 **Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Use Amazon Bedrock or self-hosted inference for agents on Amazon EKS

An agent calls a model on every turn, so the model source largely determines the agent’s latency, cost, and failure modes. The controls on model access also decide what a compromised or runaway agent can spend. Two decisions follow from that: where the model runs, and where access to it is enforced.

Amazon Bedrock needs no infrastructure and scopes access with IAM. Serving a model on the cluster lets you host the weights yourself. See [Choose a model source](#agents-inference-choose). You can combine sources. A common pattern is Amazon Bedrock for general reasoning and a self-hosted model for one specialized task.

Where access is enforced depends on who signs the model call. [Model routing](#agents-inference-through-gateway) describes both routes.
+  **The agent’s own identity signs it.** This is the case in the base setup and with the gateway on the open source path. IAM limits each agent to the model ARNs it declares.
+  **A gateway signs with its own role.** AgentCore Gateway does this on the AWS services path. IAM sees one caller for every agent, so per-agent limits move to gateway policy.

The following diagram shows how an agent reaches the model. In the base setup, the agent calls Amazon Bedrock with its own IAM role. With the gateway on, the gateway signs the call, as the agent on the open source path and as itself on the AWS services path.

![An agent reaches Amazon Bedrock in one of two ways: directly with its own IAM role, or through an egress gateway that signs the model call. Each agent is limited to its allowed models.](https://docs.aws.amazon.com/eks/latest/userguide/images/agents-inference.png)

## Open source and AWS services paths
<a name="agents-inference-paths"></a>

The following table compares how each path reaches the model. Without the gateway, both paths are the same.

| Aspect | Open source |  AWS services |
| --- | --- | --- |
| Without the gateway | The agent calls Amazon Bedrock directly with its own EKS Pod Identity credential | The agent calls Amazon Bedrock directly with its own EKS Pod Identity credential |
| With the gateway | The agent calls AgentGateway in the cluster | The agent calls AgentCore Gateway outside the cluster, through an inference target |
| Who signs the model call through the gateway | The gateway, as the calling agent | AgentCore Gateway, with its own role |
| What limits the models an agent reaches |  `modelArns` on the `Agent`, on both routes | Without the gateway, `modelArns`. With it, gateway policy: a routing rule that pins the model, a Cedar permit per target, and a rate limit per model |
| Model name the agent sends to the gateway | The backend name the gateway chart renders. The agent’s backend names the model |  `gateway_model_id`, from the connector’s own catalog in the form `bedrock/provider.model`  |
| Sample model with the gateway | Claude Sonnet 5.5 |  `bedrock/openai.gpt-oss-120b`  |
| Failover between models | Fallback models in priority order, on server errors and throttling | No built-in failover. A request interceptor can rewrite the `model` field |

## Choose a model source
<a name="agents-inference-choose"></a>

The following table compares calling Amazon Bedrock with serving a model on the EKS cluster.

| Property | Amazon Bedrock | Model on EKS |
| --- | --- | --- |
| You operate | Nothing | GPU nodes, a serving stack, model weights, and autoscaling |
| Scaling | Per request | Per replica, with cold starts measured in model load time |
| Per-agent scoping | IAM, on named model ARNs | Whatever your serving stack and the network enforce |

Amazon Bedrock is a recommended way to get started. A model served on the cluster fits a fine-tuned or open-weight model you must host, strict data residency, high sustained utilization, or latency that a local endpoint measurably improves. For serving a model on Amazon EKS, see [Run AI/ML inference workloads on Amazon EKS](ml-inference.md).

**A model on the EKS cluster cannot run inside the agent’s sandbox**
Nitro Sandboxes don’t support GPU or device passthrough, so a GPU model server can’t use a sandbox runtime class. Run it as an unsandboxed Deployment on its own node pool. The sandboxed agent reaches it over the network like any other destination: through the gateway, with a network policy rule and an authentication check in front of it. See [Isolate agent workloads on Amazon EKS](agents-isolation.md) and [Considerations](sandboxing-limitations.md).

## Model routing
<a name="agents-inference-through-gateway"></a>

In the base setup from [Set up an Amazon EKS cluster for agent workloads](agents-cluster-setup.md), on either path, the agent calls Amazon Bedrock directly:
+ It signs the call with its own EKS Pod Identity credential.
+ Network policy permits the `bedrock-runtime` endpoint in the cluster’s Region.
+ The agent receives a model ID and no endpoint. The model ID is a cross-Region inference profile, because many current models, including Anthropic Claude Sonnet 5.5, reject on-demand invocation by foundation model ID with a `ValidationException`.

With the gateway on, the agent calls [the gateway](agents-gateway.md) instead. The agent’s pod holds no model credential, and the gateway applies budgets, model selection, and content checks. The paths differ in who signs the model call:

| Route | Who signs model calls | What limits models |
| --- | --- | --- |
| Base setup | The agent |  `modelArns` on the `Agent`  |
| Open source gateway | The gateway, as the calling agent, with one model backend per agent on a per-agent path |  `modelArns` on the `Agent`  |
| AgentCore Gateway | AgentCore Gateway, with its own role. Adding an inference target lets it serve models alongside its tool targets. | The gateway, not IAM. An inference target is authorized for the connector’s whole catalog, so neither `modelArns` nor the gateway role’s model ARNs limit the model a caller gets. Pin the model in a gateway routing rule, permit each agent to the target with Cedar policy, and set a rate limit per model. Cedar decides per target, not per model. See [Route agent egress through a gateway](agents-gateway.md). |

A model is named differently at each hop between the agent and Amazon Bedrock, and a mismatch between those names is the most common reason a first model call fails. Three settings name the model, and each applies to one route:
+  **The direct model ID** is what an agent sends to Amazon Bedrock when there’s no gateway. It must be a cross-Region inference profile ID, such as `us.anthropic.claude-sonnet-5-5`, for the reason in the list above.
+  **The gateway’s Amazon Bedrock model** is the model that each per-agent backend calls on the open source path. The agent’s `modelArns` then decide whether that call is allowed, because the gateway signs as the agent.
+  **The gateway model name** is what an agent puts in the `model` field of a request to the gateway.
  +  **Open source path.** It’s the backend name the gateway chart renders. The gateway doesn’t use it to choose the model, because the agent’s backend names the model.
  +  ** AWS services path.** It’s `gateway_model_id`, an ID from the connector’s own catalog in the form `bedrock/provider.model`, not an Amazon Bedrock model ID, and the gateway routes on it. List the catalog with a `GET` on the gateway’s `/inference/v1/models` path, and pick a model that serves the OpenAI-compatible API.

**Note**
AgentCore Gateway’s catalog doesn’t include Claude Sonnet models. Its one Anthropic model is `bedrock/anthropic.claude-haiku-4-5`. The sample models differ by path:
 **Open source path.** Claude Sonnet 5.5 on both routes, because its gateway calls Amazon Bedrock as the agent.
 ** AWS services path.** `bedrock/openai.gpt-oss-120b` with the gateway on. Without the gateway, agents call Amazon Bedrock directly and use Claude Sonnet 5.5, `us.anthropic.claude-sonnet-5-5`. When the catalog adds a Sonnet model, change `gateway_model_id`.

## Guardrails and failover
<a name="agents-inference-guardrails"></a>
+  **Guardrails** screen what reaches the model, and on the open source path, the model’s responses too. Apply them at the gateway for all agents, and add per-agent guardrails where an agent needs more. Per-agent settings add to the gateway settings. See [Considerations](agents-gateway.md#agents-gateway-considerations).
  +  **Open source path.** `gateway_guardrail` names an Amazon Bedrock guardrail and a published version. AgentGateway applies it to every model request and response, and fails closed when the guardrail service doesn’t answer.
  +  ** AWS services path.** `gateway_guardrails` attaches guardrail checks to the inference target through AgentCore Policy. It refuses a chat completion whose newest message, the prompt or a tool result, scores above a threshold for jailbreak or prompt injection. It doesn’t screen the model’s response, because the agents stream every turn and AgentCore Policy’s output check refuses streamed completions.
+  **Failover between models** belongs at the gateway, which sees throttling and availability errors.
  +  **Open source path.** With fallback models configured, each agent’s backend holds them in priority order. The gateway stops sending to a provider that returns server errors or throttling and retries the request on the next model, so the agent doesn’t see the error. The models and fallbacks are the same for every agent, and each agent’s `modelArns` must include all of them, because the gateway calls Amazon Bedrock as the agent.
  +  ** AWS services path.** AgentCore Gateway has no built-in failover between models. The agent names the model, and Cedar policy and IAM limit which models it can reach. To choose the model centrally, a request interceptor can rewrite the request’s `model` field before the gateway routes it. The reference sample doesn’t configure one.
+  **Budgets** are set per agent and enforced at the gateway: tokens per hour on the open source path, and requests and tokens per minute with `gateway_rate_limits` on the AWS services path. Don’t rely on an agent to enforce its own budget, because a model chooses its next action.

## Prerequisites
<a name="agents-inference-prerequisites"></a>

The following steps give an agent access to named Amazon Bedrock models and verify a completion from inside its sandbox. You need:
+ A shell with `kubectl` access to the cluster, on the bastion or your workstation.
+  `PAVED_PATH` set to `open-source` or `aws-services`, such as with `export PAVED_PATH=open-source`.
+ Permission to manage Amazon Bedrock model access in the account.
+ An agent deployed with [Deploy an agent on Amazon EKS](agents-application-setup.md).
+ For the gateway route, the gateway turned on with [Route agent egress through a gateway](agents-gateway.md).

## Step 1: Request model access
<a name="agents-inference-step1"></a>

Request access to every model any agent calls. Access is granted per account and per Region, and calling a model without access returns `AccessDeniedException`. See [Access Amazon Bedrock foundation models](https://docs.aws.amazon.com/bedrock/latest/userguide/model-access.html) in the *Amazon Bedrock User Guide*. Step 4 fails with this error if access is missing.

## Step 2: Name the models on the agent
<a name="agents-inference-step2"></a>

 `modelArns` on the `Agent` object becomes the agent’s IAM permission. An empty list is rejected. It limits only calls signed with the agent’s identity. On the AWS services path with the gateway on, it doesn’t apply. See [Model routing](#agents-inference-through-gateway).

```yaml
spec:
  modelArns:
    - arn:aws:bedrock:us-west-2::foundation-model/anthropic.claude-sonnet-5-5
```

For a cross-Region inference profile, list the profile and the foundation model in every Region the profile routes to. Amazon Bedrock authorizes both. If you list only the profile, calls are denied on the foundation model. If you list the model in only one Region, calls fail intermittently, whenever the profile routes to another Region.

```yaml
spec:
  modelArns:
    - arn:aws:bedrock:us-west-2:111122223333:inference-profile/us.anthropic.claude-sonnet-5-5
    - arn:aws:bedrock:us-east-1::foundation-model/anthropic.claude-sonnet-5-5
    - arn:aws:bedrock:us-east-2::foundation-model/anthropic.claude-sonnet-5-5
    - arn:aws:bedrock:us-west-2::foundation-model/anthropic.claude-sonnet-5-5
```

The profile defines which Regions it routes to. List them explicitly instead of deriving them from the cluster’s Region. After you apply the `Agent`, the permissions policy on the agent’s IAM role lists the same ARNs, and Step 4 confirms them with a real call.

## Step 3: Confirm the model name matches what the gateway serves
<a name="agents-inference-step3"></a>

Skip this step if you don’t use a gateway. The two gateways pick the model differently, so check the tab for your path.

------
#### [ Open source ]

The request’s path selects the model, not its `model` field. The `Agent` resource composes a route for each agent, `/llm/<agent>`, and a backend behind it that names the Amazon Bedrock model and assumes the agent’s IAM role. The following excerpt shows both for `research`:

```yaml
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  name: llm-research
  namespace: agentgateway-system
spec:
  parentRefs:
    - name: egress
      sectionName: egress
  rules:
    - matches:
        - path:
            type: PathPrefix
            value: /llm/research
      backendRefs:
        - group: agentgateway.dev
          kind: AgentgatewayBackend
          name: bedrock-research
---
apiVersion: agentgateway.dev/v1alpha1
kind: AgentgatewayBackend
metadata:
  name: bedrock-research
  namespace: agentgateway-system
spec:
  ai:
    provider:
      bedrock:
        model: us.anthropic.claude-sonnet-5-5
        region: us-west-2
  policies:
    auth:
      aws:
        region: us-west-2
        serviceName: bedrock
        assumeRole:
          roleArn: arn:aws:iam::111122223333:role/eks-agents/my-agents-agent-research
          sessionName: research
```

The backend’s model comes from the stack’s `model.bedrockModelId` value, and the agent’s own `modelArns` still decide whether the call is allowed, because the gateway signs as the agent’s role. The `model` value the agent sends, `bedrock-claude-sonnet` by default, is passed through to the provider.

------
#### [  AWS services ]

AgentCore Gateway exposes one OpenAI-compatible endpoint, `/inference/v1`, and routes on the `model` field of each request. The reference sample creates one inference target for Amazon Bedrock by default, with the following configuration in the gateway module:

```hcl
inference_targets = {
  bedrock = {
    connector_id = "bedrock-mantle"                # Amazon Bedrock, OpenAI-compatible dialect
    credential   = { kind = "gateway_iam_role" }   # the gateway signs with its own role
  }
}
```

The agent’s `AGENT_MODEL` must be a name from that connector’s catalog, which is `gateway_model_id` from [Step 1: Turn on the gateway](agents-gateway.md#agents-gateway-step1). If no model matches, the gateway returns `404` with the unknown model name. To list the names the gateway serves, send a `GET` to the `/models` path of `OPENAI_BASE_URL` from inside the agent’s pod, with the agent’s token:

```bash
./scripts/run-stack.sh --root terraform/aws-services -- kubectl -n agents exec research -c agent -- python3 -c "
import json, os, urllib.request
token = open('/var/run/secrets/eks-agents/gateway/token').read().strip()
req = urllib.request.Request(os.environ['OPENAI_BASE_URL'].rstrip('/') + '/models', headers={'Authorization': 'Bearer ' + token})
print('\n'.join(m['id'] for m in json.load(urllib.request.urlopen(req))['data']))"
```

The output lists the catalog’s model IDs, such as `bedrock/openai.gpt-oss-120b`.

------

## Step 4: Verify with a real completion
<a name="agents-inference-step4"></a>

Run the `model` phase of the reference sample’s exercise script from the `agents` directory. It sends a chat completion from inside the agent’s sandbox, using the endpoint and model name the agent was given, so the call is subject to the agent’s identity, network policy, and sandbox.

```bash
./scripts/exercise.sh --path $PAVED_PATH model
```

The script prints a chat completion. If the call fails, check the error:
+  `404` with a model name: on the AWS services path, the agent’s model name isn’t in the gateway’s catalog. On the open source path, Amazon Bedrock rejected the backend’s model, for example because it’s deprecated. See Step 3.
+  `AccessDeniedException` from Amazon Bedrock: the agent’s `modelArns` don’t cover the model, or model access isn’t enabled in the Region.

## Next steps
<a name="agents-inference-next"></a>
+  [Give an agent tools with MCP](agents-mcp.md): Give agents tools through the gateway.
+  [Run AI/ML inference workloads on Amazon EKS](ml-inference.md): Serve a model on the EKS cluster.
