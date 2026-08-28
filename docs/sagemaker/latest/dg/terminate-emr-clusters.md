---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/terminate-emr-clusters.html
---

# Terminate an Amazon EMR cluster from Studio or Studio Classic
<a name="terminate-emr-clusters"></a>

The following procedure shows how to terminate an Amazon EMR cluster from a Studio or Studio Classic notebook.

**To terminate a cluster in a `Running` state, navigate to the list of available Amazon EMR clusters.**

1. In the Studio UI, scroll down to the **Data** node in the left navigation menu.

1. Navigate down to the **EMR Clusters** node. This opens up a page listing the Amazon EMR clusters that you have access to.

1. Select the name of the cluster that you want to terminate, and then choose **Terminate**.

1. This opens up a confirmation window informing you that any pending work or data on your cluster will be lost permanently after termination. Confirm by choosing **Terminate** again.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
