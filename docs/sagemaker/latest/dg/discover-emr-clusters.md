---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/discover-emr-clusters.html
---

# List Amazon EMR clusters from Studio or Studio Classic
<a name="discover-emr-clusters"></a>

Data scientists and data engineers can discover, and then connect to Amazon EMR clusters from Studio. The Amazon EMR clusters may be in the same AWS account as Studio or in a different AWS account.

Before users can list or connect to clusters, administrators must have configured the necessary settings in the Studio environment. For information on how administrators can configure a Studio environment to allow discovering running Amazon EMR clusters, see [Admin guide](studio-emr-admin-guide.md). If your administrator [configured the cross-account discovery of Amazon EMR clusters](studio-notebooks-configure-discoverability-emr-cluster.md), you can view a consolidated list of clusters. The list includes clusters from the AWS account used by Studio as well as clusters from remote accounts that you have been granted access to.

To view the list of available Amazon EMR clusters from within Studio:

1. In the Studio UI's left navigation menu, scroll down to **EMR Clusters**. This opens up a page listing the Amazon EMR clusters that you have access to.

   The list displays clusters in the following stages: **Bootstrapping**, **Starting** **Running**, **Waiting**. You can narrow down the displayed clusters by their current status using the filter icon.

1. Choose a particular **Running** cluster you want to connect to, and then refer to [Connect to an Amazon EMR cluster from SageMaker Studio or Studio Classic](connect-emr-clusters.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
