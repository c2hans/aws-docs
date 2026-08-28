---
source_url: https://docs.aws.amazon.com/redshift/latest/dg/copy-usage_notes-spatial-data.html
---

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025.

# Loading a column of the GEOMETRY or GEOGRAPHY data type
<a name="copy-usage_notes-spatial-data"></a>

You can COPY to `GEOMETRY` or `GEOGRAPHY` columns from data in a character-delimited text file, such as a CSV file. The data must be in the hexadecimal form of the well-known binary format (either WKB or EWKB) or the well-known text format (either WKT or EWKT) and fit within the maximum size of a single input row to the COPY command. For more information, see [COPY](r_COPY.md).

For information about how to load from a shapefile, see [Loading a shapefile into Amazon Redshift](spatial-copy-shapefile.md).

For more information about the `GEOMETRY` or `GEOGRAPHY` data type, see [Querying spatial data in Amazon Redshift](geospatial-overview.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Redshift. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query redshift` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
