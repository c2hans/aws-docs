---
source_url: https://docs.aws.amazon.com/solutions/latest/scalable-analytics-using-apache-druid-on-aws/problem-deployment-fails-due-to-unsupported-rds-engine-version.html
---

# Problem: Deployment fails due to unsupported RDS engine version
<a name="problem-deployment-fails-due-to-unsupported-rds-engine-version"></a>

You might encounter the error `Cannot find version for aurora-postgresql` during deployment of the guidance in certain regions. This occurs because the guidance deploys RDS engine version 13.9 by default, and this version may not be available in the specified region.

## Resolution
<a name="resolution-2"></a>

1. Search the RDS engine versions with the following AWS CLI.

   ```
   aws rds describe-db-engine-versions --engine aurora-postgresql --query '*[].[EngineVersion]' --output text --region <region>
   ```

1. Select an RDS engine version (it is advisable to choose the closest version to 13.9) from the provided list.

1. Configure the `druidMetadataStoreConfig` by using the selected RDS engine version.

1. Deploy the guidance again.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Guidance for Scalable Analytics Using Apache Druid on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
