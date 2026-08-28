---
source_url: https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/emr-serverless-lf-troubleshooting.html
---

# Troubleshooting
<a name="emr-serverless-lf-troubleshooting"></a>

See the following sections for troubleshooting solutions.

## Logging
<a name="emr-serverless-lf-troubleshooting-logging"></a>

EMR Serverless uses Spark resources profiles to split job execution. EMR Serverless uses the user profile to run the code you supplied, while the system profile enforces Lake Formation policies. You can access the logs for the tasks ran as the user profile.

For more information about debugging Lake Formation-enabled jobs, refer to [Debugging jobs](emr-serverless-lf-enable-debugging.html).

## Live UI and Spark History Server
<a name="emr-serverless-lf-troubleshooting-live-ui"></a>

The Live UI and the Spark History Server have all Spark events generated from the user profile and redacted events generated from the system driver.

You can see all of the tasks from the user and system drivers in the **Executors** tab. However, log links are available only for the user profile. Also, some information is redacted from Live UI, such as the number of output records.

## Job failed with insufficient Lake Formation permissions
<a name="emr-serverless-lf-troubleshooting-insufficient-lf-permissions"></a>

Make sure that your job runtime role has the permissions to run SELECT and DESCRIBE on the table that you are accessing.

## Job with RDD execution failed
<a name="emr-serverless-lf-troubleshooting-rdd-execution"></a>

EMR Serverless currently doesn't support resilient distributed dataset (RDD) operations on Lake Formation-enabled jobs.

## Unable to access data files in Amazon S3
<a name="emr-serverless-lf-troubleshooting-s3-access-failure"></a>

Make sure you have registered the location of the data lake in Lake Formation.

## Security validation exception
<a name="emr-serverless-lf-troubleshooting-security-validation"></a>

EMR Serverless detected a security validation error. Contact AWS support for assistance.

## Sharing AWS Glue Data Catalog and tables across accounts
<a name="emr-serverless-lf-troubleshooting-cross-account"></a>

You can share databases and tables across accounts and still use Lake Formation. For more information, refer to [Cross-account data sharing in Lake Formation](https://docs.aws.amazon.com/lake-formation/latest/dg/cross-account-permissions.html) and [How do I share AWS Glue Data Catalog and tables cross-account using AWS Lake Formation?](https://repost.aws/knowledge-center/glue-lake-formation-cross-account).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EMR Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query emr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
