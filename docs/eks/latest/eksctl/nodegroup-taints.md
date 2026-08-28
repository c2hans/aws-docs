---
source_url: https://docs.aws.amazon.com/eks/latest/eksctl/nodegroup-taints.html
---

# Taints
<a name="nodegroup-taints"></a>

To apply [taints](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/) to a specific nodegroup use the `taints` config section like this:

```
    taints:
      - key: your.domain.com/db
        value: "true"
        effect: NoSchedule
      - key: your.domain.com/production
        value: "true"
        effect: NoExecute
```

A full example can be found [here](https://github.com/eksctl-io/eksctl/blob/main/examples/34-taints.yaml).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EKS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query eks` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
