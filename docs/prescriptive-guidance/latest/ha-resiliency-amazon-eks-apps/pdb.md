---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/ha-resiliency-amazon-eks-apps/pdb.html
---

# Protect critical workloads with a PDB
<a name="pdb"></a>

A pod disruption budget (PDB) is an essential feature for maintaining the high availability of applications in a cluster. The PDB specifies a target size, which is the minimum availability for a particular type of pod. This means that a minimum number of replicas of a particular pod type must be running at any given time. If the number of running replicas falls below the target size, Kubernetes prevents further disruptions to the remaining replicas until the target size is met. PDBs help to ensure that workloads are not affected by these events and can continue to run uninterrupted. When a disruption occurs, Kubernetes attempts to gracefully evict pods from the affected nodes while maintaining the number of replicas specified in the PDB.

You can use a PDB to declare the `minAvailable` and `maxUnavailable` number of replicas. For example, if you want at least three copies of your app to be available, create a PDB that is similar to the following example:

```
apiVersion: policy/v1beta1
kind: PodDisruptionBudget
metadata:
  name: my-svc-pdb
spec:
  minAvailable: 3
  selector:
    matchLabels:
      app: my-svc
```

Setting up PDBs correctly for your applications helps to minimize the disruption during planned or unplanned events. You can use the anti-affinity rule to schedule a deployment's pods on different nodes and avoid PDB delays during node upgrades.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
