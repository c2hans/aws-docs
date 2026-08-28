---
source_url: https://docs.aws.amazon.com/solutions/latest/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/confirm-cost-tags-associated-with-the-guidance.html
---

# Confirm cost tags associated with the Guidance
<a name="confirm-cost-tags-associated-with-the-guidance"></a>

After you activate cost allocation tags associated with the Guidance, you must confirm the cost allocation tags to see the costs for this Guidance. To confirm cost allocation tags:

1. Sign in to the [Systems Manager console](https://console.aws.amazon.com/systems-manager).

1. In the navigation pane, choose **Application Manager**.

1. In **Applications**, choose the application name for this Guidance and select it.

1. In the **Overview** tab, in **Cost**, select **Add user tag**.
![Screenshot depicting the Application Cost add user tag screen](http://docs.aws.amazon.com/solutions/latest/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/images/AppManager_1.png)

1. On the **Add user tag** page, enter `confirm`, then select **Add user tag**.

The activation process can take up to 24 hours to complete and the tag data to appear.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Data Transfer from Amazon S3 Glacier Vaults to Amazon S3. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
