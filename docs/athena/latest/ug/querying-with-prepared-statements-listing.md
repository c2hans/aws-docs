---
source_url: https://docs.aws.amazon.com/athena/latest/ug/querying-with-prepared-statements-listing.html
---

# List prepared statements using the AWS CLI
<a name="querying-with-prepared-statements-listing"></a>

To list the prepared statements for a specific workgroup, you can use the Athena [list-prepared-statements](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/list-prepared-statements.html) AWS CLI command or the [ListPreparedStatements](https://docs.aws.amazon.com/athena/latest/APIReference/API_ListPreparedStatements.html) Athena API action. The `--work-group` parameter is required.

```
aws athena list-prepared-statements --work-group primary
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Athena. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query athena` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
