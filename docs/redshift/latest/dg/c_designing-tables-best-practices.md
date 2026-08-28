---
source_url: https://docs.aws.amazon.com/redshift/latest/dg/c_designing-tables-best-practices.html
---

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025.

# Amazon Redshift best practices for designing tables
<a name="c_designing-tables-best-practices"></a>

As you plan your database, certain key table design decisions heavily influence overall query performance. These design choices also have a significant effect on storage requirements, which in turn affects query performance by reducing the number of I/O operations and minimizing the memory required to process queries.

In this section, you can find a summary of the most important design decisions and best practices for optimizing query performance. [Automatic table optimization](t_Creating_tables.md) provides more detailed explanations and examples of table design options.

**Topics**
+ [Choose the best sort key](c_best-practices-sort-key.md)
+ [Choose the best distribution style](c_best-practices-best-dist-key.md)
+ [Let COPY choose compression encodings](c_best-practices-use-auto-compression.md)
+ [Define primary key and foreign key constraints](c_best-practices-defining-constraints.md)
+ [Use the smallest possible column size](c_best-practices-smallest-column-size.md)
+ [Use date/time data types for date columns](c_best-practices-timestamp-date-columns.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Redshift. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query redshift` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
