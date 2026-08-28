---
source_url: https://docs.aws.amazon.com/redshift/latest/dg/t_Troubleshooting_load_errors.html
---

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025.

# Troubleshooting data loads
<a name="t_Troubleshooting_load_errors"></a>

When you load data into Amazon Redshift tables you might encounter errors from Amazon S3, invalid input data, and COPY command errors. The following sections provide information about identifying and resolving data load errors.

**Topics**
+ [Troubleshooting S3 event integration and COPY JOB errors](s3-integration-troubleshooting.md)
+ [S3ServiceException errors](s3serviceexception-error.md)
+ [System tables for troubleshooting data loads](system-tables-for-troubleshooting-data-loads.md)
+ [Multibyte character load errors](multi-byte-character-load-errors.md)
+ [Load error reference](r_Load_Error_Reference.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Redshift. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query redshift` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
