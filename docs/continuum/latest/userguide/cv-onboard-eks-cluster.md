---
source_url: https://docs.aws.amazon.com/continuum/latest/userguide/cv-onboard-eks-cluster.html
---

# Connecting an Amazon EKS cluster to AWS Continuum

For read-only Kubernetes inventory collection, connect your Amazon EKS cluster to AWS Continuum. The onboarding takes about 10 minutes for each cluster. This task requires Amazon EKS administrator permissions and `kubectl` cluster-admin access. If you don't have these permissions, ask your administrator to perform these steps or grant you the required access.

**Topics**
+ [How AWS Continuum accesses your cluster](#cv-onboard-eks-cluster-how-it-works)
+ [What AWS Continuum can and cannot see](#cv-onboard-eks-cluster-scope)
+ [Prerequisites](#cv-onboard-eks-cluster-prereqs)
+ [Creating the reader IAM role in the AWS Continuum console](#cv-onboard-eks-cluster-create-role)
+ [Enabling access entries in Amazon EKS](#cv-onboard-eks-cluster-enable-access-entries)
+ [Mapping the role into your cluster](#cv-onboard-eks-cluster-map-role)
+ [Granting read-only RBAC](#cv-onboard-eks-cluster-grant-rbac)
+ [Verifying access to your cluster](#cv-onboard-eks-cluster-verify)
+ [Resolving role and RBAC errors for EKS cluster onboarding](#cv-onboard-eks-cluster-troubleshooting)

## How AWS Continuum accesses your cluster
<a name="cv-onboard-eks-cluster-how-it-works"></a>

AWS Continuum reads your cluster's Kubernetes state through the Amazon EKS cluster communication service (CCS). There is no public endpoint, no VPC peering, and no agent to install. You control access with three elements:
+ A trust-only AWS Identity and Access Management (IAM) role that the AWS Continuum collector can assume. The role grants no AWS permissions of its own.
+ An Amazon EKS access entry that maps that role to a Kubernetes group.
+ A read-only role-based access control (RBAC) binding that lets the group read resources. The binding never grants write access and never grants access to Secrets.

You can revoke access at any time by deleting the role or the access entry.

With AWS Enhanced Zero-Click Role Creation, you create only the reader IAM role. You set up the Amazon EKS access entry and the in-cluster RBAC yourself, because those use Amazon EKS and Kubernetes APIs instead of IAM.

## What AWS Continuum can and cannot see
<a name="cv-onboard-eks-cluster-scope"></a>

The following list describes what the AWS Continuum collector can and cannot see:
+ The collector reads the following resources: namespaces, nodes, pods, services, workloads (deployments, daemonsets, statefulsets, and jobs) and the replica sets and controller revisions that link pods to them, endpoint slices, ingresses and ingress classes, Gateway API resources, network policies, RBAC objects, admission webhooks, and common networking, gateway, and service mesh custom resource definitions (CRDs). A grant in the manifest for a resource type that your cluster doesn't install has no effect.
+ The collector reads only specific, named ConfigMaps and keeps only the settings that control traffic routing. Its permissions are scoped to those ConfigMaps by name. It can't list or read other ConfigMaps in your cluster.
**Important**
The collector keeps the Envoy Gateway settings file in full. Don't put credentials in this file as literal values. Reference a Kubernetes Secret with `valueFrom` instead.
+ The collector does not read Secrets and performs no write operations.

## Prerequisites
<a name="cv-onboard-eks-cluster-prereqs"></a>

Before you begin, make sure that you have the following:
+ You have access to the AWS Continuum console Kubernetes collection, which you can use to create the reader IAM role, enable the AWS collector, and turn on Kubernetes collection.
+ You have Amazon EKS administrator permissions in the account.
+ You have `kubectl` cluster-admin access to the cluster, which you use to grant read-only RBAC.
+ You have your cluster name and AWS Region.
+ If the cluster is private-only (no public endpoint), you have a host with a network path to the cluster endpoint from which to run `kubectl`.

## Creating the reader IAM role in the AWS Continuum console
<a name="cv-onboard-eks-cluster-create-role"></a>

Complete this procedure one time for each account to create the reader IAM role. For more information about IAM roles, see [IAM roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html) in the *IAM User Guide*.

**To create the reader IAM role**

1. Open the AWS Continuum console at [https://console.aws.amazon.com/continuum/](https://console.aws.amazon.com/continuum/) and sign in to the AWS account that contains the EKS cluster to collect.

1. Choose **Set up Kubernetes collection**.

1. Turn on **Kubernetes collection**.

1. Choose **Create default role**.

1. Choose **Create role**, and then save. Role creation completes in a few minutes.

If role creation fails, verify that you have the IAM permissions to create roles, and then try again.

The console creates an IAM role named `ContinuumKubernetesReader-{{collector-id}}`, which has no permissions policy attached. The procedures later in this topic decide what the role can actually read.

## Enabling access entries in Amazon EKS
<a name="cv-onboard-eks-cluster-enable-access-entries"></a>

Complete this procedure one time for each cluster. Your cluster must use the `API` or `API_AND_CONFIG_MAP` authentication mode, and the modern default is `API_AND_CONFIG_MAP`.

The authentication mode changes in one direction only. Run the following command only when the cluster is currently in `CONFIG_MAP` mode. If the cluster is already in `API` or `API_AND_CONFIG_MAP` mode, skip this procedure. For more information about access entries, see [Manage access entries](https://docs.aws.amazon.com/eks/latest/userguide/access-entries.html) in the *Amazon EKS User Guide*.

**To update the cluster configuration**

1. Run the following AWS Command Line Interface (AWS CLI) command to update the cluster configuration. Replace {{region}} with your AWS Region and {{cluster}} with your cluster name.

   ```bash
   PROMPT> aws eks update-cluster-config \
       --region {{region}} \
       --name {{cluster}} \
       --access-config authenticationMode=API_AND_CONFIG_MAP
   ```

1. If the command returns an access denied error, verify that you have Amazon EKS administrator permissions, and then try again.

## Mapping the role into your cluster
<a name="cv-onboard-eks-cluster-map-role"></a>

Complete this procedure one time for each cluster. Before you begin, create the reader IAM role in [Creating the reader IAM role in the AWS Continuum console](#cv-onboard-eks-cluster-create-role), and make sure that you have Amazon EKS administrator permissions. The command maps the reader IAM role to the Kubernetes group `continuum:readers`. You reference this group when you grant read-only RBAC.

**To map the reader IAM role to the Kubernetes group**

1. Map the reader IAM role to the Kubernetes group by running the following AWS CLI command. Replace {{region}}, {{cluster}}, {{account-id}}, and {{collector-id}} with your values.

   ```bash
   PROMPT> aws eks create-access-entry \
       --region {{region}} \
       --cluster-name {{cluster}} \
       --principal-arn arn:aws:iam::{{account-id}}:role/ContinuumKubernetesReader-{{collector-id}} \
       --kubernetes-groups continuum:readers \
       --type STANDARD
   ```

1. If the command fails because the role is missing or can't be assumed, see [Resolving role and RBAC errors for EKS cluster onboarding](#cv-onboard-eks-cluster-troubleshooting).

## Granting read-only RBAC
<a name="cv-onboard-eks-cluster-grant-rbac"></a>

Complete this procedure one time for each cluster. This procedure requires `kubectl` cluster-admin access. If you don't have cluster-admin access, ask your administrator to perform these steps. With this manifest, you grant read-only access (`get`, `list`, and `watch`) on the resources that AWS Continuum collects, while you exclude Secrets.

For a private-only cluster, run `kubectl` from a host that has a network path to the cluster endpoint, such as an in-VPC host.

**Note**
You grant read-only RBAC one time. The AWS Continuum collector never uses `kubectl`. The collector reaches your cluster only over CCS for read-only collection.

The manifest creates the `continuum-reader` ClusterRole and binds it to the `continuum:readers` group. A comment above each rule says what the rule is for.

**To apply the Kubernetes RBAC manifests**

1. Apply the following Kubernetes RBAC YAML manifest with `kubectl`.

   ```bash
   PROMPT> kubectl apply -f - <<'EOF'
   apiVersion: rbac.authorization.k8s.io/v1
   kind: ClusterRole
   metadata:
     name: continuum-reader
     labels:
       app.kubernetes.io/managed-by: continuum-k8s-collection
   rules:
     # Core API group (list-only; secrets deliberately excluded).
     - apiGroups: [""]
       resources:
         - pods
         - services
         - nodes
         - namespaces
         - serviceaccounts
       verbs: ["get", "list", "watch"]

     # Workloads, and the objects that link each pod to its workload.
     - apiGroups: ["apps"]
       resources:
         - deployments
         - statefulsets
         - daemonsets
         - replicasets
         - controllerrevisions
       verbs: ["get", "list", "watch"]
     - apiGroups: ["batch"]
       resources: ["jobs"]
       verbs: ["get", "list", "watch"]

     # Core networking and policy, and each Service's endpoints.
     - apiGroups: ["networking.k8s.io"]
       resources: ["ingresses", "ingressclasses", "networkpolicies"]
       verbs: ["get", "list", "watch"]
     - apiGroups: ["discovery.k8s.io"]
       resources: ["endpointslices"]
       verbs: ["get", "list", "watch"]

     # AWS Load Balancer Controller target group bindings (CRD).
     - apiGroups: ["elbv2.k8s.aws"]
       resources: ["targetgroupbindings"]
       verbs: ["get", "list", "watch"]

     # Amazon VPC CNI network policy endpoints, and the EKS
     # ClusterNetworkPolicies and ApplicationNetworkPolicies they
     # resolve (CRD).
     - apiGroups: ["networking.k8s.aws"]
       resources:
         - policyendpoints
         - clusterpolicyendpoints
         - clusternetworkpolicies
         - applicationnetworkpolicies
       verbs: ["get", "list", "watch"]

     # RBAC.
     - apiGroups: ["rbac.authorization.k8s.io"]
       resources: ["roles", "rolebindings", "clusterroles", "clusterrolebindings"]
       verbs: ["get", "list", "watch"]

     # Admission webhooks.
     - apiGroups: ["admissionregistration.k8s.io"]
       resources: ["mutatingwebhookconfigurations", "validatingwebhookconfigurations"]
       verbs: ["get", "list", "watch"]

     # Kubernetes Gateway API (CRD). The wildcard grants read-only access
     # (get, list, and watch) to every kind in the Gateway API group, so when the
     # collector starts to read a new Gateway API kind, such as
     # BackendTLSPolicy, you don't need to re-apply this role. The get and
     # list verbs return each object with its status, which its controller
     # writes, so reading status needs no further rule.
     - apiGroups: ["gateway.networking.k8s.io"]
       resources: ["*"]
       verbs: ["get", "list", "watch"]

     # Gateway API controllers' policies, route filters, and proxy
     # parameters (CRD): Envoy Gateway, kgateway, and NGINX Gateway
     # Fabric. A policy can authenticate or refuse a route's requests,
     # or put another load balancer in front of the gateway.
     - apiGroups: ["gateway.envoyproxy.io"]
       resources:
         - securitypolicies
         - clienttrafficpolicies
         - backendtrafficpolicies
         - envoyextensionpolicies
         - envoypatchpolicies
         - httproutefilters
         - envoyproxies
       verbs: ["get", "list", "watch"]
     - apiGroups: ["gateway.kgateway.dev"]
       resources:
         - trafficpolicies
         - httplistenerpolicies
         - listenerpolicies
         - gatewayparameters
       verbs: ["get", "list", "watch"]
     - apiGroups: ["gateway.nginx.org"]
       resources:
         - accesspolicies
         - clientsettingspolicies
         - proxysettingspolicies
         - ratelimitpolicies
         - upstreamsettingspolicies
         - snippetspolicies
         - wafpolicies
         - payloadprocessors
         - externalloadbalancers
         - authenticationfilters
         - observabilitypolicies
         - nginxproxies
       verbs: ["get", "list", "watch"]

     # CNI network policies (CRD), and the Cilium per-node settings,
     # which can turn enforcement on for some nodes.
     - apiGroups: ["cilium.io"]
       resources:
         - ciliumnetworkpolicies
         - ciliumclusterwidenetworkpolicies
         - ciliumnodeconfigs
       verbs: ["get", "list", "watch"]
     - apiGroups: ["crd.projectcalico.org"]
       resources: ["globalnetworkpolicies", "networkpolicies"]
       verbs: ["get", "list", "watch"]

     # Istio service mesh (CRD).
     - apiGroups: ["security.istio.io"]
       resources: ["authorizationpolicies", "peerauthentications", "requestauthentications"]
       verbs: ["get", "list", "watch"]
     - apiGroups: ["networking.istio.io"]
       resources:
         - virtualservices
         - destinationrules
         - gateways
         - serviceentries
         - sidecars
         - envoyfilters
       verbs: ["get", "list", "watch"]
     - apiGroups: ["install.istio.io"]
       resources: ["istiooperators"]
       verbs: ["get", "list", "watch"]
     # Istio extensions: only the kinds that change what a gateway
     # proxy does with a request.
     - apiGroups: ["extensions.istio.io"]
       resources: ["wasmplugins", "trafficextensions"]
       verbs: ["get", "list", "watch"]

     # Kubernetes cluster network policies (CRD): AdminNetworkPolicies,
     # BaselineAdminNetworkPolicies, and the ClusterNetworkPolicies
     # that replace both.
     - apiGroups: ["policy.networking.k8s.io"]
       resources: ["adminnetworkpolicies", "baselineadminnetworkpolicies", "clusternetworkpolicies"]
       verbs: ["get", "list", "watch"]

     # Kyverno cluster policies (CRD). Only these: other Kyverno kinds,
     # such as update requests, can hold copies of the objects that
     # admission was asked about.
     - apiGroups: ["kyverno.io"]
       resources: ["clusterpolicies"]
       verbs: ["get", "list", "watch"]
   ---
   apiVersion: rbac.authorization.k8s.io/v1
   kind: ClusterRoleBinding
   metadata:
     name: continuum-reader-binding
     labels:
       app.kubernetes.io/managed-by: continuum-k8s-collection
   roleRef:
     apiGroup: rbac.authorization.k8s.io
     kind: ClusterRole
     name: continuum-reader
   subjects:
     - apiGroup: rbac.authorization.k8s.io
       kind: Group
       name: continuum:readers # MUST match the access entry group.
   EOF
   ```

1. AWS Continuum also reads a few ConfigMaps by name, because the settings in them decide which traffic reaches your workloads. Grant `get` on each name, in its own namespace only, with a Role and RoleBinding. No other ConfigMap is readable. The following table lists the ConfigMaps to grant.

<table>
<thead>
  <tr><th>ConfigMap</th><th>Namespace</th><th>Grant it if</th></tr>
</thead>
<tbody>
  <tr><td><code>amazon-vpc-cni</code></td><td><code>kube-system</code></td><td>Always</td></tr>
  <tr><td><code>cilium-config</code></td><td>The Cilium agent's namespace, usually <code>kube-system</code></td><td>You run Cilium</td></tr>
  <tr><td><code>istio</code>, or <code>istio-revision</code> for each istiod revision. RBAC matches names exactly, so list each revision.</td><td>The namespace where istiod runs</td><td>You run Istio</td></tr>
  <tr><td>The name in each controller's <code>--configmap</code> argument (<code>ingress-nginx-controller</code> with the Helm chart)</td><td>The namespace in that argument</td><td>You run ingress-nginx</td></tr>
  <tr><td>The ConfigMap mounted at the controller's <code>--config-path</code> (<code>envoy-gateway-config</code> with the Helm chart)</td><td>The Envoy Gateway namespace, <code>envoy-gateway-system</code> by default</td><td>You run Envoy Gateway</td></tr>
</tbody>
</table>

   If you don't run ingress-nginx or Envoy Gateway, or you installed them with their Helm charts' default names, the table already gives each ConfigMap to grant, and you can skip to the next step. Otherwise, use the following commands to find the names.

   To find each ingress-nginx controller's ConfigMap, run the following command. It prints the controller's namespace and the value of its `--configmap` argument.

   ```bash
   PROMPT> kubectl get deployments,daemonsets,statefulsets -A \
     -o jsonpath='{range .items[*]}{.metadata.namespace}{" "}{.spec.template.spec.containers[*].command}{" "}{.spec.template.spec.containers[*].args}{"\n"}{end}' \
     | sed -nE 's/^([^ ]*) .*--configmap(=|",")([^"]*).*/\1 \3/p'
   ingress-nginx $(POD_NAMESPACE)/ingress-nginx-controller
   ```

   The value has the form `{{namespace}}/{{name}}`. Put only the name after the `/` in the Role's `resourceNames`, and create the Role in the namespace before the `/`. `$(POD_NAMESPACE)` means the controller's own namespace. In this example, the ConfigMap is `ingress-nginx-controller` in the `ingress-nginx` namespace.

   To find the Envoy Gateway ConfigMap, run the following command. It uses the Helm chart's Deployment name, `envoy-gateway`. If you renamed the Deployment, use your name. The command prints the controller's arguments and the ConfigMaps that it mounts.

   ```bash
   PROMPT> kubectl get deployment envoy-gateway --namespace {{envoy-gateway-namespace}} \
     -o jsonpath='{.spec.template.spec.containers[*].args}{" "}{.spec.template.spec.volumes[*].configMap.name}{"\n"}'
   ["server","--config-path=/config/envoy-gateway.yaml"] envoy-gateway-config
   ```

1. In the following manifest, replace {{cilium-namespace}}, {{istio-namespace}}, {{ingress-nginx-namespace}}, and {{envoy-gateway-namespace}} with your namespaces, and change the names in `resourceNames` to match your installation. Leave out the Role and RoleBinding for a controller that you don't run. Then apply the following Kubernetes manifest with `kubectl`:

   ```bash
   PROMPT> kubectl apply -f - <<'EOF'
   apiVersion: rbac.authorization.k8s.io/v1
   kind: Role
   metadata:
     name: continuum-reader-vpc-cni
     namespace: kube-system
     labels:
       app.kubernetes.io/managed-by: continuum-k8s-collection
   rules:
     - apiGroups: [""]
       resources: ["configmaps"]
       resourceNames: ["amazon-vpc-cni"]
       verbs: ["get"]
   ---
   apiVersion: rbac.authorization.k8s.io/v1
   kind: RoleBinding
   metadata:
     name: continuum-reader-vpc-cni
     namespace: kube-system
     labels:
       app.kubernetes.io/managed-by: continuum-k8s-collection
   roleRef:
     apiGroup: rbac.authorization.k8s.io
     kind: Role
     name: continuum-reader-vpc-cni
   subjects:
     - apiGroup: rbac.authorization.k8s.io
       kind: Group
       name: continuum:readers
   ---
   apiVersion: rbac.authorization.k8s.io/v1
   kind: Role
   metadata:
     name: continuum-reader-cilium
     namespace: {{cilium-namespace}}
     labels:
       app.kubernetes.io/managed-by: continuum-k8s-collection
   rules:
     - apiGroups: [""]
       resources: ["configmaps"]
       resourceNames: ["cilium-config"]
       verbs: ["get"]
   ---
   apiVersion: rbac.authorization.k8s.io/v1
   kind: RoleBinding
   metadata:
     name: continuum-reader-cilium
     namespace: {{cilium-namespace}}
     labels:
       app.kubernetes.io/managed-by: continuum-k8s-collection
   roleRef:
     apiGroup: rbac.authorization.k8s.io
     kind: Role
     name: continuum-reader-cilium
   subjects:
     - apiGroup: rbac.authorization.k8s.io
       kind: Group
       name: continuum:readers
   ---
   apiVersion: rbac.authorization.k8s.io/v1
   kind: Role
   metadata:
     name: continuum-reader-istio
     namespace: {{istio-namespace}}
     labels:
       app.kubernetes.io/managed-by: continuum-k8s-collection
   rules:
     - apiGroups: [""]
       resources: ["configmaps"]
       resourceNames: ["istio"] # Add istio-REVISION for each revisioned istiod.
       verbs: ["get"]
   ---
   apiVersion: rbac.authorization.k8s.io/v1
   kind: RoleBinding
   metadata:
     name: continuum-reader-istio
     namespace: {{istio-namespace}}
     labels:
       app.kubernetes.io/managed-by: continuum-k8s-collection
   roleRef:
     apiGroup: rbac.authorization.k8s.io
     kind: Role
     name: continuum-reader-istio
   subjects:
     - apiGroup: rbac.authorization.k8s.io
       kind: Group
       name: continuum:readers
   ---
   apiVersion: rbac.authorization.k8s.io/v1
   kind: Role
   metadata:
     name: continuum-reader-ingress-nginx
     namespace: {{ingress-nginx-namespace}}
     labels:
       app.kubernetes.io/managed-by: continuum-k8s-collection
   rules:
     - apiGroups: [""]
       resources: ["configmaps"]
       resourceNames: ["ingress-nginx-controller"] # The controller's --configmap name.
       verbs: ["get"]
   ---
   apiVersion: rbac.authorization.k8s.io/v1
   kind: RoleBinding
   metadata:
     name: continuum-reader-ingress-nginx
     namespace: {{ingress-nginx-namespace}}
     labels:
       app.kubernetes.io/managed-by: continuum-k8s-collection
   roleRef:
     apiGroup: rbac.authorization.k8s.io
     kind: Role
     name: continuum-reader-ingress-nginx
   subjects:
     - apiGroup: rbac.authorization.k8s.io
       kind: Group
       name: continuum:readers
   ---
   apiVersion: rbac.authorization.k8s.io/v1
   kind: Role
   metadata:
     name: continuum-reader-envoy-gateway
     namespace: {{envoy-gateway-namespace}}
     labels:
       app.kubernetes.io/managed-by: continuum-k8s-collection
   rules:
     - apiGroups: [""]
       resources: ["configmaps"]
       resourceNames: ["envoy-gateway-config"] # The ConfigMap mounted at --config-path.
       verbs: ["get"]
   ---
   apiVersion: rbac.authorization.k8s.io/v1
   kind: RoleBinding
   metadata:
     name: continuum-reader-envoy-gateway
     namespace: {{envoy-gateway-namespace}}
     labels:
       app.kubernetes.io/managed-by: continuum-k8s-collection
   roleRef:
     apiGroup: rbac.authorization.k8s.io
     kind: Role
     name: continuum-reader-envoy-gateway
   subjects:
     - apiGroup: rbac.authorization.k8s.io
       kind: Group
       name: continuum:readers
   EOF
   ```

   If you run more than one ingress-nginx or Envoy Gateway controller, grant each controller's ConfigMap. Grant it in the ConfigMap's own namespace, which can differ from the controller's.

   Until you grant a ConfigMap, collection still completes, but the cluster's snapshot is marked degraded, and AWS Continuum reports the results that depend on that ConfigMap's settings as undecided.

1. If some resources return a `forbidden` error, confirm that the access entry group and the binding both use `continuum:readers`.

## Verifying access to your cluster
<a name="cv-onboard-eks-cluster-verify"></a>

From a cluster-admin context, confirm that the reader group can list the resources that AWS Continuum collects and read the ConfigMaps that you granted, but cannot list Secrets or ConfigMaps.

**To verify access**

1. To confirm that the reader group can list the resources that AWS Continuum collects and read the ConfigMaps that you granted, enter the following commands. Run the ConfigMap commands with each name that you granted.

   ```bash
   PROMPT> kubectl auth can-i list nodes --as-group=continuum:readers --as=continuum-check
   PROMPT> kubectl auth can-i list gatewayclasses.gateway.networking.k8s.io --as-group=continuum:readers --as=continuum-check
   PROMPT> kubectl auth can-i list referencegrants.gateway.networking.k8s.io --as-group=continuum:readers --as=continuum-check
   PROMPT> kubectl auth can-i list tcproutes.gateway.networking.k8s.io --as-group=continuum:readers --as=continuum-check
   PROMPT> kubectl auth can-i list securitypolicies.gateway.envoyproxy.io --as-group=continuum:readers --as=continuum-check
   PROMPT> kubectl auth can-i list trafficpolicies.gateway.kgateway.dev --as-group=continuum:readers --as=continuum-check
   PROMPT> kubectl auth can-i list snippetspolicies.gateway.nginx.org --as-group=continuum:readers --as=continuum-check
   PROMPT> kubectl auth can-i list externalloadbalancers.gateway.nginx.org --as-group=continuum:readers --as=continuum-check
   PROMPT> kubectl auth can-i list replicasets.apps --as-group=continuum:readers --as=continuum-check
   PROMPT> kubectl auth can-i list ingressclasses.networking.k8s.io --as-group=continuum:readers --as=continuum-check
   PROMPT> kubectl auth can-i list endpointslices.discovery.k8s.io --as-group=continuum:readers --as=continuum-check
   PROMPT> kubectl auth can-i list targetgroupbindings.elbv2.k8s.aws --as-group=continuum:readers --as=continuum-check
   PROMPT> kubectl auth can-i list policyendpoints.networking.k8s.aws --as-group=continuum:readers --as=continuum-check
   PROMPT> kubectl auth can-i list clusterpolicyendpoints.networking.k8s.aws --as-group=continuum:readers --as=continuum-check
   PROMPT> kubectl auth can-i list clusternetworkpolicies.networking.k8s.aws --as-group=continuum:readers --as=continuum-check
   PROMPT> kubectl auth can-i list applicationnetworkpolicies.networking.k8s.aws --as-group=continuum:readers --as=continuum-check
   PROMPT> kubectl auth can-i list adminnetworkpolicies.policy.networking.k8s.io --as-group=continuum:readers --as=continuum-check
   PROMPT> kubectl auth can-i list virtualservices.networking.istio.io --as-group=continuum:readers --as=continuum-check
   PROMPT> kubectl auth can-i list authorizationpolicies.security.istio.io --as-group=continuum:readers --as=continuum-check
   PROMPT> kubectl auth can-i list wasmplugins.extensions.istio.io --as-group=continuum:readers --as=continuum-check
   PROMPT> kubectl auth can-i get configmaps/amazon-vpc-cni --namespace kube-system --as-group=continuum:readers --as=continuum-check
   PROMPT> kubectl auth can-i get configmaps/cilium-config --namespace {{cilium-namespace}} --as-group=continuum:readers --as=continuum-check
   PROMPT> kubectl auth can-i get configmaps/istio --namespace {{istio-namespace}} --as-group=continuum:readers --as=continuum-check
   PROMPT> kubectl auth can-i get configmaps/ingress-nginx-controller --namespace {{ingress-nginx-namespace}} --as-group=continuum:readers --as=continuum-check
   PROMPT> kubectl auth can-i get configmaps/envoy-gateway-config --namespace {{envoy-gateway-namespace}} --as-group=continuum:readers --as=continuum-check
   ```

1. Confirm that each response is `yes`. For a resource whose custom resource definition isn't installed, `kubectl` prints a warning that the resource type is unknown and still returns `yes`.

1. To confirm that the reader group cannot list Secrets or ConfigMaps, or read a granted ConfigMap in another namespace, enter the following commands:

   ```bash
   PROMPT> kubectl auth can-i list secrets --as-group=continuum:readers --as=continuum-check
   PROMPT> kubectl auth can-i list configmaps --as-group=continuum:readers --as=continuum-check
   PROMPT> kubectl auth can-i get configmaps/amazon-vpc-cni --namespace default --as-group=continuum:readers --as=continuum-check
   ```

1. Confirm that each response is `no`.

## Resolving role and RBAC errors for EKS cluster onboarding
<a name="cv-onboard-eks-cluster-troubleshooting"></a>

Use the following table to resolve common issues.

| Symptom | Likely cause | Fix |
| --- | --- | --- |
| AWS Continuum can't assume the role. | The role is missing or its trust policy changed. | In the AWS Continuum console, repeat the procedure in [Creating the reader IAM role in the AWS Continuum console](#cv-onboard-eks-cluster-create-role) to recreate the role and its trust policy correctly. |
| Some resources are missing or return a `forbidden` error. | You didn't apply the RBAC, or the group name doesn't match. | Repeat the procedure in [Granting read-only RBAC](#cv-onboard-eks-cluster-grant-rbac). Make sure that the access entry group and the binding both use `continuum:readers`. |
| The cluster's snapshot is degraded, and a Kubernetes `GET` of a ConfigMap failed with status 403. | You didn't grant `get` on that ConfigMap, or you granted it in another namespace. | Grant `get` on that name in the namespace in its path, as described in [Granting read-only RBAC](#cv-onboard-eks-cluster-grant-rbac). |
| `kubectl` can't reach a private cluster. | The cluster has a private-only endpoint. | Run `kubectl` from a host that has a network path to the cluster endpoint, such as an in-VPC host. |
