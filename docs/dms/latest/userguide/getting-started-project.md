---
source_url: https://docs.aws.amazon.com/dms/latest/userguide/getting-started-project.html
---

# Create a migration project in DMS Schema Conversion
<a name="getting-started-project"></a>

Now you can create a migration project. In the migration project, you specify your source and target data providers, and your instance profile.

**To create a migration project**

1. Choose **Migration projects**, and then choose **Create migration project**.

1. For **Name**, enter a unique name for your migration project. For example, enter **sc-project**.

1. For **Instance profile**, choose **sc-instance**.

1. For **Source**, choose **Browse**, and then choose **sc-source**.

1. For **Secret ID**, choose **sc-source-secret**.

1. For **IAM role**, choose **sc-source-secret-role**.

1. For **Target**, choose **Browse**, and then choose **sc-target**.

1. For **Secret ID**, choose **sc-target-secret**.

1. For **IAM role**, choose **sc-target-secret-role**.

1. Choose **Create migration project**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Database Migration Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
