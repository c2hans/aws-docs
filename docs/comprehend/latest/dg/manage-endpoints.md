---
source_url: https://docs.aws.amazon.com/comprehend/latest/dg/manage-endpoints.html
---

# Managing Amazon Comprehend endpoints
<a name="manage-endpoints"></a>

In Amazon Comprehend, endpoints make your custom models available for real-time classification or entity detection. After you create an endpoint, you can make changes to it as your business needs evolve. For example, you can monitor your endpoint utilization and apply auto scaling to automatically set endpoint provisioning to fit your capacity needs. You can manage all your endpoints from a single view, and when you no longer need an endpoint you can delete it to save costs.

Before you can manage an endpoint, you must create one. For more information, see the following procedures:
+ [Creating an endpoint for custom classification](custom-sync.md#create-endpoint)
+ [Creating an endpoint for custom entity detection](detecting-cer-real-time.md#detecting-cer-real-time-create-endpoint)

**Topics**
+ [Overview of Amazon Comprehend endpoints](manage-endpoints-overview.md)
+ [Using Amazon Comprehend endpoints](using-endpoints.md)
+ [Monitoring Amazon Comprehend endpoints](manage-endpoints-monitor.md)
+ [Updating Amazon Comprehend endpoints](manage-endpoints-update.md)
+ [Using Trusted Advisor with Amazon Comprehend](manage-endpoints-trusted-advisor.md)
+ [Deleting Amazon Comprehend endpoints](manage-endpoints-delete.md)
+ [Auto scaling with endpoints](comprehend-autoscaling.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Comprehend. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query comprehend` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
