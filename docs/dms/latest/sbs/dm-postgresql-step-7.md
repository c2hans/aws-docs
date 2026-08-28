---
source_url: https://docs.aws.amazon.com/dms/latest/sbs/dm-postgresql-step-7.html
---

# Step 7: Create a Migration Project
<a name="dm-postgresql-step-7"></a>

Now you can create a migration project. A migration project describes your instance profile, source and target data providers, and secrets from AWS Secrets Manager.

To create a migration project

1. Sign in to the AWS Management Console and open the AWS DMS console at [https://console.aws.amazon.com/dms/v2/](https://console.aws.amazon.com/dms/v2/).

1. Choose your AWS Region.

1. Choose **Migration projects**, and then choose **Create migration project**.

1. For **Name**, enter a unique name for your migration project. For example, enter `dm-project`.

1. For **Instance profile**, choose `dm-instance-profile`. You created this instance profile in [Step 5](dm-postgresql-step-5.md).

1. For **Source**, choose **Browse**, and then choose `dm-postgresql-source-provider`. You created this data provider in [Step 6](dm-postgresql-step-6.md).

1. For **Secret ID**, choose `dm-postgresql-source`. You created this secret in [Step 4](dm-postgresql-step-4.md).

1. For **IAM role**, choose `HomogeneousDataMigrationsRole`. You created this role in [Step 1](dm-postgresql-step-1.md).

1. For **Target**, choose **Browse**, and then choose `dm-postgresql-target-provider`. You created this data provider in [Step 6](dm-postgresql-step-6.md).

1. For **Secret ID**, choose `dm-postgresql-target`. You created this secret in [Step 4](dm-postgresql-step-4.md).

1. For **IAM role**, choose `HomogeneousDataMigrationsRole`. You created this role in [Step 1](dm-postgresql-step-1.md).

1. Choose **Create migration project**.

Use this migration project to migrate your source PostgreSQL database to your Amazon RDS for PostgreSQL database.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Database Migration Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
