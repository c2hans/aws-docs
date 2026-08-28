---
source_url: https://docs.aws.amazon.com/quick/latest/userguide/sharing-data-sets.html
---

# Sharing datasets
<a name="sharing-data-sets"></a>

You can give other Quick Sight users and groups access to a dataset by sharing it with them. Then they can create analyses from it. If you make them co-owners, they can also refresh, edit, delete, or reshare the dataset.

## Sharing a dataset
<a name="share-a-data-set"></a>

If you have owner permissions on a dataset, use the following procedure to share it.

**To share a dataset**

1. From the Quick start page, choose **Data** at left.

1. On the **Data** page, choose the dataset that you want to share.

1. On the dataset details page that opens, choose the **Permissions** tab, and then choose **Add users & groups**.

1. Enter the user or group that you want to share this dataset with, and then choose **Add**. You can only invite users who belong to the same Quick account.

   Repeat this step until you have entered information for everyone you want to share the dataset with.

1. For the **Permissions** column, choose a role for each user or group to give them permissions on the dataset.

   Choose **User** to allow them to create analyses and datasets from the dataset. Choose **Owner** to allow them to do that and also refresh, edit, delete, and reshare the dataset.

   Users receive emails with a link to the dataset. Groups don't receive invitation emails.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quick` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
