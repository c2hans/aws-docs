---
source_url: https://docs.aws.amazon.com/redshift/latest/mgmt/zero-etl-using.setting-up.html
---

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025.

# Getting started with zero-ETL integrations
<a name="zero-etl-using.setting-up"></a>

This set of tasks walks you through setting up your first zero-ETL integration. First, you configure your integration source and set it up with the required parameters and permissions. Then, you continue to the rest of the initial setup from the Amazon Redshift console or AWS CLI. The console provides a **Fix it for me** option to correct some configuration issues.

**Topics**
+ [Create and configure a target Amazon Redshift data warehouse](zero-etl-setting-up.rs-data-warehouse.md)
+ [Turn on case sensitivity for your data warehouse](zero-etl-setting-up.case-sensitivity.md)
+ [Configure authorization for your Amazon Redshift data warehouse](zero-etl-using.redshift-iam.md)
+ [Create a zero-ETL integration](zero-etl-setting-up.create-integration.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Redshift. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query redshift` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
