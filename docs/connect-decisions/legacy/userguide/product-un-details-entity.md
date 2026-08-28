---
source_url: https://docs.aws.amazon.com/connect-decisions/legacy/userguide/product-un-details-entity.html
---

# un\_details
<a name="product-un-details-entity"></a>

**Primary key (PK)**

The table below lists the colum names that are uniquely identified in the data entity.

| Name | Column |
| --- | --- |
| product\_un\_details | un\_id |

The table below lists the column names supported by the data entity:

|  Column name | Data type | Required | Description |
| --- | --- | --- | --- |
| un\_class | string | No | Hazardous material categories and subcategories. |
| hazmat\_class | string | No | One of nine classes of hazardous materials (as of 2024).  |
| image\_url | string | No | Image of the symbol for the hazmat class.  |
| un\_description | string | No | Description of the UN Proper Shipping Name.  |
| un\_id | string | Yes | UN IDs are four-digit numbers that identify dangerous goods, hazardous substances and articles (such as explosives, flammable liquids, toxic substances, and so on.) in the framework of international transport.  |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Decisions. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect-decisions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
