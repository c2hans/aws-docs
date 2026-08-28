---
source_url: https://docs.aws.amazon.com/solutions/latest/migration-assistant-for-amazon-opensearch-service/troubleshooting.html
---

# Troubleshooting
<a name="troubleshooting"></a>

This section provides known issue resolution when deploying or running the Migration Assistant for Amazon OpenSearch Service solution. If these instructions don’t address your issue, see the [Contact AWS Support](contact-aws-support.md) section for instructions on opening an AWS Support case for this solution. When opening a support case, please add a note to route the ticket to **AWS OpenSearch / Migrations / AWS Solutions**.

## First-signal commands
<a name="first-signal-commands"></a>

Start with the simplest question: is this a deployment problem, an authentication problem, or a workflow problem? These commands give you the fastest first signal:

```
console --version
console clusters connection-check
workflow status
workflow log all
kubectl get pods -n ma
```

## If the platform itself is not healthy
<a name="platform-not-healthy"></a>

### Pods are not starting
<a name="pods-not-starting"></a>

```
kubectl describe pod <POD_NAME> -n ma
kubectl logs <POD_NAME> -n ma
```

Common causes:
+ Image pull failures because the chart was installed without valid image overrides. The Amazon EKS bootstrap script handles this for you when run with `--version <tag>` or default settings.
+ Missing Kubernetes secrets in the `ma` namespace.
+ Insufficient AWS IAM permissions on the Pod Identity role used by the pod.
+ Pending pods caused by missing capacity or a broken `StorageClass`.

### Pods are pending
<a name="pods-pending"></a>

```
kubectl get events -n ma --sort-by='.lastTimestamp'
kubectl describe node <NODE_NAME>
```

This often means the Amazon EKS node group or Karpenter NodePool needs attention — check that capacity is available in the cluster’s Availability Zones and instance types are permitted by the NodePool selectors.

## If connectivity checks fail
<a name="connectivity-fails"></a>

Start from the Migration Console pod:

```
console clusters connection-check
console clusters curl source /
console clusters curl target /
```

Common causes:
+ Source security group does not allow traffic from the Amazon EKS cluster security group.
+ The Amazon OpenSearch Service domain or Amazon OpenSearch Serverless NextGen collection’s network configuration does not allow traffic from the Amazon EKS cluster.
+ DNS does not resolve from inside the cluster.
+ The endpoint is wrong.
+ TLS verification fails and `allowInsecure` is not set for a self-signed environment.

Quick DNS test from the Migration Console pod:

```
kubectl exec -it migration-console-0 -n ma -- nslookup <CLUSTER_ENDPOINT>
```

## If authentication fails
<a name="authentication-fails"></a>

Authentication issues usually show up as HTTP `401`, `403`, or "connection check passed from the Migration Console but the workflow failed later."

### Basic authentication
<a name="basic-auth-troubleshooting"></a>

Verify that the Kubernetes secret exists in the `ma` namespace and contains the expected keys:

```
kubectl get secret <SECRET_NAME> -n ma
kubectl get secret <SECRET_NAME> -n ma -o jsonpath='{.data}' | jq 'keys'
```

Your workflow configuration must point to that same secret name in `authConfig.basic.secretName`.

### AWS Signature Version 4 (SigV4) on Amazon EKS
<a name="sigv4-troubleshooting"></a>

The Amazon EKS deployment associates an IAM role with the Kubernetes service accounts used by the Migration Console pod and the Argo workflow executor pods through [EKS Pod Identity](https://docs.aws.amazon.com/eks/latest/userguide/pod-identities.html).

Check the identity inside the Migration Console pod:

```
kubectl exec -it migration-console-0 -n ma -- aws sts get-caller-identity
```

If the target is an Amazon OpenSearch Service domain with fine-grained access control, make sure the relevant IAM role is mapped with sufficient permissions on the domain. See [Fine-grained access control: 403 on `cluster:monitor/main`](#fgac-troubleshooting).

Use `es` as the SigV4 service name for Amazon OpenSearch Service domains and `aoss` for Amazon OpenSearch Serverless NextGen collections.

### Service account name mismatch
<a name="service-account-mismatch"></a>

The Migration Console pod does not run under a service account named `migration-console`. The Helm chart uses `migration-console-access-role`. The Argo workflow executor pods run under `argo-workflow-executor`.

If you are inspecting service accounts or troubleshooting identity, check:

```
kubectl get serviceaccount -n ma
kubectl describe serviceaccount migration-console-access-role -n ma
kubectl describe serviceaccount argo-workflow-executor -n ma
```

### Fine-grained access control: 403 on `cluster:monitor/main`
<a name="fgac-troubleshooting"></a>

If authentication succeeds but the Amazon OpenSearch Service domain returns `403` on operations such as `cluster:monitor/main`, fine-grained access control (FGAC) is enabled and the Migration Assistant identity has no role mapping inside the domain. Authentication gets you **to** the domain; FGAC authorizes what you can do **once you are in** — both must be in place.

Map the Migration Assistant identity to `all_access` (or a more scoped role) using the OpenSearch Security API. The API path differs by engine:
+  **Elasticsearch 7.x** (Open Distro Security): `/_opendistro/_security/api/rolesmapping/<role>`
+  **OpenSearch 1.x and later** (Security plugin): `/_plugins/_security/api/rolesmapping/<role>`

Use `users` for internal accounts and `backend_roles` for identities delivered by the authentication layer — an LDAP or SAML group, or an IAM role ARN when authenticating with AWS SigV4.

Elasticsearch 7.x:

```
curl -u <admin-user>:<admin-pass> \
  -H 'Content-Type: application/json' \
  -X PUT "https://<cluster>/_opendistro/_security/api/rolesmapping/all_access" \
  -d '{ "backend_roles": ["<identity>"] }'
```

OpenSearch 1.x and later:

```
curl -u <admin-user>:<admin-pass> \
  -H 'Content-Type: application/json' \
  -X PUT "https://<cluster>/_plugins/_security/api/rolesmapping/all_access" \
  -d '{ "backend_roles": ["<identity>"] }'
```

On Amazon OpenSearch Service domains that only accept IAM authentication (no admin password), you can map the role by temporarily setting the Migration Assistant IAM role as the master user:

```
aws opensearch update-domain-config \
  --domain-name <DOMAIN_NAME> \
  --advanced-security-options '{"MasterUserOptions":{"MasterUserARN":"<MIGRATION_ROLE_ARN>"}}'
```

Then scope the master user down again after the role mapping is set.

### mTLS
<a name="mtls"></a>

Capture Proxy listener mTLS is supported through `traffic.proxies.<proxy>.proxyConfig.tls.clientAuth`. Use it when clients must present certificates to the proxy. See [TLS behavior](reroute-to-proxy.md#reroute-tls).

Do not confuse proxy listener mTLS with source or target cluster `authConfig.mtls`. The schema accepts `authConfig.mtls.caCert` and `authConfig.mtls.clientSecretName`, but the standard workflow templates do not mount and pass that client certificate secret through all migration phases. Reindex-from-Snapshot can receive CA certificate parameters, while the Traffic Replayer target-auth path derives request authentication for SigV4 and basic auth only. Use cluster `authConfig.mtls` only with custom wiring and after validating the exact phases you plan to run.

## If the workflow fails after submission
<a name="workflow-fails"></a>

```
workflow status
workflow log all
workflow log all --follow
```

### Workflow already exists
<a name="workflow-already-exists"></a>

 `workflow submit` automatically stops and replaces an existing workflow with the same name, so this should rarely block you. If you see lingering custom resources after a partial failure, use `workflow reset` instead of deleting Argo workflows directly:

```
workflow reset                # lists migration custom resources
workflow reset --list         # lists migration custom resources and exits
workflow reset migration-foo  # delete a specific resource by name
workflow reset --all          # delete everything (capture proxies are protected)
workflow reset --all --include-proxies --delete-storage  # also remove capture proxies and Apache Kafka PVCs
```

**Warning**
Avoid `kubectl delete workflow …​`. It bypasses the migration custom resource lifecycle and can leave orphaned Apache Kafka persistent volume claims (PVCs) or pending assignments.

### Approval gate is blocking progress
<a name="approval-blocking"></a>

Open the interactive UI:

```
workflow manage
```

Or approve the step directly:

```
workflow approve step <STEP_NAME>
```

## If snapshot creation fails
<a name="snapshot-fails"></a>

The most common cause for Elasticsearch sources is a missing `repository-s3` plugin.

Check the source cluster:

```
curl http://<SOURCE_HOST>:9200/_cat/plugins?v
```

Also verify:
+ The source cluster can write to the snapshot bucket in Amazon S3.
+ The repository is registered correctly.
+ The bucket Region and path match the workflow configuration.

## If metadata migration fails
<a name="metadata-fails"></a>

Common causes:
+ Incompatible mappings across major versions.
+ Elasticsearch 6.x mapping-type cleanup issues — multi-type (multiple types per index) mappings from sources below Elasticsearch 7 are automatically resolved by the type-mapping sanitization transformer, which unions the types into a single mapping by default. To rename merged output or drop routed data, configure `TypeMappingSanitizationTransformerProvider` consistently across the affected metadata, document backfill, and replay phases. See [Transform type mappings](transform-type-mappings.md).
+ Target-side settings rejected by the newer version on Amazon OpenSearch Service or Amazon OpenSearch Serverless NextGen.

Use a pilot allowlist first so these failures show up on a small slice of data instead of the whole cluster.

## If document backfill is too slow or unstable
<a name="backfill-slow"></a>

Check:
+ Target cluster ingest capacity on Amazon OpenSearch Service or Amazon OpenSearch Serverless NextGen.
+ Available disk space on the target.
+ RFS worker replica count (`podReplicas`).
+ Pod memory limits for large documents.

Backfill reads from snapshots in Amazon S3, so adding RFS workers does not increase load on the source cluster. It mainly changes how quickly the target is driven.

## If `console` or `workflow` is not in `PATH`
<a name="binaries-not-in-path"></a>

Some Migration Console images install the binaries under `/.venv/bin`:

```
export PATH="/.venv/bin:$PATH"
/.venv/bin/console --version
/.venv/bin/workflow configure sample
```

## If you need more data to debug
<a name="need-more-debug-data"></a>

Collect the following before opening a support case:
+  `console --version`
+  `workflow status`
+  `workflow log all`
+  `kubectl describe pods -n ma`
+ Source and target version numbers.
+ Exact authentication mode in use (basic, SigV4, or both).
+ AWS Region and Amazon EKS cluster name.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Migration Assistant for Amazon OpenSearch Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
