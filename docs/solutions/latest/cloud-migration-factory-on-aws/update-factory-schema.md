---
source_url: https://docs.aws.amazon.com/solutions/latest/cloud-migration-factory-on-aws/update-factory-schema.html
---

# Step 6: Update the factory schema
<a name="update-factory-schema"></a>

## Update the target AWS Account Id for AWS MGN migrations
<a name="aws-mgn-only-update-the-aws-accountid-for-aws-mgn"></a>

1. On the **Migration Factory** web interface, select **Administration**, then select **Attributes**.

1. On the **Attribute Configuration** page, select **Application**, then select **Attributes**.

1. Select **AWS Account Id**, then choose **Edit**.

    **Migration Factory web interface Attribute Details tab**
![migration factory mgn attribute tab](http://docs.aws.amazon.com/solutions/latest/cloud-migration-factory-on-aws/images/migration-factory-mgn-attribute-tab.png)

1. On the **Amend attribute** page, update \* Value list\* with your target AWS account IDs and choose **Save**.

**Note**
If you have more than one AWS account ID, separate the ID with commas.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Cloud Migration Factory on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
