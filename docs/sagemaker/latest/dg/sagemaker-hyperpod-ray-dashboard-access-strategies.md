---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-ray-dashboard-access-strategies.html
---

# Access strategies and security best practices
<a name="sagemaker-hyperpod-ray-dashboard-access-strategies"></a>

An access strategy sets who can reach a Ray cluster's dashboard and Jobs API endpoint. You set it with annotations on the Ray resource.

## Annotations
<a name="sagemaker-hyperpod-ray-dashboard-access-strategies-annotations"></a>

Add the following annotations under `metadata.annotations` on your Ray resource (`RayCluster`, `RayJob`, `RayService`, or `RayCronJob`).

```
metadata:
  annotations:
    access.sagemaker.amazonaws.com/enabled: "true"
    access.sagemaker.amazonaws.com/access-strategy: ray-access-strategy-private
```

When you add these annotations to a `RayJob`, `RayService`, or `RayCronJob`, they are automatically propagated to the `RayCluster` created on their behalf. You do not need to annotate the underlying cluster separately.

## Strategies
<a name="sagemaker-hyperpod-ray-dashboard-access-strategies-strategies"></a>
+ `ray-access-strategy-private` — the default when no strategy annotation is set. Access is scoped to the identity that created the cluster.
+ `ray-access-strategy-public` — any identity with connect permission in the cluster's namespace can reach the endpoint.

**Important**
Choose `ray-access-strategy-public` only when every identity with connect permission in the namespace is meant to have read and write access to the cluster.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
