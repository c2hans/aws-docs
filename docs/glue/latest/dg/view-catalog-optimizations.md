---
source_url: https://docs.aws.amazon.com/glue/latest/dg/view-catalog-optimizations.html
---

# Viewing catalog-level optimizations
<a name="view-catalog-optimizations"></a>

 When catalog-level table optimization is enabled, anytime an Apache Iceberg table is created or updated via the `CreateTable` or `UpdateTable` APIs through AWS Management Console, SDK, or AWS Glue crawler, an equivalent table level setting is created for that table.

 After you create or update a table, you can verify the table details to confirm the table optimization. The `Table optimization` shows the `Configuration source` property set as `Catalog`.

![An image of an Apache Iceberg table with catalog-level optimization configuration has  been applied.](http://docs.aws.amazon.com/glue/latest/dg/images/catalog-optimization-enabled.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
