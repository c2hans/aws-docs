---
source_url: https://docs.aws.amazon.com/Monitron/latest/user-guide/gs-resolving-anomalies.html
---

Amazon Monitron is no longer open to new customers. Existing customers can continue to use the service as normal. For capabilities similar to Amazon Monitron, see our [blog post](https://aws.amazon.com/blogs/machine-learning/maintain-access-and-consider-alternatives-for-amazon-monitron).

# Step 4: Resolving a machine abnormality
<a name="gs-resolving-anomalies"></a>

Resolving an abnormality returns the sensor to healthy status and provides information about the issue to Amazon Monitron so it can better determine when a failure might occur in the future.

For information about failure modes and causes, and how to resolve abnormalities, see [Resolving a Machine Abnormality](https://docs.aws.amazon.com/Monitron/latest/user-guide/anom-monitoring-chapter.html#anom-resolve-anom) in the *Amazon Monitron User Guide*.

**To resolve an abnormality**

1. In the **Assets** list, choose the asset with the issue.

1. Choose the position with the resolved abnormality.

1. Choose **Resolve**.

1. For **Failure mode**, choose one of the available types.

1. For **Failure cause**, choose the cause.

1. For **Action taken** choose the action taken.

1. Choose **Submit**.

   In the **Assets** list, the asset status returns to **Healthy**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Monitron. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query Monitron` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
