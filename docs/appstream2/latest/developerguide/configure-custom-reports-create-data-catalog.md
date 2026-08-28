---
source_url: https://docs.aws.amazon.com/appstream2/latest/developerguide/configure-custom-reports-create-data-catalog.html
---

# Create a Data Catalog by Using the AWS Glue Crawler
<a name="configure-custom-reports-create-data-catalog"></a>

The AWS Glue crawler, when run, creates a Data Catalog and schema that are mapped to the structure of your sessions and applications reports. Each time a new report is stored in your Amazon S3 bucket, you must run the crawler to update your AWS Glue Data Catalog with the data from the new report.

**Note**
Charges may apply to the running of your AWS Glue crawler. For more information, see [AWS Glue Pricing](https://aws.amazon.com/glue/pricing/).

1. Open the AWS Glue console at [https://console.aws.amazon.com/glue/](https://console.aws.amazon.com/glue/).

1. Choose the AWS Region for which you have subscribed to usage reports.

1. Select the check box next to the crawler named **appstream-usage-sessions-crawler**, and then choose **Run crawler**. Repeat this step for the crawler named **appstream-usage-apps-crawler**.

   Performing these steps runs the crawlers and schedules them to run automatically according to the schedule specified in the CloudFormation stack.

1. After both crawlers finish running, in the navigation pane, choose **Databases**. A database named **appstream-usage**, which represents your usage reports, displays. This database is an AWS Glue Data Catalog that was created when **appstream-usage-sessions-crawler** and **appstream-usage-apps-crawler** were run.

1. To view the tables in the database, choose **appstream-usage**, **Tables**. Two tables, **applications** and **sessions**, which represent your applications and sessions usage reports respectively, display. Choose either table to view its schema.

   You can now query these tables in Athena by using SQL.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Applications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appstream2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
