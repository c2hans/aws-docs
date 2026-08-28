---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/userguide/activate-appregistry.html
---

# Activating AppRegistry for a workload
<a name="activate-appregistry"></a>

Using AppRegistry is optional, and AWS Business and Enterprise Support customers can activate it on a per-workload basis.

Whenever Discovery support is turned on and AppRegistry is associated with a new or existing workload, AWS Well-Architected Tool creates a service-managed attribute group. The attribute group **Metadata** in AppRegistry contains the workload ARN, the workload name, and the risks associated with the workload.
+  When Discovery support is turned on, any time there is a change to the workload, the attribute group is updated.
+  When Discovery support is turned off or the application is removed from the workload, the workload information is removed from AWS Service Catalog.

If you want an AppRegistry application to drive the data fetched from Trusted Advisor, set your workload **Resource definition** as **AppRegistry** or **All**. Create roles for all accounts that own resources in your application following the guidelines in [Activating Trusted Advisor for a workload in IAM](activate-ta-in-iam.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
