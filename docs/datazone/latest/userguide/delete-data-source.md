---
source_url: https://docs.aws.amazon.com/datazone/latest/userguide/delete-data-source.html
---

# Delete a data source in Amazon DataZone
<a name="delete-data-source"></a>

After you create an Amazon DataZone data source, you can modify it at any time to change the source details or the data selection criteria.

To complete these steps, you must have the **AmazonDataZoneFullAccess** AWS managed policy attached. For more information, see [AWS managed policies for Amazon DataZone](security-iam-awsmanpol.md).

When you no longer need an Amazon DataZone data source, you can remove it permenantly. After you delete a data source, all assets that originated from that data source are still available in the catalog, and users can still subscribe to them. However, the assets will stop receiving updates from the source. We recommend that you first move the dependent assets to a different data source before you delete it.

**Note**
You must remove all fulfillments on the data source before you can delete it. For more information, see [Amazon DataZone data discovery, subscription, and consumption](discover-subscribe-consume-data.md).

**To delete a data source**

1. On the **Data** tab for the project, choose **Data sources** from the left navigation pane.

1. Choose the data source that you want to delete.

1. Choose **Actions**, **Delete data source** and confirm deletion.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DataZone. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datazone` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
