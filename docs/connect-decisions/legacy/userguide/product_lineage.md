---
source_url: https://docs.aws.amazon.com/connect-decisions/legacy/userguide/product_lineage.html
---

# Product lineage
<a name="product_lineage"></a>

*Product lineage* refers to the relationship established between products and their previous versions or alternate products. Demand Planning uses product lineage information to create surrogate histories for these products, which serve as forecast inputs for demand predictions.

Product lineage supports the following patterns:
+ A single product has one lineage or alternate product = 1:1
![Product lineage pattern = 1:1](https://docs.aws.amazon.com/connect-decisions/legacy/userguide/images/product_lineage_pattern1.png)

  The following example shows an 1:1 scenario.
![Product lineage pattern = 1:1](https://docs.aws.amazon.com/connect-decisions/legacy/userguide/images/1 is to 1_example.png)
+ A single product has more than one product as lineage or alternate = Many:1
![Product lineage pattern = Many:1](https://docs.aws.amazon.com/connect-decisions/legacy/userguide/images/product_lineage_pattern2.png)

  Demand Planning supports product lineage relationship modeled as both *chain* or *flattened* methods.
  + **Chain format** – You can directly model lineage relationships like A to B and B to C. In the following example. Demand Planning will model the lineage relationship as A to B, B to C, and A to C.
[See the AWS documentation website for more details](http://docs.aws.amazon.com/connect-decisions/legacy/userguide/product_lineage.html)

    The following example shows an Many:1 scenario - Chain format
![Product lineage pattern = Chain format](https://docs.aws.amazon.com/connect-decisions/legacy/userguide/images/chain_format.png)
  + **Flattened format** – Demand Planning will continue to support lineage information in A to B and A to C format. In the following example, Demand planning will model the lineage relationship as A to B and A to C. B to C is not considered.
[See the AWS documentation website for more details](http://docs.aws.amazon.com/connect-decisions/legacy/userguide/product_lineage.html)
**Note**
Chain format only supports 6 levels of lineage relationship. If you have more than 6, you can use flattened format to model the lineage relationship.

  The following example shows an Many:1 scenario - Flattened format
![Product lineage pattern = Flattened format](https://docs.aws.amazon.com/connect-decisions/legacy/userguide/images/1 is to many_example.png)
+ A single product can be lineage or alternate for more than 1 product = 1 : Many
![Product lineage pattern = 1:Many](https://docs.aws.amazon.com/connect-decisions/legacy/userguide/images/product_lineage_pattern3.png)

To enable the product lineage feature, you can define the lineage relationship for the different versions of the products or alternates/substitutes in the *product\_alternate* data entity. For more information, see [Demand Planning](required_entities.md).

If your instance was created on or after September 11, 2023, you will see *product\_alternate* data entity in the AWS Supply Chain data Connection module. If your instance was created before September 11, 2023, create a new data connection to enable the *product\_alternate* data entity for ingestion.

To ingest data into the *product\_alternate* data entity, follow the guidelines below:
+ *product\_id* – The primary product to create the forecast.
+ *alternative\_product\_id* – Previous version of the product or alternate/substitute product.

  To consider multiple *alternative\_product\_id* for a single *product\_id*, enter them in separate rows.
+ Demand Planning will consider the data ONLY when the values are provided in the following format.
  + *alternate\_type* is * similar\_demand\_product*.
  + *status* is *active*.
  + *alternate\_product\_qty\_uom* is the text *percentage*.
  + *alternate\_product\_qty* – Enter the proportion of history of the alternate product you want to use for forecasting new products in the *alternate\_product\_qty* data field. For example, if it is 60%, enter 60. When you have multiple *alternative\_product\_id* for a single *product\_id*, the *alternate\_product\_qty* does not have to add up to 100.
+ The *eff\_start\_date* and *eff\_end\_date* data fields are required. However, you can leave this field empty and Demand Planning will auto-fill with 1000 and 9999 years respectively.

When the forecast is created using product lineage data, you will see an indicator *Forecast is based on alternate product's history* on the Demand Planning page when you filter by *product ID*.

The following table shows an example of how Demand Planning Product lineage feature works based on the data ingested into the *product\_alternate* data entity.

| Column | Required or Optional | Example 1 | Example 2 | Example 3 | Example 4 | Example 5 | Example 6 | Example 7 | Example 8 | Example 9 | Example 10 | Example 11 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| product\_id | Required | Product 123 | Product 123 | Product 123 | Product 123 | Product 123 | Product 123 | Product 123 | Product 123 | Product 123 | Null | Product 123 |
| alternative\_product\_id | Required | Product XYZ | Null | Product XYZ | Product XYZ | Product XYZ | Product XYZ | Product XYZ | Product XYZ | Product XYZ | Null | Product XYZ |
| alternate\_type | Required | Similar\_Demand\_Product | Similar\_Demand\_Product | Null or a different value | Similar\_Demand\_Product | Similar\_Demand\_Product | Similar\_Demand\_Product | Similar\_Demand\_Product | Similar\_Demand\_Product | Similar\_Demand\_Product | Similar\_Demand\_Product | Similar\_Demand\_Product |
| status\* | Required | active | active | active | inactive | active | active | Null | active | active | active | active |
| alternate\_product\_qty | Required | 100 | 60 | 100 | 100 | Null | 100 | 100 | 100 | 100 | 100 | 60 |
| alternate\_product\_qty\_uom | Required | percentage | percentage | percentage | percentage | percentage | Null or a different value | percentage | percentage | percentage | percentage | percentage |
| eff\_start\_date | Required | 2023-01-01 00:00:00 | 2023-01-01 00:00:00 | 2023-01-01 00:00:00 | 2023-01-01 00:00:00 | 2023-01-01 00:00:00 | 2023-01-01 00:00:00 | 2023-01-01 00:00:00 | Null | 2023-01-01 00:00:00 | 2023-01-01 00:00:00 | Null |
| eff\_end\_date | Required | 2025-12-31 23:59:59 | 2025-12-31 23:59:59 | 2025-12-31 23:59:59 | 2025-12-31 23:59:59 | 2025-12-31 23:59:59 | 2025-12-31 23:59:59 | 2025-12-31 23:59:59 | 2025-12-31 23:59:59 | Null | 2025-12-31 23:59:59 | Null |
| **Expected behavior** | NA | 100% of product XYZ's history from 1/1/2023 to 31/12/2025 will be used to forecast product 123. | Invalid mapping since alternative\_product\_id is missing. | Invalid mapping since alternate \_type is not 'similar\_demand\_product'. | Inactive mapping. | Invalid mapping since alternate\_product\_qty is missing. | Invalid mapping since alternate\_product\_qty\_uom is missing or not percentage. | Invalid mapping since status is missing. | Ingestion will fail. | Ingestion will fail. | Invalid mapping since product\_id and alternative\_product\_id are missing. | Ingestion will fail. |
|  | NA | NA | NA | NA | NA | NA | NA | NA |  Demand Planning will auto-populate the *eff\_start\_date* to year 1000. This scenario is valid and data ingestion will not fail. |  Demand Planning will auto-populate the *eff\_end\_date* to year 9999. This scenario is valid and ingestion will not fail. | NA |  Demand Planning will auto-populate the *eff\_start\_date* to year 1000 and *eff\_end\_date* to year 9999. This scenario is valid and ingestion will not fail. |

The following example explains how Demand Planning will interpret when the *status* is set as *inactive* and the product lineage is in chain format.

| Column | Column | Status |
| --- | --- | --- |
| A | B | Active |
| B | C | Inactive |
| C | D | Active |

Demand planing considers the status of the first root and child mapping as the status for the entire chain.

 A to B Active

A to C Active

A to D Active

B to C Inactive

B to D Inactive

C to D Active
