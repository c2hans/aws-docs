---
source_url: https://docs.aws.amazon.com/batch/latest/userguide/daemonset-on-batch-eks-nodes.html
---

# Run a DaemonSet on AWS Batch managed nodes
<a name="daemonset-on-batch-eks-nodes"></a>

AWS Batch sets taints on AWS Batch managed Kubernetes nodes. You can target a DaemonSet to run on AWS Batch managed nodes with the following `tolerations`.

```
tolerations:
  - key: "batch.amazonaws.com/batch-node"
    operator: "Exists"
```

Another way to do this is with the following `tolerations`.

```
tolerations:
  - key: "batch.amazonaws.com/batch-node"
    operator: "Exists"
    effect: "NoSchedule"
  - key: "batch.amazonaws.com/batch-node"
    operator: "Exists"
    effect: "NoExecute"
```
