---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/supply-chain-calculations-quick-suite/inventory.html
---

# Inventory
<a name="inventory"></a>

Inventory must be managed, planned, and controlled. The purpose of inventory is to be able to satisfy customer demand without overstocking. It represents both opportunity and risk in the supply chain. For example, if there is not enough inventory, customer service and revenue will be impacted negatively. If there is too much inventory, cost to carry and capital investment will be higher than necessary, impacting profitability.

The following table contains calculations to help you plan and manage your inventory.

|
|
| Name | Description | Calculation |
| --- |--- |--- |
| Average age of inventory | This calculation returns the average number of days it takes for a company to sell off its inventory. | `(Average cost of inventory at its current level / cost of goods sold) × 365` |
| Average inventory cost | This calculation returns the average cost of inventory for a defined time period. You typically run this calculation at the beginning or end of a fiscal period. | `Sum(inventory cost at each time period) / # of time periods` |
| Average inventory level | This calculation returns the average number of units of on-hand inventory, for a defined time period. You typically run this calculation at the beginning or end of a fiscal period. | `Sum(inventory units in each time period) / # of time periods` |
| Inventory-to-sales ratio (ISR) | This calculation compares the value of your inventory to your total sales, for a defined time period. It helps you monitor the amount of capital allocated to inventory, and it's a measurement of the financial stability of the company. ISR is closely related to inventory turnover ratio. The primary difference is that ISR returns capital investment in inventory at a specific point in time, whereas inventory turnover ratio returns how many times you churn the inventory for a defined time period. | `Inventory value for a specific point in time / Sales value for a date range` |
| Inventory turnover ratio | This calculation returns how many times a company turned over (or *cycled*) its inventory over a defined time period. The period of time is most commonly 12 months. You can calculate inventory turnover by using cost value, retail value, or units. | For a 12-month inventory turn using cost value:<br />`Annual cost of goods sold (COGS) / Average value of inventory level` |
| Inventory turn (units) | This calculation returns how many times a company turned over (or *cycled*) its inventory over a defined time period. The period of time is most commonly 12 months. You can calculate inventory turnover by using cost value, retail value, or units. | For a 12-month inventory turn based on units:<br />`Annual unit sales / Average unit inventory level` |
| Inventory velocity (IV) | Inventory velocity is measured in units and is the portion of inventory that is projected to be consumed within the next specified period. This metric helps you optimize inventory levels to balance inventory and sales. | `Opening stock / Sales forecast for upcoming period` |
| Turn-earn index (TEI) | This calculation helps you evaluate profits and use of inventory. It helps account for the differences between slow-moving, high-profit inventory and fast-moving, low-profit inventory so that you can see how your inventory turn ratio and gross profit are related. Generally, most companies want a turn-earn index of 150 or higher. | `(Inventory turnover ratio × Gross profit percentage) × 100` |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
