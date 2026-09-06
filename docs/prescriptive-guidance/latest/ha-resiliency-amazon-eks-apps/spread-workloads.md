---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/ha-resiliency-amazon-eks-apps/spread-workloads.html
---

# Spread workloads across nodes and Availability Zones
<a name="spread-workloads"></a>

Distributing a workload across [failure domains](https://cluster-api-aws.sigs.k8s.io/topics/failure-domains/) such as Availability Zones and nodes improves component availability and decreases the chances of failure for horizontally scalable applications. The following sections introduce ways to spread workloads across nodes and Availability Zones.

## Use pod topology spread constraints
<a name="spread-constraints"></a>

[Kubernetes pod topology spread constraints](https://kubernetes.io/docs/concepts/scheduling-eviction/topology-spread-constraints/) instruct the Kubernetes scheduler to distribute pods that are managed by `ReplicaSet` or `StatefulSet` across different failure domains (Availability Zones, nodes, and types of hardware). When you use pod topology spread constraints, you can do the following:
+ Distribute or concentrate pods across different failure domains depending on application requirements. For example, you can distribute pods for resilience, and you can concentrate pods for network performance.
+ Combine different conditions, such as distributing across Availability Zones and distributing across nodes.
+ Specify the preferred action if conditions can't be met:
  + Use `whenUnsatisfiable: DoNotSchedule` with a combination of `maxSkew` and `minDomains` to create hard requirements for the scheduler.
  + Use `whenUnsatisfiable: ScheduleAnyway` to reduce `maxSkew`.

If a failure zone becomes unavailable, the pods in that zone become unhealthy. Kubernetes reschedules the pods while adhering to the spread constraint if possible.

The following code shows an example of using pod topology spread constraints across Availability Zones or across nodes:

```
...
spec:
  selector:
    matchLabels:
      app: <your-app-label>
    replicas: 3
    template:
      metadata:
        labels: <your-app-label>
      spec:
        serviceAccountName: <ServiceAccountName>
...
        topologySpreadConstraints:
        - labelSelector:
            matchLabels:
              app: <your-app-label>
          maxSkew: 1
          topologyKey: topology.kubernetes.io/zone # <---spread those pods evenly over all availability zones
          whenUnsatisfiable: ScheduleAnyway
        - labelSelector:
            matchLabels:
              app: <your-app-label>
          maxSkew: 1
          topologyKey: kubernetes.io/hostname # <---spread those pods evenly over all nodes
          whenUnsatisfiable: ScheduleAnyway
```

### Default cluster-wide topology spread constraints
<a name="default-cluster-wide-topology-spread-constraints.9c952345-12d7-5844-bcd8-774fbc0f73e4"></a>

By default, Kubernetes provides a [set of topology spread constraints](https://kubernetes.io/docs/concepts/scheduling-eviction/topology-spread-constraints/#internal-default-constraints) for distributing pods across nodes and Availability Zones:

```
defaultConstraints:
  - maxSkew: 3
    topologyKey: "kubernetes.io/hostname"
    whenUnsatisfiable: ScheduleAnyway
  - maxSkew: 5
    topologyKey: "topology.kubernetes.io/zone"
    whenUnsatisfiable: ScheduleAnyway
```

**Note**
Applications that need different types of topology constraints can override the cluster-level policy.

The default constraints set a high `maxSkew`, which isn't useful for deployments that have a small number of pods. As of now, `KubeSchedulerConfiguration` [can't be changed](https://github.com/aws/containers-roadmap/issues/1468) in Amazon EKS. If you need to enforce other sets of topology spread constraints, consider using mutating admission controller like in the section below. You can also control default topology spread constraints if you run an alternative scheduler. However, managing custom schedulers adds complexity and can have implications on cluster resilience and HA. For these reasons, we don't recommend using an alternative scheduler for topology spread constraints only.

### The Gatekeeper policy for topology spread constraints
<a name="the-gatekeeper-policy-for-topology-spread-constraints.6933a860-fd41-5c8c-8aed-93eb84104b1a"></a>

Another option for enforcing topology spread constraints is to use a policy from the [Gatekeeper](https://open-policy-agent.github.io/gatekeeper/website/docs/) project. Gatekeeper policies are defined at the application level.

The following code examples show the use of a `Gatekeeper OPA` policy for deployment. You can modify the policy for your needs. For example, apply the policy only to deployments that have the label `HA=true`, or write a similar policy using a different policy controller.

This first example shows `ConstraintTemplate` used with `k8stopologyspreadrequired_template.yml`:

```
apiVersion: templates.gatekeeper.sh/v1
kind: ConstraintTemplate
metadata:
  name: k8stopologyspreadrequired
spec:
  crd:
    spec:
      names:
        kind: K8sTopologySpreadRequired
      validation:
        openAPIV3Schema:
          type: object
          properties:
            message:
              type: string
  targets:
    - target: admission.k8s.gatekeeper.sh
      rego: |
        package k8stopologyspreadrequired

        get_message(parameters, _default) =3D msg {
          not parameters.message
          msg :=_default
        }

        get_message(parameters, _default) =3D msg {
          msg := parameters.message
        }

        violation[{"msg": msg}] {
          input.review.kind.kind ="Deployment"
          not input.review.object.spec.template.spec.topologySpreadConstraint
          def_msg :"Pod Topology Spread Constraints are required for Deployments"
          msg :get_message(input.parameters, def_msg)

        }
```

The following code shows the `constraints` YAML manifest `k8stopologyspreadrequired_constraint.yml`:

```
apiVersion: constraints.gatekeeper.sh/v1beta1
kind: K8sTopologySpreadRequired
metadata:
  name: require-topologyspread-for-deployments
spec:
  match:
    kinds:
      - apiGroups: ["apps"]
        kinds: ["Deployment"]
    namespaces:  ## Without theses two lines will apply to the whole cluster
      - "example"
```

### When to use topology spread constraints
<a name="when-to-use-topology-spread-constraints.5533d1aa-c42f-52db-a4f6-a1b80fdca568"></a>

Consider using topology spread constraints for the following scenarios:
+ Any horizontally scalable application (for example, stateless web services)
+ Applications with active-active or active-passive replicas (for example, NoSQL databases or caches)
+ Applications with stand-by replicas (for example, controllers)

System components that can be used for the horizontally scalable scenario, for example, include the following:
+ [Cluster Autoscaler](https://github.com/kubernetes/autoscaler/tree/master/cluster-autoscaler) and [Karpenter](https://karpenter.sh/) (with `replicaCount > 1` and `leader-elect = true`)
+ [AWS Load Balancer Controller](https://kubernetes-sigs.github.io/aws-load-balancer-controller/latest/)
+ [CoreDNS](https://coredns.io/)

## Pod affinity and anti-affinity
<a name="anti-affinity"></a>

In some cases, it's beneficial to ensure that no more than one pod of a specific type is running on a node. For example, to avoid scheduling multiple network-heavy pods on the same node, you can use the anti-affinity rule with the label `Ingress` or `Network-heavy`. When you use `anti-affinity`, you can also use a combination of the following:
+ Taints on network-optimized nodes
+ Corresponding tolerations on network-heavy pods
+ Node affinity or node selector to ensure that network-heavy pods use network-optimized instances

Network-heavy pods are used as an example. You might have different requirements, such as GPU, memory, or local storage. For other usage examples and configuration options, see the [Kubernetes documentation](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#inter-pod-affinity-and-anti-affinity).

### Rebalance pods
<a name="rebalance-pods.07274901-c1ac-54bf-95f8-a97b6f642727"></a>

This section discusses two approaches to rebalancing pods in a Kubernetes cluster. The first uses the Descheduler for Kubernetes. The Descheduler helps to maintain pod distribution by enforcing strategies to remove pods that violate topology spread constraints or anti-affinity rules. The second approach uses the Karpenter consolidation and bin-packing feature. Consolidation continuously evaluates and optimizes resource usage by consolidating workloads onto fewer, more efficiently packed nodes.

We recommend using Descheduler if you aren't using Karpenter. If you're using Karpenter and Cluster Autoscaler together, you can use Descheduler with Cluster Autoscaler for node groups.

#### Descheduler for groupless nodes
<a name="descheduler-for-groupless-nodes.7c33cb08-d747-52c8-951d-19bad80446d5"></a>

There's no guarantee that the topology constraints remain satisfied when pods are removed. For example, scaling down a deployment might result in imbalanced pod distribution. However, because Kubernetes uses pod topology spread constraints only at the scheduling stage, pods are left unbalanced across the failure domain.

To maintain a balanced pod distribution in such scenarios, you can use [Descheduler for Kubernetes](https://github.com/kubernetes-sigs/descheduler). Descheduler is a useful tool for multiple purposes, such as to enforce the maximum pod age or time to live (TTL), or to improve the use of infrastructure. In the context of resilience and high availability (HA), consider the following Descheduler strategies:
+ [RemovePodsViolatingTopologySpreadConstraint](https://github.com/kubernetes-sigs/descheduler?tab=readme-ov-file#removepodsviolatingtopologyspreadconstraint)
+ [RemovePodsViolatingInterPodAntiAffinity](https://github.com/kubernetes-sigs/descheduler?tab=readme-ov-file#removepodsviolatinginterpodantiaffinity)
+ [RemoveDuplicates](https://github.com/kubernetes-sigs/descheduler?tab=readme-ov-file#removeduplicates)

#### Karpenter consolidation and bin-packing feature
<a name="karpenter-consolidation-and-bin-packing-feature.2d261949-6ce1-5896-93de-87ffb887fae2"></a>

For workloads that use Karpenter, you can use the consolidation and bin-packing functionality to optimize resource utilization and reduce costs in Kubernetes clusters. Karpenter continuously evaluates pod placements and node utilization, and it attempts to consolidate workloads onto fewer, more efficiently packed nodes when possible. This process involves analyzing resource requirements, considering constraints such as pod affinity rules, and potentially moving pods between nodes to improve overall cluster efficiency. The following code provides an example:

```
apiVersion: karpenter.sh/v1beta1
kind: NodePool
metadata:
  name: default
spec:
  disruption:
    consolidationPolicy: WhenUnderutilized
    expireAfter: 720h
```

For `consolidationPolicy`, you can use `WhenUnderutilized` or `WhenEmpty`:
+ When `consolidationPolicy` is set to `WhenUnderutilized`, Karpenter considers all nodes for consolidation. When Karpenter discovers a node that's empty or underused, Karpenter attempts to remove or replace the node to reduce cost.
+ When `consolidationPolicy` is set to `WhenEmpty`, Karpenter considers for consolidation only nodes that contain no workload pods.

The Karpenter consolidation decisions are not based solely on CPU or memory utilization percentages that you might see in monitoring tools. Instead, Karpenter uses a more complex algorithm based on pod resource requests and potential cost optimizations. For more information, see the [Karpenter documentation](https://karpenter.sh/docs/concepts/disruption/#consolidation).
