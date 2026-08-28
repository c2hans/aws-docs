---
source_url: https://docs.aws.amazon.com/cur/latest/userguide/table-dictionary-cur2-cost-category.html
---

# Cost category columns
<a name="table-dictionary-cur2-cost-category"></a>

Cost category columns contain data about cost categories that apply to the line item. Note that you don’t need to select this column if you selected the Tags column because resource tags are also included under the Tags column.

| Column name | Description | Data type |
| --- | --- | --- |
| cost\_category | A map column containing key-value pairs of the cost categories and their values for a given line item. These keys and values are populated based on the categorization rules you create in the cost categories feature.<br />A cost category key only appears in the map column if it has a value that applies to the specific line item.<br />The keys of this column can be queried as individual columns using the dot operator. For more information, see [Data query](https://docs.aws.amazon.com/cur/latest/userguide/dataexports-data-query.html). | map <string, string> |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cur` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
