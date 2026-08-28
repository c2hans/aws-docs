---
source_url: https://docs.aws.amazon.com/detective/latest/userguide/source-data-types-EKS.html
---

# Amazon EKS audit logs
<a name="source-data-types-EKS"></a>

Amazon EKS audit logs is an optional data source package that can be added to your Detective behavior graph. You can view the available optional source packages, and their status in your account, from the **Settings** page in the console or through the Detective API.

A 30 day free trial is provided for this data source. To learn more see [Free trial for optional data sources](free-trial-overview.md#free-trial-datasource).

Enabling Amazon EKS audit logs allows Detective to add in-depth information about resources created with Amazon EKS to your behavior graph. This data source enhances the information provided about the following entity types: EKS Cluster, Kubernetes Pod, Container Image and Kubernetes subject.

Additionally, If you have enabled EKS audit logs as a data source in Amazon GuardDuty you will be able to see details for Kubernetes findings from GuardDuty. For more info on enabling this data source in GuardDuty see [Kubernetes protection in Amazon GuardDuty](https://docs.aws.amazon.com/guardduty/latest/ug/kubernetes-protection.html).

**Note**
This data source is enabled by default for new behavior graphs created after July 26, 2022. For behavior graphs created before July 26, 2022 it must be enabled manually.

****Adding or removing Amazon EKS audit logs as an optional data source:****

1. Open the Detective console at [https://console.aws.amazon.com/detective/](https://console.aws.amazon.com/detective/).

1. From the navigation panel under **Settings**, choose **General**.

1. Under **Source packages**, select **EKS audit logs** to enable this data source. If it is already enabled, select it again to stop ingesting **EKS audit logs** into your behavior graph.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Detective. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query detective` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
