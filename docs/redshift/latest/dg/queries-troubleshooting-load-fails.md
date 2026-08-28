---
source_url: https://docs.aws.amazon.com/redshift/latest/dg/queries-troubleshooting-load-fails.html
---

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025.

# Load fails
<a name="queries-troubleshooting-load-fails"></a>

Your data load can fail for the following reasons. We suggest the following troubleshooting approaches.

**Data Source is in a different AWS Region**
By default, the Amazon S3 bucket or Amazon DynamoDB table specified in the COPY command must be in the same AWS Region as the cluster. If your data and your cluster are in different Regions, you receive an error similar to the following:

```
The bucket you are attempting to access must be addressed using the specified endpoint.
```

If at all possible, make sure your cluster and your data source are in the same Region. You can specify a different Region by using the [REGION](copy-parameters-data-source-s3.md#copy-region) option with the COPY command.

**Note**
If your cluster and your data source are in different AWS Regions, you incur data transfer costs. You also have higher latency.

**COPY command fails**
Query STL\_LOAD\_ERRORS to discover the errors that occurred during specific loads. For more information, see [STL\_LOAD\_ERRORS](r_STL_LOAD_ERRORS.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Redshift. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query redshift` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
