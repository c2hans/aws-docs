---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/supply-chain-calculations-quick-suite/distribution.html
---

# Distribution and warehousing
<a name="distribution"></a>

These calculations help you evaluate the throughput of your supply chain.

The following table contains distribution and warehousing calculations. In the following table, *units* refers to cases, cartons, or another standard unit of product measure or count, as appropriate for your supply chain.

|
|
| Name | Description | Calculation |
| --- |--- |--- |
| Aged backorder | This calculation reports the number of past-due orders, or *backorders*, based on the requested delivery date or ship date. An order is a backorder if the actual ship date occurs after the requested ship date. | `Count(# of backorders past due)`<br />To calculate if a backorder is past due:<br />`Requested ship or delivery date < actual ship or delivery date` |
| Average units received per hour | This calculation returns the rate at which units are received per hour, for a defined time period. | `# of units received / # of hours worked` |
| Average units shipped per hour | This calculation returns the rate at which units are shipped per hour, for a defined time period. | `# of units shipped / # of hours worked` |
| Average units stocked per hour | This calculation returns the rate at which units are stocked (sometimes referred to as *put away*) per hour, for a defined time period. | `# of units stocked / # of hours worked` |
| Average units picked per hour | This calculation returns the rate at which units are picked per hour, for a defined time period. | `# of units picked / # of hours worked` |
| Average units received per purchase order (PO) | This calculation returns the rate at which units are received per hour, for a defined time period. | `Total units received / # of POs` |
| Average cost per unit received | This calculation returns the average cost (or *value*) of the units received, for a defined time period. | `Total cost of units received / # of units received` |
| Average inventory value at each DC | This calculation returns the average value of the on-hand inventory at each distribution center (DC). You can perform this calculation for cost value or retail value, depending on your finance rules. You typically run this calculation at the beginning or end of a fiscal period. | `Sum of inventory value in each period / # of periods` |
| Average value per line picked | This calculation returns the average value of the lines picked, for a defined time period. | `Total value of order lines / # of lines processed` |
| Average value per order | This calculation returns the average value of the orders picked, for a defined time period. | `Total value of orders / # of orders processed` |
| Average lines picked per hour | This calculation returns the average number of lines picked per hour, for a defined time period. | `# of order lines processed / # of hours worked` |
| Average operational cost per order | This calculation returns the average total warehouse operational cost per order, for a defined time period. You can perform this calculation for fixed costs or for both variable and fixed costs. | `Total warehouse cost / Total # of orders` |
| Average orders packed per hour | This calculation returns the rate at which orders are packed per hour, for a defined time period. | `# of order numbers packed / # of hours worked` |
| Average orders picked per hour | This calculation returns the rate at which orders are picked per hour, for a defined time period. | `# of order numbers picked / # of hours worked` |
| Average SKU count per tote | This calculation returns the average number of individual SKUs packed into totes, for a defined time period. | `Count of SKU-tote combinations / # of totes` |
| Average totes processed per shipment | This calculation returns the average number of totes processed for each shipment, for a defined time period. | `Total # of totes / # of shipments` |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
