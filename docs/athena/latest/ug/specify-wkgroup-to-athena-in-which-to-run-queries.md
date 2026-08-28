---
source_url: https://docs.aws.amazon.com/athena/latest/ug/specify-wkgroup-to-athena-in-which-to-run-queries.html
---

# Specify a workgroup for queries
<a name="specify-wkgroup-to-athena-in-which-to-run-queries"></a>

To specify a workgroup to use, you must have permissions to the workgroup.

**To specify the workgroup to use**

1. Make sure your permissions allow you to run queries in a workgroup that you intend to use. For more information, see [Use IAM policies to control workgroup access](workgroups-iam-policy.md).

1.  To specify the workgroup, use one of these options:
   + If you are using the Athena console, set the workgroup by [switching workgroups](switching-workgroups.md).
   + If you are using the Athena API operations, specify the workgroup name in the API action. For example, you can set the workgroup name in [StartQueryExecution](https://docs.aws.amazon.com/athena/latest/APIReference/API_StartQueryExecution.html), as follows:

     ```
     StartQueryExecutionRequest startQueryExecutionRequest = new StartQueryExecutionRequest()
                   .withQueryString(ExampleConstants.ATHENA_SAMPLE_QUERY)
                   .withQueryExecutionContext(queryExecutionContext)
                   .withWorkGroup({{WorkgroupName}})
     ```
   + If you are using the JDBC or ODBC driver, set the workgroup name in the connection string using the `Workgroup` configuration parameter. The driver passes the workgroup name to Athena. Specify the workgroup parameter in the connection string as in the following example:

     ```
     jdbc:awsathena://AwsRegion={{<AWSREGION>}};UID={{<ACCESSKEY>}};
     PWD={{<SECRETKEY>}};S3OutputLocation=s3://amzn-s3-demo-bucket/{{<athena-output>}}-{{<AWSREGION>}}/;
     Workgroup={{<WORKGROUPNAME>}};
     ```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Athena. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query athena` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
