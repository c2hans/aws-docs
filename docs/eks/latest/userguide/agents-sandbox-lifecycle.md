---
source_url: https://docs.aws.amazon.com/eks/latest/userguide/agents-sandbox-lifecycle.html
---

 **Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Run a sandbox per agent session on Amazon EKS

A sandbox per session gives each session its own kernel and filesystem, so one session can’t read or affect another, even when both run code a model generated. For when to choose it over the default runtime, one long-lived `Sandbox` per agent, or a Deployment, see [Manage the agent session lifecycle on Amazon EKS](agents-lifecycle.md).

Per-session isolation costs more than a long-lived agent. A sandbox takes longer to start than a container, and a person waiting on the first turn sees that delay. An idle session also holds a pod, and agent sessions are idle most of the time. The following controls reduce those costs, each with a trade-off.
+  **A warm pool** boots sandboxes ahead of demand so a session adopts one without waiting for a boot. You pay for the idle sandboxes in the pool.
+  **Suspension** terminates an idle session’s pod to stop paying for its compute, and loses everything except the workspace volume.
+  **Expiry** deletes a session that nobody closed. Without it, an abandoned session runs and bills indefinitely.
+  **A durable workspace** keeps a session’s files across suspension, but a session that needs one can’t adopt from a warm pool.

The following diagram shows a warm pool. The agent creates one claim per session. A claim with no workspace adopts a Ready sandbox from the pool without waiting for a boot, and the controller refills the pool.

![The reasoning agent creates a claim for each session. The claim adopts a pre-booted sandbox from a warm pool, which the controller refills, and the execution worker in that sandbox serves only that session.](https://docs.aws.amazon.com/eks/latest/userguide/images/agents-sandbox-lifecycle.png)

## Objects
<a name="agents-sandbox-lifecycle-objects"></a>

The following table describes the four objects.

| Object | What it is |
| --- | --- |
|  `SandboxTemplate`  | The pod spec for every sandbox in a pool, including the image, resources, network-isolation annotation, and any workspace volume. Owned by the platform team. |
|  `SandboxWarmPool`  | How many pre-booted sandboxes from a template to keep Ready. A claim adopts one and the pool boots a replacement, so N active sessions mean N plus `replicas` sandboxes. Warm sandboxes use CPU and memory while idle, so size `replicas` to sessions that start at once, not to peak capacity. |
|  `SandboxClaim`  | One session. The agent creates it at run time, not from Git. A claim that names a pool adopts a Ready sandbox, and one without a pool creates a new one. |
|  `Sandbox`  | The sandbox the claim produced. It carries `operatingMode`. |

 `SandboxTemplate`, `SandboxWarmPool`, and `SandboxClaim` belong to the extensions API, which is installed separately from the core `Sandbox` CRD.

## Suspend and resume
<a name="agents-sandbox-lifecycle-suspend"></a>

Suspend terminates the pod. It does not pause it.

| Setting | What happens |
| --- | --- |
|  `operatingMode: Suspended`  | The pod and guest terminate, and compute billing stops. The `Sandbox` and workspace volume claim remain, so the Amazon EBS volume is still billed. |
|  `operatingMode: Running`  | A new pod, with a new UID, starts on the same volume. The workspace is intact. |

Only the workspace volume survives a suspend. Memory, running processes, and filesystem changes outside the workspace volume are lost. A resumed agent rebuilds its context from the workspace and session state, so a stateful agent needs [Store agent session state](agents-session-state.md).

**Note**
Set `operatingMode` on the `Sandbox`. The claim’s `lifecycle` block accepts only a shutdown policy, a shutdown time, and a time-to-live after completion.

## Adoption speed and workspace durability
<a name="agents-sandbox-lifecycle-tradeoff"></a>

A pool is fast because it hands out pods that are already Ready. A durable workspace requires a volume bound at claim time. Each template gets one or the other:

| Goal | Template | Consequence |
| --- | --- | --- |
| Fast adoption | No volume claim | Nothing survives suspend. Keep state in the session cache or the agent’s Amazon S3 prefix. |
| A durable workspace | Volume claim template | Each claim waits for a cold start, so the pool provides no benefit. |

A durable workspace is a volume that the controller creates for the session when it starts, so an idle warm pod provisions no storage. Mount it with the `ReadWriteOncePod` access mode. `ReadWriteOnce` guarantees only one node, so two pods on that node could mount one session’s workspace. Deleting the claim deletes the workspace.

Default to fast adoption, and keep state in the session cache. Use a durable workspace only when a code-executing agent’s files must persist across suspend.

## Abandoned sessions
<a name="agents-sandbox-lifecycle-expiry"></a>

A session that is never closed keeps its pod running and its volume billed. Agents can’t be trusted to close their own sessions, because a model chooses the agent’s next action, so the stack bounds every session instead. Give each claim a deadline after which the stack ends the session, and a time-to-live after completion after which the controller deletes the claim, its pod, and its workspace.

The Agent Sandbox default retains an abandoned claim’s sandbox and volume until someone deletes them, which on a per-session resource is a leak with a cost attached. Change it on every claim. Set the time-to-live from the longest pause a legitimate session can have.

## Pool security settings
<a name="agents-sandbox-lifecycle-policy"></a>

 **Don’t let the controller write network policy for the pool.** By default, the Agent Sandbox controller creates its own network policy for each template, and with no rules supplied that policy permits egress to the public internet except private ranges. It has no effect on a pod without a network device, but if anyone removes the network-isolation annotation from the template, it becomes an open egress path. Turn controller-managed policy off (`networkPolicyManagement: Unmanaged` on the template), so these pods are restricted by two controls that don’t depend on the controller. They have no network device, and the cluster’s deny-all policy selects them.

 **Scope the RBAC tightly.** Claiming a sandbox is a Kubernetes API call, so an agent that drives a pool needs a Kubernetes API token. This is the only case in this guide where an agent holds one. A model chooses the agent’s actions, so the token’s scope is the only limit on what it does:
+ Grant `create`, `get`, `list`, `watch`, and `delete` on sandbox claims, and `get` on their status.
+ Grant read-only access (`get` and `list`) to pods, pod logs, and sandboxes, so the agent can find the sandbox its claim adopted. Grant `create` and `get` on `pods/exec` and `pods/attach` to run commands in it.
+ Grant nothing on templates or pools. An agent that can edit the template can remove the network-isolation annotation and get a pod with a network interface.
+ Grant nothing on secrets, and no write access to pods or sandboxes.
+ Use a `Role` and `RoleBinding`, with no cluster-scoped grants. Bind the service account in the reasoning namespace to a `Role` in the execution namespace. The reasoning tier can then drive the pool without holding rights in its own namespace.
+ Set the pool name and namespace in the agent’s configuration. Never expose them as a tool argument the model fills in.

Do not grant `patch` on sandboxes so an agent can suspend its sessions. Kubernetes RBAC has no field-level grants and `Sandbox` has no suspend subresource, so `patch` allows changes to the whole spec. Use the claim expiry instead.

## Identity of pooled sandboxes
<a name="agents-sandbox-lifecycle-identity"></a>

Every sandbox in a pool has the template’s identity. The pods exist before any session, so they run as the template’s service account, with whatever IAM role it can assume. Claiming a pod does not change its identity.

That works for execution sandboxes that hold no identity, as described in [Isolate agent workloads on Amazon EKS](agents-isolation.md). It doesn’t work when a sandbox needs the identity of the tenant whose session it serves. For per-tenant authority, use one pool per identity, or create sandboxes on demand instead of claiming from a shared pool. See [Identity for pooled and per-tenant sessions](agents-identity-agent.md#agents-identity-pooled).

## Sandbox pools in the reference sample
<a name="agents-sandbox-lifecycle-reference"></a>

The controller is Agent Sandbox, an open source Kubernetes SIG project, with Nitro Sandboxes providing the isolation. The in-cluster components in [Set up EKS Capabilities and in-cluster components for agents](agents-capabilities-setup.md) install it, pinned to version 1.0.10. The sample’s warm pool template allows a claim to add a workspace volume. The reference sample’s `gitops/examples/warm-pool/claim.yaml` adds a 10 GiB workspace, so it waits for a cold start, and sets a delete-on-shutdown policy with a one-hour time-to-live. Remove the workspace from your claims to get fast adoption. The sample RBAC grants the read access to pods, logs, and sandboxes described in [Pool security settings](#agents-sandbox-lifecycle-policy), which is more than create, get, and delete on claims.

## Prerequisites
<a name="agents-sandbox-lifecycle-prereqs"></a>
+ The in-cluster components from [Set up EKS Capabilities and in-cluster components for agents](agents-capabilities-setup.md), synced, and a shell with `kubectl` access to the cluster, on the bastion or your workstation.
+  `PAVED_PATH` set to `open-source` or `aws-services`, such as with `export PAVED_PATH=open-source`.
+ The Agent Sandbox extensions API. Confirm it’s installed:

  ```bash
  kubectl get crd sandboxtemplates.extensions.agents.x-k8s.io
  ```
+ For a durable workspace only, a `StorageClass` for Amazon EBS. EKS Auto Mode includes the Amazon EBS CSI driver but doesn’t create a `StorageClass`. The in-cluster components ship `eks-agents-gp3`, and the sample claim names it explicitly, so a cluster with a different default doesn’t provision the workspace elsewhere.

## Step 1: Apply the template, the pool, and the RBAC
<a name="agents-sandbox-lifecycle-step1"></a>

This step creates the pool and the permissions the reasoning tier needs to claim from it. The reference sample’s `gitops/examples/warm-pool` directory contains a template with `networkPolicyManagement: Unmanaged` and the network-isolation annotation, a `SandboxWarmPool` with its `replicas` count, and the `Role` and `RoleBinding` from [Pool security settings](#agents-sandbox-lifecycle-policy). Outside these templates, create the same three objects in the execution namespace.

```bash
./scripts/run-stack.sh --root terraform/$PAVED_PATH -- bash -c '
  kubectl apply -f gitops/examples/warm-pool/warm-pool.yaml
  kubectl apply -f gitops/examples/warm-pool/rbac.yaml'
```

 `kubectl` reports each object as `created`.

## Step 2: Wait for the pool to reach its replica count
<a name="agents-sandbox-lifecycle-step2"></a>

Only the first fill waits for sandboxes to boot, and later claims skip it. If the pool needs new nodes, it also waits for instances to launch.

```bash
kubectl -n agents-execution get sandboxwarmpool execution-pool
```

The pool’s `READY` count equals its `DESIRED` count, which is 3 in the sample pool. A warm pod in `Pending` with a node-affinity message means no node can run sandboxes. See [Manage the agent session lifecycle on Amazon EKS](agents-lifecycle.md).

## Step 3: Claim a sandbox per session
<a name="agents-sandbox-lifecycle-step3"></a>

The reasoning tier creates one claim per session at run time. Name the claim after the session ID so you can trace an abandoned claim to its session. The following claim adopts from `execution-pool` through `warmPoolRef` and sets the expiry from [Abandoned sessions](#agents-sandbox-lifecycle-expiry). `shutdownPolicy` defaults to `Retain`, so set `Delete`, and `ttlSecondsAfterFinished: 3600` deletes the claim an hour after it finishes. Save it as `session-claim.yaml` in the `agents` directory.

```yaml
apiVersion: extensions.agents.x-k8s.io/v1beta1
kind: SandboxClaim
metadata:
  name: session-1234
  namespace: agents-execution
spec:
  warmPoolRef:
    name: execution-pool
  lifecycle:
    shutdownPolicy: Delete
    shutdownTime: "2030-01-01T12:00:00Z"   # replace with the session deadline
    ttlSecondsAfterFinished: 3600
```

 `shutdownTime` is the deadline that bounds an abandoned session. At that time, the controller applies the shutdown policy, here deleting the claim, its sandbox, and its workspace, even if the session never finished. Set it when you create the claim, to the session’s start time plus the longest a session may run. `ttlSecondsAfterFinished` applies only after a session finishes, so on its own it doesn’t end a session that is never closed.

For a durable workspace, add a `volumeClaimTemplates` entry to the claim, with `storageClassName: eks-agents-gp3` and the `ReadWriteOncePod` access mode. The template must set `volumeClaimTemplatesPolicy: Allowed` for a claim to add one, and the entry can’t be changed after the claim is created. A claim with a volume doesn’t adopt a warm pod, because warm pods have no such volume. The controller creates a new sandbox with the volume instead, which waits for a cold start, and the pool is unchanged. See [Adoption speed and workspace durability](#agents-sandbox-lifecycle-tradeoff) for the trade-off. Apply the claim and wait for it to bind:

```bash
./scripts/run-stack.sh --root terraform/$PAVED_PATH --file session-claim.yaml -- kubectl apply -f session-claim.yaml
./scripts/run-stack.sh --root terraform/$PAVED_PATH -- kubectl -n agents-execution wait --for=condition=Ready sandboxclaim/session-1234 --timeout=120s
./scripts/run-stack.sh --root terraform/$PAVED_PATH -- kubectl -n agents-execution get sandboxclaim session-1234
```

The claim reports `True` with the sandbox it bound to, such as `session-1234 True execution-pool-pjlrs DependenciesReady`. Without a volume, the claim binds to a Ready sandbox from the pool, and the pool boots a replacement in the background. A claim with a volume waits for a cold start, so if the wait times out, run it again.

## Clean up
<a name="agents-sandbox-lifecycle-cleanup"></a>

Delete the claims first, then the pool, template, and role. Deleting a claim deletes its sandbox and, with a durable workspace, its volume, because the controller deletes the volume claim with the claim. Deleting the pool deletes its warm sandboxes. Run the commands from the `agents` directory:

```bash
./scripts/run-stack.sh --root terraform/$PAVED_PATH -- kubectl -n agents-execution delete sandboxclaims --all
./scripts/run-stack.sh --root terraform/$PAVED_PATH -- kubectl delete -f gitops/examples/warm-pool/rbac.yaml -f gitops/examples/warm-pool/warm-pool.yaml
```

## Next steps
<a name="_next_steps"></a>

 [Store agent session state](agents-session-state.md) for what a resumed session reads to reconstruct itself.
